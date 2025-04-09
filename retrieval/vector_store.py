from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import AzureOpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.schema import Document

from utils.config import (
    AOAI_ENDPOINT,
    AOAI_API_KEY,
    DEPLOY_EMBED_3_SMALL,
)

import os
from pathlib import Path

# 벡터스토어 저장 위치 및 PDF 경로
VECTOR_STORE_DIR = "./vector_store"
PDF_PATH = "./retrieval/docs/pet_guide.pdf"

# ✅ 1. 임베딩 모델 설정 (chunk_size 제거)
def get_embedding_model():
    return AzureOpenAIEmbeddings(
        azure_endpoint=AOAI_ENDPOINT,
        api_key=AOAI_API_KEY,
        api_version="2023-07-01-preview",
        model=DEPLOY_EMBED_3_SMALL
    )

# ✅ 2. PDF 기반 벡터스토어 생성 (source 메타데이터 포함)
def create_vector_store_from_pdf():
    # 1. PDF 문서 로드
    loader = PyPDFLoader(PDF_PATH)
    raw_docs = loader.load()

    # 2. 텍스트 분할 (짧고 빠른 처리용)
    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    split_docs = splitter.split_documents(raw_docs)

    # 3. 각 문서에 source 메타데이터 추가
    for doc in split_docs:
        doc.metadata["source"] = os.path.basename(PDF_PATH)  # 경로 숨기고 파일명만 표시

    # 4. 임베딩 및 벡터스토어 생성
    embeddings = get_embedding_model()
    vectorstore = FAISS.from_documents(
        split_docs,
        embedding=embeddings,
        normalize_L2=True  # ✅ similarity_search_with_score용
    )

    # 5. 저장
    Path(VECTOR_STORE_DIR).mkdir(parents=True, exist_ok=True)
    vectorstore.save_local(VECTOR_STORE_DIR)
    print("✅ PDF 기반 벡터스토어 생성 완료")

# ✅ 3. 벡터스토어 로딩
def load_vector_store() -> FAISS:
    embeddings = get_embedding_model()
    return FAISS.load_local(
        VECTOR_STORE_DIR,
        embeddings,
        allow_dangerous_deserialization=True
    )
