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
    st.session_state.rand_item = random.choice(['chair', 'street', 'earth', 'friend', 'heart', 'mountain', 'mouse', 'snow', 'woman'])

# Load a random word when the app starts
if st.session_state.rand_item is None:
    restart()

# Display quiz elements
st.header(':red[The English IPA Quiz:] :blue[_Decoding Words_]', divider='rainbow')
st.write("\n")
st.write("\n")
st.subheader(':blue[Embark on a linguistic adventure with the _immersive IPA (International Phonetic Alphabet) Quiz_] :red[designed to challenge and enhance your understanding of _British English pronunciation_]')
st.write("\n")
st.write("\n")
expander = st.expander("As a brief recall, click here to see what symbols mean in the IPA ")
expander.write("""
    This table shows the phonemic chart of English sounds:
""")
expander.image("https://www.englishclub.com/images/pronunciation/Phonemic-Chart.jpg")
st.write("\n")
st.write("\n")
st.subheader(":uk: :uk: :uk: Let's go! :uk: :uk: :uk:", divider='grey')
st.subheader(':blue[Decipher the] :red[IPA symbol]')
st.write("\n")
st.write("\n")

# Load and display the image for the current word
picture = "image/" + st.session_state.rand_item + '.jpg'
img = Image.open(picture)
st.image(img, width=500)

# User input for the English word
st.session_state.user_input = st.text_input("Type in the English word you see in the IPA symbol. **Remember to first press Enter and then click on Continue.**", key=1)

# Continue button
if st.button("Continue"):
    # Check if the user input is correct
    if st.session_state.user_input and st.session_state.user_input.lower() == str(st.session_state.rand_item):
        text_to_translate = str(st.session_state.rand_item)
        translator = Translator(to_lang='it')
        result = Translator.translate(translator, text_to_translate)

        placeholder = st.empty()
        with placeholder.container():
            st.title(":blue[Great job! That is correct!] :star-struck: :tada: :confetti_ball:")
            st.write("The word '", st.session_state.rand_item, "' translates to '", result, "' in Italian.")
            st.write("Now you can practice the pronunciation of this word. Click on the **play button** to listen to the associated sound.")
            tts = gTTS(text=st.session_state.rand_item, lang='en', tld='co.uk')
            tts.save('user.mp3')
            st.audio('user.mp3')
            st.write("**Well done! If you want to keep practising, just refresh this page.**")

        # Load a new random word for the next question
        restart()

    else:
        text_to_translate = str(st.session_state.rand_item)
        translator = Translator(to_lang='it')
        result = Translator.translate(translator, text_to_translate)

        placeholder = st.empty()
        with placeholder.container():
            st.title(":red[Unfortunately, that is incorrect] :slightly_frowning_face:")
            st.write("The correct word was '", st.session_state.rand_item, "'.")
            st.write("The word '", st.session_state.rand_item, "' translates to '", result, "' in Italian.")
            st.write("Now you can practice the pronunciation of this word. Click on the **play button** to listen to the associated sound.")
            tts = gTTS(text=st.session_state.rand_item, lang='en', tld='co.uk')
            tts.save('user.mp3')
            st.audio('user.mp3')
            st.write("**Well done! If you want to keep practising, just refresh this page.**")

        # Load a new random word for the next question
        restart()
