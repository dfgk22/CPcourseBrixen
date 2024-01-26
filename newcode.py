import streamlit as st
from g2p_en import G2p
import random

g2p = G2p()

def get_ipa(word):
    return ' '.join(g2p(word.lower()))

def main():
    st.title("Word Guessing Game")

    # Generate a random word
    word_list = ['apple', 'banana', 'chocolate', 'elephant', 'umbrella', 'computer', 'python']
    word = random.choice(word_list)

    # Get IPA pronunciation of the selected word
    ipa = get_ipa(word)

    # User input for word guessing
    guess = st.text_input("Guess the word:")

    # Check if the guessed word is correct
    if guess.lower() == word.lower():
        st.success(f"Correct! The IPA pronunciation is: {ipa}")
        
        # For demonstration purposes, you can add some hardcoded Italian translations
        translations = {
            'apple': 'mela',
            'banana': 'banana',
            'chocolate': 'cioccolato',
            'elephant': 'elefante',
            'umbrella': 'ombrello',
            'computer': 'computer',
            'python': 'pitone',
        }
        
        st.write(f"Translation in Italian: {translations[word]}")
    else:
        st.error(f"Wrong! The correct word is: {word}")
        
        # Show correct pronunciation
        st.write(f"Correct IPA pronunciation: {ipa}")

if __name__ == "__main__":
    main()
