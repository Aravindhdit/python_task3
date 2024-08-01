# To-do List Program

def display_menu():
    print("To-Do List Manager")
    print("==================")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    print("==================")

def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task(tasks):
    task = input("Enter the task to add: ")
    tasks.append(task)
    print(f"Task '{task}' has been added to your to-do list.")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' has been removed from your to-do list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Exiting To-Do List Manager.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
