from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import schemas
from database import get_db
from AI import restaurant_assistant


router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)

@router.post(
    "/chat",
    response_model=schemas.AIChatResponse
)
def ai_chat(
    request: schemas.AIChatRequest,
    db: Session = Depends(get_db)
):
    response = restaurant_assistant.process_message(
        db,
        request.message
    )

    return {
        "response": response
    }