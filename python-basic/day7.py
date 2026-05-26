# Day 6: Dictionaries 
student = {
    "name": "Ashiqur Rahman",
    "age": "29",
    "class":"MSC"
}
student["country"] = "Bangladesh"

# print(student["name"])
# print(student["age"])

# student["age"] = 30

# print(student["age"])

# print(student)

for key, value in student.items():
    print(f"{key} : {value}")