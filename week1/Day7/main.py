from student import Student
from student_manager import StudentManager

#object of StudentManager class
manager = StudentManager()

#object creation of Student class
rahul = Student("Rahul", 21, "B.tech", 100)
priya = Student("Priya", 22, "B.tech", 90)
amit = Student("Amit", 23, "B.tech", 80)
john = Student("John", 24, "B.E", 70)
raghu = Student("Raghu", 25, "B.E", 60)

#Adding students to the manager
manager.add_student(rahul)
manager.add_student(priya)
manager.add_student(amit)
manager.add_student(john)
manager.add_student(raghu)

# Displaying all students
manager.display_students()

#Finding a student by name
student = manager.find_student("Rahul")
if student:
    print("Student found:")
    student.display()
else:
    print("Student not found.")

# Updating a student's marks
student = manager.find_student("amit")
if student:
    if student.update_marks(85):
        print("Marks updated successfully.")
    else:
        print("Invalid marks.")
else:
    print("Student not found.")

# Deleting a student
if manager.delete_student("amit"):
    print("Student deleted successfully.")
else:
    print("Student not found.")

#Counting the total number of students
print(f"total number of students: {manager.count_students()}")