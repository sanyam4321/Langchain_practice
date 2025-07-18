from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('books\Mindset-The-New-Psychology-of-Success-Dweck.pdf') 
docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=0,
    separator=''
)

output = splitter.split_text(text)
print(output)