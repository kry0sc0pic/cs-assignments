"""
Write a method to create a textfile ‘original’ with 5 lines in it. Copy all the
contents of the original file into another file called ‘copy’, by removing all the
lines that contain alphabet ‘a’ in it.

@author: Krishaay Jois
"""

def createFile():
    try:
        f = open('files/original.txt','w')
        f.write("apple\nrynthm\norange\nbell\ncat")
        f.close()
    except:
        print("Error in creating file")

def createCopy():
    try:
        f = open('files/original.txt','r')
        f_new = open('files/copy.txt','w')
        lines = []
        for line in f.readlines():
            if "a" in line:
                lines.append(line)
        f_new.writelines(lines)
        f.close()
        f_new.close()
    except:
        print("Error in creating copy")

createFile()
createCopy()