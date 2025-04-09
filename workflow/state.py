# workflow/state.py

from typing import TypedDict, List, Optional

class GraphState(TypedDict):
    """
    LangGraph의 공유 상태 정의
    """
    question: str                          # 사용자 질문
    use_rag: bool                          # RAG 사용 여부
    documents: Optional[List[str]]        # 검색된 문서들
    answer: Optional[str]                 # 최종 상담 응답
