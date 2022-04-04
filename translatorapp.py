from googletrans import Translator
import streamlit as st

translator = Translator()

st.title('Translator')

word = st.text_input('Give me a word or a phrase to translate into italian') 

abc = translator.translate(word, dest='it')

st.write('The translation is', abc.text)
