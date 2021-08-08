import streamlit as st
import text2emotion as te


st.set_page_config(page_title="Networked Loss",
                   layout="centered",
                   initial_sidebar_state="collapsed")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


st.title('Networked Loss')

with st.form(key='textInput', clear_on_submit=True):
    message = st.text_input(label='Write your message')
    submit = st.form_submit_button(label='Send away')

if submit:
    final_message = f'{message}'
    print(final_message)

    emotion = te.get_emotion(final_message)
    st.write(emotion)
    print(emotion)
