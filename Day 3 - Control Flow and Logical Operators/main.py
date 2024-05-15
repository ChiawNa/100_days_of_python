# # print("Lesson1 :- Control Flow with if/else and Conditional Operators\n")

# # print("Welcome to the rollercoaster!")
# # height = int(input("What is your height in cm? "))

# # if height > 120:
# #     print("You can ride the rollercoaster.")
# # else:
# #     print("Sorry, you have to grow taller before you can ride.")


# # #Write a program that works out whether if a given number is an odd or even number.
# # #Even numbers can be divided by 2 with no remainder.

# # number = int(input())

# # if number % 2 == 0:
# #     print("This is an even number.")
# # else:
# #     print("This is an odd number.")


# print("Lesson2 :- Nested if and elif statements\n")

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height > 120:
#     print("You can ride the rollercoaster.")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Please pay $5.")
#     elif 12<age<18: #elif age <=18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")


# #Write a program that interprets the Body Mass Index (BMI) 
# #based on a user's weight and height.

# # Enter your height in meters e.g., 1.55
# height = float(input())
# # Enter your weight in kilograms e.g., 72
# weight = int(input())

# BMI = float(weight/(height*height))

# if BMI < 18.5:
#     print(f"Your BMI is {BMI}, you are underweight.")
# elif BMI < 25:
#     print(f"Your BMI is {BMI}, you have a normal weight.")
# elif BMI < 30:
#     print(f"Your BMI is {BMI}, you are slightly overweight") 
# elif BMI < 35:
#     print(f"Your BMI is {BMI}, you are obese.")
# else:
#     print(f"Your BMI is {BMI}, you are clinically obese.")

#Write a program that works out whether if a given year is a leap year. 
#A normal year has 365 days, leap years have 366, with an extra day in February. 


year = int(input())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Lear year")
else:
    print("Not leap year")