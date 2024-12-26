from langchain.document_loaders import PyMuPDFLoader

loader = PyMuPDFLoader("./asset/sample.pdf")
documents = loader.load()

print(f"문서 개수: {len(documents)}")
print(f"첫 번째 문서의 내용: {documents[0].page_content}")
print(f"첫 번째 문서의 메타데이터: {documents[0].metadata}")