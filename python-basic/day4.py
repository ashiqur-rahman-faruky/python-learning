#Practice some beginner level problem & practice loops

# Write a program that takes an integer N and prints numbers from 1 to N.
# N = int(input("Enter an integer N:"))

# for i in range(1, N+1):
#     print(i)

# Take an integer N and calculate the sum from 1 to N.
# N = int(input("Enter an integer N:"))
# sum = 0
# for i in range (1, N+1):
#     sum += i
# print(sum)


# Take a number N and print its multiplication table from 1 to 10.
# N = int(input("Enter an integer N:"))

# for i in range (1, 11):
#     print(f"{N} x {i} = {N*i}")


# Take an integer N and count how many even numbers exist between 1 and N.
# N = int(input("Enter an integer N:"))
# even_count = 0
# for i in range(1, N+1):
#     if i % 2 == 0:
#         even_count += 1
# print(even_count)

# Print the following pattern for N = 5:
# *
# **
# ***
# ****
# *****

# for i in range (1, 6):
#     print("*" * i)


# *****
# ****
# ***
# **
# *

# for i in range(5, 0, -1):
#     print("*" * i)

i = 5
while i > 0:
    print("*" * i)
    i -= 1 