"""
Write a method to create a textfile ‘original’ with 5 lines in it. Copy all the
contents of the original file into another file called ‘copy’, by removing all the
lines that contain alphabet ‘a’ in it.

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
    
create("files/original.txt", eval(input()))
contents = readfile("files/original.txt")
copy_contents = []
for i in contents.split("\n"):
    if "a" not in i:
        copy_contents.append(i)
        
with open("files/copy.txt", "w") as f:
    f.writelines(copy_contents)