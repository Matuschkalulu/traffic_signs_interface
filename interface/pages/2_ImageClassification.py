import streamlit as st
import requests
from PIL import Image
import os
import subprocess
from io import BytesIO
import numpy as np
import cv2

# for the Streamlit interface
st.title("Traffic Sign Recognition")
st.write("Identify traffic signs in images.")

st.sidebar.image("https://static.vecteezy.com/system/resources/previews/009/458/871/original/traffic-signs-icon-logo-design-template-vector.jpg", width=100)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Loading CSS
url_css = os.path.join(os.getcwd(),'interface', 'pages', 'frontend', 'css', 'streamlit.css')
local_css(url_css)


def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

# Loading CSS
    local_css("frontend/css/streamlit.css")
    remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

st.markdown('<style>...</style>', unsafe_allow_html=True)


if uploaded_file is not None:
    # displaying the uploaded image
    image = Image.open(uploaded_file)
    print(image)
    placeholder = st.image(image, caption="Uploaded Image", use_column_width=True)
    #pred_image = Image.open(io.BytesIO(image_bytes))

    # making a prediction
    if st.button("Classify"):
        # Prepare the image data
        image_data = uploaded_file.getvalue()
        files = {"file": image_data}
        print (files)
        #response = requests.post("https://trafficsignscode-ugznwmrhlq-ew.a.run.app/ImagePrediction/", files=files)
        response = requests.post("http://localhost:8080/ImagePrediction/", files=files)
        image_path = os.path.join(os.getcwd(),'output_image.png')
        if os.path.exists(image_path):
                    os.remove(image_path)
        print(response)
        if response.status_code == 200:
            # the prediction result
            image_bytes = response.content
            placeholder.image(image_bytes, use_column_width=True)
        else:
            st.error("Failed to classify the image. Please try again.")
