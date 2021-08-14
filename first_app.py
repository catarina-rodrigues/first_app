import streamlit as st
import text2emotion as te
from pythonosc.udp_client import SimpleUDPClient
import socket


host_name = socket.gethostbyname(socket.gethostname())
print(host_name)
st.write(host_name)

ip = "192.168.0.4"  # update to ip of exhibition wifi
port = 12345
client = SimpleUDPClient(ip, port)

st.set_page_config(page_title="Networked Veil",
                   layout="centered",
                   initial_sidebar_state="collapsed")

hide_streamlit_style = """
            <style>
            # MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.caption('Welcome to')
st.title('Networked Veil')

with st.form(key='textInput', clear_on_submit=True):
    message = st.text_input(label='Write your message')
    submit = st.form_submit_button(label='Send away')

emotion = ''

if submit:
    final_message = f'{message}'
    emotion = te.get_emotion(final_message)
    st.write(emotion)
    print(emotion)
    values = list(emotion.values())
    client.send_message("/happy", values[0])
    client.send_message("/angry", values[1])
    client.send_message("/surprise", values[2])
    client.send_message("/sad", values[3])
    client.send_message("/fear", values[4])
