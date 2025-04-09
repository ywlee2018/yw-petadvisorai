# workflow/graph.py

from langgraph.graph import StateGraph
from workflow.state import GraphState
from workflow.node import (
    input_node,
    rag_node,
    advisor_node,
    save_node,
    should_use_rag
)

def create_advisor_graph() -> StateGraph:
    """
    LangGraph 기반 반려견 상담 플로우 정의
    """

    graph = StateGraph(GraphState)

    # 노드 추가
    graph.add_node("입력", input_node)
    graph.add_node("RAG검색", rag_node)
    graph.add_node("상담응답", advisor_node)
    graph.add_node("저장", save_node)

    # 기본 플로우
    graph.set_entry_point("입력")
    graph.add_conditional_edges(
        "입력",
        should_use_rag,
        {
            "use_rag": "RAG검색",
            "no_rag": "상담응답"
        }
    )
    graph.add_edge("RAG검색", "상담응답")
    graph.add_edge("상담응답", "저장")
    graph.set_finish_point("저장")

    return graph
