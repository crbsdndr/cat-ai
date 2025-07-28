from fastapi import APIRouter, HTTPException
import models
import users

router = APIRouter()

@router.post("/register")
async def register(user: models.Register):
    result, status = users.auth.register(user)
    if status != 201:
        raise HTTPException(status_code=status, detail=result["error"])
    return result

@router.post("/login")
async def login(user: models.Login):
    result, status = users.auth.login(user)
    if status != 201:
        raise HTTPException(status_code=status, detail=result["error"])
    return result