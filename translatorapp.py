import streamlit as st
from googletrans import Translator

translator = Translator()

st.title('Translator')

word = st.text_input('Give me a word or a phrase to translate into Italian', 'word') 


abc = translator.translate(word, dest='it')

st.write('The translation is', abc.text)
