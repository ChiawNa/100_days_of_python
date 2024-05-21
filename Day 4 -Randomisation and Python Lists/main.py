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


print("Lesson 2 - Offset and Appending Item to List\n")

states_of_america = ["Delaware", "New Jersey", "Georgia", "New York","Alaska", "Hawaii"]
print(states_of_america[-1])

states_of_america.append("California")
print(states_of_america)

