"""
Create a textfile with 5 lines in it. Read the textfile line by line and display each
word separated by ‘#’

@author: Krishaay Jois
"""


def createFile():
    try:
        f = open('files/textfile35.txt', 'w')
        f.write(
            "This is Line 1\nThis is Line2\nThis is Line3\nThis is Line4\nThis is Line5")
        f.close()
    except:
        print("Error in creating file")


def hash_separate():
    try:
        f = open('files/textfile35.txt', 'r')
        for line in f.readlines():
            words = line.split()
            for word in words:
                print(word+"#", end="")
            print()
        f.close()
    except:
        print("Error in hashing")

createFile()
hash_separate()