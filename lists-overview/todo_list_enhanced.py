#!/usr/bin/env python3
"""
Enhanced Terminal Todo List with File Persistence
Saves tasks to a JSON file so they persist between sessions
"""

import json
import os
from datetime import datetime


TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from file"""
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("⚠️  Error reading tasks file. Starting fresh.")
            return []
    return []


def save_tasks(tasks):
    """Save tasks to file"""
    try:
        with open(TASKS_FILE, 'w') as f:
            json.dump(tasks, f, indent=2)
    except Exception as e:
        print(f"⚠️  Error saving tasks: {e}")


def display_menu():
    """Display the main menu options"""
    print("\n" + "="*40)
    print("📝 TODO LIST MANAGER (Enhanced)")
    print("="*40)
    print("1. View all tasks")
    print("2. View pending tasks")
    print("3. View completed tasks")
    print("4. Add a task")
    print("5. Mark task as complete")
    print("6. Mark task as pending")
    print("7. Delete a task")
    print("8. Clear completed tasks")
    print("9. Clear all tasks")
    print("10. Exit")
    print("="*40)


def view_tasks(tasks, filter_type="all"):
    """Display tasks with optional filtering"""
    if filter_type == "pending":
        filtered = [t for t in tasks if not t["completed"]]
        title = "📋 Pending Tasks:"
    elif filter_type == "completed":
        filtered = [t for t in tasks if t["completed"]]
        title = "✅ Completed Tasks:"
    else:
        filtered = tasks
        title = "📋 All Tasks:"
    
    if not filtered:
        print(f"\n✨ No {filter_type} tasks!")
        return
    
    print(f"\n{title}")
    print("-" * 60)
    for i, task in enumerate(tasks, 1):
        if filter_type == "all" or (
            (filter_type == "pending" and not task["completed"]) or
            (filter_type == "completed" and task["completed"])
        ):
            status = "✅" if task["completed"] else "⬜"
            created = task.get("created", "Unknown")
            print(f"{i}. {status} {task['description']}")
            print(f"   📅 Created: {created}")
    print("-" * 60)
    print(f"Total: {len(filtered)} tasks")


def add_task(tasks):
    """Add a new task to the list"""
    description = input("\n📝 Enter task description: ").strip()
    
    if description:
        task = {
            "description": description,
            "completed": False,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        tasks.append(task)
        save_tasks(tasks)
        print(f"✅ Added: '{description}'")
    else:
        print("❌ Task description cannot be empty!")


def complete_task(tasks):
    """Mark a task as completed"""
    if not tasks:
        print("\n❌ No tasks available!")
        return
    
    view_tasks(tasks)
    
    try:
        index = int(input("\nEnter task number to mark complete: ")) - 1
        
        if 0 <= index < len(tasks):
            if tasks[index]["completed"]:
                print("ℹ️  This task is already completed!")
            else:
                tasks[index]["completed"] = True
                save_tasks(tasks)
                print(f"✅ Marked complete: '{tasks[index]['description']}'")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number!")


def uncomplete_task(tasks):
    """Mark a task as pending again"""
    if not tasks:
        print("\n❌ No tasks available!")
        return
    
    view_tasks(tasks)
    
    try:
        index = int(input("\nEnter task number to mark pending: ")) - 1
        
        if 0 <= index < len(tasks):
            if not tasks[index]["completed"]:
                print("ℹ️  This task is already pending!")
            else:
                tasks[index]["completed"] = False
                save_tasks(tasks)
                print(f"⬜ Marked pending: '{tasks[index]['description']}'")
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
            save_tasks(tasks)
            print(f"🗑️  Deleted: '{deleted_task['description']}'")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number!")


def clear_completed_tasks(tasks):
    """Clear only completed tasks"""
    completed = [t for t in tasks if t["completed"]]
    
    if not completed:
        print("\n❌ No completed tasks to clear!")
        return
    
    confirm = input(f"\n⚠️  Delete {len(completed)} completed tasks? (yes/no): ").lower()
    
    if confirm in ["yes", "y"]:
        tasks[:] = [t for t in tasks if not t["completed"]]
        save_tasks(tasks)
        print(f"🗑️  Cleared {len(completed)} completed tasks!")
    else:
        print("❌ Cancelled.")


def clear_all_tasks(tasks):
    """Clear all tasks with confirmation"""
    if not tasks:
        print("\n❌ No tasks to clear!")
        return
    
    confirm = input(f"\n⚠️  Delete all {len(tasks)} tasks? (yes/no): ").lower()
    
    if confirm in ["yes", "y"]:
        tasks.clear()
        save_tasks(tasks)
        print("🗑️  All tasks cleared!")
    else:
        print("❌ Cancelled.")


def main():
    """Main program loop"""
    tasks = load_tasks()
    
    print("\n🎉 Welcome to your Todo List Manager!")
    if tasks:
        pending = len([t for t in tasks if not t["completed"]])
        completed = len([t for t in tasks if t["completed"]])
        print(f"📊 Loaded {len(tasks)} tasks ({pending} pending, {completed} completed)")
    
    while True:
        display_menu()
        choice = input("\nChoose an option (1-10): ").strip()
        
        if choice == "1":
            view_tasks(tasks, "all")
        elif choice == "2":
            view_tasks(tasks, "pending")
        elif choice == "3":
            view_tasks(tasks, "completed")
        elif choice == "4":
            add_task(tasks)
        elif choice == "5":
            complete_task(tasks)
        elif choice == "6":
            uncomplete_task(tasks)
        elif choice == "7":
            delete_task(tasks)
        elif choice == "8":
            clear_completed_tasks(tasks)
        elif choice == "9":
            clear_all_tasks(tasks)
        elif choice == "10":
            print("\n👋 Goodbye! Stay productive!")
            break
        else:
            print("\n❌ Invalid option! Please choose 1-10.")


if __name__ == "__main__":
    main()
