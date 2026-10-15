import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Rắn Săn Mồi",
    page_icon="🐍",
    layout="wide"
)

st.title("🐍 Rắn Săn Mồi")

game_path = Path(__file__).parent / "game.html"

if game_path.exists():
    html_code = game_path.read_text(encoding="utf-8")
    components.html(
        html_code,
        height=750,
        scrolling=True
    )
else:
    st.error("Không tìm thấy file game.html!")
    import base64

with open("Tôi thấy hoa vàng trên cỏ xanh.mp3", "rb") as f:
  st.audio("Tôi thấy hoa vàng trên cỏ xanh.mp3", format="audio/mp3")
    
