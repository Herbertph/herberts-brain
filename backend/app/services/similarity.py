from sqlalchemy.orm import Session
from math import sqrt
from app.models import Question


def cosine_similarity(v1: list[float], v2: list[float]) -> float:
    dot = sum(a * b for a, b in zip(v1, v2))
    norm1 = sqrt(sum(a * a for a in v1))
    norm2 = sqrt(sum(b * b for b in v2))

    if norm1 == 0 or norm2 == 0:
        return 0.0

    return dot / (norm1 * norm2)


def find_best_match(
    db: Session,
    embedding: list[float],
    threshold: float = 0.85,
):
    questions = db.query(Question).all()

    best_score = 0.0
    best_question = None

    for q in questions:
        score = cosine_similarity(embedding, q.embedding)

        if score > best_score:
            best_score = score
            best_question = q

    if not best_question or best_score < threshold:
        return None

    return {
        "question": best_question.text,
        "answer": best_question.answer,
        "score": best_score,
    }
