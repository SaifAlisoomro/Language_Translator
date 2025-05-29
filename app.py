import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="AI Language Translator", layout="centered")
st.title("🌍 AI Language Translator")
st.markdown("Developed By : SAIF SOOMRO")

# Text input
text = st.text_area("Enter text to translate:")

# Language options
languages = [
    'english', 'urdu', 'spanish', 'french', 'german',
    'arabic', 'chinese (simplified)', 'hindi', 'italian', 'japanese'
]

target_lang = st.selectbox("Select target language:", languages)

# Translate
if st.button("Translate"):
    if text.strip() != "":
        try:
            translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
            st.success(translated)
        except Exception as e:
            st.error(f"Translation failed: {e}")
    else:
        st.warning("Please enter some text.")
