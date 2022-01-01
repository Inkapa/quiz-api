import uuid

import pydantic
from typing import List


class AnswerResponse(pydantic.BaseModel):
    """
    Pydantic Answer schema to return as part of the Quiz response
    """

    class Config:
        orm_mode = True

    # key: uuid.UUID (not needed without the verification endpoint)
    text: str
    correct: bool


class QuestionResponse(pydantic.BaseModel):
    """
    Pydantic Question schema to return as part of the Quiz response
    """
    class Config:
        orm_mode = True

    # key: uuid.UUID
    question: str
    answers: List[AnswerResponse]


class QuizResponse(pydantic.BaseModel):
    """
    Pydantic schema to return JSON object of a quiz on GET
    """
    class Config:
        orm_mode = True

    title: str
    questions: List[QuestionResponse]


class QuizResponseWithId(pydantic.BaseModel):
    """
    Pydantic schema to return JSON object of a quiz on GET, quiz key included
    """

    class Config:
        orm_mode = True

    key: uuid.UUID
    title: str
    questions: List[QuestionResponse]


# class VerifyResponse(pydantic.BaseModel):
#     class Config:
#         orm_mode = True
#
#     correct: bool
#     answers: List[uuid.UUID]
#
#
# class VerifyRequest(pydantic.BaseModel):
#     class Config:
#         orm_mode = True
#
#     question_key: uuid.UUID
#     answer_key: uuid.UUID
