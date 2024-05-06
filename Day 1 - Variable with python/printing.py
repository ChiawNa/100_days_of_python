print("Lesson 1:- Printing\n")

print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")

print("She said: \"Hello\" and then left.")
print('She said: "Hello" and then left.')   

print("A 'single quote' inside a double quote")
print('A "double quote" inside a single quote')
print("Alternatively you can just \"escape\" the quote")
print("\n")


print("Lesson 2:- Debugging\n")

#Fix the code below 👇

# print(Day 1 - String Manipulation")
# print("String Concatenation is done with the "+" sign.")
#   print('e.g. print("Hello " + "world")')
# print(("New lines can be created with a backslash and n.")

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")
print("\n")


print("Lesson 3:- Input Function\n")

#Write a program that calculates and outputs the number of characters in any name. 
#The automated tests will try out lots of different names as the input. 
#Your code should work for any name. 
#Your code should only output the number, no other text is needed.

name=input("What is your name? ")
print(len(name))
print("\n")


print("Lesson 4:- Variables\n")

# Write a program that switches the values stored in the variables a and b.

a = input("Insert the value of a: ")
b = input("Insert the value of b: ")

temp = a
a = b
b = temp

print("a: " + a)
print("b: " + b)
print("\n")