"""
Accept 3 marks of 5 students in a nested
tuple. Display the total & average marks 
of each student.

"""
main_tup = tuple()
for _ in range(5):
    num = input("Enter student name: ")
    m1 = int(input("Enter first marks: "))
    m2 = int(input("Enter second marks: "))
    m3 = int(input("Enter third marks: "))
    main_tup += ((num,m1,m2,m3),)
    
for num, m1, m2, m3 in main_tup:
    total = m1 + m2 + m3
    print(num)
    print("Total marks:", total)
    print("Average marks:", total/3)