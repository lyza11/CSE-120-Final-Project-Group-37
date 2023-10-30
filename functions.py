# Function for the menu
def menu():
    print("Options:")
    print('1 - add')
    print('2 - subtract')
    print('3 - multiply')
    print('4 - divide')
    print('5 - special functions')
    print('6 - quit')
    print()

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y