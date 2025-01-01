import chainlit as cl
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory

chat = ChatOpenAI(
  model="gpt-3.5-turbo",
)

memory = ConversationBufferWindowMemory(
  return_messages=True, # Chat models에 쉽게 전달할 수 있는 형식으로 출력
  k=3, # 메모리에 저장할 메세지의 수 (사용자, ai 메세지를 모두 포함하여 총 6개)
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
  messages = chain.memory.load_memory_variables({})["history"] # 저장된 메세지 가져오기
  
  print(f"저장된 메세지 개수: {len(messages)}")

  for saved_message in messages:
    print(saved_message.content)
  
  result = chain(
    message
  )

  await cl.Message(content=result["response"]).send()
  