from ormar import Integer, String, Boolean, UUID, ForeignKey, Model
import uuid
import src.config as config


class Quiz(Model):
    """
    Ormar model representing the Quiz table in DB
    """
    class Meta:
        tablename = "quiz"
        database = config.database
        metadata = config.metadata

    id: int = Integer(primary_key=True, autoincrement=True)
    key: uuid.UUID = UUID(default=uuid.uuid4, unique=True)
    title: str = String(max_length=100, nullable=False)


class Question(Model):
    """
    Ormar model representing the Question table in DB
    """
    class Meta:
        tablename = "question"
        database = config.database
        metadata = config.metadata

    id: int = Integer(primary_key=True, autoincrement=True)
    # key: uuid.UUID = UUID(default=uuid.uuid4, unique=True)
    question: str = String(max_length=150, nullable=False)
    quiz: Quiz = ForeignKey(Quiz)


class Answer(Model):
    """
    Ormar model representing the Answer table in DB
    """
    class Meta:
        tablename = "answer"
        database = config.database
        metadata = config.metadata

    id: int = Integer(primary_key=True, autoincrement=True)
    # key: uuid.UUID = UUID(default=uuid.uuid4, unique=True)
    text: str = String(max_length=100, nullable=False, index=True)
    correct: bool = Boolean(nullable=False)
    question: Question = ForeignKey(Question)
