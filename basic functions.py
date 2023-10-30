
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

# Main calculator loop
while True:
    # User menu
    print("Options:")
    print('1 - add')
    print('2 - subtract')
    print('3 - multiply')
    print('4 - divide')
    print('5 - quit')

    user_input = input(": ")

    if user_input == "5":
        break
    elif user_input in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "1":
            result = add(num1, num2)
        elif user_input == "2":
            result = subtract(num1, num2)
        elif user_input == "3":
            result = multiply(num1, num2)
        elif user_input == "4":
            result = divide(num1, num2)

        print("Result: " + str(result))
    else:
        print("Invalid input. Please try again.")

