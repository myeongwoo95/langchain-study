### 체인

- chains는 일련의 처리를 하나의 묶음으로 처리할 수 있는 모듈이다.
- 여러가지 기능이 많지만 크게 3가지이다.
  - 여러 모듈의 조합을 쉽게할 수 있다. (e.g LLMChain = PromptTemplate + ChatOpenAI 합침)
  - 특정 용도에 특화된 체인 (e.g LLMRequestChain은 주어진 URL에 접속해 얻은 결과와 질문을 조합하여 언어모델 호출)
  - 여러 체인을 묶을 수 있다.

### 체인종류

- LLMChain: LLMChain은 PromptTemplate + 언어모델
- ConverstaionChain: Memory + 언어모델

### chains에서 어떤 처리가 이뤄지고 있는지 자세히 보기

- chain = someChain(verbose=true)

### 특정 기능에 특화된 Chains

- Retrieval을 학습하면서 살펴본 바와 같이, 언어모델은 학습된 지식 외의 정보를 기반으로한 답변을 할 수없다. 그래서 chains 모듈에서는
  특정 url에서 정보를 가져와 그 정보를 바탕으로 답변을 생성할 수 있는 LLMRequestsChain이 준비돼 있다.

### 여러 체인 묶기

- chains 자체를 순서대로 실행하는 SimpleSequentialChain
- 언어 모델은 한 번의 호출로 여러 작업을 실행하려고 하면 결과가 안정적이지 못하거나 품질이 떨어질 수 있다. 이럴때 SimpleSequentialChain
  모듈을 사용해 작업을 분할해 순서대로 실행시켜보자.

### 체인 종류류

- ConverstaionChain: 대화 이력(Memory)을 유지하며 상호작용하는 체인, 이전 대화 내용을 기억하고 문맥을 파악하여 응답

  - ConversationBufferMemory: 모든 대화 내용을 그대로 저장
  - ConversationBufferWindowMemory: 최근 N개의 대화만 유지
  - ConversationSummaryMemory: 이전 대화 내용을 요약하여 저장

- LLMRequestsChain: URL을 입력받아 해당 페이지의 내용을 스크래핑하고, 이를 기반으로 질문에 답변
- SimpleSequentialChain: 여러 체인을 순차적으로 연결하는 단순한 형태의 체인
- RouterChain: 사용자 질문의 의도를 파악하여 수학 문제는 MathChain으로, 번역 요청은 TranslationChain으로 전달
- LLMMathChain: 수학 문제를 해결하는 체인, LLM과 Python의 eval() 함수를 조합하여 복잡한 수학 계산을 처리
- LLMCheckerChain: LLM의 출력을 검증하는 체인, 첫 번째 LLM의 응답을 다른 LLM이 팩트체크하고 검증, 출력의 정확성과 신뢰성을 높이는 데 사용
- OpenAIModerationChain: OpenAI의 Moderation API를 사용하여 콘텐츠를 검수하는 체인, 유해하거나 부적절한 내용을 필터링, 안전한 출력을 보장하는데 사용
- TransformChain: 입력을 사용자가 정의한 함수로 변환하는 단순한 체인 (chain 연결할 때 함수말고 chain으로 대체하기 위함)
- APIChain: API 문서를 읽고 자동으로 적절한 API 호출을 생성하는 체인
- SQLDatabaseChain: 자연어를 SQL 쿼리로 변환하고 실행하는 체인
- PALChain: 복잡한 추론 문제를 해결하기 위해 중간 단계에서 코드를 생성하고 실행
- QAWithSourcesChain: 문서 기반 질의응답에 특화된 체인, 답변과 함께 정보의 출처를 함께 제공
