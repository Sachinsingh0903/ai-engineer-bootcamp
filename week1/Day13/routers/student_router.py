from fastapi import APIRouter,HTTPException
from models import Student, updateStudent


from services.student_service import (
    create_student,
    get_students,
    find_student,
    remove_student,
    update_student_marks
)

router = APIRouter(
    prefix="/students",
    tags=["students"]
)

@router.post("/",response_model=Student)
def create(student: Student):
    return create_student(student)

@router.get("/",response_model=list[Student])
def get_all():
    return get_students()

@router.get("/{name}",response_model=Student)
def get_by_name(name: str):
    student = find_student(name)
    if student:
        return student
    raise HTTPException(status_code=404, detail="Student not found")

@router.delete("/{name}")
def delete(name: str):
    deleted = remove_student(name)
    if deleted:
        return {"message": "Student deleted successfully"}
    raise HTTPException(status_code=404, detail="Student not found")

@router.patch("/{name}",response_model=Student)
def update(name: str, data: updateStudent):
    updated_student = update_student_marks(name, data)
    if updated_student:
        return updated_student
    raise HTTPException(status_code=404, detail="Student not found")

