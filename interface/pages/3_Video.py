
import streamlit as st
import requests
import os
import base64
import subprocess
import io

# for the Streamlit interface
st.title("Traffic Sign Recognition")
st.write("Identify traffic signs in videos.")

#logo
st.sidebar.image(os.path.join(os.getcwd(),'logo.png'))
# center logo
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Loading CSS
print('Start Loading CSS')
url_css = os.path.join(os.getcwd(), 'interface','pages', 'frontend', 'css', 'streamlit.css')
local_css(url_css)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)
    # Loading CSS
    print('CSS Loading Done')
    local_css("frontend/css/streamlit.css")
    remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

uploaded_file = st.file_uploader("Choose a video...", type=["mp4", "mov", "svi", "mkv"])
st.markdown('<style>...</style>', unsafe_allow_html=True)

video_path = os.path.join(os.getcwd(),'interface/testout_1.mp4')
if os.path.exists(video_path):
    os.remove(video_path)

print('Upload File')
if uploaded_file is not None:
    # displaying the uploaded image
    print('Start Reading File')
    g = io.BytesIO(uploaded_file.read())  ## BytesIO Object
    temporary_location = "interface/testout_simple.mp4"
    with open(temporary_location, 'wb') as out:  ## Open temporary file as bytes
        out.write(g.read())  ## Read bytes into file

    subprocess.run(['ffmpeg', '-i', 'interface/testout_simple.mp4', '-c:v', 'libx264', '-preset', 'slow', '-crf', '22', '-c:a', 'copy', 'interface/testout_1.mp4'])
    print('Start Reading Converted File')
    f= open('interface/testout_1.mp4', 'rb')
    video_bytes = f.read()
    print('Reading Converted File Done')

    print('Start Writing Input File in Bytes')
    placeholder = st.video(video_bytes)
    video_caption = st.markdown("<p style='text-align: center;color : grey;'>Original Video</p>", unsafe_allow_html=True)

    # making a prediction
    if st.button("Traffic Sign Detection", use_container_width=True):
        # Prepare the image data
        files={'file': open('interface/testout_1.mp4', 'rb')}

        print('Start Video Processing')
        #res = requests.post("http://localhost:8000/VideoPrediction", files = files)
        res = requests.post("https://trafficsignscode-ugznwmrhlq-ew.a.run.app/VideoPrediction/", files = files)

        if res.status_code == 200:
            video_bytes = res.content
            with open('myvideo.mp4', 'wb') as f:
                f.write(video_bytes)
            subprocess.run(['ffmpeg', '-i', 'myvideo.mp4', '-c:v', 'libx264', '-preset', 'slow', '-crf', '22', '-c:a', 'copy', 'outputFromStreamlit.mp4'])
            with open('outputFromStreamlit.mp4', 'rb') as f:
                video_bytes = f.read()
            print('Start Writing Output File in Bytes')
            placeholder.video(video_bytes)
            video_caption.markdown("<p style='text-align: center;color : grey;'>Original Video with Detection</p>", unsafe_allow_html=True)
        else:
            st.markdown("**Oops**, something went wrong :sweat: Please try again.")
            print(res.status_code, res.content)

        output_video_path = os.path.join(os.getcwd(),'outputFromStreamlit.mp4')
        if os.path.exists(output_video_path):
            os.remove(output_video_path)

        input_video_path = os.path.join(os.getcwd(),'interface/testout_1.mp4')
        if os.path.exists(input_video_path):
            os.remove(input_video_path)
        print('I am Done!')
