from langchain.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(
  lang="ko",
)

documents = retriever.get_relevant_documents( # Wikipedia에서 관련 문서를 가져옴
  "대형 언어 모델", # 검색할 키워드
)

print(f"검색 결과: {len(documents)}건")

for document in documents:
  print("------검색한 메타데이터------")
  print(document.metadata)
  print("------검색한 텍스트------")
  print(document.page_content[:100])
