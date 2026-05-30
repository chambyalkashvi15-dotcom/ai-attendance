import streamlit as st

def header_home():
    logo_url = "https://d33wubrfki0l68.cloudfront.net/0a8c67db73d10c46937fb6dc239895bbb7bb4efc/9b527/assets/img/logos/custom/snapclass-logo.png"
    st.markdown(f"""
      <div style= "display:flex; flex-direction:column; items-align:center; justify-content:center; margin-bottom=30px; ">
           <img src= '{logo_url}' style='height:100px;'/>
           <h1 style=' text-align:center; color: #E0E3FF'>SNAP<br/> CLASS </h1>
      </div>
    """, unsafe_allow_html=True)
    
