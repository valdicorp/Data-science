import streamlit as st
import speech_recognition as sr

# Define the speech-to-text function
def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Parlez maintenant...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("Vous avez dit :", text)
        return text
    except sr.UnknownValueError:
        print("Je n'ai pas compris votre voix.")
        return None
    except sr.RequestError as e:
        print("Erreur de reconnaissance vocale :", e)
        return None

# Prepare the icon (replace with your actual icon)
icon_html = """
<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-mic">
  <path d="M10 16v-3a6 6 0 0 0-12 0v3m4 0h10a6 6 0 0 1 12 0v-3a6 6 0 0 0-12 0v3z"></path>
</svg>
"""

# Create the text area and button
text = st.text_area("Entrez votre texte ici", height=200)
microphone_button = st.button("Activer le microphone")

# Add the icon to the text area
st.write(icon_html, unsafe_allow_html=True)

# Apply CSS styling (add this to your custom CSS or head section)
st.markdown("""
<style>
  /* Style the text area to allow for icon placement */
  .stTextArea {
    position: relative; /* Enable relative positioning */
  }

  /* Style the icon */
  .icon {
    position: absolute; /* Position the icon absolutely within the text area */
    top: 10px; /* Adjust the top position as needed */
    left: 10px; /* Adjust the left position as needed */
    cursor: pointer; /* Make the icon clickable */
  }

  /* Replace with your icon's specific CSS classes or inline styles */
  .icon svg {
    width: 20px; /* Adjust the icon size as needed */
    height: 20px;
  }

  .icon i {
    font-size: 20px; /* Adjust the icon font size as needed */
  }
</style>
""", unsafe_allow_html=True)

# Handle microphone button click
if microphone_button:
    speech_text = speech_to_text()
    if speech_text:
        text = speech_text  # Update the text area with the recognized speech

# Handle icon click (add your action code here)
# ... Your action code here ...

