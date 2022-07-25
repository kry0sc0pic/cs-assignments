"""
Write a program to print every number between 2 and n (both inclusive)
which is divisble by m. Take m and n as input.

"""
m, n = int(input()), int(input())
for i in range(2, n+1):
    if not i % m:
        print(i)
