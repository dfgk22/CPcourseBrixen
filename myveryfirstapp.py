import streamlit as st
import json, requests

st.title('Welcome to the weather forecast app')
st.title('Welcome to the weather forecast')
APIkey = '84b9d611cf03e3a6ae68ef145b1a6ffc'
location = st.radio("Please select a city:",('Trento', 'Bolzano', 'Rome', 'Naples', 'Monteforte Irpino'))

url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location +'&appid=' + APIkey + '&lang=it' + '&units=metric'
response = requests.get(url) 
weatherData = json.loads(response.text)
st.header('This is the weather forecast for ' + location + ' today')
col1, col2, col3 = st.columns(3)
col1.metric(label="Current Temperature", value=str(weatherData['main']['temp']) + 'ºC')
col2.metric(label="Minimum Temperature", value=str(weatherData['main']['temp_min']) + 'ºC')
col3.metric(label="Maximum Temperature", value=str(weatherData['main']['temp_max']) + 'ºC')
