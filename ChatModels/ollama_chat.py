from langchain_ollama import ChatOllama

model = ChatOllama(model="llama3.2", temperature=1.1, num_predict=1000)

result = model.invoke("give me 5 us human names")

print(result.content)