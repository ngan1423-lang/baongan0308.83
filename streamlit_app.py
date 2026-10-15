import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Rắn Săn Mồi",
    page_icon="🐍",
    layout="wide"
)

st.title("🐍 Rắn Săn Mồi")
st.write("Dùng các phím mũi tên để điều khiển rắn!")

st.info(
    "Đây là khung ứng dụng Streamlit. "
    "Bước tiếp theo cần đưa mã HTML/CSS/JavaScript "
    "đầy đủ của game vào ứng dụng."
)
