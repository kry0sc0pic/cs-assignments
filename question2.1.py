"""
Question:
Write a function generate() which will accept an integer as argument ,generates a random
number with exactly ‘n’ digits and returns it. Accept a number ‘n’ from the user and
pass it to the generate function . If ‘n’ is not passed to the function during the call then the
function should return a 3 digit number generated randomly.

@author: Krishaay Jois
"""

import random
def generate(n: int = 3) -> int:
    if n is None:
        n = 3
    num = ""
    for _ in range(n):
        num+=str(random.randint(0, 9) if len(num) > 0 else random.randint(1, 9))
    return int(num)

# Run with input
print(generate(int(i) if  (i := input("Enter Number: ")) else None))
# Run without input
# print(generate())