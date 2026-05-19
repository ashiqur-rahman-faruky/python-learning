# Python Lists - Quick Reference Cheat Sheet

## Creating Lists
```python
empty = []
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14]
```

## Accessing Elements
```python
fruits[0]        # First element
fruits[-1]       # Last element
fruits[1:3]      # Slice [start:end]
len(fruits)      # Length
```

## Adding Elements
```python
fruits.append("date")              # Add to end
fruits.insert(1, "apricot")        # Insert at position
fruits.extend(["fig", "grape"])    # Add multiple
```

## Removing Elements
```python
fruits.remove("banana")   # Remove by value
last = fruits.pop()       # Remove last and return
item = fruits.pop(1)      # Remove at index
del fruits[0]             # Delete by index
fruits.clear()            # Remove all
```

## Searching & Checking
```python
"apple" in fruits         # Check membership
fruits.index("banana")    # Find index
fruits.count("apple")     # Count occurrences
```

## Sorting & Reversing
```python
numbers.sort()                # Sort in place
sorted_nums = sorted(numbers) # Return new sorted list
numbers.reverse()             # Reverse in place
reversed_nums = numbers[::-1] # Return new reversed
```

## Iterating
```python
for fruit in fruits:
    print(fruit)

for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

## List Comprehensions
```python
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
upper = [s.upper() for s in fruits]
```

## Common Patterns in Todo App
```python
# Filter list
pending = [task for task in tasks if not task["completed"]]

# Check if empty
if not tasks:
    print("No tasks")

# Get element safely
if 0 <= index < len(tasks):
    task = tasks[index]

# Loop with index
for i, task in enumerate(tasks, 1):  # Start at 1
    print(f"{i}. {task['description']}")
```

## Key List Operations Used in Todo App

1. **append()** - Add new tasks
2. **pop()** - Delete tasks by index
3. **enumerate()** - Display tasks with numbers
4. **len()** - Count tasks
5. **clear()** - Clear all tasks
6. **List comprehension** - Filter completed/pending tasks
7. **Indexing** - Access and modify specific tasks
8. **in operator** - Check if element exists
