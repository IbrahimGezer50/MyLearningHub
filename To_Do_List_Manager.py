#  Project: To-Do List Manager

# To-Do List Manager

tasks = []
done = False

while True:
    print("\nOptions:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Search task")
    print("4. Remove task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        task = input("Enter task title:").strip()
        tasks.append({"title": task, "done": False})
        print("Task added")
        print(tasks)
        pass
    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            print("Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['title']} [ ]")
        pass
    elif choice == "3":
        if not tasks:
            print("No tasks yet.")
        else:
            task_search = input("Search Task: ").lower().strip()
            found = False
            for task in tasks:
                if task_search in task["title"].lower():
                    print(task)
                    found = True
            if not found:
                print("No matching tasks found.")
        pass
    elif choice == "4":
        task_to_remove = input("Which task do you want to remove?")
        found = False
        for task in tasks:
            if task_to_remove.lower() == task["title"].lower():
                tasks.remove(task)
                print("Successfully removed.")
                found = True
                break
        if not found:
            print("Task not found.")
        pass
    elif choice == "5":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1 to 5.")
