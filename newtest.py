import streamlit as st
import random
import json, requests
from PIL import Image
from gtts import gTTS
#from googletrans import Translator  #googletrans not working???
from translate import Translator

if "page" not in st.session_state:
  st.session_state.page = 0
if "user_input" not in st.session_state:
  st.session_state.user_input = None
if "rand_item" not in st.session_state:
  st.session_state.rand_item = None
def nextpage():  st.session_state.page += 1
def restart():
    st.session_state.page = 0
    st.session_state.rand_item = random.choice(['woman', 'cloud', 'chair', 'cold', 'heart', 'earth', 'friend', 'mountain', 'mouse', 'snow'])

placeholder = st.empty()
#st.button("NEXT",on_click=nextpage,disabled=(st.session_state.page > 1))

if st.session_state.page == 0:
  items = ['woman', 'cloud', 'chair', 'cold', 'heart', 'earth', 'friend', 'mountain', 'mouse', 'snow']    
  if 'item' not in st.session_state:
    st.session_state.rand_item = random.choice(items)
    st.session_state.item = st.session_state.rand_item
  else:
    rand_item = st.session_state.item
  with placeholder.container():
    st.title("WELCOME TO YOUR APHASIA APP!")
    st.write("\n")
    st.header("What do you see on the picture below?")
    st.write("\n")
    st.write("\n")
    #st.session_state.user_input = st.text_input("Enter the word and press NEXT")
  picture = "image/" + st.session_state.rand_item + '.jpg'
  img = Image.open(picture)
  st.image(img, width=300)
  st.session_state.user_input = st.text_input("Enter the word and press NEXT", key=1)
  st.button("NEXT",on_click=nextpage,disabled=(st.session_state.page > 1))
  

elif st.session_state.page == 1:
  if st.session_state.user_input:
    if st.session_state.user_input.lower() == str(st.session_state.rand_item):
      placeholder.header("Well done! You entered the correct word!")
      st.button("NEXT",on_click=restart,disabled=(st.session_state.page > 1))
    else:
      with placeholder.container():
        picture = "image/" + st.session_state.rand_item + '.jpg'
        img = Image.open(picture)
        st.image(img, width=300)
        st.write("You entered:", st.session_state.user_input)
        st.write("Unfortunately this is incorrect. Hear the pronunciation of the word and try again!.")
        st.write("\n")
        st.write("\n")
        tts=gTTS(text= st.session_state.rand_item, lang='en')
        tts.save('user.mp3')
        st.audio('user.mp3')
        #st.button("NEXT",on_click=nextpage,disabled=(st.session_state.page > 1))
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
            #st.write("Or you can do a NEW EXCERCISE by pressing NEXT.")
            st.button("NEXT",on_click=restart,disabled=(st.session_state.page > 1))
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
