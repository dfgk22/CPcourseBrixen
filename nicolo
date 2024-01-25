import streamlit as st
import language_tool_python
from gtts import gTTS

def correct_german_text(text):
  tool = language_tool_python.LanguageToolPublicAPI('de-DE')
  return tool.correct(text)

def speak_german_text(mytext):
  tts1=gTTS(text=mytext, lang="de")
  tts1.save('file.mp3')
  audio_file = open("file.mp3", "rb")
  return audio_file

def main():
  st.title("DeutschCoach")
  user_input = st.text_area("Schreib deinen Text hier:", max_chars=500)

  if st.button("Los geht's!"):
    if len(user_input) > 0:
      if len(user_input) > 500:
        st.error("Der Text darf maximal 500 Zeichen lang sein!!")
      else:
        corrected_text = correct_german_text(user_input)
        st.success("Hier findest du deinen korrigierten Text:")
        st.write(corrected_text)
        st.subheader("Klick mal hier unten, um die richtige Aussprache anzuhören!")
        st.audio(data=speak_german_text(corrected_text), format="audio/mp3", start_time=0)

if __name__ == "__main__":
  main()
