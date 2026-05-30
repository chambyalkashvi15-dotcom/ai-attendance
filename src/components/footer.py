import streamlit as st

def footer_home():
    logo_url = "https://d33wubrfki0l68.cloudfront.net/0a8c67db73d10c46937fb6dc239895bbb7bb4efc/9b527/assets/img/logos/custom/snapclass-logo.png"
    st.markdown(f"""
      <div style= "margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
           <p style="font-weight:bold; color:white; ">Created with ❤️ by </p>
           <img src='{logo_url}' style='max-height:25px'/>
      </div>
    """, unsafe_allow_html=True)