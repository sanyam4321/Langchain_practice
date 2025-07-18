from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('books\Mindset-The-New-Psychology-of-Success-Dweck.pdf') 
docs = loader.lazy_load()

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=30,
    separator=''
)

output = splitter.split_documents(docs)
print(output[0].page_content)
print(len(output))