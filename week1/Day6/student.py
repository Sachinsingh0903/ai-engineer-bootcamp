class Student:
    def __init__(self, name, age, course, marks):
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def display(self):
        return f"Name: {self.name}, Age: {self.age}, Course: {self.course}, Marks: {self.marks}"

    def update_marks(self, new_marks):
        if new_marks >= 0 and new_marks <= 100:
            self.marks = new_marks
            return True
        return False
        
    def get_grade(self):
        if self.marks >= 90:
            return "Grade: A"
        elif self.marks >= 80:
            return "Grade: B"  
        elif self.marks >= 70:
            return "Grade: C"
        elif self.marks >= 60:
            return "Grade: D"
        else:
            return "Grade: F"
            

    
    