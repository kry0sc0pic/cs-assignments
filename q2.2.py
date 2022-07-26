"""
Calculate the sum of the following series for n terms. Accept x and n from the user and
pass it to the function sum.

s = x - x^3/3! + x^5/5! - x^7/7! + x^9/9! ......

Create functions for the following:


-> power which will calculate the power of x and returns it(not to use math.pow())
-> factorial which will calculate the factorial of the given number and returns it
-> Sum which will call the functions power and factorial , calculates the sum of the
given series and returns it

"""

def power(a, b):
    return a ** b

def factorial(n):
    prod = 1
    for i in range(2, n + 1):
        prod *= i
    return prod

def series_sum(x, n):
    sum = 0
    sign = 1
    for i in range(1, 2*n, 2):
        sum += sign * power(x, i)/factorial(i)
        sign *= -1
    return sum

print(series_sum(int(input("Enter x: ")), int(input("Enter n: "))))