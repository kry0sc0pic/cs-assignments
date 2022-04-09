"""
Write a function findinlist(list,n)in Python, which accepts a list of numbers and length of list , the
function will return the minimum value from the first half and maximum value from the second half.

List=[1,2,3,4,5,6,7,8,9,0]

Output:
Minimum number in [1,2,3,4,5] is 1
Maximum number in [6,7,8,9,0] is 9

@author: Krishaay Jois
"""

def findinlist(l: list , n: int) -> None:
    half = n//2
    first_half = l[:half]
    second_half = l[half:]
    print(f"Minimum number in {first_half} is {min(first_half)}")
    print(f"Maximum number in {second_half} is {max(second_half)}")

inp_list = eval(input("Enter List: "))
findinlist(inp_list, len(inp_list))