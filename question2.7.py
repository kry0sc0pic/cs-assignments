"""
Declare a dictionary named department globally with the following keys : deptno,dname and loc

Write the following following functions to:
Add() : To add records in the dictionary deoartment
Delete(): Accept deptno from user and delete the records
Update() Accept deptno and update the records(dname or location)
Display() display all records
Exit() End the application

Call the functions using proper menu

"""

department = {}
option = 0
print("Welcome to the department database")

def Add(deptno1, dname1, loc1):
    department[deptno1] = [dname1, loc1]
    print("\nDepartment", dname1, "added to database!")
    
def Delete(deptno1):
    if department.get(deptno1, None):
        department.pop(deptno1)
        print("\nDepartment", deptno1, "deleted from database!")
    else:
        print("\nSorry, department number not found!")
       
def Update(deptno1, dname1):
    if department.get(deptno1, None):
        department[deptno1][0] = dname1
        print("\nName of Department", deptno1, "updated in database!")
    else:
        print("\nSorry, department number not found!")
    
def Display():
    print(department)
    
    
while option != 5:
    print("\nOptions")
    print("1. Add a new department record into the database")
    print("2. Delete department details from database")
    print("3. Change a department's name or location")
    print("4. Display all departments")
    print("5. Quit menu")
    print("\nWhat do you wish to do? Enter the option number: ")
    option = int(input())
    
    if option == 1:
        new_num = int(input("Enter new department number: "))
        new_name = input("Enter new department name: ")
        new_loc = input("Enter new department location: ")
        Add(new_num, new_name, new_loc)

    elif option == 4:
        Display()
        
    elif option != 5:
        num = int(input("Enter department number: "))
        isdept = department.get(num, None)
        if not isdept:
            print("Sorry, department number not found!")
        else:
            if option == 2:
                Delete(num)
                    
            elif option == 3:
                Update(
                    num,
                    input("Enter new department name: ")
                )

print("Menu exited")
