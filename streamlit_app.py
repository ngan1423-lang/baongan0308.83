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
import streamlit as st

with open("Tôi thấy hoa vàng trên cỏ xanh.mp3", "rb") as f:
    audio_bytes = f.read()

audio_base64 = base64.b64encode(audio_bytes).decode()

st.markdown(
    f"""
    <audio controls loop>
        <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mpeg">
    </audio>
    """,
    unsafe_allow_html=True
)
