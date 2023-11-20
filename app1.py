import streamlit as st 
from PIL import Image

st.title("Welcome To My First App")
img = Image.open("chiwendu.jpg")
st.sidebar.image(img)

col1, col2 = st.columns(2)

with col1: 
    st.number_input("How old are you?", step=1)
    st.selectbox("Title",["Mr","Mrs","Miss"])
    st.text_input("Name")

with col2:
    st.text_area("Address")
    st.sidebar.radio("Gender",["Male","Female","Others"])
    st.sidebar.checkbox("Agree")
    st.balloons()
    st.button("Calculate")
    st.spinner("In Progress")