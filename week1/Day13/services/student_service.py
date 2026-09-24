from models import Student, StudentUpdate

from repositories.student_repository import (
    save_student,
    get_all_students,
    find_student_by_name,
    delete_student,
    update_student
    )

def create_student(student: Student):
    return save_student(student)


def get_students():
    return get_all_students()


def find_student(name: str):
    return find_student_by_name(name)


def remove_student(name: str):
    student = find_student_by_name(name)

    if student:
        delete_student(student)
        return True

    return False

def update_student_marks(name: str, data: StudentUpdate):
    student = find_student_by_name(name)
    if student is None:
        return None
    
    if data.marks is not None:
        student.marks = data.marks

    return update_student(student)
