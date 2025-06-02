print("---- 🧮 My Calculator App! ----")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("🧣 Cannot divide by zero.")
        return None
    return x / y

def calculator():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        else:
            print("❌ Invalid operator.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("❌ Please enter valid numbers.")
        return

    # Continue loop
    while True:
        continue_c = input("Continue? (yes to continue, stop to quit): ").lower()
        if continue_c == "stop":
            print("👋 Goodbye!")
            break
        elif continue_c == "yes":
            try:
                operator = input("Enter operator (+, -, *, /): ")
                next_num = float(input("Enter next number: "))
                if operator == "+":
                    result = add(result, next_num)
                elif operator == "-":
                    result = subtract(result, next_num)
                elif operator == "*":
                    result = multiply(result, next_num)
                elif operator == "/":
                    result = divide(result, next_num)
                else:
                    print("❌ Invalid operator.")
                    continue
                print(f"Updated Result: {result}")
            except ValueError:
                print("❌ Please enter valid number.")
        else:
            print("❌ Type 'yes' or 'stop' only.")

calculator()
