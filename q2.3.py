"""
Write a function listreplace (ARR,n)in Python, which accepts a list ARR of numbers , the function will
increase the odd number by value 100 and multiply even number by 10 .
Sample Input Data of the list is: a=[10,20,23,45]

>>>
listreplace(a,4)
output : [100, 200, 123, 145]

"""

def listreplace(ARR, n):
    for i in range(n):
        if not ARR[i] % 2:
            ARR[i] *= 10
        else:
            ARR[i] += 100
    return ARR

lst = eval(input("Enter list: "))
print(listreplace(lst, len(lst)))