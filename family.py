import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import os
import gtts
from playsound import playsound
from PIL import Image
import Database as db



st.set_page_config(
    page_title="Family Identify"
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.set_option('deprecation.showfileUploaderEncoding', False)


##@st.cache(allow_output_mutation=True)
##@st.cache_data(allow_output_mutation=True)
@st.cache_resource()
def load_model():
    model = tf.keras.models.load_model(os.path.join('model','family_3_1.h5'))
    return model


with st.spinner('Model is being loaded..'):
    model = load_model()

st.write("""
         # Family Identify
         """
         )
##st.camera_input("capture Image",key ="First Camera")

##file = st.file_uploader("", type=["jpg", "png"])
file = st.camera_input("capture Image",key ="First Camera")

def import_and_predict(image_data, model):
    size = (256, 256)
    image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    img = np.asarray(image)
    img_reshape = img[np.newaxis, ...]
    prediction = model.predict(img_reshape)
    return prediction

def plasound():
    playsound("Welcome.mp3")

def savae(sound):
    sound.save("Welcome.mp3")

text=""
if file is None:
    st.text("Make sure face is in frame ")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    predictions = import_and_predict(image, model)
   ## class_names = ['Mansi', 'Parth', 'Premlata']
    class_names = ['Manoj', 'Mansi', 'Parth', 'Premlata']
    string = class_names[np.argmax(predictions)]
    dis=string+" ji"
    st.success(dis)
    if string == 'Parth':
     text="मालिक श्री आपका स्वागत हे ।"
    else:
      if string == 'Premlata' or string == 'Manoj':
            relation = "पुत्र"
      if string == 'Mansi':
            relation = "छोटे भाई"

      text = "नमस्ते! " + string + " जी, यह इंटरफ़ेस आपका हार्दिक अभिनंदन करता हैं , जो आपके "+ relation +" पार्थ गुप्ता के द्वारा बनाया गया है ।"
    ##st.success(text)

    ##playsound(os.path.join('wel.mp3'))
    warn=""
    sph=""
    data = db.getp(string)
    cur_med = data.get("cur_med")
    if cur_med[0] != "no":
     st.warning("MEDICATIONS")
     for x in cur_med:
      sph=sph+x+","
      st.success(x)
     text=text+"हमारे डेटाबेस के हिसाब से आपका उपचार चल रहा है जिसमे दवाई ,"+sph+"का प्रयोग हो रहा है ।"

    ecg = data.get("ecg")
    if ecg != "no":
     st.warning("ECG REPORT")
     link="https://drive.google.com/uc?export=view&id="+ecg
     st.image(link,caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
     text=text+"आपका ईसीजी रिपोर्ट स्क्रीन पर दर्ज करदिया गया  है ।"
    else:
     warn="हमारे पास आपका ईसीजी रिपोर्ट मोजूद नहीं है ।"

    rep = data.get("rep")
    if rep[0] != "no":
     st.warning("REPORTS")
     n=0
     for x in rep:
      n=n+1
      cap="report no-"+ str(n)
      link = "https://drive.google.com/uc?export=view&id=" + x
      st.image(link, caption=cap, width=200, use_column_width=20, clamp=False, channels="RGB", output_format="auto")
     text=text+"आपकी"+str(n)+", रिपोर्ट्स को स्क्रीन पर दर्ज करदिया गया है ।"
    else:
     warn=warn+" हमारे पास आपकी कोई अन्य रिपोर्ट्स मोजूद नहीं है । कृपया जल्द से जल्द रिपोर्ट्स को दर्ज करवाए । "

    text=text+warn;
    text=text+"  ,,हम आपके स्वस्थ रहने की कामना करते है , धन्यवाद ।"
    sound = gtts.gTTS(text,lang='hi')
    sound.save("wel.mp3")
    ##playsound(os.path.join('wel.mp3'))
    st.audio('wel.mp3')

##st.image("https://drive.google.com/uc?export=view&id=1HoFeOPKDReddiq-0SZmSWz49D15pEAYo",caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             
             background-image: url("https://cdn.pixabay.com/photo/2020/12/08/16/54/brain-5814961__340.jpg");
             
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )

add_bg_from_url()
html_link = """

    Made by <a href="/" style="color:green;" target="_blank">Parth Gupta </a>
    """
st.markdown(html_link, unsafe_allow_html=True)