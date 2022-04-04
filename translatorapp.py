import streamlit as st


st.title('Translator')

word = st.text_input('Give me a word or a phrase to translate into Italian') 

abc = Translator.translate(word, dest='it')

st.write('The translation is', abc.text)
