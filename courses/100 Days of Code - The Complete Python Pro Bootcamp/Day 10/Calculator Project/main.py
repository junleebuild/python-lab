from art import logo


def add(n1, n2):
    return n1 + n2

def minus(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

operations = {"+": add, "-": minus, "/":divide, "*":multiply }
should_continue = True
while should_continue == True:
    print(logo)
    f_number = int(input("What's the first number?: "))
    calculate_continue = True
    while calculate_continue == True:
        for key in operations:
            print(key)
        operation = input("Pick an operation: ")
        next_number = int(input("What's the next number?: "))
        answer = operations[operation](f_number, next_number)
        print(f"{f_number} {operation} {next_number} = {answer}")
        continue_start = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if continue_start ==  'y':
            f_number = answer
        else:
            calculate_continue = False
            print("\n" * 20)


