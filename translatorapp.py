import streamlit as st
from googletrans import Translator

translator = Translator()

st.title('Translator')

word = st.text_input('Give me a word or a phrase to translate into Italian', '') 

if word != '':
  lang = st.text_input('Give me a target language', '') 
  if lang != '':
    abc = translator.translate(word, dest='lang')
    st.write('The translation is', abc.text)
