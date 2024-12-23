import time
import langchain 
from langchain.cache import InMemoryCache
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

langchain.llm_cache = InMemoryCache() # ll_cache를 InMemoryCache로 설정
# 이걸 설정함으로써 같은 질문을 2번 물어보면 2번째부터는 캐시된 결과를 사용한다.

chat = ChatOpenAI() # 기본값으로 "gpt-3.5-turbo"를 사용

start = time.time() # 시작 시간 저장
result = chat(
  [
    HumanMessage(content="안녕하세요"),
  ]
)
end = time.time() # 종료 시간 저장

print(result.content)
print(f"첫번째 소요 시간: {end - start}초") # 소요 시간 출력

start = time.time() 
result = chat(
  [
    HumanMessage(content="안녕하세요"),
  ]
)
end = time.time() 

print(result.content)
print(f"두번째 소요 시간: {end - start}초")

