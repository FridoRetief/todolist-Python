tasks = []
completed_tasks = []
menu = ""

# name of function display_menu when runs 4 outputs for users in 4 strings
# menu add_task view_task exit

# add tasks till you chose not to
# have option to remove tasks by the number of the task

# add another list where you can move finished tasks to

def display_menu():
    print("______________________________")
    print("Todolist MENU:")
    print("1. add_task")
    print("2. view_task/remove_task")
    print("3. mark your tasks as finished")
    print("4. exit")
    print("______________________________")

def add_task(menu):
    while menu.lower() != 'exit':
        task = input("Enter the task:")
        print("Success!")
        print("________________________________________________________________")
        menu = input("Type 'exit' to revert to main menu or Enter to add another task:")
        tasks.append(task)

def view_tasks(tasks):
    print("tasks:")
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task}")
    print("Here are all your tasks.")
    print("________________________")

    item_number = input("Press Enter to go back to main menu or type the number asigned to the task that you want to remove:")
    print("___________________________________________________________________________________________________")

    if item_number.isdigit():
        item_number = int(item_number)
        if 1 <= item_number <= len(tasks):
            del tasks[item_number - 1]
    print("Success!")

def finished_tasks(menu):
    while menu.lower() != 'exit':
        print("pending tasks")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")
        print("Here are all youre pending tasks.")
        print("_________________________________")
        
        print("finished tasks")
        for index, index_to_move in enumerate(completed_tasks, 1):
            print(f"{index}. {index_to_move}")
        print("Here are all your finished tasks.")
        print("_________________________________")
        
        index_to_move = int(input("Enter the number of the task you want to mark as done:")) - 1

        if 0 <= index_to_move < len(tasks):
            item_to_move = tasks.pop(index_to_move)
            completed_tasks.append(item_to_move)
        print("Success!")
        print("______________________________________________________")

        print("updated pending tasks")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")
        print("Here are all youre pending tasks.")
        print("_________________________________")

        print("updated finished tasks")
        for index, index_to_move in enumerate(completed_tasks, 1):
            print(f"{index}. {index_to_move}")
        print("Here are all youre finished tasks.")
        print("__________________________________")

        menu = input("Type 'exit' to go back to main menu or press enter to mark another task as finished:")

while True:
    display_menu()
    choice = input("Enter choice(1-3).")
    print("__________________")

    if choice == '1':
        add_task(menu)
    elif choice == '2':
        view_tasks(tasks)
    elif choice == '3':
        finished_tasks(menu)
    elif choice == '4':
        print("Goodbye ;)")
        break
    else:
        print("Invalid choice please enter number between 1 and 4.")
