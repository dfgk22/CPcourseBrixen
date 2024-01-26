import streamlit as st
import random
from PIL import Image
from gtts import gTTS
from translate import Translator

# List of image filenames in your GitHub repository
image_filenames = [
    "https://raw.githubusercontent.com/dfgk22/CPcourseBrixen/main/chair.jpg",
    "https://raw.githubusercontent.com/dfgk22/CPcourseBrixen/main/cloud.jpg",
    "https://raw.githubusercontent.com/dfgk22/CPcourseBrixen/main/woman.jpg",
]

def get_random_image_filename():
    return random.choice(image_filenames)

if "user_input" not in st.session_state:
    st.session_state.user_input = None

st.title("Guess the Word Quiz")

image_filename = get_random_image_filename()

img = Image.open(image_filename)
st.image(img, caption="Guess the word", use_column_width=True)

st.session_state.user_input = st.text_input("Type in your guess:")

# Check answer
if st.session_state.user_input:
    correct_words = ["chair", "cloud", "woman"]

    if st.session_state.user_input.lower() in correct_words:
        st.success("Congratulations! You guessed it right.")
        correct_word = st.session_state.user_input

        text_to_translate = correct_word
        translator = Translator(to_lang='it')
        result = Translator.translate(translator, text_to_translate)
        st.write(f"The word '{correct_word}' translates to '{result}' in Italian.")

        tts = gTTS(text=correct_word, lang='en')
        tts.save('pronunciation.mp3')
        st.audio('pronunciation.mp3', format='audio/mp3')
    else:
        st.error(f"Sorry, your guess '{st.session_state.user_input}' is incorrect.")
        st.write(f"The correct words are: {', '.join(correct_words)}.")

        for correct_word in correct_words:
            text_to_translate = correct_word
            translator = Translator(to_lang='it')
            result = Translator.translate(translator, text_to_translate)
            st.write(f"'{correct_word}' translates to '{result}' in Italian.")

        tts = gTTS(text=correct_word, lang='en')
        tts.save('pronunciation.mp3')
        st.audio('pronunciation.mp3', format='audio/mp3')
