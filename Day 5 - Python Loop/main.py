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


print("Lesson 2:- For loop and Range() function\n")

# You are going to write a program that calculates the sum of all the even numbers from 1 to X. 
# If X is 100 then the first even number would be 2 and the last one is 100:
# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

target = int(input()) # Enter a number between 0 and 1000

total = 0
for i in range(2, target+1, 2):
    total = total + i
print(total)


# while loop

target = int(input()) # Enter a number between 0 and 1000

i = 2
total = 0

while (i<=target):
  total = total + i
  i = i + 2
print(total)



# use modules %

target = int(input()) # Enter a number between 0 and 1000

total = 0

for i in range(2, target+1):
  if i%2 == 0:
    total = total + i
print(total)
