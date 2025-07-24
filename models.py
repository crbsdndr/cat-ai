from pydantic import BaseModel

class Register(BaseModel):
    name: str
    email: str
    password: str
    role: str

class Login(BaseModel):
    email: str
    password: str

class Chat(BaseModel):
    session_id: str
    message: str