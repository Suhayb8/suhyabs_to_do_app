import json
import os
def load_tasks():
    try:
        if os.path.exists("todo.json"):
            with open("todo.json", "r") as f:
                load = json.load(f)
                return load
        else:
            print("No task yet!")
    except ValueError:
        print("Please Enter valid value")
def add_task():
    tasks = []
    while True:
        user_input = input("Enter a task (or type 'done' to finish): ")
        if user_input == "done":
            break
        tasks.append(user_input)
    return tasks

tasks = add_task()
def save_task(tasks):
    with open("todo.json" , "w") as f:
        json.dump(tasks, f)

save_task(tasks)
show = load_tasks()

def numbring_tasks(show):
    for i,task in enumerate(show, start=1):
        print(f"{i}: {task}")

numbring_tasks(show)

def delete_task(tasks):
    print("----Choose wich do you want remove----")
    for i,task in enumerate(tasks, start=1):
        print(f"{i}: {task}")
    try:
        ask_dele = int(input("Enter the number of the task you want remove: ")) -1
        if 0 <= ask_dele < len(tasks):
            removed = tasks.pop(ask_dele)
            print(f"✅Removed: {removed}")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("❌ Please enter a valid number.")
delete_task(tasks)
save_task(tasks)

def edit_task(tasks):
    for i, task in enumerate(tasks, start=1):
        print(f"{i}: {task}")
    try:
        edit = int(input("Enter the number of the task you want to change: ")) - 1
        if 0 <= edit < len(tasks):
            print("👇🏼 Under this line enter the new task:")
            new_task = input("")
            old = tasks[edit]
            tasks[edit] = new_task
            print(f"✅ Replaced '{old}' with '{new_task}'")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("❌ Please enter a valid number.")

edit_task(tasks)
save_task(tasks)

