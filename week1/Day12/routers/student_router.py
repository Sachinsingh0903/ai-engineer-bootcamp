from fastapi import APIRouter
from model import Student
from services.student_service import (add_student, find_student, get_all_students)

router = APIRouter(
    prefix="/students",
    tags=["students"]
)

@router.post("/")
def create(student: Student):
    return add_student(student)


@router.get("/")
def get_students():
    return get_all_students()


@router.get("/{name}")
def get_student(name: str):
    student = find_student(name)

    if student:
        return student

    return {"message": "Student not found"}

