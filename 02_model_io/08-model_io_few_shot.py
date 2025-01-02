from langchain.llms import OpenAI
from langchain.prompts import FewShotPromptTemplate, PromptTemplate

llm = OpenAI(
  model = "gpt-3.5-turbo-instruct",
)

examples = [
  {
    "input": "충청도의 계룡산 전라도의 내장산 강원도의 설악산은 모두 국립 공원이다", 
    "output": "충청도의 계룡산, 전라도의 내장산, 강원도의 설악산은 모두 국립 공원이다." 
  },
]

prompt = PromptTemplate(
  input_variables=["input", "output"],
  template="입력: {input}\n출력: {output}", 
)

# prefix: 가장 앞에 배치되는 텍스트
# suffix: 예시를 출력하는 프롬프트 뒤에 배치되는 텍스트로, 사용자의 입력이들어간다.
few_shot_prompt = FewShotPromptTemplate(
  examples=examples,
  example_prompt=prompt,
  prefix="아래 문장부호가 빠진 입력에 문장부호를 추가하세요. 추가할 수 있는 문장부호는 ',', '.'입니다. 다른 문장부호는 추가하지마세요.",
  suffix="입력: {input_string}\n출력:",
  input_variables=["input_string"], 
)

formatted_prompt = few_shot_prompt.format(
  input_string="집을 보러 가면 그 집이 내가 원하느 조건에 맞는지 살기에 편한지 망가진 곳은 없는지 확인해야 한다"
)

result = llm.predict(formatted_prompt)

print("formatted_prompt:", formatted_prompt)
print("result:", result)
