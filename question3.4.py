"""
Write a method to read characters from the keyboard one by one. Write all
lowercase alphabets get in a file ‘lower’, all upper case alphabets in a file ‘upper’
and all other characters in ‘others’. Display the contents of all the three files.\

"""

def readfile(filename):
    fs = open(filename, "r")
    contents = fs.read()
    fs.close()
    return contents

def create(filename, content_to_write):
    fs = open(filename, "w")
    fs.write(content_to_write)
    fs.close()

lower = ""
upper = ""
others = ""

while True:
    print("Loop stops on entering -1")
    char = input()
    if char == "-1":
        break
    elif char.islower():
        lower += char
    elif char.isupper():
        upper += char
    else:
        others += char

create("files/lower.txt", lower)
create("files/upper.txt", upper)
create("files/others.txt", others)

print(readfile("files/lower.txt"))
print(readfile("files/upper.txt"))
print(readfile("files/other.txt"))
