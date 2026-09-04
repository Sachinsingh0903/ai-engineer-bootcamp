class Student:

    def __init__(self, name, age, course, marks):
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def update_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.marks = new_marks
            return True

        return False

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        else:
            return "F"

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.get_grade()}")