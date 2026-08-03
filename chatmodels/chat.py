from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

from langchain_openai import ChatOpenAI
load_dotenv()

# OpenAI Chat Model
#chat_model = init_chat_model("gpt-4.1") # using init_chat_model to initialize the chat model with the specified model name
#response = chat_model.invoke("Hello, how are you?")

# chat_model = ChatOpenAI(model_name="gpt-4.1")  # using OpenAIChat to initialize the chat model with the specified model name
# response = chat_model.invoke("what is the weather in Pune City today?")
# print(response.content)

# Gemini Chat Model
# chat_model = init_chat_model("google_genai:gemini-2.5-pro") # using init_chat_model to initialize the chat model with the specified model name
# response = chat_model.invoke("write single line code to print hello world in python?") 

# from langchain_google_genai import ChatGoogleGenerativeAI
# model = ChatGoogleGenerativeAI(model="gemini-2.5-pro")
# response = model.invoke("write single line code to print hello world in python?")
# print(response.content)


# Groq Chat Model
# chat_model = init_chat_model("groq:llama-3.1-8b-instant") # using init_chat_model to initialize the chat model with the specified model name
# response = chat_model.invoke("write single line code to print hello world in python?")    
# print(response.content)

# from langchain_groq import ChatGroq
# chat_model = ChatGroq(model="llama-3.1-8b-instant") # using init_chat_model to initialize the chat model with the specified model name
# response = chat_model.invoke("write single line code to print hello world in python?")    
# print(response.content)

# mistral Chat Model
# chat_model = init_chat_model("mistral-small-2603") # using init_chat_model to initialize the chat model with the specified model name
# response = chat_model.invoke("write single line code to print hello world in python?")    
# print(response.content)

# from langchain_mistralai import ChatMistralAI
# chat_model = ChatMistralAI(model="mistral-small-2603") # using init_chat_model to initialize the chat model with the specified model name
# response = chat_model.invoke("write single line code to print hello world in python?")    
# print(response.content)