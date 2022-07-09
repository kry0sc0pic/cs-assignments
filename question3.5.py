"""
Create a textfile with 5 lines in it. Read the textfile line by line and display each
word separated by ‘#’

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

create("files/test.txt", eval(input("Enter 5 lines: ")))
s = readfile("files/test.txt")
for i in s.split("\n"):
    print("#".join(i.split()))