import speech_recognition as sr
import streamlit as st


def vocale():
    rec=sr.Recognizer()
    mic=sr.Microphone()

    with mic as src:
        audio=rec.listen(src)
        text=rec.recognize_google(audio,language="fr-FR")
        # print(text)
    return text
col1, col2 = st.columns(2)  # Create two columns with equal width

with col1:
    st.write("Contenu dans la colonne 1")  # Place elements in column 1

with col2:
    st.button('button')
voice=st.button('voice')

if voice :
    st.write(vocale())