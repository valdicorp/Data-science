import streamlit as st
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from PIL import Image
from nltk.stem import WordNetLemmatizer
import string
# foction de clean
def clean_text(text):
    # suppression des caracteres speciaux et des ponctuations
    text=re.sub(r"[^\w\s]","",text)
    text = text.lower()  # Convertit le texte en minuscules
    text = re.sub('\[.*?\]', '', text)  # Supprime le texte entre crochets
    text = re.sub("\\W"," ", text)  # Remplace les non-alphanumériques par des espaces
    text = re.sub('https?://\S+|www\.\S+', '', text)  # Supprime les URLs
    text = re.sub('<.*?>+', '', text)  # Supprime les balises HTML
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)  # Supprime la ponctuation
    text = re.sub('\n', '', text)  # Supprime les nouvelles lignes
    text = re.sub('\w*\d\w*', '', text)  # Supprime les mots contenant des chiffres
    
    # traduction
    
    #Tokenisation
    tokens=word_tokenize(text)
    # lematisation
    tokens2=[]
    for i in tokens:
        lem1=WordNetLemmatizer().lemmatize(i,pos='v')
        lem2=WordNetLemmatizer().lemmatize(lem1,pos='s')
        lem=WordNetLemmatizer().lemmatize(lem2,pos='a')
        tokens2.append(lem)
    tokens=tokens2
    
    #suppresiion des mots vides
    stop_words=[]
    tokens=[word for word in tokens if word not in stop_words]
    
    #joindre les token en une seul chaine
    cleaned_text=' '.join(tokens)
    
    return cleaned_text

#model load
model=joblib.load(filename="sentiment.joblib")
vectorizer=joblib.load(filename="vectorizer.joblib")
# text prediction
def sentiment_prediction(text):
    text_clean=clean_text(text)
    text_final=vectorizer.transform([text_clean])
    text_final=text_final.toarray()
    prediction=model.predict(text_final)
    return prediction[0]

image2 = Image.open("ia8.png")
resized_image = image2.resize((300, 300))
# visuel
st.image(resized_image )
st.title("Application de prediction des sentiments")
st.write(("cette application permet de predire le sentiment qui se degage d'une phrase : sentiment positif ou negatif"))
text = st.text_input("Entrer un text en anglais :", placeholder="exemple:I am feeling very sad and alone right now.")
button_clicked = st.button("Prediction")



image1 = Image.open("joy2.jfif")
image3 = Image.open("bad3.jfif")
if button_clicked:
  pred=sentiment_prediction(text)
  if pred==1:
     st.write('cette phrase degage un sentiment positif 😊')
     st.image(image1)
  else:
     st.write('cette phrase degage un sentiment negatif😒')
     st.image(image3)