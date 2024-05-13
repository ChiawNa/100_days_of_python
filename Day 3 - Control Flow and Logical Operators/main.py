print("Lesson1 :- Control Flow with if/else and Conditional Operators\n")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster.")
else:
    print("Sorry, you have to grow taller before you can ride.")


#Write a program that works out whether if a given number is an odd or even number.
#Even numbers can be divided by 2 with no remainder.

number = int(input())

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")