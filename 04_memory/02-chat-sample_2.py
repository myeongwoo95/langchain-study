from langchain.chat_models import ChatOpenAI
from langchain.schema import (
  HumanMessage,
  AIMessage
)

chat = ChatOpenAI(
  model="gpt-3.5-turbo",
)

result = chat([
    HumanMessage(content="계란찜을 만드는 재료를 알려주세요"),
    AIMessage(
      content="""계란찜을 만드는데 필요한 재료는 다음과 같습니다:

1. 계란 4개
2. 물 1컵
3. 소금 약간
4. 후추 약간
5. 다진 양파 1/4컵
6. 다진 대파 1/4컵
7. 다진 당근 1/4컵
8. 다진 대파 1/4컵
9. 다진 양배추 1/4컵
10. 식용유 약간

이 외에도 자신이 원하는 다양한 야채나 고기를 추가하여 계란찜을 맛있게 만들 수 있습니다."""),
    HumanMessage(content="위의 답변을 영어로 번역하세요."),
])

print(result.content)