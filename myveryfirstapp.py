import streamlit as st
import json, requests
 
APIkey = '84b9d611cf03e3a6ae68ef145b1a6ffc'
location = 'Trento'

url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location +'&appid=' + APIkey + '&lang=it' + '&units=metric'
response = requests.get(url) 
weatherData = json.loads(response.text)

st.text(weatherData['main']['temp_min']) 
