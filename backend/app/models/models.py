from sqlalchemy import Column, Integer, Text
from pgvector.sqlalchemy import Vector
from app.core.database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False, unique=True)
    answer = Column(Text, nullable=False)
    embedding = Column(Vector(768), nullable=False)


class UnansweredQuestion(Base):
    __tablename__ = "unanswered_questions"

    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False, unique=True)
