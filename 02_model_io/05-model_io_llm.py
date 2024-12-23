from langchain.llms import OpenAI

llm = OpenAI(
  model = "gpt-3.5-turbo-instruct",
)

result = llm(
  "맛있는 라면을",
  stop="." # 마침표를 만나면 생성을 중단한다.
)

print(result)