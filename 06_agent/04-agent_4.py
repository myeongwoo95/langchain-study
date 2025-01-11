from re import A
from tabnanny import verbose
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.agents.agent_toolkits import create_retriever_tool  #← create_retriever_tool을 가져오기
from langchain.chat_models import ChatOpenAI
from langchain.retrievers import WikipediaRetriever #←WikipediaRetriever를 가져오기
from langchain.tools import WriteFileTool

chat = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
)

tools = []

tools.append(WriteFileTool(
  root_dir="./",
))

retriever = WikipediaRetriever(
  lang="ko",
  doc_content_chars_max=500, # 글의 최대 길이를 500자로 설정
  top_k_results=1, # 검색 결과 중 상위 1개의 결과만 가져오기
)

tools.append(
  create_retriever_tool(
    name="WikipediaRetriever",
    description="받은 단어에 대한 위키백과 기사를 검색할 수 있다.",
    retriever=retriever
  )
)

agent = initialize_agent(
  tools,
  chat,
  agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, # 여러 입력을 가진 툴을 사용하는 에이전트
  verbose=True,
  max_iterations=5  # 최대 반복 횟수
)

result = agent.run("스카치 위스키에 대해 Wikipedia에서 찾아보고 그 개요를 한국어로 result.txt 파일에 저장하세요.")
print(f"실행결과: {result}")