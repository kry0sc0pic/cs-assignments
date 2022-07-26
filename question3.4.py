"""
Write a method to read characters from the keyboard one by one. Write all
lowercase alphabets get in a file ‘lower’, all upper case alphabets in a file ‘upper’
and all other characters in ‘others’. Display the contents of all the three files.\

@author: Krishaay Jois
"""


def keylog():
    shouldExit = False
    while not shouldExit:
        try:
            char = input("Enter a character: ")
            if char.isalpha():
                if char.isupper():
                    f = open('files/upper.txt', 'a')
                    f.write(char)
                    f.close()
                elif char.islower():
                    f = open('files/lower.txt', 'a')
                    f.write(char)
                    f.close()
            else:
                f = open('files/others.txt', 'a')
                f.write(char)
                f.close()
        except:
            print("Error in keylog")
        finally:
            print("Do you want to continue? (y/n)")
            if input().lower() == "y":
                shouldExit = False
            else:
                shouldExit = True
