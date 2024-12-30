from langchain.chat_models import ChatOpenAI
from langchain.retrievers import WikipediaRetriever, RePhraseQueryRetriever

from langchain import LLMChain
from langchain.prompts import PromptTemplate
from tomlkit import document

retriever = WikipediaRetriever(
  lang="ko",
  doc_content_chars_max=500, # 검색할 텍스트의 최대 글자수를 지정
)

# promptTemplate과 chat models를 통합해 프롬프트 생성
llm_chain = LLMChain(
  llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
  ),

  prompt=PromptTemplate(
    input_variables=["question"],
    template="""아래 질문에서 위키백과에서 검색할 키워드를 추출해 주세요.
질문: {question}
"""
))

# 기본전제1: "나를 라면을 좋아합니다. 그런데 소주란 무엇인가요?"를 검색하면 제대로된 검색 결과를 얻을 수 없다.
# 기본전제2: 위에서 필요한 키워드는 "소주"이다. 이 키워드를 추출하고, 이를 위키백과에서 검색하면 제대로된 검색 결과를 얻을 수 있다.
# RePhraseQueryRetriever는 질문을 재구성하기 위한 Retriever로 llm_chain과 retriever를 인자로 받음
# RePhraseQueryRetriever는 먼저 질문을 재구성하고, 그 결과를 WikipediaRetriever에 전달해 검색을 수행한다.
re_phrase_query_retriever = RePhraseQueryRetriever(
  llm_chain=llm_chain,
  retriever=retriever,
)

documents = re_phrase_query_retriever.get_relevant_documents("나를 라면을 좋아합니다. 그런데 소주란 무엇인가요?")

print(documents)