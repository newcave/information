"""KISTI × 도메인 협업 / AI 과학자 국가 미션 — Water Co-Scientist 설득 페이지.

실행: streamlit run app.py
문구·수치·출처 수정은 content.py 에서.
"""
import importlib

import streamlit as st

import common
import content

# Streamlit Cloud는 수정된 보조 모듈을 다시 읽지 않고 예전 버전을 쓰는 경우가 있어,
# 매 실행마다 content·common 을 새로 읽어 옵니다.
importlib.reload(content)
importlib.reload(common)
from common import inject_css  # noqa: E402

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
        st.Page("views/team.py", title="4인 협업 구상", icon=":material/groups:"),
    ],
    position="top",
)
nav.run()
