from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.embeddings import embed_text
from app.services.similarity import find_best_match
from app.models import UnansweredQuestion

router = APIRouter(tags=["ask"])


@router.post("/ask")
def ask(user_question: str):
    print(">>> ENTERED /ask")
    print("Question:", user_question)

    try:
        from app.services.embeddings import embed_text
        print(">>> imported embed_text")

        embedding = embed_text(user_question)
        print(">>> embedding len:", len(embedding))

        return "ok"
    except Exception:
        traceback.print_exc()
        raise