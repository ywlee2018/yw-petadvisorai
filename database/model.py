# database/model.py

from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

# SQLAlchemy 모델 베이스 클래스 생성
Base = declarative_base()

class QAHistory(Base):
    """
    반려견 상담 Q&A 히스토리를 저장하는 테이블 정의
    """
    __tablename__ = "qa_history"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    timestamp = Column(DateTime)
