from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

texts = [
    "You are going to learn gen ai",
    "Generative AI is a type of artificial intelligence that can create new content, such as text, images, or music, based on the data it has been trained on.",
]
vectors = embeddings.embed_documents(texts)
print(vectors)