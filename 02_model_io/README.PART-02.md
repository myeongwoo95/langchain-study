```
Model I/O
│
├─── Language Models ──┬─── Chat Models (대화형 모델)
│                      └─── LLMs (Complete Models, 텍스트 완성 모델)
│
├─── Prompts (입력 템플릿)
│
└─── Output Parsers (출력 형식 파서)
```

### model I/O

## Language models: AI 모델 호출/변경, 채팅

- HumanMessage, AIMessage, SystemMessage가 있다.
- 캐싱 기능도 제공한다.

## Prompts: 프롬프트를 동적으로 생성

- promptTemplate를 이용해서 프롬프트를 생성할 수 있다.
- promptTemplate 초기화 방법의 종류: {}, PrompotTemplate.from_template(), JSON 파일에 저장한 프롬프트를 읽어오기

## Output parsers: 모델에서 받은 결과를 구조화

- HumanMessage 인자에 함수를 이용해서 'foo, bar, baz' 형식의 목록을 요청받도록 하고, 받은 문자열을 배열로 분할.

## Language Models: 캐싱

- 같은 질문을 2번 물어보면 2번째부터는 캐시된 결과를 사용한다.
- 장기간 캐싱이 필요하거나 프로그램 재시작 후에도 캐시를 유지해야하는 경우 InMemoryCache가 아닌 db에 저장한다.

## Language Models: Streaming(실행 중인 프로세스를 순차적으로 표시하는 모듈)

- 순차적 표시란 처리가 완료되기 전에 일부 결과를 순차적으로 수신해 표시하는 것 (e.g 긴응답일때)
- 랭체인은 Streaming 모듈을 활용하기 위해 Callbacks 모듈을 제공한다.
- Callbacks 모듈은 특정 처리가 발생했을 때 실행되는 함수나 클래스를 지정할 수 있다.

## Templates

- 간단한 문장/지시만으로 수행하기 어려운 작업이 있다. (과학 논문 요약 생성, 전문지식이 필요한 문장작성, 고도의 인터랙션 등) Templates 모듈은 프롬프트 엔지니어링을 돕고, 프롬프트를 쉽게 구축할 수 있는 기능을 제공한다.
- few-shoot 프롬프팅
