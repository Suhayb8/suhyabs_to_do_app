

print("----my version calculator----")
import json
import os

def load_history_cal():
    if os.path.exists("my_version_calculator.json"):
        try:
            with open("my_version_calculator.json", "r") as f:
                my_load = json.load(f)
                return my_load
        except json.JSONDecodeError:
            return []
    return []

def save_history_cal(history: list):
    with open("my_version_calculator.json", "w") as f:
        json.dump(history, f, indent=4)

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0:
        print("🧣Undefined by Zero")
        return None
    return x / y
def record_history_cal(history, expresion):
    history.append(expresion)
    return history
def calculation_history_cal(history):
        try:
            num1 = float(input("Enter a number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter a number: "))

            if operator == "+":
                result = add(num1, num2)
                history.append(f"{num1} + {num2} = {result}")
            elif operator == "-":
                result = subtract(num1, num2)
                history.append(f"{num1} - {num2} = {result}")
            elif operator == "*":
                result = multiply(num1, num2)
                history.append(f"{num1} * {num2} = {result}")
            elif operator == "/":
                result = divide(num1, num2)
                if result is None:
                    return
                history.append(f"{num1} / {num2} = {result}")
            else:
                print("❌ Invalid operator.")
                return


            save_history_cal(history)

        except ValueError:
            print("❌ Please enter valid numbers.")


history = load_history_cal()
calculation_history_cal(history)

def show_history_cal(history):
    if history:  # checks if list has any items
        print("--- Calculation History ---")
        for entry in history:
            print(entry)
        else:
            print("No calculation history found.")

show_history_cal(history)
def main():
    history = load_history_cal()
    show_history_cal(history)
    try:
        num1 = float(input("Enter a number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter a number: "))

        if operator == "+":
            result = add(num1, num2)
            history.append(f"{num1} + {num2} = {result}")
        elif operator == "-":
            result = subtract(num1, num2)
            history.append(f"{num1} - {num2} = {result}")
        elif operator == "*":
            result = multiply(num1, num2)
            history.append(f"{num1} * {num2} = {result}")
        elif operator == "/":
            result = divide(num1, num2)
            if result is None:
                return
            history.append(f"{num1} / {num2} = {result}")
        else:
            print("❌ Invalid operator.")
            return
        history.append(f"{num1} {operator} {num2} = {result}")
        save_history_cal(history)
        print(f"Result: {result}")
    except ValueError:
        print("❌ Please enter valid numbers.")
        return
    while True:
            cont = input("Continue? (yes/stop): ").lower()

            if cont == "stop":
                print("Goodbye 👋")
                break
            elif cont == "yes":
                try:
                        next_numb = float(input("Enter next number: "))
                        operator = input("Enter operator (+, -, *, /): ")
                        if operator == "+":
                            new_result = add(result, next_numb)
                        elif operator == "-":
                            new_result = subtract(result, next_numb)
                        elif operator == "*":
                            new_result = multiply(result, next_numb)

                        elif operator == "/":
                            new_result = divide(result, next_numb)
                            if new_result is None:
                                print("🧣 Cannot divide by zero.")
                                return

                        else:
                            print("❌ Invalid operator.")
                            continue
                        history.append(f"{result} {operator} {next_numb} = {new_result}")
                        save_history_cal(history)
                        result = new_result
                        print(f"Updated Result: {result}")


                except ValueError:
                    print("❌ Invalid operator.")
            else:
                 print("❌ Please type 'yes' or 'stop'.")
main()

