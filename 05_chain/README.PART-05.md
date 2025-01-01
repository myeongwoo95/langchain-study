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

### 여러 체인 묶기
