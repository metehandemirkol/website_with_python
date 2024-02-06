import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key = "email_forms"):
    user_email = st.text_input("Your email address")
    user_topic = st.selectbox("What topic do you want to discuss?",('Job Inquiries','Project Proposals','Other'))
    message = st.text_area("Your message")
    message = message + "\n" + user_email
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)