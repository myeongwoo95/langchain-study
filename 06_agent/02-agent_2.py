from tabnanny import verbose
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI
from langchain.tools.file_management import WriteFileTool
from regex import F

chat = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
)

tools = load_tools(
  [
    "requests_get",
    "serpapi"
  ],
  llm=chat,
)

tools.append(WriteFileTool(
  root_dir="./",
))

agent = initialize_agent(
  tools,
  chat,
  agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, # 여러 입력을 가진 툴을 사용하는 에이전트트
  verbose=True,
)

result = agent.run("경주시의 특산품을 검색해 result.txt 파일에 한국어로 저장하세요.")

print(f"실행결과: {result}")