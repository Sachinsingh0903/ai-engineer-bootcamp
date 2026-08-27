
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# course= input("Enter your course: ")
# marks = float(input("Enter your marks: "))

students = [{
    "Name": "Rahul",
    "Age": 30,
    "Course": "BE",
    "Marks": 85.5
    },
    {
        "Name": "Priya",
        "Age": 25,
        "Course": "ME",
        "Marks": 90.0   
    },
    {
        "Name": "Amit",
        "Age": 28,
        "Course": "BSc",
        "Marks": 78.0
    },
    {
        "Name": "Sneha",
        "Age": 22,
        "Course": "MSc",
        "Marks": 92.5
    },
    {
        "Name": "Rohit",
        "Age": 27,
        "Course": "BTech",
        "Marks": 88.0
    }]

def display_menu():
    print("\n Menu options:")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Exit")

while True:
    display_menu()
    input_choice = input("Enter your choice (1-6): ")

    if input_choice == "1":
        print("\nAdd Student:")
        new_name = input("Enter name: ")
        new_age = int(input("Enter age: "))
        new_course = input("Enter course: ")    
        new_marks = float(input("Enter marks: "))

        new_student = {
            "Name": new_name,
            "Age": new_age,
            "Course": new_course,
            "Marks": new_marks
        }

        students.append(new_student)
        print(f"Student {new_name} has been added.")

    elif input_choice == "2":
        print("\nStudent Details:")
        for student in students:
            print(f"Name: {student['Name']}")
            print(f"Age: {student['Age']}")
            print(f"Course: {student['Course']}")
            print(f"Marks: {student['Marks']}\n")
            
    elif input_choice == "3":
        print("\nSearch Student:")
        search_name = input("To search student by name, enter the name of the student: ")

        for student in students:
            if student['Name'] == search_name:
                print(f"Student found!")
                print(f"Name: {student['Name']}")
                print(f"Age: {student['Age']}")
                print(f"Course: {student['Course']}")
                print(f"Marks: {student['Marks']}\n")
                break
            else:
                print("Student not found.")

    elif input_choice == "4":
        print("\nUpdate Student Marks:")
        update_name = input("Enter the name of the student whose marks you want to update: ")
        for student in students:
            if student['Name'] == update_name:
                new_marks = float(input(f"Enter new marks for {update_name}: "))
                student['Marks'] = new_marks
                print(f"Marks updated for {update_name}. New Marks: {new_marks}\n")
                break
            else:
                print("Student not found.")

    elif input_choice == "5":
        delete_name = input("To delete a student, enter the name of the student: ")
        for student in students:
            if student['Name'] == delete_name:
                students.remove(student)
                print(f"Student {delete_name} has been deleted.\n")
                break
            else:
                print("Student not found.")

    elif input_choice == "6":
        print("\nExiting the program.")
        exit()

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

