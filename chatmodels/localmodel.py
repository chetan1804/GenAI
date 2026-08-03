from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace

pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    max_new_tokens=512,
    do_sample=False,
)

llm = HuggingFacePipeline(pipeline=pipe)
chat_model = ChatHuggingFace(llm=llm)

response = chat_model.invoke("What is Generative AI?")
print(response.content)