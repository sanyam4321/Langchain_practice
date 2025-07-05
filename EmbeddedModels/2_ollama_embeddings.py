from langchain_ollama import OllamaEmbeddings

embedding = OllamaEmbeddings(model="nomic-embed-text")

documents = [
        "Delhi is the capital of india",
        "Kolkata is the capital of west bengal",
        "Paris is the capital of france"
            ]

result = embedding.embed_documents(documents)

print(result)