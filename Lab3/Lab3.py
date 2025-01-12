# task 1
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

with open("example.txt", "r") as file:
    for line in file:
        print(line)

#task 2
line = str(input())
with open("user_input.txt", "w") as file:
    file.write(line)
with open("user_input.txt", "r") as file:
    content = file.read()
    print(content)

line = str(input())
with open("user_input.txt", "a") as file:
    file.write(line)
with open("user_input.txt", "r") as file:
    content = file.read()
    print(content)

#task 3
try:
    with open("noFile.txt", "r") as file:
        content = file.read()
        print(content)
except:
    print("Such file doesn't exist, try another")

