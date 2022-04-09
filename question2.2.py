"""
Calculate the sum of the following series for n terms. Accept x and n from the user and
pass it to the function sum.

s = x - x^3/3! + x^5/5! - x^7/7! + x^9/9! ......

Create functions for the following:


-> power which will calculate the power of x and returns it(not to use math.pow())
-> factorial which will calculate the factorial of the given number and returns it
-> Sum which will call the functions power and factorial , calculates the sum of the
given series and returns it

@author: Krishaay Jois
"""

def power(x:int , power: int) -> int:
    return x ** power

def factorial(n:int) -> int:
    p = 1
    for i in range(2,n+1):
        p*=i
    return p

def Sum(x: int, n: int):
    s = x
    for i in range(3,x+1,2):
        s+= (power(x,i)/factorial(i))
    return x

x = int(input("Enter (x): ").strip())
n = int(input("Enter (n): ").strip())

print(Sum(x,n))