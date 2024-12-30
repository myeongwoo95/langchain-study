import chainlit as cl
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

chat = ChatOpenAI(
  model="gpt-3.5-turbo",
)

memory = ConversationBufferMemory(
  return_messages=True, # Chat models에 쉽게 전달할 수 있는 형식으로 출력
)

chain = ConversationChain(
  memory=memory,
  llm=chat,
)

@cl.on_chat_start
async def on_chat_start():
  await cl.Message(content="저는 대화의 맥락을 고려해 답변할 수 있는 채팅봇입니다. 메세지를 입력하세요.").send()

@cl.on_message
async def on_message(message: str):
  
  # 과거 메세지 검색, 새로운 메세지 추가, 챗봇에 그 메세지를 전달, 응답을 메모리에 저장을 한번에 수행
  result = chain(
    message
  )

  await cl.Message(content=result["response"]).send() # 챗봇의 답변을 출력