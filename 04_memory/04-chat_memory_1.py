import chainlit as cl
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage

chat = ChatOpenAI(
  model="gpt-3.5-turbo",
)

memory = ConversationBufferMemory(
  return_messages=True, # Chat models에 쉽게 전달할 수 있는 형식으로 출력
)

@cl.on_chat_start
async def on_chat_start():
  await cl.Message(content="저는 대화의 맥락을 고려해 답변할 수 있는 채팅봇입니다. 메세지를 입력하세요.").send()

@cl.on_message
async def on_message(message: str):
  memory_message_result = memory.load_memory_variables({}) # 메모리 내용을 로드

  messages = memory_message_result['history'] # 메모리 내용에서 메세지만 얻음 (history안에 메세지가 있음)

  messages.append(HumanMessage(content=message)) # 사용자 메세지 추가

  # 챗봇에 메세지 전달
  result = chat(
    messages
  ) 

  memory.save_context(
    {
      "input": message,
    },
    {
      "output": result.content
    }
  )

  await cl.Message(content=result.content).send() # 챗봇의 답변을 출력