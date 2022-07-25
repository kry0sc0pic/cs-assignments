"""
Write a menu driven program to do the following
1) Create a dict having product code and name
2) Accept a product code and change the name
3) Accept a product code and delete the product
4) Accept a product code and display the name

"""
product_db = {}
option = 0
print("Welcome to my market")
while option != 5:
    print("\nOptions")
    print("1. Add a new product into the database")
    print("2. Change a product's name")
    print("3. Delete product details from database")
    print("4. Display a product's name")
    print("5. Quit menu")
    print("\nEnter the option number: ")
    option = int(input())
    
    if option == 1:
        new_prod = input("Enter new product name: ")
        new_code = int(input("Enter new product code: "))
        product_db[new_code] = new_prod
        print("Product added in database!")
        
    elif option != 5:
        product_code = int(input("Enter product code: "))
        isproduct = product_db.get(product_code, None)
        if not isproduct:
            print("Sorry, product not found!")
        else:
            if option == 2:
                newname = input("Enter new name for product: ")
                product_db[product_code] = newname
                print("Product renamed.")
                    
            elif option == 3:
                deleted = product_db.pop(product_code)
                print("Product deleted.")
                
            elif option == 4:
                print("Product name: ", product_db[product_code])