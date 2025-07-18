from langchain_community.document_loaders import YoutubeLoader
loader = YoutubeLoader('4AeSZcRGp1E')

docs = loader.load()
print(docs)