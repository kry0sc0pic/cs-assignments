"""
Write a function generate() which will accept an integer as argument, generates a random
number with exactly ‘n’ digits and returns it. Accept a number ‘n’ from the user and
pass it to the generate function . If ‘n’ is not passed to the function during the call then the
function should return a 3 digit number generated randomly.

"""

import random as rng
def generate(n = 3):
    result = str(rng.randint(1, 9))
    for i in range(n-1):
        result += str(rng.randint(0, 9))
        
    return int(result)

print(generate())
print(generate(int(input())))