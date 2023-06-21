import streamlit as st
import requests
import os
import base64
import subprocess
import io
from ffmpeg import FFmpeg, Progress
#Comment for Git

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

# for the Streamlit interface
st.title("Traffic Sign Recognition")
st.write("Identify traffic signs in videos.")

#logo
st.sidebar.image("https://static.vecteezy.com/system/resources/previews/009/458/871/original/traffic-signs-icon-logo-design-template-vector.jpg", width=100)

# center logo
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Loading CSS
url_css = os.path.join(os.getcwd(), 'pages', 'frontend', 'css', 'streamlit.css')
local_css(url_css)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

# Loading CSS

remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')
uploaded_file = st.file_uploader("Choose a video...", type=["mp4", "mov", "svi", "mkv"])
st.markdown('<style>...</style>', unsafe_allow_html=True)


if uploaded_file is not None:
    # displaying the uploaded image
    #video_file = open(uploaded_file, 'rb')
    #video_bytes = uploaded_file.read()
    #st.video(video_bytes)
    g = io.BytesIO(uploaded_file.read())  ## BytesIO Object
    temporary_location = "testout_simple.mp4"
    #print (g)
    #subprocess.run(['ffmpeg', '-i', 'testout_simple.mp4', '-c:v', 'libx264', '-preset', 'slow', '-crf', '22', '-c:a', 'copy', 'testout_simple.mp4'])
    with open(temporary_location, 'wb') as out:  ## Open temporary file as bytes
        out.write(g.read())  ## Read bytes into file
    f= open('testout_simple.mp4', 'rb')
    video_bytes = f.read()
    st.video(video_bytes)

    # making a prediction

    if st.button("Classify"):
        # Prepare the image data
        video_data = uploaded_file.read()
        video_file_buffer = uploaded_file
        if video_file_buffer is not None:
            col1, col2 = st.columns(2)
        with col1:
            st.video(video_file_buffer)
        with col2:
            with st.spinner("Labeling signs ..."):
                # img_bytes = img_file_buffer.getvalue()
                video_data=uploaded_file.getvalue()
                files={'video': video_data}
                res = requests.post("http://127.0.0.1:8000/VideoPrediction", files=files)
                video_path = os.path.join(os.getcwd(),'outputFromStreamlit.mp4')
                if os.path.exists(video_path):
                    os.remove(video_path)

                if res.status_code == 200:
                    video_bytes = res.content
                    with open('myvideo.mp4', 'wb') as f:
                        f.write(video_bytes)
                    subprocess.run(['ffmpeg', '-i', 'myvideo.mp4', '-c:v', 'libx264', '-preset', 'slow', '-crf', '22', '-c:a', 'copy', 'outputFromStreamlit.mp4'])
                    with open('outputFromStreamlit.mp4', 'rb') as f:
                        video_bytes = f.read()
                    st.video(video_bytes)
                else:
                    st.markdown("**Oops**, something went wrong :sweat: Please try again.")
                    print(res.status_code, res.content)
