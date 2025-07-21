from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

loader = TextLoader('cricket.txt', encoding='utf-8')
docs = loader.load()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

prompt = PromptTemplate(
    template='Write a summary for the following poem: {poem}',
    input_variables=['poem']
)
parser = StrOutputParser()

chain = prompt | model | parser
output = chain.invoke({'poem': docs[0].page_content})

print(output)