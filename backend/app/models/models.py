from sqlalchemy import Column, Integer, Text
from app.core.database import Base
from app.core.config import settings

# Escolha dinâmica do tipo de coluna
if settings.use_pgvector:
    from pgvector.sqlalchemy import Vector
    EmbeddingColumn = Vector(768)
else:
    from sqlalchemy import JSON
    EmbeddingColumn = JSON


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False, unique=True)
    answer = Column(Text, nullable=False)

    # embedding (JSON local / vector em prod)
    embedding = Column(EmbeddingColumn, nullable=False)


class UnansweredQuestion(Base):
    __tablename__ = "unanswered_questions"

    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False, unique=True)
