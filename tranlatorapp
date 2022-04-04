from googletrans import Translator

translator = Translator()

while True:
  word = input('Give me a word or a phrase to translate, else just type nothing ') 
  if word == 'nothing':
    print('okay bye!')
    break
  destlang = input('Tell e a two letter code for the destination language like es or en: ')
  abc = translator.translate(word, dest=destlang)
  print('The translatoon is', abc.text)
