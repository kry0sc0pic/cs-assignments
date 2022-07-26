"""
Write a function listreplace (ARR,n)in Python, which accepts a list ARR of numbers , the function will
replace the odd number by value 100 and multiply even number by 10 .
Sample Input Data of the list is: a=[10,20,23,45]

>>>
listreplace(a,4)
output : [100, 200, 123, 145]

@author: Krishaay Jois
"""

def listreplace(a: list,n: int) -> list:
    for i in range(n):
        if(a[i]%2==0):
            a[i] = a[i] * 10
        else:
            a[i] = a[i] + 100
    return a
inp_list = eval(input("Enter List: "))
print(listreplace(inp_list, len(inp_list)))