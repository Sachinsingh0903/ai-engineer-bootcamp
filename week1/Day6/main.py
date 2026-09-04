
from student import Student

rahul = Student("Rahul", 21, "B.tech", 100)
priya = Student("Priya", 22, "B.sc", 85)
amit = Student("Amit", 20, "B.com", 75)

students = [rahul, priya, amit]
for student in students:
    print(student.display())
    if student.name == "Rahul":
        print(student.update_marks(95))
        print(student.get_grade())
