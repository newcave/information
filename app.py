"""KISTI × 도메인 협업 / AI 과학자 국가 미션 — Water Co-Scientist 설득 페이지.

실행: streamlit run app.py
문구·수치·출처 수정은 content.py 에서.
"""
import streamlit as st

from common import inject_css

st.set_page_config(
    page_title="Water Co-Scientist | KISTI 협력 기획",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="collapsed",
)
inject_css()

nav = st.navigation(
    [
        st.Page("views/landscape.py", title="KISTI 협업 지형", icon=":material/hub:", default=True),
        st.Page("views/ai_scientist.py", title="AI 과학자 · 국가 미션", icon=":material/science:"),
    ],
    position="top",
)
nav.run()
