from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

model = ChatOllama(model="llama3.2", num_predict=1000)

template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)


template2 = PromptTemplate(
    template='Write a 5 line summary on following text\n. {text}',
    input_variables=['text']
)


prompt1 = template1.invoke({'topic': 'football'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text': result.content})

result = model.invoke(prompt2)

print(result.content)


