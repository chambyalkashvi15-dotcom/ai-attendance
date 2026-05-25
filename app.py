import streamlit as st
def main():
    st.header("this is title")
    name=st.text_input('Enter your name:')
    st.button('Display my name',type='primary') 
    