print("Lesson 1:- For loop with Python Lists\n")

# You are going to write a program that calculates the average student height from a List of heights.

# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  
total_height = 0
for height in student_heights:
  total_height += height

total_student = 0
for student in student_heights:
  total_student += 1

average_height = round(total_height / total_student)

print(f"\ntotal height = {total_height}")
print(f"number of students = {total_student}")
print(f"average height = {average_height}")
