import streamlit as st

st.set_page_config(
    page_title="人脸对比",
    page_icon="👋",
)


st.write("# :rainbow[Try Our Face Comparision Demo]👋")

st.sidebar.success("点击上方体验不同功能")

st.markdown(
"""
本项目是一款基于科大讯飞API开发的人脸识别小程序
"""
)


col1, col2 = st.columns(2)
  
with col1:
    option1 = st.selectbox(
    'How would like to Input Picture1?',
    ('upload', 'camera'))

    if option1 == "camera":
        picture1 = st.camera_input("Take a picture1")   
    
    if option1 == "upload":
        picture1  = st.file_uploader("Choose a file1")
        
    if picture1:
        st.image(picture1)

with col2:
    option2 = st.selectbox(
    'How would like to Input Picture2?',
    ('upload', 'camera'))
    
    if option2 == "camera":
        picture2 = st.camera_input("Take a picture2")   
        
    if option2 == "upload":
        picture2  = st.file_uploader("Choose a file2")
        
    if picture2:
        st.image(picture2)

        