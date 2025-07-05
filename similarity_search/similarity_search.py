from langchain_ollama import OllamaEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embedding = OllamaEmbeddings(model="nomic-embed-text")

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "tell me about MS Dhoni"





doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

# both much be 2d lists
similarity_scores = cosine_similarity([query_embedding], doc_embeddings)[0]

index, score = sorted(list(enumerate(similarity_scores)), key=lambda x: x[1])[-1]

print(query)
print(documents[index])
print("similarity score is: ", score)