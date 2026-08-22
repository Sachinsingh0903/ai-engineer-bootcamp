# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# course= input("Enter your course: ")
# marks = float(input("Enter your marks: "))

students = [{
    "name": "Rahul",
    "age": 30,
    "course": "BE",
    "marks": 85.5
    },
    {
        "name": "Priya",
        "age": 25,
        "course": "ME",
        "marks": 90.0   
    },
    {
        "name": "Amit",
        "age": 28,
        "course": "BSc",
        "marks": 78.0
    },
    {
        "name": "Sneha",
        "age": 22,
        "course": "MSc",
        "marks": 92.5
    },
    {
        "name": "Rohit",
        "age": 27,
        "course": "BTech",
        "marks": 88.0
    }
]

def display_menu():
    print("\n Menu options:")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Exit")

def add_student():
    print("\nAdd Student:")
    new_name = input("Enter name: ")
    new_age = int(input("Enter age: "))
    new_course = input("Enter course: ")    
    new_marks = float(input("Enter marks: "))

    new_student = {
        "name": new_name,
        "age": new_age,
        "course": new_course,
        "marks": new_marks
    }

    students.append(new_student)
    print(f"Student {new_name} has been added.")

def view_students():
    print("\nStudent Details:")
    for student in students:
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Course: {student['course']}")
        print(f"Marks: {student['marks']}\n")

def search_student(name):
    print("\nSearch Student:")
    #search_name = input("To search student by name, enter the name of the student: ")
    # found=False
    for student in students:
        if student['name'] == name:
            print(f"Student found!")
            # found=True
            return student
            # break
    return None
        
def update_student_marks():
    print("\nUpdate Student Marks:")
    update_name = input("Enter the name of the student whose marks you want to update: ")
    found = False
    for student in students:
        if student['name'] == update_name:
            new_marks = float(input(f"Enter new marks for {update_name}: "))
            student['marks'] = new_marks
            print(f"Marks updated for {update_name}. New Marks: {new_marks}\n")
            found = True
            break
    if not found:
        print("Student not found.")

def delete_student():
    print("\nDelete Student:")
    delete_name = input("To delete a student, enter the name of the student: ")
    found = False
    for student in students:
        if student['name'] == delete_name:
            students.remove(student)
            print(f"Student {delete_name} has been deleted.\n")
            found = True
            break
    if not found:
        print("Student not found.")

while True:
    display_menu()
    input_choice = input("Enter your choice (1-6): ")

    if input_choice == "1":
        add_student()

    elif input_choice == "2":
        view_students()
            
    elif input_choice == "3":
        search_name = input("To search student by name, enter the name of the student: ")
        find_stud = search_student(search_name)
        if find_stud:
            print(f"Name: {find_stud['name']}")
            print(f"Age: {find_stud['age']}")
            print(f"Course: {find_stud['course']}")
            print(f"Marks: {find_stud['marks']}\n")
        else:
            print("Student not found.")

    elif input_choice == "4":
        update_student_marks()

    elif input_choice == "5":
        delete_student()

    elif input_choice == "6":
        print("\nExiting the program.")
        exit()

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

