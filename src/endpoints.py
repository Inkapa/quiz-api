import uuid

import src.config as config
from fastapi import HTTPException
import random
from src.objects.schema import QuizResponseWithId, QuizResponse
from ormar.exceptions import NoMatch
from src.objects.models import Quiz


@config.app.get("/quiz/random", response_model=QuizResponse)
async def get_random_quiz():
    """
    Fetch a random quiz from the database and return its information
    Includes nested questions and answers but omits the validity of
    an answer to avoid cheating

    :return: Quiz object
    """

    # ormar doesn't yet support func.random() in order_by
    quizs = await Quiz.objects.select_all(follow=True).all()
    return random.choice(quizs)


@config.app.get("/quiz/{quiz_key}", response_model=QuizResponse)
async def get_quiz_with_id(quiz_key: uuid.UUID):
    """
    Return a quiz from the database matching the given id
    Includes nested questions and answers but omits the validity of
    an answer to avoid cheating.
    :param quiz_key: Primary key of the quiz we want to return
    :return: Quiz object
    """
    print(quiz_key)
    try:
        quiz = await Quiz.objects.select_all(follow=True).get(key=quiz_key)
    except NoMatch:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return quiz.dict()


@config.app.post("/quiz/create", response_model=QuizResponseWithId)
async def create_quiz(quiz: Quiz.get_pydantic(exclude={
    "id",
    "key",
    "questions__id",
    "questions__key",
    "questions__answers__id",
    "questions__answers__key"
})):
    """
    Creates a new quiz object with its nested questions and answers

    :param quiz: Quiz object to create
    :return: Newly created quiz with its generated ids
    """

    quiz = Quiz(**quiz.dict())
    await quiz.save()
    await quiz.save_related(follow=True)
    return quiz

# Endpoint to check if a response is valid
# Removed because it wasn't worth the latency and people can still cheat with it
#
# @config.app.post("/quiz/verify", response_model=VerifyResponse)
# async def verify(answer: VerifyRequest):
#     """
#     Verify if an answer is correct
#     :param answer: Answer and Question keys
#     :return: Correctness of the input, and the array of correct answers
#     """
#
#     # Using a UUID prevent bruteforcing and cheating, but does slow down the process
#     try:
#         current_answer = await Answer.objects.get(key=answer.answer_key)
#     except NoMatch:
#         raise HTTPException(status_code=404, detail="The specified answer was not found")
#     try:
#         current_question = await Question.objects.get(key=answer.question_key)
#     except NoMatch:
#         raise HTTPException(status_code=404, detail="The specified question was not found")
#
#     if current_answer.question.id != current_question.id:
#         raise HTTPException(status_code=420, detail="Given answer does not correspond to the question.")
#     correct_answers = [answer.key for answer in await current_question.answers.all(correct=True)]
#     if current_answer.correct:
#         return {'correct': True, 'answers': correct_answers}
#     return {'correct': False, 'answers': correct_answers}
