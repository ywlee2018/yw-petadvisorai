from langchain_openai import AzureChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from retrieval.search_service import search_similar_documents
from utils.config import AOAI_ENDPOINT, AOAI_API_KEY, DEPLOY_GPT4O
from openai import BadRequestError
import traceback

def get_advisor_response(user_input: str) -> str:
    # 🔍 관련 문서 검색 (PDF + 웹)
    documents = search_similar_documents(user_input)

    # 🔸 문서 내용 추출
    context_text = "\n\n".join([doc.page_content for doc in documents]) if documents else "관련 정보 없음"

    # ✅ AzureChatOpenAI 인스턴스 생성
    llm = AzureChatOpenAI(
        azure_endpoint=AOAI_ENDPOINT,
        api_key=AOAI_API_KEY,
        api_version="2023-07-01-preview",
        model=DEPLOY_GPT4O,
        temperature=0.7,
    )

    # 🔸 시스템 프롬프트 구성
    system_prompt = (
        "당신은 친절하고 경험 많은 반려견 상담사입니다. "
        "사용자의 질문에 대해 아래 문서를 참고하여 구체적이고 실용적인 조언을 제공하세요. "
        "너무 전문적인 용어는 피하고, 보호자가 바로 실천할 수 있는 방식으로 설명해주세요.\n\n"
        "단, 다음과 같은 민감하거나 부적절한 주제에 대해서는 절대 답변하지 마세요:\n"
        "- 성적 내용, 음란물\n"
        "- 자해/자살 관련 내용\n"
        "- 폭력 또는 학대 행위\n"
        "- 법적으로 문제가 될 수 있는 정보\n\n"
        "이러한 주제가 포함된 경우에는 정중하게 다음과 같이 응답하세요:\n"
        "'죄송합니다. 해당 주제에 대해서는 안내해 드릴 수 없습니다.'\n\n"
        f"### 참고 문서:\n{context_text}"
    )

    # 🔸 메시지 구성
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_input)
    ]

    # 🔸 응답 생성 (콘텐츠 필터링 예외 처리 포함)
    try:
        response = llm.invoke(messages)
        return response.content

    except BadRequestError as e:
        if "content_filter" in str(e):
            print("🚫 [Azure OpenAI 필터링 차단됨] 사용자 입력:", user_input)
            traceback.print_exc()
            return (
                "⚠️ 죄송합니다. 이 질문은 OpenAI 정책상 안내해 드릴 수 없습니다.\n"
                "반려견에 대한 다른 궁금한 점이 있으시면 알려주세요! 😊"
            )
        else:
            print("⚠️ [LLM 요청 오류] 예상치 못한 예외 발생")
            traceback.print_exc()
            return "⚠️ 예상치 못한 문제가 발생했습니다. 다시 시도해주세요."

