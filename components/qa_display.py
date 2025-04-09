# components/qa_display.py

import streamlit as st

def render_qa(question: str, answer: str):
    st.markdown("---")
    
    # 사용자 질문
    with st.container():
        st.markdown(
            f"""
            <div style='
                background-color: #e0f7fa;
                padding: 1rem;
                border-radius: 10px;
                margin-bottom: 1rem;
                max-width: 80%;
            '>
                <strong>🙋 사용자:</strong><br>{question}
            </div>
            """,
            unsafe_allow_html=True
        )

    # 상담사 응답
    with st.container():
        st.markdown(
            f"""
            <div style='
                background-color: #f1f8e9;
                padding: 1rem;
                border-radius: 10px;
                margin-bottom: 1rem;
                max-width: 80%;
            '>
                <strong>🐶 반려견 상담사:</strong><br>{answer}
            </div>
            """,
            unsafe_allow_html=True
        )
