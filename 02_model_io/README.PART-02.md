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
