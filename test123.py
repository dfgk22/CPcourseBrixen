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

# Function to get a random item
def get_random_item():
    items = ['chair', 'cold', 'earth', 'friend', 'heart', 'mountain', 'mouse', 'snow', 'woman']
    return random.choice(items)

# Function to display image
def display_image(item):
    picture = f"image/{item}.jpg"
    img = Image.open(picture)
    st.image(img, width=300)

# Function to translate text and save audio
def translate_and_save_audio(item):
    text_to_translate = str(item)
    translator = Translator(to_lang='it')
    result = Translator.translate(translator, text_to_translate)

    tts = gTTS(text=item, lang='en')
    tts.save('user.mp3')
    st.audio('user.mp3')

    return result

# Function to handle page 0
def handle_page_0():
    st.title("The Ultimate IPA Quiz: Decoding English Words")
    st.write("\n")
    st.text("Embark on a linguistic adventure with the immersive IPA (International Phonetic Alphabet) Quiz, designed to challenge and enhance your understanding of English pronunciation")
    st.write("\n")
    st.header("Decipher the IPA symbol :uk: :uk: :uk:")
    st.write("\n")
    st.write("\n")

# Function to handle page 1
def handle_page_1():
    if st.session_state.user_input:
        if st.session_state.user_input.lower() == str(st.session_state.rand_item):
            # ... (rest of your correct answer code)
            text_to_translate = str(st.session_state.rand_item)
            translator = Translator(to_lang='it')
            result = Translator.translate(translator, text_to_translate)
            picture = "image/" + st.session_state.rand_item + '.jpg'
            img = Image.open(picture)
            st.image(img, width=300)
            placeholder.header("Great job! That is correct!.")
            st.write("The word '",st.session_state.rand_item,"' translates to '",result,"' in italian.")
            st.write("Now you can practice the pronunciation of this word")
            tts=gTTS(text= st.session_state.rand_item, lang='en')
            tts.save('user.mp3')
            st.audio('user.mp3')
        else:
            # ... (rest of your incorrect answer code)
            text_to_translate = str(st.session_state.rand_item)
            translator = Translator(to_lang='it')
            result = Translator.translate(translator, text_to_translate)
            picture = "image/" + st.session_state.rand_item + '.jpg'
            img = Image.open(picture)
            st.image(img, width=300)
            placeholder.header("Unfortunately, that is not correct.")
            st.write("The correct word was '",st.session_state.rand_item,"'.")
            st.write("The word '",st.session_state.rand_item,"' translates to '",result,"' in italian.")
            st.write("Now you can practice the pronunciation of this word")
            tts=gTTS(text= st.session_state.rand_item, lang='en')
            tts.save('user.mp3')
            st.audio('user.mp3')

# Main code
placeholder = st.empty()

if st.session_state.page == 0:
    st.session_state.rand_item = get_random_item()
    st.session_state.item = st.session_state.rand_item

    handle_page_0()

    display_image(st.session_state.rand_item)

    st.session_state.user_input = st.text_input("Type in the English word you see in the IPA symbol", key=1)
    st.button("Continue", on_click=nextpage, disabled=(st.session_state.page > 1))

elif st.session_state.page == 1:
    handle_page_1()
