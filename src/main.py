from fastapi import FastAPI
from src.endpoints.url import router

app = FastAPI()


app.include_router(router)