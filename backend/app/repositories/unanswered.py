from sqlalchemy.orm import Session
from app.models.models import UnansweredQuestion


def save_unanswered(db: Session, text: str) -> None:
    """
    Salva uma pergunta sem resposta, se ainda não existir.
    """
    exists = (
        db.query(UnansweredQuestion)
        .filter(UnansweredQuestion.text == text)
        .first()
    )

    if exists:
        return

    unanswered = UnansweredQuestion(text=text)
    db.add(unanswered)
    db.commit()


def list_unanswered(db: Session, skip: int = 0, limit: int = 50) -> list[UnansweredQuestion]:
    """
    Lista perguntas não respondidas (admin).
    """
    return (
        db.query(UnansweredQuestion)
        .offset(skip)
        .limit(limit)
        .all()
    )


def delete_unanswered(db: Session, unanswered_id: int) -> bool:
    """
    Remove uma pergunta não respondida após aprendizado.
    """
    item = db.query(UnansweredQuestion).get(unanswered_id)
    if not item:
        return False

    db.delete(item)
    db.commit()
    return True
