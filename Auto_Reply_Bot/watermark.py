import streamlit as st

def add_watermark():
    st.markdown("""
    <div style='text-align: center; padding: 10px; background-color: #1e1e1e; border-radius: 10px; margin-top: 20px; color: #f0f0f0;'>
        <h4 style='margin: 0; color: #ff4b4b;'>🔮 Built by <span style='color:#f0f0f0;'>Sonu Kumar Sharma</span></h4>
        <a href='https://www.linkedin.com/in/sonukumars' target='_blank' style='color: #4ea1ff;'>LinkedIn</a> |
        <a href='https://github.com/Golu1464' target='_blank' style='color: #4ea1ff;'>GitHub</a> |
        <a href='https://instagram.com/sonukumars' target='_blank' style='color: #4ea1ff;'>Instagram</a>
    </div>
    """, unsafe_allow_html=True)
