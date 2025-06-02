import json
import os


print("---🧮 Calculator with History---")

def load_history():
    if os.path.exists("calc_history.json"):
        with open("calc_history.json", "r") as f:
            try:
                history = json.load(f)
                return history
            except json.JSONDecodeError:
                return []
    else:
        return []

def save_history(history: list):
    with open("calc_history.json", "w") as f:
        json.dump(history , f, indent=4)

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

def record_calculation(history, expression):
    history.append(expression)
    return history

def calculator(history):

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = add(num1, num2)
            history.append(f"{num1} + {num2} = {result}")
            save_history(history)
        elif operator == "-":
            result = subtract(num1, num2)
            history.append(f"{num1} - {num2} = {result}")
            save_history(history)
        elif operator == "*":
            result = multiply(num1, num2)
            history.append(f"{num1} * {num2} = {result}")
            save_history(history)
        elif operator == "/":
            result = divide(num1, num2)
            if result is None:  # means division by zero
                print("🧣 Cannot divide by zero.")
                return  # stop here, don’t add to history or print result
            history.append(f"{num1} / {num2} = {result}")
            save_history(history)
        else:
            print("❌ Invalid operator.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("❌ Please enter valid numbers.")
        return


def main():
    history = load_history()
    print("Welcome to Calculator with History!")

    # First calculation to get initial result
    calculator(history)
    if not history:
        print("No calculations done.")
        return

    # Get initial result from last calculation
    last_expr = history[-1]
    # Extract result from last expression by splitting at '='
    try:
        result = float(last_expr.split('=')[1].strip())
    except:
        print("Error parsing last result. Exiting.")
        return

    while True:
        continue_c = input("Continue? (yes to continue, stop to quit): ").lower()
        if continue_c == "stop":
            print("Goodbye!")
            break
        elif continue_c == "yes":
            try:
                operator = input("Enter operator (+, -, *, /): ")
                next_num = float(input("Enter next number: "))

                if operator == "+":
                    new_result = add(result, next_num)
                    expr = f"{result} + {next_num} = {new_result}"
                elif operator == "-":
                    new_result = subtract(result, next_num)
                    expr = f"{result} - {next_num} = {new_result}"
                elif operator == "*":
                    new_result = multiply(result, next_num)
                    expr = f"{result} * {next_num} = {new_result}"
                elif operator == "/":
                    if next_num == 0:
                        print("🧣 Cannot divide by zero.")
                        continue
                    new_result = divide(result, next_num)
                    expr = f"{result} / {next_num} = {new_result}"
                else:
                    print("❌ Invalid operator.")
                    continue

                result = new_result
                history.append(expr)
                save_history(history)
                print(f"Updated Result: {result}")

            except ValueError:
                print("❌ Please enter a valid number.")
        else:
            print("❌ Please enter 'yes' or 'stop'.")

    # Optional: print full history at the end
    print("\n📜 Calculation History:")
    for h in history:
        print(h)



main()
