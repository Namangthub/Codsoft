tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' has been added to the list.")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' has been removed from the list.")
    else:
        print(f"Task '{task}' not found in the list.")

def show_tasks():
    if tasks:
        print("Tasks in the To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
        
        else:
            print("To-Do List is empty.")

while True:
    print("\nTo-Do List App Menu:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Show tasks")
    print("4. Ouit")

    choice = input("Enter your choice (1/2/3/4) : ")

    if choice == '1':
        task = input("Enter the task to add:")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove:")
        remove_task(task)
    elif choice == '3':
        show_tasks()
    elif choice == '4':
        print("exit")
        break
    else:
        print("Invalid choice. Please choose a valid option.")