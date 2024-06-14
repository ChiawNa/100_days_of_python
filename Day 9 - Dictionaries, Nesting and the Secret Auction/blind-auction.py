import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


from art import logo

print(logo)

bids = {}
finish = False

def highest_bidder(record):
    highest_bidder = 0
    winner = ""

    # record = {"Kang": 123, "Hee": 345}

    for bidder in record:       #record is argument
        bid_amount = record[bidder]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bidder}. ")

while not finish:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $ "))
    bids[name] = price      #dictionary[key] = value
    decision = input("Are there any other bidders? Type 'yes' or 'no'. ")

    if decision == 'yes':

        clear()

    elif decision == 'no':
        finish = True
        highest_bidder(bids)



# to understand the 'record'

# def find_largest(numbers):
#     largest = numbers[0]
#     for number in numbers:
#         if number > largest:
#             largest = number
#     return largest

# my_numbers = [10, 20, 30, 40, 50]
# print(find_largest(my_numbers))


        

