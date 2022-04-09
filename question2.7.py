"""
Declare a dictionary named department globally with the following keys : deptno,dname and loc

Write the following following functions to:
Add() : To add records in the dictionary deoartment
Delete(): Accept deptno from user and delete the records
Update() Accept deptno and update the records(dname or location)
Display() display all records
Exit() End the application

Call the functions using proper menu

@author: Krishaay Jois
"""

DB = {}

def displayopts() -> None:
    # print("\n") 
    print("1 -> Add")
    print("2 -> Delete")
    print("3 -> Update")
    print("4 -> Display")
    print("5 -> Exit")
    print("---------------")
def processOpt(opt: str) -> None:
    global DB
    if(opt == "1" or opt == "3"):
        print("[+] New Record" if opt == "1" else "[+] Update Record")
        deptNo = input("Department Number: ").strip()
        deptName = input("Department Name: ").strip()
        loc = input("LOC: ").strip()
        DB[deptNo] = {
            "deptName": deptName,
            "loc": loc
        }
        print(f"Created {deptNo}" if opt == "1" else f"Updated {deptNo}")
    elif(opt == "2"):
        print("[-] Delete Record")
        deptNo = input("Department Number: ").strip()
        del DB[deptNo]
        print(f"Deleted {deptNo}")
    elif(opt == "4"):
        print("Listing all records in DB\n")
        for num,data in DB.items():
            print(f"{num}:{data}")
        print('------------------')
    else:
        print("[!] Unknown Option")

shouldExit = False
while(not shouldExit):
    displayopts()
    option = input("Enter Option: ").strip()
    if(option == "5"):
        shouldExit = True
        print("Exiting..")
    else:
        processOpt(option)
