# Day 6: Lists - Storing and Managing Collections of Data
# This script features a 'Terminal Todo List' to demonstrate creating, modifying, and accessing list elements (append, remove, index, and looping through items).

# fruits = ["apple", "banana", "mango"]
# fruits.append("date")

# for fruit in fruits:
#     print(fruit)


#simple todo example
# todos = []
# todos.append("Learn Python")
# todos.append("Build Project")

# for task in todos:
#     print(task)


#todo application
todos =[]
while True:
    print("\nTODO Application")
    print("1. Add Task")
    print("2. Show Task")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        task = input("Enter Task:")
        todos.append(task)
        print("Task added")
    elif choice == 2:
        print("\nYour Tasks:")
        for task in todos:
            print("-",task)
    elif choice == 3:
            print("Goodbye!")
            break
    else:
        print("Invalid choice")

    