from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')


prompt1 = PromptTemplate(
    template='Write a joke about {topic} under 100 words',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain the following Joke: {text} under 100 words',
    input_variables=['text']
)

def word_count(text):
    return len(text.split())

parser = StrOutputParser()

joke_gen_chain = prompt1 | model | parser

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_count),
    'explaination': RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

output = final_chain.invoke({'topic': 'cricker'})

print(output)