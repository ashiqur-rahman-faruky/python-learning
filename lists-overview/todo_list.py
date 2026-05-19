#!/usr/bin/env python3
"""
Simple Terminal Todo List Application
Demonstrates Python list operations
"""

def display_menu():
    """Display the main menu options"""
    print("\n" + "="*40)
    print("📝 TODO LIST MANAGER")
    print("="*40)
    print("1. View all tasks")
    print("2. Add a task")
    print("3. Mark task as complete")
    print("4. Delete a task")
    print("5. Clear all tasks")
    print("6. Exit")
    print("="*40)


def view_tasks(tasks):
    """Display all tasks with their status"""
    if not tasks:
        print("\n✨ No tasks yet! You're all clear.")
        return
    
    print("\n📋 Your Tasks:")
    print("-" * 40)
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["completed"] else "⬜"
        print(f"{i}. {status} {task['description']}")
    print("-" * 40)


def add_task(tasks):
    """Add a new task to the list"""
    description = input("\n📝 Enter task description: ").strip()
    
    if description:
        task = {
            "description": description,
            "completed": False
        }
        tasks.append(task)
        print(f"✅ Added: '{description}'")
    else:
        print("❌ Task description cannot be empty!")


def complete_task(tasks):
    """Mark a task as completed"""
    if not tasks:
        print("\n❌ No tasks to complete!")
        return
    
    view_tasks(tasks)
    
    try:
        index = int(input("\nEnter task number to mark complete: ")) - 1
        
        if 0 <= index < len(tasks):
            if tasks[index]["completed"]:
                print("ℹ️  This task is already completed!")
            else:
                tasks[index]["completed"] = True
                print(f"✅ Marked complete: '{tasks[index]['description']}'")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number!")


def delete_task(tasks):
    """Remove a task from the list"""
    if not tasks:
        print("\n❌ No tasks to delete!")
        return
    
    view_tasks(tasks)
    
    try:
        index = int(input("\nEnter task number to delete: ")) - 1
        
        if 0 <= index < len(tasks):
            deleted_task = tasks.pop(index)
            print(f"🗑️  Deleted: '{deleted_task['description']}'")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number!")


def clear_all_tasks(tasks):
    """Clear all tasks with confirmation"""
    if not tasks:
        print("\n❌ No tasks to clear!")
        return
    
    confirm = input(f"\n⚠️  Delete all {len(tasks)} tasks? (yes/no): ").lower()
    
    if confirm in ["yes", "y"]:
        tasks.clear()
        print("🗑️  All tasks cleared!")
    else:
        print("❌ Cancelled.")


def main():
    """Main program loop"""
    tasks = []
    
    # Optional: Start with some sample tasks
    # tasks = [
    #     {"description": "Learn Python lists", "completed": True},
    #     {"description": "Build todo app", "completed": False},
    # ]
    
    print("\n🎉 Welcome to your Todo List Manager!")
    
    while True:
        display_menu()
        choice = input("\nChoose an option (1-6): ").strip()
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            clear_all_tasks(tasks)
        elif choice == "6":
            print("\n👋 Goodbye! Stay productive!")
            break
        else:
            print("\n❌ Invalid option! Please choose 1-6.")


if __name__ == "__main__":
    main()
