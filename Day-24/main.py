file = open("text.txt")
content = file.read()
print(content)
file.close()

# doesn't require to close the text
with open("text.txt") as file:
    content = file.read()
    print(content)

with open("text.txt", mode="a") as file:  # mode "a" append the text
    file.write("\nNew text")

with open("new_text.txt", mode="w") as file:  # mode "w" write file by clearing the previous text
    file.write("This is new text")

with open("/Users/user/Desktop/desktop.txt") as file:
    content = file.read()
    print(content)
