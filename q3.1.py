"""
Write a method in Python to create a text file ‘notes’.
Read the file and count ‘.’ and ‘,’ (as separate counts). Display the contents of
original file and count.

"""

def create(filename, content_to_write):
    fs = open(filename, "w")
    fs.write(content_to_write)
    fs.close()  
    
def readfile(filename):
    fs = open(filename, "r")
    contents = fs.read()
    fs.close()
    return contents
  
contents = input()
create("files/notes.txt", eval(contents))
new_content = readfile("files/notes.txt")
print(
      new_content, 
      new_content.count("."), 
      new_content.count(","),
      sep="\n")
