from functions import menu, special_functions_menu, add, subtract, multiply, divide, pythagorean_theorem

while True:
    menu()
    user_input = input(": ")
    if user_input == "6":
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
        print()
    else:
        print("Invalid input. Please try again.")

    if user_input == "5":
        special_functions_menu()
        special_user_input = input(": ")
        if special_user_input == "1":
            print(pythagorean_theorem())
        elif special_user_input == "2":
            pass
        elif special_user_input == "3":
            pass
        elif special_user_input == "4":
            pass
        elif special_user_input == "5":
            pass
        else:
            print("Invalid input. Please try again.")
