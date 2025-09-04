# app.py
import streamlit as st
from chatbot import HiringAssistantChatbot
from data_handler import DataHandler
from textblob import TextBlob
from googletrans import Translator

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(page_title="💼 TalentScout – AI Hiring Assistant", page_icon="🤖", layout="wide")

# ----------------------------
# Init Session State
# ----------------------------
if "chatbot" not in st.session_state:
    st.session_state.chatbot = HiringAssistantChatbot()

if "data_handler" not in st.session_state:
    st.session_state.data_handler = DataHandler()

if "history" not in st.session_state:
    st.session_state.history = []

if "initialized" not in st.session_state:
    st.session_state.history.append(("Bot", "👋 Please type 'hi' to start."))
    st.session_state.initialized = True

if "language" not in st.session_state:
    st.session_state.language = "en"  # default English

if "username" not in st.session_state:
    st.session_state.username = None

translator = Translator()

# ----------------------------
# Sidebar Controls
# ----------------------------
st.sidebar.header("⚙️ Chat Settings")
lang_choice = st.sidebar.selectbox("🌍 Language", ["English", "French", "German", "Spanish", "Telugu", "Hindi"])
lang_map = {
    "English": "en",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Telugu": "te",
    "Hindi": "hi"
}
st.session_state.language = lang_map[lang_choice]

# ----------------------------
# Main Title
# ----------------------------
st.title("💼 TalentScout – AI Hiring Assistant 🤖")
st.caption("Your personal HR assistant to collect candidate details & generate tailored questions.")

# ----------------------------
# Input Form
# ----------------------------
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("💬 Type your message:", key="user_message")
    submit = st.form_submit_button("Send")

if submit and user_input:
    # Translate input to English if needed
    if st.session_state.language != "en":
        translated = translator.translate(user_input, src=st.session_state.language, dest="en").text
    else:
        translated = user_input

    # Process message with chatbot
    response = st.session_state.chatbot.process_message(
        translated, context=None, data_handler=st.session_state.data_handler
    )

    # Sentiment Analysis
    sentiment = TextBlob(translated).sentiment.polarity
    if sentiment > 0.2:
        response += "\n\n🙂 I sense positive vibes!"
    elif sentiment < -0.2:
        response += "\n\n😟 I sense some concerns. Don’t worry, I’ll guide you through."

    # Personalization: Add candidate's name if known
    if st.session_state.chatbot.candidate_info.get("full_name") and not st.session_state.username:
        st.session_state.username = st.session_state.chatbot.candidate_info["full_name"]
    if st.session_state.username:
        response = f"{st.session_state.username}, {response}"

    # Translate response back to selected language
    if st.session_state.language != "en":
        response = translator.translate(response, src="en", dest=st.session_state.language).text

    # Save history
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", response))

# ----------------------------
# Conversation Display (Dark Mode)
# ----------------------------
for sender, msg in st.session_state.history:
    st.markdown(f"""
    <div style='background:black; color:white; padding:10px; border-radius:10px; margin:5px 0;'>
    <b>{'🧑 You' if sender == 'You' else '🤖 Bot'}:</b> {msg}
    </div>
    """, unsafe_allow_html=True)

