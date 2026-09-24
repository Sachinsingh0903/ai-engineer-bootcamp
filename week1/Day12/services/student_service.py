from model import Student

students = []

def add_student(student: Student):
    students.append(student)
    return {"message": "Student added successfully!"}

def find_student(name: str):
    for student in students:
        if student.name.lower() == name.lower():
            return student
    return None

def get_all_students():
    return students