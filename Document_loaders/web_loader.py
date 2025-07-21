from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
prompt = PromptTemplate(
    template='Answer the following question: {question}, based on the following text: {text}',
    input_variables=['question', 'text']
)
parser = StrOutputParser()

url = 'https://www.amazon.in/Daikin-Fixed-Copper-Filter-FTL28U/dp/B09R4SF5SP/ref=sr_1_1?crid=3OKX9EYC9ELDB&dib=eyJ2IjoiMSJ9.ZeLsLNuo30ALNIqMduy5lsGOLtFRZj3crFrYga3_VjaS7fHF39KCLyJX2utp3b54wv9yJgND7u6S85Wy4uVUcsAd-YeswoCMxRWY3tRdW_4.-NDhdwIXuh1MMWrOxGdyY8mhuAAAvK3HH1xxxhQhXzc&dib_tag=se&keywords=air+conditioner+1.5+ton&nav_sdd=aps&qid=1752769090&refinements=p_n_feature_eleven_browse-bin%3A2753096031&rnid=2753095031&s=kitchen&sprefix=air+con&sr=1-1'
loader = WebBaseLoader(url) # it can even get multiple webpages and we can pass list of urls

chain = prompt | model | parser

docs = loader.load()

output = chain.invoke({
    'question': 'what is the specification of the product',
    'text': docs[0].page_content
})

print(output)