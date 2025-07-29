from fastapi import APIRouter, HTTPException
import app.schemas.user as schemas_user
import app.users.auth as users_auth

router = APIRouter()

@router.post("/register")
async def register(user: schemas_user.Register):
    result, status = users_auth.register(user)
    if status != 201:
        raise HTTPException(status_code=status, detail=result["error"])
    return result

@router.post("/login")
async def login(user: schemas_user.Login):
    result, status = users_auth.login(user)
    if status != 201:
        raise HTTPException(status_code=status, detail=result["error"])
    return result