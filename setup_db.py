# setup_db.py

from database.model import Base
from database.session import engine

# DB에 정의된 테이블들을 생성합니다
Base.metadata.create_all(bind=engine)

print("✅ 데이터베이스 테이블 생성 완료")