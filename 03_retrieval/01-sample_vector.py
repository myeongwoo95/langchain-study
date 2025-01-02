from langchain.embeddings import OpenAIEmbeddings
from numpy import dot # 벡터유사도 계산
from numpy.linalg import norm

embeddings = OpenAIEmbeddings(
  model="text-embedding-ada-002"
)

query_vector = embeddings.embed_query("비행 자동차의 최고 속도는?") # 질문을 백터화

print(f"벡터화된 질문: {query_vector[:5]}")
print(f"벡터의 전체 길이: {len(query_vector)}") # 1536

document_1_vector = embeddings.embed_query("비행 자동차의 최고 속도는 시속 150km입니다.") # 문서라 가정
document_2_vector = embeddings.embed_query("닭고기를 적당히 양념한 후 중불로 굽다가 가끔 뒤집어 주면서 겉은 고소하고 속은 부드럽게 익힌다.")

cos_sim_1 = dot(query_vector, document_1_vector) / (norm(query_vector) * norm(document_1_vector))
print(f"문서 1과 질문의 유사도: {cos_sim_1}")

cos_sim_2 = dot(query_vector, document_2_vector) / (norm(query_vector) * norm(document_2_vector))
print(f"문서 2과 질문의 유사도: {cos_sim_2}")

