import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


from art import logo
print(logo)

finish = False
new_calculating = False

def add(first_num, second_num):
    return(first_num + second_num) 

def substract(first_num, second_num):
    return first_num - second_num

def multiply(first_num, second_num):
    return first_num * second_num

def divide(first_num, second_num):
    return first_num / second_num


operation = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def calculator(): 

    first_num = float(input("What's the first number?: "))

    for key in operation:
        print(key)

    while not finish:
        operation_symbol = input("Pick an operation: ")
        second_num = float(input("What's the next number?: "))

        if operation_symbol in operation:
            operation_function = operation[operation_symbol]
            answer = operation_function(first_num, second_num)
            print(f"{first_num} {operation_symbol} {second_num} = {answer}")
        else:
            print("Invalid operation. Please try again.")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.")

        if choice == "y":
            first_num = answer

        elif choice == "n":
            clear()
            calculator()

calculator()
