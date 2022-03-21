import streamlit as st
st.header("Hello World!")
st.text("from Brixen")
title = st.text_input('Please insert a film title')
st.write('The current film title is', title)

genre = st.radio("What's your favourite movie genre",('COMEDY', 'DRAMA', 'DOCUMENTARY'))
if genre == 'COMEDY':
  st.write('You selected comedy.')
  else:
    st.write('You didnt')
