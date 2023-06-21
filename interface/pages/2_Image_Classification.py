import streamlit as st
import requests
import os

st.title("Traffic Sign Recognition")
st.write("Detecting traffic signs")

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

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

with st.columns(2)[0]:

# image is uploading
 if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

    api_endpoint = " "
    files = {'image': uploaded_file}

    # making API request
    response = requests.post(api_endpoint, files=files)

    # check the api
    if response.status_code == 200:
        result = response.json()

        # Display result
        st.write("### Detection Result")
        st.write(f"Is registration image: {result['is_registration_image']}")
        st.write(f"Confidence: {result['confidence']}")
