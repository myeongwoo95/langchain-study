## ConversationBufferMemory

- 메모리에 대화 히스토리를 저장하고 불러올 수 있다.

## ConversationChain

- 대화의 맥락을 고려한 챗봇을 만들기 위해 이전 메세지를 합쳐서 내용을 보냈는데, 대화 내용 Memory에 저장, 과거 메세지 불러오기, 언어 모델 호출을 따로따로 수행했는데 랭체인은 이러한 과정을 쉽게 구현할 수 있는 ConversationChain 모듈을 제공한다.
  (거 메세지 검색, 새로운 메세지 추가, 챗봇에 그 메세지를 전달, 응답을 메모리에 저장을 한번에 수행)

- redis 사용

## 매우 긴 대화 기록에 대응

- 오래된 대화 삭제하기 (ConversationBufferWindowMemory)
- 대화를 요약해 토큰 수 제한에 대응 (ConversationBufferSummaryMemory)
