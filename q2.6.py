"""
A palindrome is a sequence of characters which reads the same backward as
forward, such as madam or racecar.
Write a function check(string) which accept a string and check if it is a palindrome or not .
Display appropriate messages.

"""

def is_palindrome(string):
    if string == string[::-1]:
        print("palindrome")
    else:
        print("not palindrome")


is_palindrome(input())
