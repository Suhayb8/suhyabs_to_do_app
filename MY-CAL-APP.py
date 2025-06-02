

print("-_- MY CAL APP -_-")

import json
import os

def load_cal():
    if os.path.exists("my_cal.json"):
        try:
            with open("my_cal.json", "r") as f:
                my_cal_load = json.load(f)
                return my_cal_load
        except json.JSONDecodeError:
            return []
    else:
        return []

def save_cal(history: list):
    with open("my_cal.json", "w") as f:
        json.dump(history, f)

def add(x,y): return x+y
def subtract(x,y): return x-y
def multiply(x,y): return x*y
def divide(x,y):
    if y == 0:
        return None
    return x/y
def add_to_the_record(history, expresion):
    history.append(expresion)
    return history
def calculation(history):
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator(+, -, *, /): ")
        num2 = float(input("Enter the second number: "))
        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)


        elif operator =="*":
            result = multiply(num1, num2)

        elif operator == "/":
            result = divide(num1, num2)
            if result is None:
                print("🧣 Cannot divide by zero.")
                return
        else:
            print("🧣 Invalid operator.")

        history.append(f"✅ {num1} {operator} {num2}  = {result}")
        save_cal(history)
        print(f"\n🎯 Result: {result}\n")

        old_result = result
        while True:
            ask_user = input("Do you want to use the previous result? (yes/no): ").lower()
            if ask_user != "yes":
                break
            next_num = float(input("Enter a number: "))
            option_oprator = input("Choose an operator(+, -, *, /): ")
            if option_oprator == "+":
                result = add(result, next_num)
            elif option_oprator == "-":
                result = subtract(result, next_num)
            elif option_oprator == "*":
                result = multiply(result, next_num)
            elif option_oprator == "/":
                result = divide(result, next_num)
                if result is None:
                    print("🧣 Cannot divide by zero.")
                    return
            else:
                print("🧣 Invalid operator.")

            history.append(f"✅ {old_result} {option_oprator} {next_num}  = {result}")
            save_cal(history)
            print(f"\n🎯 Result: {result}\n")
    except ValueError:
        print("🧣Invalid value")


def clear_cal(history):
    confrime = input("⚠️ Are you sure you want to delete ALL the history? (yes/no): ").lower()
    if confrime == "yes":
        history.clear()
        print("🗑️All history removed.")
        return
    else:
        print("❌ Cancelled. Tasks not removed.")
def show_cal(history):
    print("\n🔁 History:")
    if not history:
        print("No calculation history yet.")
    for i,h in enumerate(history, start=1):
        print("🧾", i,  h)
def Remove_specific_cal(history):
    try:
        if history:
            ask_remove_spacific = int(input("Enter the specific number you want remove from the history: ")) - 1
            if 0 <= ask_remove_spacific < len(history):
                removed_item = history.pop(ask_remove_spacific)
                print(f"🫗{removed_item} Removed from the history")
            else:
                print("No history to remove.")
    except ValueError:
        print("Please enter a valid value!")
def history_txt_f(history):
    if history:
        with open("history_export.txt", "w") as f:
            f.write("🧾 Calculation History\n------------------------\n")
            for i, item in enumerate(history, start=1):
                f.write(f"{i}. {item}\n")
            print("✅ History successfully exported to 'history_export.txt'")
        with open("history_export.txt", "r") as f:
            print("📂 Contents of history_export.txt:\n")
            print(f.read())

    else:
        print("⚠️ No history to export.")
def main():

    history = load_cal()

    while True:
        print("\n -_-🤗welcome to Suhyab's Calculator!-_-")
        print("1.The calculator.")
        print("2.Undo")
        print("3.show all the history")
        print("4.Clear all the history.")
        print("5.Remove a specific calculation from history.")
        print("6.Quit")
        print("7.Export history to a text file")
        choose = input("Choose an option (1–4): ")
        if choose == "1":
            while True:
                calculation(history)

                con_cal = input("Do you want continue ? (yes/no): ").lower()
                if con_cal != "yes":
                    break
            save_cal(history)

        elif choose == "2":
            if history:
                removed = history.pop()
                print(f"🗑️ Removed last calculation: {removed}")
            else:
                print("No history to undo.")
            save_cal(history)
        elif choose == "3":
            show_cal(history)
        elif choose == "4":
            clear_cal(history)
            save_cal(history)
        elif choose == "5":
            Remove_specific_cal(history)
            save_cal(history)
        elif choose == "7":
            history_txt_f(history)
        elif choose == "6":
            print("👋Good bye!")
            break
        else:
            print("❌ Invalid choice. Try again.")


main()
