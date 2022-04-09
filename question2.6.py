"""
A palindrome is a sequence of characters which reads the same backward as
forward, such as madam or racecar.
Write a function check(string) which accept a string and check if it is a palindrome or not .
Display appropriate messages.

@author: Krishaay Jois
"""

def check(string: str) -> bool:
    if(string == string[::-1]):
        return True
    return False

string = input("Enter String: ").strip()
print("Palindrome" if check(string) else "Not a palindrome")
