from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv() 

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

loader = PyPDFLoader('git-cheat-sheet-education.pdf')
docs = loader.load()
print(len(docs))

