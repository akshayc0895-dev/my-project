# Project 12: Simple To-Do List
# Add and view tasks in a list

print("=" * 40)
print("SIMPLE TO-DO LIST")
print("=" * 40)

tasks = []

while True:
    print("\n" + "-" * 40)
    print("MENU:")
    print("1. Add task")
    print("2. View all tasks")
    print("3. Mark task as done")
    print("4. Exit")
    print("-" * 40)
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print(f"Task added: '{task}'")
    
    elif choice == '2':
        if len(tasks) == 0:
            print("Your to-do list is empty.")
        else:
            print("\nYOUR TO-DO LIST:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            print(f"Total: {len(tasks)} task(s)")
    
    elif choice == '3':
        if len(tasks) == 0:
            print("No tasks to mark as done.")
        else:
            print("\nCurrent tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            
            try:
                task_num = int(input("Enter task number to mark as done: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"Task completed: '{removed}'")
                else:
                    print(f"Invalid number. Choose 1 to {len(tasks)}")
            except ValueError:
                print("Please enter a valid number.")
    
    elif choice == '4':
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")

print("=" * 40)