from fastapi import APIRouter, HTTPException

from ..settings import settings

router = APIRouter()


def check_token(token: str):
    accept_token = settings.accepted_token
    if token != accept_token:
        raise HTTPException(status_code=401, detail="Invalid token")
