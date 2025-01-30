import streamlit as st

x = st.slider("x")  # 👈 this is a widget

st.download_button("LABEL", data=f"HELLO PEOPLE {x}!", on_click="ignore")
