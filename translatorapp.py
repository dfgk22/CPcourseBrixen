from googletrans import Translator
import streamlit as st

translator = Translator()

word = st.text_input('Give me a word or a phrase to translate, else just type nothing ') 

abc = translator.translate(word)

st.write('The translatoon is', abc.text)
