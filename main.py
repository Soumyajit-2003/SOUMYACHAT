from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
import uvicorn
from src.routes.route import router

app = FastAPI()


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
