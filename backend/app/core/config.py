from pydantic import BaseModel
from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env", override=True)



class Settings(BaseModel):
    env: str = os.getenv("ENV", "local")

    database_url: str = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://postgres:postgres@localhost:5432/herberts_brain"
    )

    admin_key: str = os.getenv("ADMIN_KEY", "change-me")

    embedding_provider: str = os.getenv("EMBEDDING_PROVIDER", "ollama")
    ollama_url: str = os.getenv("OLLAMA_URL", "http://localhost:11434")
    ollama_embed_model: str = os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text")

settings = Settings()
