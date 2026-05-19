# Python Lists - Complete Guide

## What are Lists?

Lists are ordered, mutable collections that can store multiple items of different types.

```python
# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty = []
```

## Accessing Elements

```python
fruits = ["apple", "banana", "cherry", "date"]

# Index starts at 0
print(fruits[0])      # "apple"
print(fruits[2])      # "cherry"

# Negative indexing (from end)
print(fruits[-1])     # "date"
print(fruits[-2])     # "cherry"

# Slicing [start:end:step]
print(fruits[1:3])    # ["banana", "cherry"]
print(fruits[:2])     # ["apple", "banana"]
print(fruits[2:])     # ["cherry", "date"]
print(fruits[::2])    # ["apple", "cherry"]
```

## Modifying Lists

```python
# Adding elements
fruits.append("elderberry")        # Add to end
fruits.insert(1, "apricot")        # Insert at index
fruits.extend(["fig", "grape"])    # Add multiple items

# Removing elements
fruits.remove("banana")            # Remove first occurrence
last = fruits.pop()                # Remove and return last item
second = fruits.pop(1)             # Remove at index
del fruits[0]                      # Delete by index
fruits.clear()                     # Remove all items

# Changing elements
fruits[0] = "avocado"
fruits[1:3] = ["blueberry", "cantaloupe"]
```

## Common List Operations

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Length
print(len(numbers))           # 8

# Sorting
numbers.sort()                # Sort in place
sorted_nums = sorted(numbers) # Return new sorted list

# Reversing
numbers.reverse()             # Reverse in place
reversed_nums = numbers[::-1] # Return new reversed list

# Counting and finding
count = numbers.count(1)      # Count occurrences
index = numbers.index(4)      # Find first index

# Checking membership
if 5 in numbers:
    print("5 is in the list")
```

## List Comprehensions

```python
# Create lists efficiently
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

evens = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

upper_fruits = [fruit.upper() for fruit in ["apple", "banana"]]
# ["APPLE", "BANANA"]
```

## Iterating Over Lists

```python
fruits = ["apple", "banana", "cherry"]

# Basic iteration
for fruit in fruits:
    print(fruit)

# With index
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# While loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
```

## Practice Exercises

1. Create a list of your 5 favorite movies
2. Add 2 more movies to the end
3. Insert a movie at position 2
4. Remove the movie at index 4
5. Print the list in reverse order
6. Sort the list alphabetically
7. Find if a specific movie is in your list
8. Create a new list with only movies that have more than 10 characters

## Ready for the Project?

Now that you understand lists, let's build a todo list application!
