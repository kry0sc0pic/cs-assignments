"""
Write a program to print every number between 2 and n 
which is divisble by n including m and n. Take m and n as input.

"""
n = int(input('Enter End Number: '))
m = int(input('Enter Divisor Number: '))

for i in range(2,n+1):
    print(i if i%m==0 else '')
