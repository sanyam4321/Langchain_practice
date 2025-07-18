from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# we define separators \n\n --> paragraph or \n --> lines\sentences or ' ' --> words or '' --> characters

loader = PyPDFLoader('books\git-cheat-sheet-education.pdf') 
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=0
)

output = splitter.split_text(docs[0].page_content)
print(output)