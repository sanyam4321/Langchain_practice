from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='Iris.csv')

docs = loader.load()

for doc in docs:
    print(doc)