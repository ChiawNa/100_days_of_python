from random import randint
from art import logo 

def play_game(attempt):

    number = randint(1,100)
    finish_guess = False

    while attempt > 0 and not finish_guess:
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess > number:
            print("Too high.")
        
        elif guess < number:
            print("Too low.")
        
        elif guess == number:
            print(f"You got it! The answer is {number}")
            finish_guess = True

        attempt -= 1

        if attempt > 0 and not finish_guess:
            print("Guess again.")

    if not finish_guess:
        print(f"Sorry, you've run out of attempts. The correct answer is {number}.")


print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ")

if difficulty == 'easy':
    play_game(10)
elif difficulty == 'hard':
    play_game(5)

