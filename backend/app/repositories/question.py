from sqlalchemy.orm import Session
from app.models.models import Question


def get_all_questions(db: Session) -> list[Question]:
    """
    Retorna todas as perguntas respondidas.
    Usado pelo motor de similaridade.
    """
    return db.query(Question).all()


def get_question_by_text(db: Session, text: str) -> Question | None:
    """
    Busca uma pergunta exata (útil para admin no futuro).
    """
    return db.query(Question).filter(Question.text == text).first()


def create_question(
    db: Session,
    text: str,
    answer: str,
    embedding: list[float],
) -> Question:
    """
    Cria uma pergunta respondida com embedding já calculado.
    """
    question = Question(
        text=text,
        answer=answer,
        embedding=embedding,
    )
    db.add(question)
    db.commit()
    db.refresh(question)
    return question
