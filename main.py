import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Metehan Demirkol")
    content = """
    Hi, I am Metehan! I am Python programmer,and GIS Analyst. I graduated in 2015 in Survey Engineer field.I have
    worked with companies from various countries.
    
    """

    st.info(content)

content2 = """
Below you can find some of the app I have built in Python.Feel free to contact me!
"""

st.write(content2)


col3,col4 = st.columns(2)
df = pandas.read_csv("data.csv",sep=";")

with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])