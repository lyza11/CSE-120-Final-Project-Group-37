from functions import menu, add, subtract, multiply, divide

while True:
    menu()
    user_input = input(": ")
    if user_input == "6":
        break
    elif user_input in ["1", "2", "3", "4", "5", "6"]:
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
        print()
    else:
        print("Invalid input. Please try again.")
