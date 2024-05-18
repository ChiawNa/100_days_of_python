print("Lesson3 :- Multiple If statements\n")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age <18:
        bill = 7
        print("Please pay $7.")
    else:
        bill = 12
        print("Please pay $12.")

    want_photo = input("Do you want a photo taken? Y or N. ")
    if want_photo == "Y":
        bill += 3

    print(f"Your final bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")


    
# Based on a user's order, work out their final bill.
# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1

print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N

bill = 0

if size == "S":
    bill = 15

    if add_pepperoni == "Y":
        bill += 2

elif size == "M":
    bill = 20

else:
    bill = 25

if add_pepperoni == "Y":
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

print("Lesson4 :- Logical Operators\n")


#You are going to write a program that tests the compatibility between two people.
#To work out the love score between two people:
#Take both people's names and check for the number of times the letters in the word TRUE occurs.
#Then check for the number of times the letters in the word LOVE occurs.
#Then combine these numbers to make a 2 digit number.

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
combined_name = name1 + name2
lower_names = combined_name.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
total1 = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
total2 = l + o + v + e

score = int(str(total1) + str(total2))

if score<10 or score >90:
    print(f"Your score is {score}, you go together like coke and mentos.")

elif score>40 or score <50:
    print(f"Your score is {score}, you are alright together.")

else:
    print(f"Your score is {score}.")


