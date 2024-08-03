import streamlit as st 



with open("testimageabstract.png", "rb") as file:
    st.download_button(
        label="Download image",
        data=file,
        file_name="testimageofabstractpainting.png"
    )