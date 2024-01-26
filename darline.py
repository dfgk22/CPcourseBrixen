import streamlit as st
import random
import json, requests
from PIL import Image
from gtts import gTTS

if "page" not in st.session_state:
  st.session_state.page = 0
if "user_input" not in st.session_state:
  st.session_state.user_input = None
if "rand_item" not in st.session_state:
  st.session_state.rand_item = None
def nextpage():  st.session_state.page += 1
def restart():
    st.session_state.page = 0
    st.session_state.rand_item = random.choice(['woman', 'cloud', 'chair', 'friend', 'mountain', 'heart', 'earth', 'snow', 'mouse', 'cold'])

placeholder = st.empty()
#st.button("NEXT",on_click=nextpage,disabled=(st.session_state.page > 1))

if st.session_state.page == 0:
  items = ['woman', 'cloud', 'chair', 'friend', 'mountain', 'heart', 'earth', 'snow', 'mouse', 'cold']    
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
  st.session_state.user_input = st.text_input("Enter the word and press NEXT")
  st.button("NEXT",on_click=nextpage,disabled=(st.session_state.page > 1))
  

elif st.session_state.page == 1:
  if st.session_state.user_input:
    if st.session_state.user_input.lower() == str(st.session_state.rand_item):
      placeholder.header("Well done! You entered the correct word!")
      st.button("NEXT",on_click=nextpage,disabled=(st.session_state.page > 1))
    else:
      with placeholder.container():
        picture = "image/" + st.session_state.rand_item + '.jpg'
        img = Image.open(picture)
        st.image(img, width=300)
        st.write("You entered:", st.session_state.user_input)
        st.write("Unfortunately this is incorrect. Get a hint below.")
        st.write("\n")
        st.write("\n")
        option = st.selectbox("Choose one for help", ["None selected. Select your hint", "It is another word for", "It sounds like", "Similar in meaning to", "It rhymes with"])

        if option:
            key_dict = {"It is another word for": "rel_syn", "It sounds like": "sl", "Similar in meaning to": "ml", "It rhymes with": "rel_rhy"}
            key = key_dict[option] if option in key_dict else None

            if key:
                keyword = st.session_state.rand_item
                url = 'https://api.datamuse.com/words?' + key + "=" + keyword
                response = requests.get(url)
                dataFromDatamuse = json.loads(response.text)
                st.write(dataFromDatamuse[0]["word"])
            
                st.write("\n")
                st.write("Still no idea? Choose another hint!")
                st.write("\n")
                st.session_state.user_input2 = st.text_input("Or try again and enter the word")
                if st.session_state.user_input2:
                    #st.write("You entered:",st.session_state.user_input2)
                    if st.session_state.user_input2.lower() == str(st.session_state.rand_item):
                        st.write("Super!" "You entered:",st.session_state.user_input2, "This is the correct word!")
                        st.write("Finally, let us speak the word together. Please press the play button below")
                        tts=gTTS(text= st.session_state.rand_item, lang='en')
                        tts.save('user.mp3')
                        st.audio('user.mp3')
                        st.button("NEXT",on_click=nextpage,disabled=(st.session_state.page > 1))
                    else:
                        st.write("Unfortunately, this is incorrect again. The word starts with the letter", st.session_state.rand_item[0])
                        st.session_state.user_input3 = st.text_input("This is the last chance, enter the word here")
                        if st.session_state.user_input3:
                          #st.write("You entered:",st.session_state.user_input3)
                          if st.session_state.user_input3.lower() == str(st.session_state.rand_item):
                                        st.write("Super! You entered:",st.session_state.user_input3, "This is the correct word!")
                                        st.write("Finally, let us speak the word together. Please press the play button below")
                                        tts=gTTS(text= st.session_state.rand_item, lang='en')
                                        tts.save('user.mp3')
                                        st.audio('user.mp3')
                                        st.button("NEXT",on_click=nextpage,disabled=(st.session_state.page > 1))
                          else:
                            st.write("Unfortunately this is incorrect again. The word was: ", st.session_state.rand_item)
                            st.write("Nevertheless, let us speak the word together. Please press the play button below")
                            tts=gTTS(text= st.session_state.rand_item, lang='en')
                            tts.save('user.mp3')
                            st.audio('user.mp3')
                            st.button("NEXT",on_click=nextpage,disabled=(st.session_state.page > 1))
                        
                        


else:
    with placeholder.container():
        st.header("Well done! You completed this exercise. If you want to continue practicing, click on the NEW EXERCISE button")
        st.button("NEW EXERCISE",on_click=restart)
