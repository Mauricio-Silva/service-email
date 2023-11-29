from fastapi import FastAPI
from app.router.email import router

app = FastAPI()


app.include_router(router)
