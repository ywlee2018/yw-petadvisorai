from .vector_store import load_vector_store
from .web_search import web_search
from streamlit import session_state as st_session
from langchain.schema import Document


def search_similar_documents(query: str, k: int = 3, score_threshold: float = 0.9) -> list[Document]:
    """
    PDF + DuckDuckGo 웹 검색 모두 실행 후 결과 병합하여 반환
    """
    vectorstore = load_vector_store()
    results_with_score = vectorstore.similarity_search_with_score(query, k=k)

    print(f"\n[📄 PDF 검색 결과 (score 포함)] {len(results_with_score)}건:")
    pdf_docs = []
    for i, (doc, score) in enumerate(results_with_score):
        print(f"  {i+1}. score={score:.2f} / {doc.page_content[:80].replace(chr(10), ' ')}...")
        if score >= score_threshold:
            pdf_docs.append(doc)

    # DuckDuckGo 웹 검색 항상 수행
    print("[🌐 DuckDuckGo 웹 검색 수행 중...]")
    web_results = web_search(query)
    web_docs = []
    for i, item in enumerate(web_results):
        content = item.get("body", "") or item.get("title", "")
        source = item.get("href", "출처 없음")
        print(f"  [웹 {i+1}] {content[:80].replace(chr(10), ' ')}... ({source})")
        web_docs.append(Document(page_content=content, metadata={"source": source}))

    # ✅ PDF + 웹 결과 병합
    merged_docs = pdf_docs + web_docs

    print(f"[✅ 최종 문서 병합 결과] PDF {len(pdf_docs)}건 + 웹 {len(web_docs)}건 → 총 {len(merged_docs)}건")
    st_session["rag_documents"] = merged_docs

    return merged_docs
