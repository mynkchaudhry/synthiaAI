import streamlit as st
import os
from groq import Groq
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.environ["GROQ_API_KEY"]

def display_navbar():
    st.markdown("""
        <style>
        .navbar {
            display: flex;
            align-items: center;
            padding: 8px 16px;
            background-color: transparent;
        }
        .logo {
            width: 150px;
            margin-right: 10px;
        }
        .title {
            font-size: 60px;
        }
        .title span.first-two {
            color: red;
            font-weight: bold;
            font-size: 60px;
        }
        .title span.rest {
            color: black;
            font-weight: bold;
            font-family: Arial, sans-serif; /* Change this to your desired bold font */
        }
        .response-text {
            font-size: 20px;
            font-weight: bold;
            color: black;
        }
        .sidebar-content {
            background-color: transparent;
        }
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: transparent;
            text-align: center;
            padding: 10px 0;
        }
        .footer a {
            color: black;
            text-decoration: none;
            margin: 0 10px;
        }
        /* New style for semi-transparent text area */
        .custom-text-area {
            background-color: rgba(255, 255, 255, 0.9); /* Adjust the alpha value for transparency */
            border-radius: 5px;
            padding: 10px;
            margin-bottom: 10px;
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="navbar">
            <img src="https://cdn3d.iconscout.com/3d/premium/thumb/chatbot-6899426-5627910.png?f=webp" alt="Logo" class="logo">
            <span class="title">
                <span class="first-two">SY</span>
                <span class="rest">NTHIA</span>
            </span>
        </div>
    """, unsafe_allow_html=True)

def add_customization_options():
    st.sidebar.title("LLMs")
    model = st.sidebar.selectbox(
        "Select Language Model",
        [
            "mixtral-8x7b-32768",
            "gemma-7b-it",
            "llama3-70b-8192",
            "llama3-8b-8192",
        ],
    )
    conversational_memory_length = st.sidebar.slider(
        "Conversational Memory Length:", 1, 1000, value=5
    )
    return model, conversational_memory_length

def main():
    display_navbar()

    model, conversational_memory_length = add_customization_options()

    memory = ConversationBufferWindowMemory(k=conversational_memory_length)

    user_question = st.text_area("Ask a question:")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    groq_chat = ChatGroq(groq_api_key=groq_api_key, model_name=model)
    conversation = ConversationChain(llm=groq_chat, memory=memory)

    if user_question:
        if st.button("Generate Response"):
            with st.spinner("Generating response..."):
                response = conversation(user_question)
                message = {"human": user_question, "AI": response["response"]}
                st.session_state.chat_history.append(message)
                st.markdown(f"<p class='response-text'>{response['response']}</p>", unsafe_allow_html=True)

    if st.button("New Chat"):
        clear_chat_history()

    if st.checkbox("Show Chat History"):
        display_chat_history()

    set_background_image(model)

    st.markdown("""
        <div class="footer">
            <a href="https://www.linkedin.com/in/mynkchaudhry/">LinkedIn</a>
            <a href="https://github.com/mynkchaudhry">Github</a>
        </div>
    """, unsafe_allow_html=True)

def clear_chat_history():
    st.session_state.chat_history = []
    st.text_area("Ask a question:", value="", key="clear_text")
    st.experimental_rerun()

def display_chat_history():
    st.subheader("Chat History")
    for message in st.session_state.chat_history:
        st.write(f"User: {message['human']}")
        st.write(f"Chatbot: {message['AI']}")
        st.markdown("---")

def set_background_image(model):
    background_image = {
        "mixtral-8x7b-32768": "https://cdn.pixabay.com/photo/2022/04/18/17/25/artwork-7141103_960_720.png",
        "gemma-7b-it": "https://cdn.pixabay.com/photo/2022/04/18/17/25/artwork-7141103_960_720.png",
        "llama3-70b-8192": "https://cdn.pixabay.com/photo/2022/04/18/17/25/artwork-7141103_960_720.png",
        "llama3-8b-8192": "https://cdn.pixabay.com/photo/2022/04/18/17/25/artwork-7141103_960_720.png",
    }

    if model in background_image:
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-size: cover;
                background-image: url("{background_image[model]}");
            }}
            .response-text {{
                font-size: 22px;
                font-weight: bold;
            }}
            </style>
            """,
            unsafe_allow_html=True,
        )

if __name__ == "__main__":
    main()
