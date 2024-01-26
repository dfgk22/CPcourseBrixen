import streamlit as st
import random
from PIL import Image
from gtts import gTTS
from translate import Translator

st.title("The Ultimate IPA Quiz: Decoding English Words")
st.text("Embark on a linguistic adventure with the immersive IPA (International Phonetic Alphabet) Quiz, designed to challenge and enhance your understanding of English pronunciation")
st.header("Decipher the IPA symbol :uk: :uk: :uk:")
st.write("\n")
st.image(Image.open(f"image/{st.session_state.rand_item}.jpg"), width=300)
st.session_state.user_input = st.text_input("Type in the English word you see in the IPA symbol", key=1)
st.button("Continue", on_click=next_page, disabled=(st.session_state.page > 1))
