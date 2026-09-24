from fastapi import FastAPI

from routers.student_router import router as student_router

app = FastAPI(
    title="Student Management API",
    version="1.0.0",
)

@app.get("/")
def home():
    return {"message": "Welcome to the Student Management API"}

app.include_router(student_router)
