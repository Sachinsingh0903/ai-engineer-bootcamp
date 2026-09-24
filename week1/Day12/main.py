from fastapi import FastAPI
from routers.student_router import router as student_router


app = FastAPI()


@app.get("/")
def home():
    return {"message": "Student API is running"}


app.include_router(student_router)