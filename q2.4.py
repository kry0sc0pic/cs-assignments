"""
Write a function listshift(list,n)in Python, which accepts a list of numbers and length of list n; the
function will replace the first half of the list with second

List=[11,22,33,44,55,66]

Output:
[44,55,66,11,22,33]

"""

def listshift(list1, n):
    list1[:n//2], list1[n//2:] = list1[n//2:], list1[:n//2]
    return list1

inp_list = eval(input("Enter list: "))
print(listshift(inp_list, len(inp_list)))