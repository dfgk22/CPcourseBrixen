import streamlit as st
st.header("Hello World!")
st.text("from Brixen")
title = st.text_input('Please insert a film title', 'lorem ipsum')
st.write('The current film title is', title)
