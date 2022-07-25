"""
A file ‘sports’ contains information in following format :
Event participant (in notepad with a single space separating both).
Write a method that would read the contents and creates a file named ‘athletics’,
copying only those records from sports where the event name is ‘athletics’.

"""

def readfile(filename):
    fs = open(filename, "r")
    contents = fs.read()
    fs.close()
    return contents

def filter_athletics():
    details = readfile("files/sports.txt")
    new_content = []
    for i in details.split('\n'):
        if i.split()[1].lower() == "athletics":
            new_content.append(i)
            
    with open("files/athletics.txt") as f:
        f.writelines(new_content)

filter_athletics()