import json,requests
from pprint import pprint

keyword=input('plz give me a keyword ')
url= 'https://api.datamuse.com/words?sl=' + keyword + '&max=10'


response = requests.get(url)   

dataFromDatamuse = json.loads(response.text) 

pprint(dataFromDatamuse[0:4])#if you just want to see the first 9 results

option = st.selectbox('How would you like to be contacted?', ('Email', 'Home phone', 'Mobile phone’))
st.write('You selected:', option):
                                                               
                                                               
