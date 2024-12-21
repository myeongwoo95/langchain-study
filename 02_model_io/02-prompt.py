from langchain import PromptTemplate
from sympy import product

# promptTemplate을 사용해 프롬프트를 생성하기

prompt = PromptTemplate(
  template="{product}는 어느 회사에서 개발한 제품인가요?", # {product}라는 변수를 포함하는 프롬프트 작성하기

  input_variables=[
    "product" # product에 입력할 변수 지정
  ]
)

print(prompt.format(product="아이폰"))
print(prompt.format(product="갤럭시"))