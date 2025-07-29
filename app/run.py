import os
from fastapi import FastAPI
print(f"wffw: {os.getcwd()}")
from app.routers import user


app = FastAPI()
app.include_router(user.router)