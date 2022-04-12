"""
Accept a string and check if it contains all unique
characters. Display the string and the message unique
or not unique

@author: Krishaay Jois
"""
string = input("Enter String: ").strip()
print(string)
if(len(list(string.replace(' ',''))) > len(set(list(string.replace(' ',''))))):
    print("NOT UNIQUE")
else:
    print("UNIQUE")
