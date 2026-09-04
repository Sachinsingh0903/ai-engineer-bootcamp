from person import Person

class Student(Person):
    def __init__(self, name, age, course, marks, address):
        #parent's initializer
        super().__init__(name, age)
        self.course = course
        self.marks = marks
        self.address = address

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
    
    #overriding the display method of parent class
    def display(self):
        super().display()
        print(f"Course: {self.course}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.get_grade()}")
        print(f"Address: {self.address.city}, {self.address.state}")

    def describe(self):
        return "I am a student"


class Address:
    def __init__(self,city, state):
        self.city = city
        self.state = state
        

    