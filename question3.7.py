"""
WRAP to work with a binary file. 
The file contains the records of the student
having the following format.
Sno, Name and marks (taken as a list)

Write a menu driven program to do the following.
a. Add a record
b. Display all records
c. Accept Sno and modify the marks of that student
d. Accept Sno and modify the name of that student.

"""

import pickle as pkl
option = 0
print("Welcome to the student binary file datbase!")
MAINFILE = "files/student.dat"

def add(rec1):
    f = open(MAINFILE, "ab")
    pkl.dump(rec1, f)
    f.close()

def display():
    f = open(MAINFILE, "rb")
    try:
        while True:
            print(pkl.load(f))
    except:
        f.close()

def Marks_mod(srno, new_marks):
    f = open(MAINFILE, "rb+")
    s = []
    try:
        while True:
            s.append(pkl.load(f))
    except:
        f.seek(0)
        isname = False
        for i in s:
            if i[0] == srno:
                i[2] = new_marks
                isname = True
                break
        if isname:
            for i in s:
                pkl.dump(i, f)
            print("\nMarks modified")
        else:
            print("Sorry, serial number not found!")
        
        f.close()


def Name_mod(srno, new_name):
    f = open(MAINFILE, "rb+")
    s = []
    try:
        while True:
            s.append(pkl.load(f))
    except:
        f.seek(0)
        isname = False
        for i in s:
            if i[0] == srno:
                i[1] = new_name
                isname = True
                break
        if isname:
            for i in s:
                pkl.dump(i, f)
            print("\nMarks modified")
        else:
            print("Sorry, serial number not found!")
        
        f.close()


while option != 5:
    print("\nOptions")
    print("1. Add a record")
    print("2. Display all records")
    print("3. Modify the marks of the student of given serial number")
    print("4. Modify the name of the student of given serial number")
    print("5. Quit menu")
    print("\nWhat do you wish to do? Enter the option number: ")
    option = int(input())
    
    if option == 1:
        new_num = int(input("\Enter serial number: "))
        new_name = input("Enter student name: ")
        new_marks = input("Enter marks: ")
        add([new_num, new_name, new_marks])
        print(f"\n{new_name} added to binary file database")

    elif option == 2:
        display()
        
    elif option != 5:
        num = int(input("Enter serial number: "))

        if option == 3:
            Marks_mod(
                num,
                input("Enter new student marks: ")
            )
                
        elif option == 4:
            Name_mod(
                num,
                input("Enter new student name: ")
            )

print("Menu exited")
