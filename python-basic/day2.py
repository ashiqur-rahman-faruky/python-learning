# Day 2: Control Flow - Logic and Comparison Operators
# This script features an 'Age Checker' to demonstrate if/else statements
# and comparison operators (>, <, >=, <=, ==).

age = int(input('What is your age? '));

if(age < 0):
    print('Invalid age');
elif(age <= 12):
    print('You are a child');
elif(age <= 17):
    print('You are a teenager');
elif(age <= 59):
    print('You are an adult');
else:    
    print('You are a senior citizen');