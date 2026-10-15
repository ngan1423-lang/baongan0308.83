import streamlit as st

st.title("Ứng dụng của Bảo Ngân")
st.write("Chào mừng bạn đến với ứng dụng của tôi!")

ten = st.text_input("Nhập tên của bạn")

if ten:
    st.success(f"Xin chào {ten}!")
