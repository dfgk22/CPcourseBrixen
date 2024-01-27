import streamlit as st
import random
from PIL import Image
from gtts import gTTS
from translate import Translator

# Initialize session state variables
if "user_input" not in st.session_state:
    st.session_state.user_input = None
if "rand_item" not in st.session_state:
    st.session_state.rand_item = None

# Define functions
def restart():
    st.session_state.rand_item = random.choice(['chair', 'cold', 'earth', 'friend', 'heart', 'mountain', 'mouse', 'snow', 'woman'])

# Load a random word when the app starts
if st.session_state.rand_item is None:
    restart()

# Display quiz elements
st.title("The Ultimate IPA Quiz: Decoding English Words")
st.write("\n")
st.text("Embark on a linguistic adventure with the immersive IPA (International Phonetic Alphabet) Quiz, designed to challenge and enhance your understanding of English pronunciation")
st.write("\n")
st.header("Decipher the IPA symbol :uk: :uk: :uk:")
st.write("\n")
st.write("\n")

# Load and display the image for the current word
picture = "image/" + st.session_state.rand_item + '.jpg'
img = Image.open(picture)
st.image(img, width=300)

# User input for the English word
st.session_state.user_input = st.text_input("Type in the English word you see in the IPA symbol", key=1)

# Continue button
if st.button("Continue"):
    # Check if the user input is correct
    if st.session_state.user_input and st.session_state.user_input.lower() == str(st.session_state.rand_item):
        text_to_translate = str(st.session_state.rand_item)
        translator = Translator(to_lang='it')
        result = Translator.translate(translator, text_to_translate)

        placeholder = st.empty()
        with placeholder.container():
            st.title("Great job! That is correct!.")
            st.write("The word '", st.session_state.rand_item, "' translates to '", result, "' in Italian.")
            st.write("Now you can practice the pronunciation of this word")
            tts = gTTS(text=st.session_state.rand_item, lang='en')
            tts.save('user.mp3')
            st.audio('user.mp3')

        # Load a new random word for the next question
        restart()

    else:
        text_to_translate = str(st.session_state.rand_item)
        translator = Translator(to_lang='it')
        result = Translator.translate(translator, text_to_translate)

        placeholder = st.empty()
        with placeholder.container():
            st.title("Unfortunately, that is not correct.")
            st.write("The correct word was '", st.session_state.rand_item, "'.")
            st.write("The word '", st.session_state.rand_item, "' translates to '", result, "' in Italian.")
            st.write("Now you can practice the pronunciation of this word")
            tts = gTTS(text=st.session_state.rand_item, lang='en')
            tts.save('user.mp3')
            st.audio('user.mp3')

        # Load a new random word for the next question
        restart()
