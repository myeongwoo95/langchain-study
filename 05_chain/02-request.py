from langchain.chains import LLMChain, LLMRequestsChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

chat = ChatOpenAI(
    model="gpt-3.5-turbo"
)

prompt = PromptTemplate(
  input_variables=[
    "query",
    "requests_result",
  ],

  template="""아래 문장을 바탕으로 질문에 답해 주세요.
문장: {requests_result}
질문: {query}
""",
)

llm_chain = LLMChain(
    llm=chat,
    prompt=prompt,
    verbose=True,
)

chain = LLMRequestsChain(  
    llm_chain=llm_chain,  
)

print(chain({
  "query": "비트코인의 가격을 알려주세요.",
  "url": "https://www.businesspost.co.kr/BP?command=article_view&num=379570"
}))