import streamlit as st
import requests
import os

st.title("Team")

#logo
st.sidebar.image(os.path.join(os.getcwd(),'logo.png'))
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
    st.markdown("<p style='text-align: left;'>Team Leader : Ludwig Matuschka</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left; background-color: #586E75;\
                    border-width:3px; border-radius: 3px;\
                    padding:20px; padding-left:20px; padding-top: 20px;\
                    padding-right: 20px; height: 140px;'>\
                        info ... \
                    </p>", unsafe_allow_html=True)

columns = st.columns(2)
with columns[0]:
    st.image("https://ca.slack-edge.com/T02NE0241-U0546A39LD7-ac41db3e2be7-512", width=200)
with columns[1]:
    st.markdown("<p style='text-align: left;'>Team Member : Madhu Jatheendran</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left;background-color:#586E75;\
                border-width:3px; border-radius: 3px;\
                padding:20px; padding-left:20px; padding-top: 20px;\
                padding-right: 20px; height: 140px;'>\
                    Sometimes I feel like the incredible Hulk! But unfourtunatly I am too calm to ever transform to him\
                        </p>", unsafe_allow_html=True)

columns = st.columns(2)
with columns[0]:
 st.image("https://ca.slack-edge.com/T02NE0241-U053L7GSJ14-4fe0152b6753-512", width=200)
with columns[1]:
    st.markdown("<p style='text-align: left;'>Team Member : Mohamed Aly</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left;background-color:#586E75;\
                border-width:3px; border-radius: 3px;\
                padding:20px; padding-left:20px; padding-top: 20px;\
                padding-right: 20px; height: 140px;'>\
                        MSc theoretical particle physics and data science enthusiast. My best friends\
                        are Kaggle, Stack Overflow, Towards Data Science and recently ChatGPT.\
                </p>", unsafe_allow_html=True)

columns = st.columns(2)
with columns[0]:
   st.image("https://ca.slack-edge.com/T02NE0241-U054G6P4KRR-89bb2943c4be-192", width=200)
with columns[1]:
    st.markdown("<p style='text-align: left;'>Team Member : James Tidsanu Nampradid</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left;background-color:#586E75;\
                border-width:3px; border-radius: 3px;\
                padding:20px; padding-left:20px; padding-top: 20px;\
                padding-right: 20px; height: 140px;'>\
                        I'm the worst person to be stuck with in a traffic jam...\
                        Jokessssss!\
                </p>", unsafe_allow_html=True)
