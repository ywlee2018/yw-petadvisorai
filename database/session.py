# database/session.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLite DB 연결
DATABASE_URL = "sqlite:///history.db"

# 엔진 생성 (check_same_thread: SQLite에서 필수 옵션)
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# 세션 팩토리 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session():
    """
    데이터베이스 세션을 반환합니다.
    """
    return SessionLocal()
