from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

model = ChatOllama(model="llama3.2")

chat_history = [
    SystemMessage(content="You are a helpful AI Doctor")
]

while True:
    user_input = input("You: ")
    
    if(user_input.lower() == "exit"):
        break

    chat_history.append(HumanMessage(content=user_input))

    result = model.stream(chat_history)

    print("AI: ", end="", flush=True)

    model_response = ""
    for chunk in result:
       print(chunk.content, end="", flush=True)
       model_response += chunk.content

    chat_history.append(AIMessage(content=model_response))
    print()


print(chat_history)