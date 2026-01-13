from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from src.handlers.chat_handler import chat_agent_handler

router = APIRouter()


@router.post("/chat")
def chat_agent_route(message: str) -> dict[str, str]:
    return chat_agent_handler(message=message)
