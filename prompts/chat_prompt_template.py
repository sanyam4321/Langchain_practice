from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', "Your are helpful {domain} expert"),
    ('human', "Explain in simple terms, what is {topic}")
])

prompt = chat_template.invoke({'domain': 'cricket', "topic": "wicket"})

print(prompt)
# message placeholder