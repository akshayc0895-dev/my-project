# CLI To-Do App
# Add, remove, list, and complete tasks with file storage

import os
from datetime import datetime

TODO_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from file into dictionary."""
    tasks = {}
    if os.path.exists(TODO_FILE):
        try:
            with open(TODO_FILE, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        task_id, description, status = line.split('|')
                        tasks[int(task_id)] = {
                            'description': description,
                            'status': status,
                            'created': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        }
        except Exception as e:
            print(f"Error loading tasks: {e}")
    return tasks

def save_tasks(tasks):
    """Save tasks from dictionary to file."""
    try:
        with open(TODO_FILE, 'w') as f:
            for task_id, task_info in tasks.items():
                f.write(f"{task_id}|{task_info['description']}|{task_info['status']}\n")
        return True
    except Exception as e:
        print(f"Error saving tasks: {e}")
        return False

def add_task(tasks, description):
    """Add a new task."""
    if not description:
        print("Error: Task description cannot be empty.")
        return False
    
    task_id = max(tasks.keys()) + 1 if tasks else 1
    tasks[task_id] = {
        'description': description,
        'status': 'pending',
        'created': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return save_tasks(tasks)

def list_tasks(tasks, filter_status=None):
    """List all tasks with optional status filter."""
    if not tasks:
        print("\nNo tasks found.")
        return
    
    filtered_tasks = tasks
    if filter_status:
        filtered_tasks = {k: v for k, v in tasks.items() if v['status'] == filter_status}
    
    if not filtered_tasks:
        print(f"\nNo {filter_status} tasks found." if filter_status else "\nNo tasks found.")
        return
    
    print("\n" + "=" * 60)
    print(f"{'ID':<5} {'Status':<10} {'Task'}")
    print("=" * 60)
    
    for task_id, task_info in sorted(filtered_tasks.items()):
        status_display = "✓" if task_info['status'] == 'completed' else "○"
        print(f"{task_id:<5} {status_display:<10} {task_info['description']}")
    
    print("=" * 60)
    print(f"Total: {len(filtered_tasks)} tasks")

def complete_task(tasks, task_id):
    """Mark a task as completed."""
    if task_id not in tasks:
        print(f"Error: Task {task_id} not found.")
        return False
    
    if tasks[task_id]['status'] == 'completed':
        print(f"Task {task_id} is already completed.")
        return True
    
    tasks[task_id]['status'] = 'completed'
    return save_tasks(tasks)

def remove_task(tasks, task_id):
    """Remove a task."""
    if task_id not in tasks:
        print(f"Error: Task {task_id} not found.")
        return False
    
    removed = tasks.pop(task_id)
    print(f"Removed: {removed['description']}")
    return save_tasks(tasks)

def get_valid_number(prompt):
    """Get a valid number from user input."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")

def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 40)
    print("CLI TO-DO APP")
    print("=" * 40)
    print("1. Add task")
    print("2. List all tasks")
    print("3. List pending tasks")
    print("4. List completed tasks")
    print("5. Complete a task")
    print("6. Remove a task")
    print("7. Exit")
    print("=" * 40)

def main():
    """Main program loop."""
    tasks = load_tasks()
    print(f"Loaded {len(tasks)} tasks from {TODO_FILE}")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            description = input("Enter task description: ")
            if add_task(tasks, description):
                print("Task added successfully.")
        
        elif choice == '2':
            list_tasks(tasks)
        
        elif choice == '3':
            list_tasks(tasks, 'pending')
        
        elif choice == '4':
            list_tasks(tasks, 'completed')
        
        elif choice == '5':
            if not tasks:
                print("No tasks to complete.")
                continue
            list_tasks(tasks, 'pending')
            task_id = get_valid_number("Enter task ID to complete: ")
            if complete_task(tasks, task_id):
                print("Task marked as completed.")
        
        elif choice == '6':
            if not tasks:
                print("No tasks to remove.")
                continue
            list_tasks(tasks)
            task_id = get_valid_number("Enter task ID to remove: ")
            if remove_task(tasks, task_id):
                print("Task removed successfully.")
        
        elif choice == '7':
            print("Goodbye! Tasks saved.")
            break
        
        else:
            print("Invalid choice. Please enter 1-7.")

if __name__ == "__main__":
    main()