from langchain.llms import OpenAI
from langchain.prompts import FewShotPromptTemplate, PromptTemplate

examples = [
  {
    "input": "충청도의 계룡산 전라도의 내장산 강원도의 설악산은 모두 국립 공원이다."
  },

  {
    "output": "충청도의 계룡산, 전라도의 내장산, 강원도의 설악악산은 모두 국립 공원이다."
  },
]

prompt = PromptTemplate(
  input_variables=["input", "output"], # input과 output 변수로 설정
  template="입력: {input}\n출력: {output}", # 탬플릿
)