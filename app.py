import streamlit as st


st.title("Download Button ignore rerun!")

x = st.slider("LABEL", 0, 100, 50)

button_value = st.download_button(
    "Download button label",
    data=f"JUST {x} DATA STRING!",
    on_click="ignore",
)

st.subheader("Rerun triggers balloons!")
st.balloons()
