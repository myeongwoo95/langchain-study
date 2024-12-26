from unittest import loader
from langchain.document_loaders import PyMuPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import SpacyTextSplitter
from langchain.vectorstores import Chroma

loader = PyMuPDFLoader("./asset/sample.pdf")
documents = loader.load()

text_splitter = SpacyTextSplitter(
  chunk_size=300, # 분할할 크기를 설정(문자단위: 300자)
  pipeline="ko_core_news_sm" # 분할에 사용할 언어 모델: 한국어 모델 사용
)
splitted_documents =text_splitter.split_documents(documents) # 문서를 분할

embeddings = OpenAIEmbeddings(
  model="text-embedding-ada-002"
)

database = Chroma(
  persist_directory="./.data", # 영속화 데이터 저장 위치 지정
  embedding_function=embeddings # 벡터화할 모델을 지정
)

database.add_documents( 
  splitted_documents, # 추가할 문서를 지정
)

print("데이터베이스 생성이 완료되었습니다.")
