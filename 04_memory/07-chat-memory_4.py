import os
import chainlit as cl
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory, RedisChatMessageHistory # redis 사용을 위함
from langchain.schema import HumanMessage

chat = ChatOpenAI(
  model="gpt-3.5-turbo",
)

@cl.on_chat_start
async def on_chat_start():
  thread_id = None
  while not thread_id:
    res = await cl.AskUserMessage(content="저는 대화의 맥락을 고려해 답변할 수 있는 채팅봇입니다. 스레드 ID를 입력하세요",
                                  timeout=600).send()
    
    if res:
      thread_id = res["content"]

  
  history = RedisChatMessageHistory(
    session_id=thread_id,
    url=os.environ.get("REDIS_URL"),
  )

  memory = ConversationBufferMemory(
    return_messages=True, 
    chat_memory=history, 
  )

  chain = ConversationChain(
    memory=memory,
    llm=chat,
  )

  memory_message_result = chain.memory.load_memory_variables({}) # 메모리 내용 가져오기
  messages = memory_message_result["history"] # 메모리 내용에서 메세지만 얻음 (history안에 메세지가 있음)

  # 이전 대화 내역 UI 출력
  for message in messages:
    if isinstance(message, HumanMessage):
      await cl.Message(  
        author="User",
        content=f"{message.content}"
      ).send()
    else:   
      await cl.Message(  
        author="Chatbot",
        content=f"{message.content}"
      ).send()

  # 이전 대화 내역 Chainlit 세션에 저장
  cl.user_session.set("chain", chain) #기록을 세션에 저장 

@cl.on_message
async def on_message(message: str):
  chain = cl.user_session.get("chain") # 세션에서 대화내역 가져오기

  result = chain(
    message,
  )

  await cl.Message(content=result["response"]).send()