- Agent는 단순히 Tool을 조작하는 것이 아니라, 어떤 Tool을 사용하면 좋을지 고민하고 실행하고, 결과 검증까지 스스로 한다.
- Agents 모듈에는 Tool, Agent 두 가지 하위모듈이 있다.
- Tool은 언어 모델만으로는 할 수 없는 일을 할 수 있게 하는 모듈이다.
- Tool은 랭체인이 제공하는 것 외에도 직접 만든 Tool을 사용할 수 있다.
- 랭체인이 제공하는 툴:
  - LLMMath: 언어모델이 취약한 계산을 위한 툴
  - Requests: 지정된 URL로 요청을 보낼 수 있다.
  - File System Tools: PC 내 파일에 접근해 파일을 읽고 쓸 수 있다.
  - SerpApi: 구글이나 야후 검색을 API로 하는 serpApi라는 웹 서비스와 연동할 수 있다.

### ReAct 기법 (에이전트 기법중 하나)

- 1. 사용자로부터 작업을 받는다.
- 2. 준비된 Tool 중에서 어떤 Tool을 사용할지, 어떤 정보를 입력할지를 결정한다.
- 3. Tool을 사용해 결과를 얻는다.
- 4. 3에서 얻은 결과를 통해 과업이 달성되고 있는지를 확인한다.
- 5. 에이전트가 작업을 완료했다고 판단할 수 있을 때 까지 2~4를 반복한다.

### Agent.Type

### 대화(Chat) 관련 타입

#### 1. CHAT_CONVERSATIONAL_REACT_DESCRIPTION

- 대화형 방식, ReAct, 대화 컨텍스트 유지
- 사용자와의 자연스러운 대화를 통해 복잡한 작업을 수행하기에 적합

### 2. CHAT_ZERO_SHOT_REACT_DESCRIPTION

- 대화형 방식, ReAct, 제로샷
- 새로운 상황이나 질문에 빠르게 적응 가능

### 3. CONVERSATIONAL_REACT_DESCRIPTION

- 순수한 대화형 에이전트, 대화 컨텍스트 유지
- 자연스러운 대화 흐름 유지에 중점

### OpenAI 관련 타입

### 1. OPENAI_FUNCTIONS

- OpenAI의 함수 호출 기능을 활용
- 특정 함수나 도구를 직접 호출할 수 있는 능력
- 구조화된 출력을 생성하는데 적합

### 2. OPENAI_MULTI_FUNCTIONS

- 여러 OpenAI 함수를 동시에 사용 가능
- 복잡한 작업을 여러 단계로 분해하여 처리
- 다중 도구 사용이 필요한 상황에 적합

### 기타 특수 타입:

### 1. REACT_DOCSTORE

- 문서 저장소와 연동된 ReAct 프레임워크
- 문서 검색과 정보 추출에 특화
- 대규모 문서 데이터베이스 작업에 적합

### 2. SELF_ASK_WITH_SEARCH

- 자체적으로 질문을 생성하고 검색하는 능력
- 복잡한 질문을 작은 하위 질문으로 분해
- 단계적 추론이 필요한 작업에 유용

### 3. STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION

- 구조화된 출력을 생성하는 제로샷 방식
- 정형화된 형식의 응답이 필요한 경우에 사용
- 템플릿 기반의 응답 생성에 적합

### 4. ZERO_SHOT_REACT_DESCRIPTION

- 기본적인 제로샷 ReAct 프레임워크
- 사전 학습 없이 즉시 추론 및 행동
- 범용적인 작업 처리에 적합

### ReAct 기법과 OpenAI Function Calling 차이

- ReAct 기법은 에이전트가 "생각하고 → 행동하고 → 관찰하는" 과정을 명시적으로 보여준다.
- OpenAI Function Calling 함수의 형태(스키마)를 미리 정의해두고, LLM이 직접 함수를 호출하고 에이전트의 사고 과정이 명시적으로 드러나지 않는다.
