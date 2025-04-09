# retrieval/web_search.py

from duckduckgo_search import DDGS

def web_search(query: str, max_results: int = 3) -> list[dict]:
    """
    DuckDuckGo를 통해 외부 검색 결과를 가져옵니다.
    각 결과는 title, href, body를 포함한 dict 형태로 반환됩니다.
    """
    results = []

    try:
        with DDGS() as ddgs:
            search_results = ddgs.text(
                query,
                region="kr-kr",              # 한국 지역 설정
                safesearch="Moderate",       # 적절한 수위의 결과만 표시
                max_results=max_results
            )

            for r in search_results:
                title = r.get("title")
                href = r.get("href")
                body = r.get("body", "")

                if title and href:
                    results.append({
                        "title": title.strip(),
                        "href": href.strip(),
                        "body": body.strip()
                    })

    except Exception as e:
        print(f"[⚠️ DuckDuckGo Web Search Error]: {e}")

    return results
