from fastapi import FastAPI
from pydantic import Field,BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int = Field(gt=0)
    course: str
    marks: float = Field(ge=0,le=100)
    email: str | None = None    

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/student")
def get_student(course: str | None = None):
    if course:
        return {"message": f"Details of student in course {course}"}
    
    return {
        "name" : "John Doe",
        "age" : 20,
        "course" : "B.Tech",
        "marks" : 85
    }

@app.get("/student/{name}")
def get_student_by_name(name: str):
    return {
        "message": f"Searching for student {name}",
    }

@app.post("/student", response_model=Student)
def create_student(student: Student):
    return student