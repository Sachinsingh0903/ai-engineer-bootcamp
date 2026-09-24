from models import Student,updateStudent

students = []

def save_student(student: Student):
    students.append(student)
    return student

def get_all_students():
    return students

def find_student_by_name(name: str):
    for student in students:
        if student.name.lower() == name.lower():
            return student
    return None


def delete_student(student: Student):
    students.remove(student)

def update_student(student: Student):
    return student