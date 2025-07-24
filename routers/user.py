from fastapi import APIRouter, HTTPException
from user.register import user_register
from user.login import user_login
import models

router = APIRouter()

@router.post("/register")
async def register(user: models.Register):
    result, status = user_register(user)
    if status != 201:
        raise HTTPException(status_code=status, detail=result["error"])
    return result

@router.post("/login")
async def login(user: models.Login):
    result, status = user_login(user)

    if status != 201:
        print("Masuk")
        raise HTTPException(status_code=status, detail=result["error"])
    return result