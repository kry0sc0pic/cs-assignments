"""
WAP to work with a CSV file. The file contains the records of the student
having the following format
Rno, Name and marks (taken as a list)
Write a menu driven program to do the following.
a.Add a single record
b.Add a multiple record in one GO
c.Display all records
"""

def addRecord(record: str):
    with open('files/student.csv','a+') as f:
        f.write(f'{record}\n')

def addMultipleRecord(records: list):
    with open('files/student.csv','a+') as f:
        for record in records:
            f.write(f"{record}\n")

def displayRecord():
    with open('files/student.csv','r') as f:
        for line in f:
            print(line)

def main():
    while True:
        print("1. Add a single record")
        print("2. Add a multiple record in one GO")
        print("3. Display all records")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            record = input("Enter the record: ").strip()
            addRecord(record)
        elif choice == 2:
            records = input("Enter the records: ").split('\n')
            addMultipleRecord(records)
        elif choice == 3:
            displayRecord()
        elif choice == 4:
            break
        else:
            print("Invalid choice")

main()