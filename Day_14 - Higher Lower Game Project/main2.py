from logo import logo, vs
from game_data import data
import random

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def format_data(account):
# 3. Takes the account data and returns into printable format.
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return(f"{account_name}, a {account_description}, from {account_country}.")


def check_answer(guess, a_followers, b_followers):
## 5. Take the user guess and follower counts and returns if they got it right.
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

    # if a_followers > b_followers:
    #     if guess == "a":
    #         return True
    #     else:
    #         return False

# 1. Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# 8. Make the game repeatable.
while game_should_continue: 

    # 2. Generate a random account from the game data.
    # 9. Making the account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")


    # 4. Ask user for a guess. 
    guess = input("Who has the more followers? Type 'A' or 'B': ").lower()


    # 5. Check if user is correct.
    ## Get follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

# 10. Clear the screen between rounds.
    clear()
    print(logo)

    # 6. Give user feedback on their guess.
    # 7. Score keeping.
    if is_correct:
        score += 1
        print(f"You're correct! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, you're wrong. Final score: {score}.")
