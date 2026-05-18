# Day 3: Loops - Repetition in Code
# This script features a 'Counter' to demonstrate for loops (when iteration count is known)
# and while loops (when repetition depends on a condition).

print("=" * 50)
print("For Loops")
print("=" * 50)

# basic for loop with range()
print("\n1. Basic for loop with range()")
for i in range(5):
    print(f"Iteration {i}")

# range(start, stop, step)
print("\n2. For loop with range(start, stop)")
for i in range(2, 7):
    print(f"Iteration {i}")

# For loop with range(start, stop, step)
print("\n3. range with step range(start, stop, step)")
for i in range(10, 20, 3):
    print(f"Iteration {i}")

#Loop through a list
print("\n4. Loop through a list")
fruits = ['Apple', 'Banana', 'Cherry', 'Date']
for fruit in fruits:
    print(f"I like {fruit}")


#Loop through a string
print("\n5. Loop through a string")
for char in "Hello World!":
    print(f"Letter: {char}")

#Loop through a string with enumerate() to get index and character
print("\n6. Loop through a string with enumerate() function")
for index, char in enumerate("Hello World!"):
    print(f"Character {index}: {char}")

#Loop through dictionary
print("\n7. Loop through a dictionary")
person = {"name": 'Ashiqur Rahman', "age": 29, "city": 'Dhaka'}
for key, value in person.items():
    print(f"{key}: {value}")

#Nested loops
print("\n8. Nested loops")
for i in range(4):
    for j in range(2):
        print(f"Outer loop {i}, Inner loop {j}")

print("\n" + "=" * 50)
print("While Loops")
print("=" * 50)

print("\n1. Basic while loop")
count = 0
while count <5:
    print(f"Count : {count}")
    count += 1


#while loop with condition 
print("\n2. while loop with condition")
number = 1
while number<=10: 
    print(f"Number: {number}")
    number += 3

#while True with break 
print("\n3. Infinite loop with break")
number = 1;
while True:
    print(f"Number: {number}")
    number += 1
    if(number == 5):
        break


# ==============================================
# 3. LOOP CONTROL STATEMENTS
# ==============================================


print("\n" + "=" * 50)
print("Loop Control Statements")
print("=" * 50)

# continue - skip to next iteration
print("\n1. break statement:")
for i in range (5, 10):
    if(i == 7):
        print(f"Breaking at {i}")
        break
    print(f"Number: {i}")



# continue - skip to next iteration
print("\n2. continue statement:")
for i in range(5, 10):
    if(i == 7):
        print(f"Skipping {i}")
        continue
    print(f"Number: {i}")


# else with loops (runs if loop completes without break)
print("\n3. else with for loop:")

for i in range(5, 10):
    print(f"Number: {i}")
else:
    print("Loop completed without break")

print("\n4. else with break:")
for i in range(5, 10):
    if(i == 7):
        print(f"Breaking at {i}")
        break
    print(f"Number: {i}")
else:
    print("Not printed because loop was broken")