from unittest import result
from joblib import Memory
from langchain.agents import AgentType, initialize_agent
from langchain.agents.agent_toolkits import create_retriever_tool
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory  
from langchain.retrievers import WikipediaRetriever

chat = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
)

tools = []

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

memory = ConversationBufferMemory(
  memory_key="chat_history",
  return_messages=True, # 메세지를 반환하도록 설정
)

agent = initialize_agent(
  tools,
  chat,
  agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION, # Agent의 유형을 대화형으로 변경 (여러개의 입력을 받을 수 없어 WriteFileTool을 제거)
  memory=memory,
  verbose=True,
  max_iterations=5  # 최대 반복 횟수
)

result = agent.run("스카치 위스키에 대해 Wikipedia에서 찾아보고 그 개요를 한국어로 result.txt 파일에 저장하세요.")
print(f"1차 실행결과: {result}")

result_2 = agent.run("이전 지시를 다시 한번 실행하세요.")
print(f"2차 실행결과: {result_2}") # 결과가 제대로 출력된다면 이전 대화 내용이 잘 기억되었다는 뜻
