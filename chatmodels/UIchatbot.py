import os

from dotenv import load_dotenv
import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv(dotenv_path=".env")

st.set_page_config(page_title="Mood Based AI Chatbot", page_icon="🤖", layout="wide")

MODE_PROMPTS = {
    "Angry": "You are an angry AI. Respond in an angry tone.",
    "Funny": "You are a funny AI. Respond in a humorous tone.",
    "Sad": "You are a sad AI. Respond in a melancholic tone.",
}


@st.cache_resource
def get_model():
    api_key = os.getenv("MISTRAL_API_KEY") or os.getenv("MISTRALAI_API_KEY")
    if not api_key:
        st.error("Missing MISTRAL_API_KEY in your environment or .env file.")
        st.stop()

    return ChatMistralAI(
        model_name="mistral-small-2603",
        temperature=0.9,
        api_key=api_key,
    )


def build_messages(history, selected_mode):
    messages = [SystemMessage(content=MODE_PROMPTS[selected_mode])]
    for entry in history:
        if entry["role"] == "user":
            messages.append(HumanMessage(content=entry["content"]))
        else:
            messages.append(AIMessage(content=entry["content"]))
    return messages


st.title("🤖 GenAI Chatbot")
st.caption("A ChatGPT-style chat UI powered by Mistral.")

with st.sidebar:
    st.header("Chat Controls")
    selected_mode = st.selectbox("Choose AI mode", list(MODE_PROMPTS.keys()))
    if st.button("Reset chat"):
        st.session_state.messages = []

if "messages" not in st.session_state:
    st.session_state.messages = []

if not st.session_state.messages:
    st.info("Start the conversation by typing a message below.")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Message the assistant...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    model = get_model()
    history = build_messages(st.session_state.messages, selected_mode)
    response = model.invoke(history)
    assistant_reply = response.content

    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
    with st.chat_message("assistant"):
        st.markdown(assistant_reply)