import streamlit as st
import json, requests
 
APIkey = '84b9d611cf03e3a6ae68ef145b1a6ffc'
location = st.text_input('Please enter a city', '<Enter the city name here>')

url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location +'&appid=' + APIkey + '&lang=it' + '&units=metric'
response = requests.get(url) 
weatherData = json.loads(response.text)

st.header('This is the weather forecast for ' + location + ' for today')
st.text('The minimun temperature for ' + location + ' will be ' + str(weatherData['main']['temp_min']) + 'ºC')
st.text('The maximun temperature for ' + location + ' will be ' + str(weatherData['main']['temp_max']) + 'ºC')
