print("Lesson 1:- Python Primitive Data Types\n")

print("Hello"[0]) #subcript

# #Integer
print(123 + 456)

# #Float
3.14159

# #Boolean
True
False


print("\nLesson 2:- Type Error, Type Checking and Type Conversion\n")
# #below code has error (type error: int->str)

num_char = len(input("What is your name?\n"))
print("your name has " + num_char + "characters.\n")


# #solution

num_char = len(input("What is your name?\n"))
print(type(num_char))
new_num_char = str(num_char)
print("Your name has " + new_num_char + "characters.\n")

a = 123
print(type(a))

a = str(123)
print(type(a))

print(70 + float("100.5"))
print(str(70)+str(100))


print("Lesson 3:- [Interactive Coding Exercise] Data Types")

# #Write a program that adds the digits in a 2 digit number. 
# #e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input()
#print(type(two_digit_number))
print(int(two_digit_number[0]) + int(two_digit_number[1]))


print("Lesson 4:- Mathematical Operations")

# PEMDASLR
# ()
# **
# */
# +-

print(3*(3+3)/3-3)


#Write a program that calculates the Body Mass Index (BMI) 
#from a user's weight and height.

height = input()
weight = input()

float_height = float(height)
int_weight = int(weight)

BMI = (int_weight/(float_height*float_height))
int_BMI = int(BMI)

print(int_BMI)


print("Lesson 5:- Number Manipulation and F Strings\n")

print(round(2.6666, 2))
print(8//3) #answer in int
print(8/3) #answer in float

# f string (to combine dff data type)

score = 0 
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, your are winning is {isWinning}")

#Create a program using maths and f-Strings that tells us how many weeks we have left, 
#if we live until 90 years old.

# A years have 52 weeks.
age = input()
x = (90 - int(age)) * 52
print(f"You have {x} weeks left.")

