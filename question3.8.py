"""
WAP to work with a CSV file. The file contains the records of the student
having the following format
Rno, Name and marks (taken as a list)
Write a menu driven program to do the following.
a.Add a single record
b.Add a multiple record in one GO
c.Display all records
"""
import csv
def addRecord(record: list):
    with open('files/student.csv','a+',newline="") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(record)
        
def addMultipleRecord(records: list):
    with open('files/student.csv','a+',newline="") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerows(records)

def displayRecord():
    with open('files/student.csv','r') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            print(row)

def main():
    while True:
        print("1. Add a single record")
        print("2. Add a multiple record in one GO")
        print("3. Display all records")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            record = eval(input("Enter the record: "))
            addRecord(record)
        elif choice == 2:
            records = eval(input("Enter the records: "))
            addMultipleRecord(records)
        elif choice == 3:
            displayRecord()
        elif choice == 4:
            break
        else:
            print("Invalid choice")

main()