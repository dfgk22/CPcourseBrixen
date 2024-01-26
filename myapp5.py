import streamlit as st
import random
from PIL import Image
from gtts import gTTS
from translate import Translator

# Initialize session state variables
if "page" not in st.session_state:
    st.session_state.page = 0
if "user_input" not in st.session_state:
    st.session_state.user_input = None
if "rand_item" not in st.session_state:
    st.session_state.rand_item = None

# Define functions
def restart():
    st.session_state.page = 0
    st.session_state.rand_item = random.choice(['chair', 'cloud', 'cold', 'earth', 'friend', 'heart', 'mountain', 'mouse', 'snow', 'woman'])

# Main logic
placeholder = st.empty()

if st.session_state.page == 0:
    items = ['chair', 'cloud', 'cold', 'earth', 'friend', 'heart', 'mountain', 'mouse', 'snow', 'woman']
    st.session_state.rand_item = random.choice(items)
    with placeholder.container():
        st.title("The Ultimate IPA Quiz: Decoding English Words")
        st.text("Embark on a linguistic adventure with the immersive IPA (International Phonetic Alphabet) Quiz, designed to challenge and enhance your understanding of English pronunciation")
        st.header("Decipher the IPA symbol :uk: :uk: :uk:")
        st.write("\n")
        st.image(Image.open(f"image/{st.session_state.rand_item}.jpg"), width=300)
        st.session_state.user_input = st.text_input("Type in the English word you see in the IPA symbol", key=1)
        if st.session_state.user_input:
            st.button("Check Answer", disabled=(st.session_state.page > 1))

    if st.session_state.user_input2:
        if st.session_state.user_input2.lower() == str(st.session_state.rand_item):
            st.write(f"Great! That is correct. The word is {st.session_state.rand_item}")
            text_to_translate = str(st.session_state.rand_item)
            translator = Translator(to_lang='it')
            result = Translator.translate(translator, text_to_translate)
            st.write("\n")
            st.write(f"The word '{st.session_state.rand_item}' translates to '{result}' in Italian.")
            st.write("\n")
            st.write("Now you can keep practicing the pronunciation of this word...")
            tts = gTTS(text=st.session_state.rand_item, lang='en')
            tts.save('user.mp3')
            st.audio('user.mp3')
            st.button("Continue", on_click=restart, disabled=(st.session_state.page > 1))
        else:
            text_to_translate = str(st.session_state.rand_item)
            translator = Translator(to_lang='it')
            result = Translator.translate(translator, text_to_translate)
            st.write(f"Sorry, but {st.session_state.user_input2} is not correct either. The correct word is {st.session_state.rand_item}.")
            st.write(f"'{st.session_state.rand_item}' translates to '{result}' in Italian.")
            st.write("Make sure to practice by pronouncing this word with the audio.")
            tts = gTTS(text=st.session_state.rand_item, lang='en')
            tts.save('user.mp3')
            st.audio('user.mp3')

else:
    with placeholder.container():
        st.header("Well done! You completed this exercise. If you want to continue practicing, click on the NEW EXERCISE button")
        st.button("NEW EXERCISE", on_click=restart)
