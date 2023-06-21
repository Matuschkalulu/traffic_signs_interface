import streamlit as st
import requests
import os

st.title("CREATOR TEAM")
st.write("PRODUCTION TEAM BY")

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

columns = st.columns(2)
with columns[0]:
 st.image("https://ca.slack-edge.com/T02NE0241-U05400ZCNBG-f02a98a3286d-512", width=200)
with columns[1]:
  st.markdown('**Team Leader : Ludwig Matuschka**')
  text = '''
  <p style="text-align: justify;">
  write here...
  </p>
  '''
  st.markdown(text, unsafe_allow_html=True)


columns = st.columns(2)
with columns[0]:
 st.image("https://ca.slack-edge.com/T02NE0241-U0546A39LD7-ac41db3e2be7-512", width=200)
with columns[1]:
  st.markdown('**Team Member : Madhu Jatheendran**')
  text = '''
  <p style="text-align: justify;">
  write here...
  </p>
  '''
  st.markdown(text, unsafe_allow_html=True)

columns = st.columns(2)
with columns[0]:
  st.image("https://ca.slack-edge.com/T02NE0241-U053L7GSJ14-4fe0152b6753-512", width=200)
with columns[1]:
  st.markdown('**Team member : Mohad Aly**')
  text = '''
  <p style="text-align: justify;">
  write here...
  </p>
  '''
  st.markdown(text, unsafe_allow_html=True)

columns = st.columns(2)
with columns[0]:
    st.image("https://ca.slack-edge.com/T02NE0241-U054G6P4KRR-89bb2943c4be-192", width=200)
with columns[1]:
    st.markdown('**Team Members: James Tidsanu Nampradid**')
    text = '''
    <p style="text-align: justify;">
    I am the worst person to be stuck in traffic
    </p>
    '''
    st.markdown(text, unsafe_allow_html=True)
