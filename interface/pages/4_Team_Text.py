import streamlit as st
import os

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


st.title("Traffic Sign Recognition")
st.write("Production Team by")

st.sidebar.image("https://static.vecteezy.com/system/resources/previews/009/458/871/original/traffic-signs-icon-logo-design-template-vector.jpg", width=100)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

url_css = os.path.join(os.getcwd(), 'pages','frontend', 'css', 'streamlit.css')
local_css(url_css)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

# Loading CSS
local_css("frontend/css/streamlit.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

st.text_area('Team Leader : Ludwig Matuschka', '''
    info...
    ''')

st.text_area('Team Member : Madhu Jatheendran', '''
    info...
    ''')

st.text_area('Team member : Mohad Aly', '''
    info...
    ''')

st.text_area('Team Members : James Tidsanu Nampradid', '''
    info...
    ''')
