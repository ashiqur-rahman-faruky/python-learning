#Goal
#We will build a system that can:
#Save them to a file
#Load users back
#View all users

import json
def load_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except:
        return []

def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file)


users = load_users()
while True:
    print("\n1. Add User")
    print("2. Show Users")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1": 
        name = input("Enter user name: ")
        age = input("Enter user age: ")

        user = {
            "name":name,
            "age":age
        }

        users.append(user)
        save_users(users)
        print("User Saved!")

    elif choice == "2":
        print("\n All Users:")

        for user in users:
            print(f"{user["name"]} - {user["age"]}")
    elif choice == "3":
        print("Bye")
        break
    else:
        print("Invalid Choice")
