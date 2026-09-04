class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None

    def delete_student(self, name):
        student = self.find_student(name)
        if student:
            self.students.remove(student)
            return True
        return False

    def display_students(self):
        for student in self.students:
            student.display()
            print("-" * 30)

    def count_students(self):
        return len(self.students)