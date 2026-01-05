from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.embeddings import embed_text
from app.services.similarity import find_best_match
from app.models import UnansweredQuestion
from app.core.config import settings

router = APIRouter(tags=["ask"])


@router.post("/ask")
def ask(user_question: str, db: Session = Depends(get_db)):
    print(">>> ENTERED /ask")

    embedding = embed_text(user_question)
    print(">>> embedding len:", len(embedding))
    exists = (
        db.query(UnansweredQuestion)
        .filter(UnansweredQuestion.text == user_question)
        .first()
    )

    if not exists:
        unanswered = UnansweredQuestion(text=user_question)
        db.add(unanswered)
        db.commit()

    return {
        "answer": "Ainda não sei responder. Vou aprender com isso."
    }