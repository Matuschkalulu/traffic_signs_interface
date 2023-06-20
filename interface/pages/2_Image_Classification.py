import streamlit as st
import requests
import os

st.title("Traffic Sign Recognition")
st.write("Classification on images")

st.sidebar.image("https://static.vecteezy.com/system/resources/previews/002/538/982/non_2x/traffic-concept-drawing-vector.jpg", width=200)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

# Loading CSS
url_css = os.path.join(os.getcwd(), 'pages', 'frontend', 'css', 'streamlit.css')
local_css(url_css)
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')
