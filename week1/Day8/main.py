from person import Person
from student import Student,Address
from teacher import Teacher

person  = Person("John Doe", 30)
person.display()

address = Address("Bengaluru", "Karnataka")

student = Student("Rahul", 43 , "B.tech", 100, address)
student.display()

rahul = Student("Rahul", 21, "B.tech", 100, address)
priya = Teacher("Priya", 22, "Maths", 5)
neha = Student("Neha", 23, "B.tech", 90, address)
sakshi = Teacher("Sakshi", 28, "Science", 9)

people = [rahul, priya, neha, sakshi]

for person in people:
    message=person.describe()
    print(message)