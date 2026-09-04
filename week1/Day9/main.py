from student import Student

rahul = Student("Rahul", 30, "BE", 85)

print(rahul.marks)

rahul.marks = 95

print(rahul.marks)
print(rahul.get_grade())

print(Student.is_valid_marks(85))
print(Student.is_valid_marks(150))

Student.change_school("New AI Engineering College")

print(Student.school)
print(rahul.school)