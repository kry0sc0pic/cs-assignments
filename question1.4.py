"""
Accept 3 Marks of 5 students in a nested
tuple.Display the total & average marks 
of each student

@author: Krishaay Jois
"""

tup = []

for i in range(5):
    # stu_name = input("Enter Name: ")
    stu_m1 = int(input("Marks 1: "))
    stu_m2 = int(input("Marks 2: "))
    stu_m3 = int(input("Marks 3: "))
    tup.append((stu_m1,stu_m2,stu_m3))

tup = tuple(tup)
n = 1
for i,j,k in tup:
    print("Student:",str(n))
    print("Total:",str(i+j+k))
    print("Average:",str((i+j+k)/3))
    print('\n')
    n+=1
