from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import SpacyTextSplitter

loader = PyMuPDFLoader("./asset/sample.pdf")
documents = loader.load()

text_splitter = SpacyTextSplitter(
  chunk_size=300, # 분할할 크기를 설정(문자단위: 300자)
  pipeline="ko_core_news_sm" # 분할에 사용할 언어 모델: 한국어 모델 사용
)
splitted_documents =text_splitter.split_documents(documents) # 문서를 분할

print(f"분할 전 문서 개수: {len(documents)}")
print(f"분할 후 문서 개수: {len(splitted_documents)}")   
