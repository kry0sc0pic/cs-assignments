"""
Write a function listshift(list,n)in Python, which accepts a list of numbers and length of list , the
function will replace the first half of the list with second

List=[11,22,33,44,55,66]

Output:
[44,55,66,11,22,33]

@author: Krishaay Jois
"""

def listshift(l: list,n: int) -> list:
    half = n//2
    first_half = l[:half]
    second_half = l[half:]
    second_half+=first_half
    return second_half

inp_list = eval(input("Enter List: "))
print(listshift(inp_list,len(inp_list)))