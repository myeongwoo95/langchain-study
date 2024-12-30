from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.retrievers import WikipediaRetriever

chat = ChatOpenAI(
    model="gpt-3.5-turbo"
)

retriever = WikipediaRetriever(
  lang="ko",
  doc_content_chars_max=500, # 검색할 텍스트의 최대 글자수를 지정
  top_k_results=2, # 검색 결과 중 상위 몇건을 가져올건지 지정
)

chain = RetrievalQA.from_llm(
  llm=chat, # 모델 지정
  retriever=retriever, # Retriever 지정(위키디피아)
  return_source_documents=True # 응답에 참고한 원본 문서를 포함할지를 결정
) 

result = chain("소주란?")
source_documents = result["source_documents"] # 정보 출처의 문서를 가져옴

print(f"검색 결과 건수: {len(source_documents)}건")
for document in source_documents:
  print("------검색한 메타데이터------")
  print(document.metadata)
  print("------검색한 텍스트------")
  print(document.page_content[:100])

print("------응답------")
print(result["result"]) # 응답 결과