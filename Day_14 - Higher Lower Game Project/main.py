import random
from logo import logo, vs
from game_data import data

# Display art
print(logo)

score = 0
finish_game = False

# Generate the random choice for user to guess
compare_1 = random.choice(data)
compare_2 = random.choice(data)
if compare_1 == compare_2:
    compare_2 = random.choice(data)


def data(compare):
# Format the choice into printable format
    compare_name = compare["name"]
    compare_description = compare["description"]
    compare_country = compare["country"]
    return f"Compare A: {compare_name}, a {compare_description}, from {compare_country}."


choice = input("Who has more followers? Type 'A' or 'B': ")

while not finish_game:
    if choice == 'A':
        if {compare_1['follower_count']} > {compare_2['follower_count']}:
            print("You're correct.")
            score += 1

        else:
            print(f"Sorry that's wrong. Current score: {score}")
            finish_game = True

    elif choice == 'B': 
        if {compare_1['follower_count']} < {compare_2['follower_count']}:
            print("You're correct.")
            score += 1

        else:
            print(f"Sorry that's wrong. Current score: {score}")
            finish_game = True


##