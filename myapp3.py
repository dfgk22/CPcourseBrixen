import streamlit as st
import random
from PIL import Image
from gtts import gTTS
from translate import Translator

#Define functions
def nextpage():
  st.session_state.page += 1
def restart():
  st.session_state.page = 0
  st.session_state.rand_item = random.choice(['chair', 'cloud', 'cold', 'earth', 'friend', 'heart', 'mountain', 'mouse', 'snow', 'woman'])


st.title("The Ultimate IPA Quiz: Decoding English Words lalala")
st.write("\n")
st.text("Embark on a linguistic adventure with the immersive IPA (International Phonetic Alphabet) Quiz, designed to challenge and enhance your understanding of English pronunciation")
st.write("\n")
st.header("Decipher the IPA symbol :uk: :uk: :uk:")
st.write("\n")
st.write("\n")
picture = "image/" + st.session_state.rand_item + '.jpg'
img = Image.open(picture)
st.image(img, width=300)
st.session_state.user_input = st.text_input("Type in the English word you see in the IPA symbol", key=1)
st.button("Continue",on_click=nextpage,disabled=(st.session_state.page > 1))
  

if st.session_state.page == 1:
  if st.session_state.user_input:
    if st.session_state.user_input.lower() == str(st.session_state.rand_item):
      placeholder.header("Great job! Ready for the next challenge?")
      st.button("I'm on!",on_click=restart,disabled=(st.session_state.page > 1))
    else:
      with placeholder.container():
        picture = "image/" + st.session_state.rand_item + '.jpg'
        img = Image.open(picture)
        st.image(img, width=300)
        st.write("You entered:", st.session_state.user_input)
        st.write("Oops! Take a moment to hear the word and try again")
        st.write("\n")
        st.write("\n")
        tts=gTTS(text= st.session_state.rand_item, lang='en')
        tts.save('user.mp3')
        st.audio('user.mp3')
        st.session_state.user_input2 = st.text_input("Enter the word and press Enter", key=2)
        if st.session_state.user_input2:
          if st.session_state.user_input2.lower() == str(st.session_state.rand_item):
            st.write("Great! That is correct. The word is " ,st.session_state.rand_item)
            text_to_translate = str(st.session_state.rand_item)
            translator = Translator(to_lang='it')
            result = Translator.translate(translator, text_to_translate)
            st.write("\n")
            st.write("The word '", st.session_state.rand_item,"' translates to '",result,"' in italian.")
            st.write("\n")
            st.write("Now you can keep practicing the pronunciation of this word...")
            tts=gTTS(text= st.session_state.rand_item, lang='en')
            tts.save('user.mp3')
            st.audio('user.mp3')
            st.button("Continue",on_click=restart,disabled=(st.session_state.page > 1))
          else:
            text_to_translate = str(st.session_state.rand_item)
            translator = Translator(to_lang='it')
            result = Translator.translate(translator, text_to_translate)
            st.write("Sorry, but ",st.session_state.user_input2,"is not correct either. The correct word is " ,st.session_state.rand_item,".")
            st.write("'",st.session_state.rand_item,"' translates to '",result,"' in italian.")
            st.write("Make sure to practice by pronouncing this word with the audio.")
            tts=gTTS(text= st.session_state.rand_item, lang='en')
            tts.save('user.mp3')
            st.audio('user.mp3')
              

else:
    with placeholder.container():
        st.header("Well done! You completed this exercise. If you want to continue practicing, click on the NEW EXERCISE button")
        st.button("NEW EXERCISE",on_click=restart)