"""
Write a method in Python to create a text file ‘notes’.
Read the file and count ‘.’ and ‘,’ (as separate counts). Display the contents of
original file and count.

@author: Krishaay Jois
"""

def createFile() -> None:
    try:
        f = open('files/notes.txt','w')
        f.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
        f.close()
    except:
        print("Error in creating file")
    
def readFile() -> None:
    try:
        f = open('files/notes.txt','r')
        print((data := f.read()))
        comma_count = data.count(',')
        fstop_count = data.count('.')
        f.close()
        print("Comma Count:",comma_count)
        print("Fstop Count:",fstop_count)
    except:
        print("Error in reading file")

createFile()
readFile()
