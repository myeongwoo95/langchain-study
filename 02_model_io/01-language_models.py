from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

# 기본 사용방법

chat = ChatOpenAI(
  model = "gpt-3.5-turbo",
)

result = chat(
  [
    SystemMessage(content="당신은 친한 친구입니다. 존댓말을 쓰지 말고 솔직하게 답변해주세요."),
    HumanMessage(content="안녕!"),
  ]
)

print(result.content)

#  LangChain은 기본적으로 OPENAI_API_KEY 환경 변수를 찾아서 사용합니다.