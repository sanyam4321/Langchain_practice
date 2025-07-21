from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

chat_history = [
    SystemMessage(content="You are a helpful AI Assistant")
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