# components/history.py

import streamlit as st
from database.repository import get_all_qa

def render_history_section():
    """
    사이드바에서 히스토리 목록 보여주고 선택된 질문 반환
    """
    st.sidebar.markdown("---")
    st.sidebar.subheader("📜 이전 상담 기록")

    history_items = get_all_qa()

    if not history_items:
        st.sidebar.write("저장된 상담 기록이 없습니다.")
        return None

    options = [f"{i.timestamp.strftime('%Y-%m-%d %H:%M')} - {i.question[:20]}..." for i in history_items]
    selected = st.sidebar.selectbox("상담 기록 선택", [""] + options)

    if selected and selected != "":
        index = options.index(selected)
        return history_items[index]  # 선택된 QAHistory 객체 반환

    return None
