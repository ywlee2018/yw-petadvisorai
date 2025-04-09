# utils/config.py

import os
from dotenv import load_dotenv

load_dotenv()

# Azure OpenAI 기본 정보
AOAI_ENDPOINT = os.getenv("AOAI_ENDPOINT")
AOAI_API_KEY = os.getenv("AOAI_API_KEY")

# GPT 모델 배포 이름
DEPLOY_GPT4O = os.getenv("AOAI_DEPLOY_GPT4O")
DEPLOY_GPT4O_MINI = os.getenv("AOAI_DEPLOY_GPT4O_MINI")

# Embedding 모델 배포 이름
DEPLOY_EMBED_3_LARGE = os.getenv("AOAI_DEPLOY_EMBED_3_LARGE")
DEPLOY_EMBED_3_SMALL = os.getenv("AOAI_DEPLOY_EMBED_3_SMALL")
DEPLOY_EMBED_ADA = os.getenv("AOAI_DEPLOY_EMBED_ADA")
