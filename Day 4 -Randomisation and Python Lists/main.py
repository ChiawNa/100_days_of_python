# print("Lesson 1 - Random Module\n")

# import random

# random_integer = random.randint(1,10)
# print(random_integer)

# random_float =  random.random()*5
# print(random_float)


# #You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# #You should generate a random number, either 0 or 1. Then use that number to print out "Heads" or "Tails".
# #e.g. 1 means Heads 0 means Tails


# import random

# random_side = random.randint(0,1)
# if random_side == 1:
#     print("Heads")
# else:
#     print("Tails")


# print("Lesson 2 - Offset and Appending Item to List\n")

# states_of_america = ["Delaware", "New Jersey", "Georgia", "New York","Alaska", "Hawaii"]
# print(states_of_america[-1])

# states_of_america.append("California")
# print(states_of_america)


# You are going to write a program that will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.

# import random

# names_string = "Angela, Ben, Jenny, Michael, Chloe"
# names = names_string.split(", ")

# random_name =  random.choice(names)
# print(f"{random_name} is going to buy the meal today!")


# print("Lesson 3 - Index Error and Working with Nested List\n")

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[1][1])

# print(dirty_dozen)

# print(dirty_dozen[0])
# print(dirty_dozen[1])

# print(dirty_dozen[1][2])
# print(dirty_dozen[1][3])


print("Exercise - Treasure Map\n")

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter) # will get 1
number_index = int(position[1]) - 1 # will get 2
map[number_index][letter_index] = "X"

# print(letter_index)
#print(number_index)

print(f"{line1}\n{line2}\n{line3}")