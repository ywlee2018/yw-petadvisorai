# components/sidebar.py

import streamlit as st

def render_sidebar() -> str:
    st.sidebar.title("🐶 반려견 상담사")

    # 질문 입력
    user_question = st.sidebar.text_area(
        "반려견에 대해 궁금한 점을 입력해주세요",
        placeholder="예: 우리 강아지가 자꾸 발을 핥아요. 왜 그런 걸까요?",
        height=150
    )

    # 질문 제출 버튼
    submitted = st.sidebar.button("상담 요청하기")

    if submitted and user_question.strip():
        return user_question.strip()
    
    return None
