# Day 3: Loops - Repetition in Code (Practice)
# This script features a 'Counter' to demonstrate for loops (when iteration count is known)
# and while loops (when repetition depends on a condition).


# Example 1: Sum of numbers (1 to 10)

print("\n1. Sum of numbers from 1 to 10")
total = 0
for i in range(1, 11):
    total += i
    # if i < 10:
    #     print(f"{i} +", end=' ')
    # else:
    #     print(f"{i} = ", end=' ')

    print(i, end=' + ' if i < 10 else ' = ')
print(total)

print("\n1. Sum of numbers from 1 to 10")
numbers = range(1, 11)
print(" + ".join(map(str, numbers)) + " = " + str(sum(numbers)))


# Example 2: Find even numbers
print("\n2. Odd numbers between 55 to 65")
total_odd = 0;
for i in range(55, 66):
    if i % 2 != 0:
        print(i, end=' ')
        total_odd += 1
print(f"\nTotal of odd numbers between 55 to 65 is: {total_odd}")


# Example 3: Countdown
print("\n3. Countdown:")
count = 5
while count > 0:
    print(count, end=' -> ')
    count -=1
print("Boom!")