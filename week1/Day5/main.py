from student_utils import calculate_average_marks, get_grade

marks = [85, 90, 78, 92]
average = calculate_average_marks(marks)
grade = get_grade(average)

print(f"Average Marks: {average}")
print(f"Grade: {grade}")

import calculator

print(f"5 + 3 = {calculator.add(5, 3)}")
print(f"10 - 4 = {calculator.subtract(10, 4)}")
print(f"6 * 7 = {calculator.multiply(6, 7)}")
print(f"8 / 2 = {calculator.divide(8, 2)}")