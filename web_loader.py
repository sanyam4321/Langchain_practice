from langchain_community.document_loaders import WebBaseLoader

url = 'https://www.amazon.com/'
loader = WebBaseLoader(url)

docs = loader.load()
print("length", len(docs))

print(docs)