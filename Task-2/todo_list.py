def display_menu():
    """Display the main menu options."""
    print("\n" + "=" * 50)
    print("TO-DO LIST APP")
    print("=" * 50)
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark task as completed")
    print("4. Delete a task")
    print("5. Exit")
    print("=" * 50)


def add_task(tasks):
    """
    Add a new task to the to-do list.
    
    Args:
        tasks (list): List of task dictionaries
    """
    task_name = input("\nEnter the task: ").strip()
    
    if task_name:
        task = {
            'name': task_name,
            'completed': False
        }
        tasks.append(task)
        print(f"Task '{task_name}' added successfully!")
    else:
        print("Task cannot be empty!")


def view_tasks(tasks):
    """
    Display all tasks with their status.
    
    Args:
        tasks (list): List of task dictionaries
    """
    if not tasks:
        print("\nNo tasks in your to-do list!")
        return
    
    print("\n" + "=" * 50)
    print("YOUR TASKS:")
    print("=" * 50)
    
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task['completed'] else "✗"
        task_display = f"[{status}] {task['name']}"
        
        if task['completed']:
            print(f"{index}. {task_display} (Completed)")
        else:
            print(f"{index}. {task_display}")
    
    print("=" * 50)


def mark_completed(tasks):
    """
    Mark a task as completed.
    
    Args:
        tasks (list): List of task dictionaries
    """
    if not tasks:
        print("\nNo tasks to mark as completed!")
        return
    
    view_tasks(tasks)
    
    try:
        task_number = int(input("\nEnter the task number to mark as completed: "))
        
        if 1 <= task_number <= len(tasks):
            if tasks[task_number - 1]['completed']:
                print(f"Task '{tasks[task_number - 1]['name']}' is already completed!")
            else:
                tasks[task_number - 1]['completed'] = True
                print(f"Task '{tasks[task_number - 1]['name']}' marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")


def delete_task(tasks):
    """
    Delete a task from the to-do list.
    
    Args:
        tasks (list): List of task dictionaries
    """
    if not tasks:
        print("\nNo tasks to delete!")
        return
    
    view_tasks(tasks)
    
    try:
        task_number = int(input("\nEnter the task number to delete: "))
        
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f"Task '{deleted_task['name']}' deleted successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")


def main():
    """
    Main function to run the To-Do List application.
    """
    tasks = []  # List to store all tasks
    
    print("\nWelcome to the To-Do List App!")
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                add_task(tasks)
            elif choice == '2':
                view_tasks(tasks)
            elif choice == '3':
                mark_completed(tasks)
            elif choice == '4':
                delete_task(tasks)
            elif choice == '5':
                print("\n Thank you for using the To-Do List App!")
                print("Goodbye! \n")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")
                
        except KeyboardInterrupt:
            print("\n\n Program terminated by user.")
            break


if __name__ == "__main__":
    main()
