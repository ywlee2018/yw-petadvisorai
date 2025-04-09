# database/repository.py

from .model import QAHistory
from .session import get_session
from sqlalchemy.orm import Session
from datetime import datetime

def save_qa(question: str, answer: str):
    """
    질문과 응답을 DB에 저장합니다.
    """
    session: Session = get_session()
    qa = QAHistory(
        question=question,
        answer=answer,
        timestamp=datetime.utcnow()
    )
    session.add(qa)
    session.commit()

def get_all_qa():
    """
    저장된 모든 Q&A를 리스트로 반환합니다.
    """
    session: Session = get_session()
    return session.query(QAHistory).order_by(QAHistory.timestamp.desc()).all()
