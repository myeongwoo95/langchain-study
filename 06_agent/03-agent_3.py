import random
from unittest import result  
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import WriteFileTool

chat = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
)

tools = []

tools.append(WriteFileTool(
  root_dir="./",
))

def min_limit_random_number(min_number):
  return random.randint(int(min_number), 100000)

tools.append(
  Tool(
    name="Random",
    description="입력한 숫자를 최소값으로 설정하고, 그 숫자부터 100000 사이에서 무작위로 하나의 숫자를 뽑아주는 함수입니다.",
    func=min_limit_random_number
  )
)

agent = initialize_agent(
  tools,
  chat,
  agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, # # 여러 입력을 가진 툴을 사용하는 에이전트
  verbose=True,
  max_iterations=5  # 최대 반복 횟수
)

result = agent.run("10 이상의 난수를 생성해 random.txt 파일에 저장하세요.")

print(f"실행결과: {result}")