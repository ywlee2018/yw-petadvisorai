# utils/state_manager.py

import streamlit as st

def init_session_state():
    """
    Streamlit 세션 상태를 초기화합니다.
    """
    if "question" not in st.session_state:
        st.session_state["question"] = ""

    if "answer" not in st.session_state:
        st.session_state["answer"] = ""

    if "use_rag" not in st.session_state:
        st.session_state["use_rag"] = True  # 기본값: RAG 활성화

    if "last_question" not in st.session_state:
        st.session_state["last_question"] = ""

    if "last_answer" not in st.session_state:
        st.session_state["last_answer"] = ""
