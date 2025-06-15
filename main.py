# main.py

import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from career_explainer import get_gemini_response

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

st.set_page_config(page_title="Career Suggestion Bot 💼", page_icon="🧠")

st.title("🎯 Career Suggestion Assistant")
st.write("Tell me about what you’re interested in, and I’ll help you find a matching career path!")

# --- Session state for chat history ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_history" not in st.session_state:
    st.session_state.chat_history = ""

# --- Display chat history ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- User input ---
user_input = st.chat_input("What's your interest?")

if user_input:
    # Save user input
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.chat_history += f"User: {user_input}\n"

    # Gemini response
    with st.chat_message("assistant"):
        response = get_gemini_response(user_input, st.session_state.chat_history)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.session_state.chat_history += f"Assistant: {response}\n"
