from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

chat = ChatOpenAI(
    model="gpt-3.5-turbo"
)

embeddings = OpenAIEmbeddings(
  model="text-embedding-ada-002"
)

database = Chroma(
  persist_directory="./.data", 
  embedding_function=embeddings 
)

# db를 Retriever로 변환
retriever = database.as_retriever()

qa = RetrievalQA.from_llm(
    llm=chat, # 모델 지정
    retriever=retriever, # Retriever 지정
    return_source_documents=True # 응답에 참고한 원본 문서를 포함할지를 결정
)

result = qa("비행 자동차의 최고 속도는?")
print(result["result"]) # 결과 출력
print(result["source_documents"]) # 원본 문서 출력