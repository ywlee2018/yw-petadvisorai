import streamlit as st
from components.sidebar import render_sidebar
from components.history import render_history_section
from components.qa_display import render_qa
from advisor_agent.agent import get_advisor_response
from database.repository import save_qa
from utils.state_manager import init_session_state
from retrieval.search_service import search_similar_documents
from langchain.schema import Document

# 앱 기본 설정
st.set_page_config(page_title="반려견 상담사", layout="wide")

# 세션 상태 초기화
init_session_state()

# 사이드바 렌더링 (질문 입력 + 히스토리)
user_question = render_sidebar()

if user_question:
    with st.spinner("반려견 상담사가 답변 중입니다..."):
        # ✅ Step 1~2: PDF + DuckDuckGo 병합 검색
        rag_docs = search_similar_documents(user_question)

        # ✅ Step 3: 답변 생성
        response = get_advisor_response(user_question)

    # ✅ Step 4: 답변 출력
    render_qa(question=user_question, answer=response)

    # ✅ Step 5: 참고 자료 출력
    if "rag_documents" in st.session_state:
        documents = st.session_state["rag_documents"]
        if documents:
            with st.expander("📚 참고 자료 확인하기"):
                seen_sources = set()
                index = 1
                for doc in documents:
                    source = doc.metadata.get("source", "출처 없음")
                    if source in seen_sources:
                        continue
                    seen_sources.add(source)

                    if "pet_guide.pdf" in source:
                        filename = source.split("/")[-1]  # ✅ 파일명만 추출
                        st.markdown(f"**📄 문서 {index} (내부 가이드 문서)** 출처:\n`{filename}`")
                    elif "http" in source:
                        st.markdown(f"**🌐 문서 {index} (웹 검색 결과)** 출처:\n[{source}]({source})")
                    else:
                        st.markdown(f"**문서 {index} 출처:** {source}")
                    index += 1
        else:
            st.info("📌 관련된 참고 문서를 찾지 못했습니다.")

    # ✅ Step 6: 히스토리 저장
    save_qa(user_question, response)

    # ✅ Step 7: 세션 상태 업데이트
    st.session_state['last_question'] = user_question
    st.session_state['last_answer'] = response

else:
    st.markdown("## 🐶 반려견 상담사에게 궁금한 점을 물어보세요!")
    st.markdown("사이드바에 질문을 입력하고 **'상담 요청하기'** 버튼을 눌러보세요.")
    st.markdown("예시 질문:")
    st.code("강아지가 밥을 안 먹어요", language="text")
    st.code("자꾸 짖어요", language="text")
    st.code("산책하다가 갑자기 멈춰요", language="text")

# ✅ 이전 상담 히스토리 보기
selected_history = render_history_section()
if selected_history:
    render_qa(selected_history.question, selected_history.answer)
