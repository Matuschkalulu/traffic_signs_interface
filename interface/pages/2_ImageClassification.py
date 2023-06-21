import streamlit as st
import requests
from PIL import Image
import os
import io
from io import BytesIO
import numpy as np
import cv2

<<<<<<< HEAD
import base64


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('png-clipart-marvel-avengers-illustration-avengers-group-close-up-comics-and-fantasy-various-comics-thumbnail.png')



# for the Streamlit interface
st.title("Traffic Sign Recognition")
st.write("Classify traffic signs in images.")
=======
import subprocess


from io import BytesIO
import numpy as np
import cv2

# for the Streamlit interface
st.title("Traffic Sign Recognition")
st.write("Identify traffic signs in images.")
>>>>>>> main

st.sidebar.image("https://static.vecteezy.com/system/resources/previews/009/458/871/original/traffic-signs-icon-logo-design-template-vector.jpg", width=100)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Loading CSS
<<<<<<< HEAD
url_css = os.path.join(os.getcwd(), 'pages', 'frontend', 'css', 'streamlit.css')
=======
url_css = os.path.join(os.getcwd(),'interface', 'pages', 'frontend', 'css', 'streamlit.css')
>>>>>>> main
local_css(url_css)


def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

# Loading CSS
    local_css("frontend/css/streamlit.css")
<<<<<<< HEAD
=======

>>>>>>> main
    remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

<<<<<<< HEAD
=======
st.markdown('<style>...</style>', unsafe_allow_html=True)


>>>>>>> main

if uploaded_file is not None:
    # displaying the uploaded image
    image = Image.open(uploaded_file)
    print(image)
<<<<<<< HEAD
    st.image(image, width=400, caption="Uploaded Image", use_column_width=True)
    st.markdown("""
    <style>
       {
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
    )
=======
    placeholder = st.image(image, caption="Uploaded Image", use_column_width=True)

>>>>>>> main

    #pred_image = Image.open(io.BytesIO(image_bytes))

    # making a prediction
    if st.button("Classify"):
        # Prepare the image data
        image_data = uploaded_file.getvalue()
        files = {"file": image_data}
        print (files)
        #response = requests.post("https://trafficsignscode-ugznwmrhlq-ew.a.run.app/ImagePrediction/", files=files)
<<<<<<< HEAD
        response = requests.post("http://127.0.0.1:8080/ImagePrediction", files=files)
        print(response)
        if response.status_code == 200:
            # the prediction result
            prediction = response.json()
            #print(prediction)
            st.image(os.path.join(os.getcwd(), 'image0.png'), use_column_width=True)
            if prediction['Actual Prediction Value'][0] >= 0.4:
                st.error('This is an unreadable!') #, icon=f"\N:rotating_light:")
                print(prediction)
            if prediction['Actual Prediction Value'][0] < 0.4:
                st.success('This is a readable!') #icon=f"\N:white_check_mark:")
=======
        response = requests.post("http://localhost:8080/ImagePrediction/", files=files)
        image_path = os.path.join(os.getcwd(),'output_image.png')
        if os.path.exists(image_path):
            os.remove(image_path)


        print(response)
        if response.status_code == 200:
            # the prediction result
            image_bytes = response.content
            placeholder.image(image_bytes, use_column_width=True)

>>>>>>> main
        else:
            st.error("Failed to classify the image. Please try again.")
