from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

chat = ChatOpenAI(
  streaming = True, # 스트리밍 모드로 설정
  callbacks = [
    StreamingStdOutCallbackHandler()# 콜백 핸들러 설정
    # StreamingStdOutCallbackHandler은 LangChain에서 기본적으로 제공하는 
    # 콜백 핸들러로 스트리밍 응답을 표준 출력(stdout:터미널) 으로 실시간 출력해준다.
  ] 
)

resp = chat([
  HumanMessage(content="맛있는 스테이크 굽는 법을 알려주세요"),
])

response_text = resp.content # 응답 텍스트를 저장
print(response_text)