import streamlit as st
import requests
import os

# for the Streamlit interface
st.title("Project information")
st.write("About Project.")

#logo
st.sidebar.image("https://i.pinimg.com/474x/bb/7f/49/bb7f49fc358e5b2b45a735d349ded379.jpg", width=200)

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


st.markdown('**Introduction**')
text = '''
<p style="text-align: justify;">
The advancement of autonomous vehicles and smart transportation systems has led to a significant focus on the development of intelligent systems that can detect and interpret traffic signs accurately. Traffic sign recognition plays a crucial role in ensuring road safety, assisting drivers, and enabling autonomous vehicles to navigate effectively. While existing systems have made substantial progress in recognising standard traffic signs, they often struggle with detecting unrecognisable or damaged signs, posing a potential risk on the road. To address this challenge, the Go project introduces a cutting-edge solution called "Detection The Unrecognizable Traffic Sign Recognition."
</p>
'''
st.markdown(text, unsafe_allow_html=True)

st.markdown('**Purpose**')
text = '''
<p style="text-align: justify;">
The primary purpose of the Go project is to develop an advanced system capable of detecting and  interpreting  unrecognizable  traffic  signs on the road.  Unrecognizable  signs can  occur  due  to various factors,  including weathering,  graffiti, partial  obstruction, or damage  caused  by  accidents. Traditional traffic sign recognition algorithms may fail to accurately  interpret  such  signs,  which can lead to incorrect interpretations or complete ignorance of the sign's intended message. The Go project aims to overcome these limitations by leveraging state-of-the-art computer vision techniques, machine learning algorithms, and deep neural networks.
</p>
'''
st.markdown(text, unsafe_allow_html=True)
