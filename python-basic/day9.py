# file system
# error handling

# test_file = open("test.txt", "w")
# test_file.write("Hello world! I am Ashiqur Rahman")
# test_file.close()

# test_file = open("test.txt", "r")
# content = test_file.read()
# print(content)
# test_file.close()

#recommended way
try:
    with open("test.txt", "a") as file:
        content = file.write("\nCan you share your name also")

        print(content)
except Exception as e:
    print("Error: ", e)