from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

model = ChatMistralAI(
    model="mistral-small-2603",
    temperature=0.9,
)

print("Choose your AI mode:")
print("1. For Angry mode")
print("2. For Funny mode")
print("3. For Sad mode")

choice = input("Enter your choice (1, 2, or 3): ")

if choice == "1":
    system_message = SystemMessage(content="You are an angry AI. Respond in an angry tone.")
elif choice == "2":
    system_message = SystemMessage(content="You are a funny AI. Respond in a humorous tone.")
elif choice == "3":
    system_message = SystemMessage(content="You are a sad AI. Respond in a melancholic tone.")


messages =[system_message]


print("Welcome to the AI Chatbot! Type '0' to quit.")

while True:
    prompt = input("You: ")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0":
        break
    response = model.invoke(messages)

    messages.append(AIMessage(content=response.content))
    print(f"Bot: {response.content}")

print(messages)