## For the following piece of code, I took inspiration and had help from many many people. 
## I would like to acknowledge the help of my classmates, Eleonora, Nicolò, Darline, and Filippo for their ideas and codes
## Also, people that helped me put everything together and debug issues that were not working at the beginning: Javier, Tiago and Enrico.
## Special thanks to my wife Cristina for her support whenever the code did not work
## Also, here are some possible references form the several pages, forums, and videos I watched in order to assemble everything together:
## https://pypi.org/project/pillow/8.4.0/
## https://github.com/streamlit/streamlit/issues/4420
## https://pypi.org/project/translate/
## https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/app-dependencies
## https://gtts.readthedocs.io/en/latest/module.html
## https://docs.streamlit.io/library/api-reference/media/st.audio
## https://docs.streamlit.io/library/api-reference

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

# Define function
def restart():
    st.session_state.rand_item = random.choice(['bus',
                                                'blue',
                                                'cat',
                                                'chair',
                                                'chameleon',
                                                'child',
                                                'choir',
                                                'coffee',
                                                'cloud',
                                                'cold',
                                                'colonel',
                                                'computer',
                                                'earth',
                                                'english'
                                                'friend',
                                                'heart',
                                                'honey',
                                                'image',
                                                'jealous',
                                                'learner',
                                                'leisure',
                                                'money',
                                                'moon',
                                                'mountain', 
                                                'mouse',
                                                'phone',
                                                'photo',
                                                'post',
                                                'queue',
                                                'squirrel',
                                                'street',
                                                'through',
                                                'time',
                                                'tongue',
                                                'train',
                                                'vulnerable', 
                                                'woman'
                                                'yacht',
                                                'yellow'])

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
st.image(img, width=400)

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
