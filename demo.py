from track import *
import tempfile
import cv2
import torch
import streamlit as st
import os


if __name__ == '__main__':
    st.set_page_config(
    page_title="车辆计数DEMO",
    page_icon="🚗",)
    st.write("# :rainbow[车辆计数 DEMO] 🚗")
    st.sidebar.markdown("# :rainbow[车辆计数 DEMO简介]")
    st.sidebar.markdown("这是一个基于YOLOv5和Deepsort的车辆计数项目🏄‍♂️")
    st.sidebar.markdown("你可以自行上传视频，系统会实时计数并在统计完成时保存视频🤩")
    st.sidebar.markdown("除此之外，你还可以手动选择想要统计的车辆种类，调整检测置信度与检测线位置🤗")
    st.sidebar.markdown('---') 
    # upload video
    video_file_buffer = st.sidebar.file_uploader("请上传视频", type=['mp4', 'mov', 'avi'])

    if video_file_buffer:
        st.sidebar.text('输入视频')
        st.sidebar.video(video_file_buffer)
        # save video from streamlit into "videos" folder for future detect
        with open(os.path.join('videos', video_file_buffer.name), 'wb') as f:
            f.write(video_file_buffer.getbuffer())

    st.sidebar.markdown('---')
    st.sidebar.title('设置')
    # custom class
    custom_class = st.sidebar.checkbox('自定义类别')
    assigned_class_id = [0, 1, 2, 3]
    names = ['car', 'motorcycle', 'truck', 'bus']

    if custom_class:
        assigned_class_id = []
        assigned_class = st.sidebar.multiselect('选择自定义类', list(names))
        for each in assigned_class:
            assigned_class_id.append(names.index(each))
    
    # st.write(assigned_class_id)

    # setting hyperparameter
    confidence = st.sidebar.slider('置信度', min_value=0.0, max_value=1.0, value=0.5)
    line = st.sidebar.number_input('检测线位置', min_value=0.0, max_value=1.0, value=0.6, step=0.1)
    st.sidebar.markdown('---')

    
    status = st.empty()
    stframe = st.empty()
    if video_file_buffer is None:
        status.markdown('<font size= "4"> **Status:** Waiting for input </font>', unsafe_allow_html=True)
    else:
        status.markdown('<font size= "4"> **Status:** Ready </font>', unsafe_allow_html=True)

    car, bus, truck, motor = st.columns(4)
    with car:
        st.markdown('**Car**')
        car_text = st.markdown('__')
    
    with bus:
        st.markdown('**Bus**')
        bus_text = st.markdown('__')

    with truck:
        st.markdown('**Truck**')
        truck_text = st.markdown('__')
    
    with motor:
        st.markdown('**Motorcycle**')
        motor_text = st.markdown('__')

    fps, _,  _, _  = st.columns(4)
    with fps:
        st.markdown('**FPS**')
        fps_text = st.markdown('__')


    track_button = st.sidebar.button('START')
    # reset_button = st.sidebar.button('RESET ID')
    if track_button:
        # reset ID and count from 0
        reset()
        opt = parse_opt()
        opt.conf_thres = confidence
        opt.source = f'videos/{video_file_buffer.name}'

        status.markdown('<font size= "4"> **Status:** Running... </font>', unsafe_allow_html=True)
        with torch.no_grad():
            detect(opt, stframe, car_text, bus_text, truck_text, motor_text, line, fps_text, assigned_class_id)
        status.markdown('<font size= "4"> **Status:** Finished ! </font>', unsafe_allow_html=True)
        # end_noti = st.markdown('<center style="color: blue"> FINISH </center>',  unsafe_allow_html=True)

    # if reset_button:
        # reset()
    #     st.markdown('<h3 style="color: blue"> Reseted ID </h3>', unsafe_allow_html=True)
