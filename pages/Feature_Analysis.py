import streamlit as st

st.set_page_config(
    page_title="人脸对比",
    page_icon="👋",
)

st.write("# :rainbow[Try Face Analysis by Yourself]👋")


option1 = st.selectbox(
'How would like to Input Picture1?',
('upload', 'camera'))

if option1 == "camera":
    picture1 = st.camera_input("Take a picture1")   

if option1 == "upload":
    picture1  = st.file_uploader("Choose a file1")
    
if picture1:
    st.image(picture1)


st.sidebar.success("点击上方体验不同功能")

