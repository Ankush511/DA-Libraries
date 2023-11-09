import streamlit as st
import pandas as pd

st.subheader('Loading the CSV file')
df = st.file_uploader('Upload the CSV file : ', type=['csv','xlsx'])


st.subheader('Displaying the CSV file')
df = pd.read_csv('/Users/Ankush/Desktop/Data Science/Streamlit/Products.csv')

if df is not None:
    st.table(df.head())


st.subheader('Displaying the images while uploading')
img_file = st.file_uploader('Upload the Image file : ', type=['png','jpeg'])
if img_file is not None:
    st.image(img_file)

st.subheader('Displaying the images directly')
st.image('/Users/Ankush/Desktop/Data Science/Streamlit/img.png')


st.subheader('Working with video files')
vid_file = st.file_uploader('Upload the Video file : ', type=['mkv','mp4'])
if vid_file is not None:
    st.video(vid_file, start_time=5)


st.subheader('Working with audio files')
aud_file = st.file_uploader('Upload the Audio file : ', type=['mp3'])
if aud_file is not None:
    st.audio(aud_file)
