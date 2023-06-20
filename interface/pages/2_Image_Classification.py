import streamlit as st
import requests
import os

st.title("Creatation Team")
st.write("Production Team by")

#logo
st.sidebar.image("https://static.vecteezy.com/system/resources/previews/002/538/982/non_2x/traffic-concept-drawing-vector.jpg", width=200)

# center logo
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

# Loading CSS
url_css = os.path.join(os.getcwd(),'interface', 'pages', 'frontend', 'css', 'streamlit.css')
local_css(url_css)

# Loading CSS
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')
