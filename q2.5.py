"""
Write a function findinlist(list,n)in Python, which accepts a list of numbers and length of list , the
function will return the minimum value from the first half and maximum value from the second half.

List=[1,2,3,4,5,6,7,8,9,0]

Output:
Minimum number in [1,2,3,4,5] is 1
Maximum number in [6,7,8,9,0] is 9

"""

def findinlist(List, n):
    print("Minimum number in", List[:n//2], "is", min(List[:n//2]))
    print("Maximum number in", List[n//2:], "is", max(List[n//2:]))

inp_list = eval(input("Enter list: "))
findinlist(inp_list, len(inp_list))