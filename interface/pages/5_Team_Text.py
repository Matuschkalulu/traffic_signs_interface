import streamlit as st
import requests
import os

st.title("Creatation Team")
st.write("Production Team by")

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

st.image("https://ca.slack-edge.com/T02NE0241-U05400ZCNBG-f02a98a3286d-512", width=200)
st.text_area('Team Leader : Ludwig Matuschka', '''
    info...
    ''', height=100)

st.image("https://ca.slack-edge.com/T02NE0241-U0546A39LD7-ac41db3e2be7-512", width=200)
st.text_area('Team Member : Madhu Jatheendran', '''
    info...
    ''', height=100)

st.image("https://ca.slack-edge.com/T02NE0241-U053L7GSJ14-4fe0152b6753-512", width=200)
st.text_area('Team member : Mohad Aly', '''
    info...
    ''', height=100)

st.image("https://ca.slack-edge.com/T02NE0241-U054G6P4KRR-89bb2943c4be-192", width=200)
st.text_area('Team Members : James Tidsanu Nampradid', '''
    info...
    ''', height=100)
