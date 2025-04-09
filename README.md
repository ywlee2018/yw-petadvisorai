# 반려견 상담사 AI

반려견 관련 고민을 자연어로 입력하면, 내부 PDF 가이드 문서와 인터넷 검색 결과를 바탕으로 적절한 조언을 제공하는 RAG 기반 상담 챗봇입니다.

## 기능 소개

- PDF 문서 기반 검색 (FAISS + Azure OpenAI Embedding)
- DuckDuckGo를 통한 웹 문서 검색 (fallback 또는 병합)
- GPT-4o 기반 자연스러운 답변 생성
- 출처 정보 표시 (내부 문서 / 웹 문서 구분)
- 스트림릿 기반 대화형 UI
- 질문-응답 히스토리 저장

## 기술 스택

- LangChain
- Azure OpenAI (GPT-4o, Embedding)
- FAISS
- DuckDuckGo Search API
- Streamlit

## 프로젝트 구조

pet_advisor/
├── advisor_agent/
│   └── agent.py
├── components/
│   ├── history.py
│   ├── qa_display.py
│   └── sidebar.py
├── database/
│   └── repository.py
├── retrieval/
│   ├── docs/
│   │   └── pet_guide.pdf
│   ├── search_service.py
│   ├── vector_store.py
│   └── web_search.py
├── utils/
│   ├── config.py
│   └── state_manager.py
├── vector_store/                # FAISS 인덱스 저장 경로
├── .env                         # 환경 변수 설정
├── init_vector_store.py         # 벡터스토어 초기화
├── main.py                      # Streamlit 앱 메인
├── requirements.txt
└── README.md
