# advisor_agent/prompt.py

def get_system_prompt() -> str:
    """
    AI 반려견 상담사의 역할을 정의하는 시스템 메시지.
    """
    return (
        "당신은 경험 많고 친절한 반려견 상담사입니다. "
        "사용자의 질문에 대해 이해하기 쉽게 설명하고, 필요한 경우 건강, 행동, 식습관 등 다양한 측면을 함께 고려하여 조언해주세요. "
        "전문 용어는 피하고, 보호자가 실천할 수 있는 구체적인 방법을 제시해주세요."
    )

def build_rag_prompt(context_documents: list[str], user_question: str) -> str:
    """
    RAG용 프롬프트 구성: 검색된 문서를 참고로 포함하여 질문에 답할 수 있도록 구성.
    """
    context = "\n\n".join(context_documents)
    
    return (
        f"다음은 반려견 관련 배경 정보입니다:\n"
        f"{context}\n\n"
        f"위 정보를 참고하여 다음 질문에 답변해주세요:\n{user_question}"
    )
