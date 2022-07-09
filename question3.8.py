"""
WRAP to work with a CSV file. The file contains the records of the student
having the following format
Rno, Name and marks (taken as a list)
Write a menu driven program to do the following.
a.Add a single record
b.Add a multiple record in one GO
c.Display all records

"""

import csv

MAINFILE = "files/student.csv"
print("Welcome to the student CSV file datbase!")

option = 0

def add_one(rec1):
    f = open(MAINFILE, "a", newline = "")
    writer = csv.writer(f)
    writer.writerow(rec1)
    f.close()

def add_many(recs):
    f = open(MAINFILE, "a", newline = "")
    writer = csv.writer(f)
    writer.writerows(recs)
    f.close()

def display_all():
    f = open(MAINFILE, "r", newline = "")
    reader = csv.reader(f)
    for i in reader:
        print(*i, sep = ", ")
    f.close()

while True:
    print("\nOptions")
    print("1. Add a single record")
    print("2. Add multiple records at once")
    print("3. Display all records")
    print("4. Quit menu")
    print("\nWhat do you wish to do? Enter the option number: ")
    option = int(input())
    
    if option == 1:
        new_rec = eval(input("Enter new record as a list: "))
        add_one(new_rec)
        print(f"\n{new_rec} added to CSV file database")

    elif option == 2:
        new_recs = eval(input("Enter new records as a nested list: "))
        add_many(new_recs)
        print("New records added to CSV file database")
        
    elif option == 3:
        display_all()

    elif option == 4:
        break

print("Menu exited")