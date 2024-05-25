# print("Lesson 1:- For loop with Python Lists\n")

# # You are going to write a program that calculates the average student height from a List of heights.

# # Input a Python list of student heights
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
  
# total_height = 0
# for height in student_heights:
#   total_height += height

# total_student = 0
# for student in student_heights:
#   total_student += 1

# average_height = round(total_height / total_student)

# print(f"\ntotal height = {total_height}")
# print(f"number of students = {total_student}")
# print(f"average height = {average_height}")


# You are going to write a program that calculates the highest score from a List of scores.

# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

max_score = 0

for score in student_scores:
  if score > max_score:
    max_score = score

print(f"The highest score in the class is: {max_score}")
