"""
Write a menu driven program to do the following
1) Create a dict hacing product code and name
2) Accept a product code and change the name
3) Accept a product code and delete the product
4) Accept a product code and display the name
"""

options = {
    1: "create",
    2: "edit",
    3: "delete",
    4: "get",
    5: "exit"
}
db = {}
shouldExit = False
while not shouldExit:
    print("Options:\n1 -> Create\n2 -> Edit\n3 -> Delete\n4 -> Get\n5 -> Exit")
    opt = int(input("Option >> "))
    print('\n\n')
    if(opt == 5):
        shouldExit = True
    elif(opt==1 or opt == 2):
        code = input("Enter Product Code: ")
        pname = input("Enter Product Name: ")
        db[code] = pname
    elif(opt == 3):
        code = input("Enter Product Code: ")
        try:
            pname = db[code]
            print("Deleting Product:",pname)
            del db[code]
        except KeyError:
            print("ERROR: No such product exists")
    elif(opt == 4):
        code = input("Enter Product Code: ")
        try:
            pname = db[code]
            print(code,"->",pname)
        except KeyError:
            print("ERROR: No such product exists")
    print('\n\n')