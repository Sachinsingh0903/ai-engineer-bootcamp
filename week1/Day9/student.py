class Student:

    school = "AI Engineering College"

    def __init__(self, name, age, course, marks):
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            raise ValueError("Marks must be between 0 and 100")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.get_grade()}")

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

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    @staticmethod
    def is_valid_marks(marks):
        return 0 <= marks <= 100