import streamlit as st
import requests
from PIL import Image
import os
from io import BytesIO
import numpy as np


# for the Streamlit interface
st.title("Traffic Sign Recognition")
st.write("Identify traffic signs in images.")

st.sidebar.image("https://i.pinimg.com/474x/bb/7f/49/bb7f49fc358e5b2b45a735d349ded379.jpg", width=200)

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

st.image('https://cdn-icons-png.flaticon.com/512/2555/2555555.png')
