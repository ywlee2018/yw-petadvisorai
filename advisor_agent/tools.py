# advisor_agent/tools.py

from langchain.tools import Tool

# 간단한 증상 키워드 → 설명 매핑 예시 (데모용)
symptom_database = {
    "긁는다": "반려견이 긁는 행동은 피부 알레르기, 기생충(벼룩/진드기), 건조함 등이 원인일 수 있어요.",
    "짖는다": "짖는 원인은 외부 자극, 분리불안, 사회화 부족 등이 있을 수 있어요.",
    "발 핥기": "스트레스, 습진, 혹은 통증으로 인해 자주 발을 핥을 수 있어요.",
    "음식 거부": "입맛, 건강 문제, 사료 변경 등이 원인일 수 있어요.",
}

def search_symptom_info(symptom: str) -> str:
    """
    증상 키워드를 기반으로 간단한 조언 반환 (데모용 지식 기반).
    """
    for key in symptom_database:
        if key in symptom:
            return symptom_database[key]
    return "해당 증상에 대한 정보가 데이터베이스에 없습니다. 더 자세한 상담이 필요합니다."

# LangChain에서 사용할 수 있는 도구 형태로 등록
symptom_tool = Tool(
    name="증상검색기",
    func=search_symptom_info,
    description="강아지의 증상을 설명하면, 간단한 원인이나 조언을 알려줍니다. 예: '우리 강아지가 계속 긁어요'"
)

def get_advisor_tools():
    """
    LangChain 에이전트에서 사용할 도구 리스트 반환
    """
    return [symptom_tool]
