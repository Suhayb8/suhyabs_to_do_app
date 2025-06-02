import json
import os
from json import JSONDecodeError

print("📝 Welcome to My To-Do App")

# Load tasks from file if available
def load_tasks():
    if os.path.exists("todo.json"):
        try:
            with (open("todo.json", "r") as f):
               return json.load(f)

        except JSONDecodeError:
            return []
    return []


# Save tasks to file
def save_tasks(tasks):
    with open("todo.json", "w") as f:
        json.dump(tasks, f)

# Add a new task
def add_task(tasks):
    new_task = input("➕ Enter a new task: ")
    tasks.append({"task": new_task, "done": False})
    print("✅ Task added.")

# Show all tasks with status
def show_tasks(tasks):
    print("\n📋 Your Tasks:")
    if not tasks:
        print("No tasks yet.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {task['task']} [{status}]")

# Mark a task as done
def mark_done(tasks):
    show_tasks(tasks)
    try:
        done_index = int(input("\n✔️ Enter the number of the task you finished: ")) - 1
        if 0 <= done_index < len(tasks):
            tasks[done_index]["done"] = True
            print(f"🎉 Marked as done: {tasks[done_index]['task']}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Edit an existing task
def edit_task(tasks):
    show_tasks(tasks)
    try:
        edit_index = int(input("\n✏️ Enter the number of the task to edit: ")) - 1
        if 0 <= edit_index < len(tasks):
            new_text = input("Enter the new task text: ")
            old_text = tasks[edit_index]["task"]
            tasks[edit_index]["task"] = new_text
            print(f"🛠️ Replaced '{old_text}' with '{new_text}'")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        delete_index = int(input("\n🗑️ Enter the number of the task to delete: ")) - 1
        if 0 <= delete_index < len(tasks):
            removed_task = tasks.pop(delete_index)
            print(f"🗑️ Deleted: {removed_task['task']}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
            print("❌ Please enter a valid number.")


#Emtying all the data
def clear_all_tasks(tasks):
    confirm = input("⚠️ Are you sure you want to delete ALL tasks? (yes/no): ").lower()
    if confirm == "yes":
        tasks.clear()
        print("🧹 All tasks removed.")
    else:
        print("❌ Cancelled. Tasks not removed.")

# Main menu loop
def main():
    tasks = load_tasks()
    while True:
        print("\n📌 Menu:")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Edit Task")
        print("5. Delete Task")
        print("6. Clear All Tasks")
        print("7. Quit")
        choice = input("Choose an option (1–6): ")

        if choice == "1":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
            save_tasks(tasks)
        elif choice == "4":
            edit_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "6":
            clear_all_tasks(tasks)
            save_tasks(tasks)
        elif choice == "7":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

main()
