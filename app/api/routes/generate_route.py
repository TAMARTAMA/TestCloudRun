
from datetime import datetime
from fastapi import APIRouter, Depends
# from services.model_service import ModelService
# from core.settings import get_db
# from models.schemas import GenerateResponse, MessageAuthor, QuestionRequest
# import uuid

# from services.db_service import add_message


router = APIRouter()
@router.post("")
def generate(request: dict):
    return {"message": "This is a placeholder for the generate endpoint."}
# model = ModelService()
# @router.post("", response_model=GenerateResponse, tags=["Generate"])
# async def generate(
#     request: QuestionRequest,
#     db=Depends(get_db)
# ):
#     answer_text = model.send_prompt(prompt="answer the question", question=request.question)
#     message = add_message(
#         db=db,
#         session_id=request.session_id,
#         message_id=request.message_id,
#         message_number=1,#?
#         author="user",
#         content=request.question
#     )

#     message = add_message(
#         db=db,
#         session_id=request.session_id,
#         message_number=1,#?
#         author="RAMBAM",
#         content=answer_text
#     )

#     print({"message_id": message.id, "conversation_id": message.conversation_id})
#     return GenerateResponse(
#         session_id=request.session_id,
#         message_id=request.message_id,
#         answer_message_id=message.id,
#         question=request.question,
#         answer=answer_text,
#         timestamp=datetime.now()
#     )
    # db_user = db_service.create_user(user)