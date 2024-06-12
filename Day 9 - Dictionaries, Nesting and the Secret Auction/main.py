# You have access to a database of student_scores in the format of a dictionary. 
# The keys in student_scores are the names of the students and the values are their exam scores.

# Write a program that converts their scores to grades. 
# By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values.

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for student, score in student_scores.items():
    if score > 90:
        grade = "Outstanding"
    elif score > 80:
        grade = "Exceeds Expectation"
    elif score > 70:
        grade = "Acceptable"
    else:
        grade = "Fail"

    student_grades[student] = grade

# 🚨 Don't change the code below 👇
print(student_grades)