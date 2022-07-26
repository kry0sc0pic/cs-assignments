"""
WAP to work with a binary file. 
The file contains the records of the student
having the following format.
Sno, Name and marks (taken as a list)

Write a menu driven program to do the following.
a. Add a record
b. Display all records
c. Accept Sno and modify the marks of that student
d. Accept Sno and modify the name of that student.
"""

import pickle

def addRecord(record: list) -> None:
    with open('files/student','ab') as f:
        pickle.dump(record,f)
    

def displayRecords() -> None:
    with open('files/student','rb') as f:
        try:
            while True:
                print(pickle.load(f))
        except EOFError:
            pass


def updateMarks(sno: int , marks: int) -> None:
    newD = []
    with open('files/student','rb') as f:
        try:
            while True:
                d = pickle.load(f)
                if d[0] == sno:
                    d[2] = marks
                newD.append(d)
        except EOFError:
            pass
    with open('files/student','wb') as f:
        for r in newD:
            pickle.dump(r,f)


def updateName(sno: int , name: str ) -> None:
    newD = []
    with open('files/student','rb') as f:
        try:
            while True:
                d = pickle.load(f)
                if d[0] == sno:
                    d[1] = name
                newD.append(d)
        except EOFError:
            pass
    with open('files/student','wb') as f:
        for r in newD:
            pickle.dump(r,f)


def main() -> None:
    shouldExit = False
    while not shouldExit:
        # dispaly a menu and choose options
        print("1. Add a record")
        print("2. Display all records")
        print("3. Update marks")
        print("4. Update name")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            record = []
            sno = int(input("Enter the sno: "))
            name = input("Enter the name: ")
            marks = int(input("Enter the marks: "))
            record.append(sno)
            record.append(name)
            record.append(marks)
            addRecord(record)
        elif choice == 2:
            displayRecords()
        elif choice == 3:
            sno = int(input("Enter the sno: "))
            marks = int(input("Enter the marks: "))
            updateMarks(sno,marks)
        elif choice == 4:
            sno = int(input("Enter the sno: "))
            name = input("Enter the name: ")
            updateName(sno,name)
        elif choice == 5:
            shouldExit = True
        else:
            print("Invalid choice")

main()