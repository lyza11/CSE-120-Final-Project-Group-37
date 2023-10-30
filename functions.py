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

def pythagorean_theorem():
    print("What side are you missing? (1 - Hypotenuse, 2 - Leg)")
    action = input(": ")
    if action == "1":
        adjacent = float(input("Enter the Adjacent side: "))
        opposite = float(input("Enter the Opposite side: "))
        return (adjacent * adjacent) + (opposite * opposite)
    elif action == "2":
        hypotenuse = float(input("Enter the Hypotenuse: "))
        leg = float(input("Enter the Leg: "))
        return math.sqrt((hypotenuse*hypotenuse) - (leg*leg)) 
    else:
        print("Invalid input. Please try again.")
