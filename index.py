with open("txt.txt.txt","r") as file:
    content = file.read()
    print(content)
    
with open("example.txt", "w") as file:
    file.write("New Content")

with open("example.txt", "a") as file:
    file.write("\njarjar")

with open("example.txt","r") as file:
    content = file.read()
    print(content)
