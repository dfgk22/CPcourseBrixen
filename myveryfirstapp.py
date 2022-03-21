import streamlit as st
import json, requests
 
APIkey = '84b9d611cf03e3a6ae68ef145b1a6ffc'
location = st.radio("Please select a city:",('Trento', 'Bolzano', 'Rome', 'Naples', 'Milan'))

url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location +'&appid=' + APIkey + '&lang=it' + '&units=metric'
response = requests.get(url) 
weatherData = json.loads(response.text)

st.header('This is the weather forecast for ' + location + ' today')
st.metric(label="Temperature", value=str(weatherData['main']['temp']))
st.text('The current temperature for ' + location + ' is ' + str(weatherData['main']['temp']) + 'ºC')
st.text('The minimun temperature for ' + location + ' will be ' + str(weatherData['main']['temp_min']) + 'ºC')
st.text('The maximun temperature for ' + location + ' will be ' + str(weatherData['main']['temp_max']) + 'ºC')
