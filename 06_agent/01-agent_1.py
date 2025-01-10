from tabnanny import verbose
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
)

tools = load_tools(
  [
    "requests",
  ]
)

agent = initialize_agent(
  tools=tools,
  llm=chat,
  agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, # 하나의 입력만 받아드릴 수 있는 툴을 사용하는 에이전트
  verbose=True,
)

result = agent.run("""아래 URL에 접속하여 기사 내용을 정리하여 한국어로 답하세요.
https://www.bbc.com/news/world-asia-60927598
""")

print(f"실행결과: {result}")