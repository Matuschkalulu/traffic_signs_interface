import streamlit as st
import requests
from PIL import Image
import os
from io import BytesIO
import numpy as np


# for the Streamlit interface
st.sidebar.image(os.path.join(os.getcwd(),'logo.png'))
st.markdown("<h1 style='text-align: center;'>Traffic Sign Detection</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Is the sign readable or not?</h2>", unsafe_allow_html=True)



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

st.image(os.path.join(os.getcwd(),'1_Image.png'), use_column_width=True)
