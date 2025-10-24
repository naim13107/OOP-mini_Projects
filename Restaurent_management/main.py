from fooditem import FoodItem
from menu import Menu
from orders import Order
from restaurent import Restaurent
from user import Customer,Admin,Employee

mamar_restaurent = Restaurent("Mamar Restaurent")
def customer_menu():
    name=input('Enter your name : ')
    email=input('Enter your email : ')
    phone = input('Enter your Phone : ')
    address = input('Enter your Address : ')

    customer = Customer(name=name,email=email,phone=phone,address=address)
    
    while True :
        print(f'Welcome {customer.name}')
        print("1. View Menu ")
        print("2. Add item to cart ")
        print("3. View cart ")
        print("4. Pay bill ")
        print("5. Exit ")

        choice = int(input('Enter your Choice : '))

        if choice == 1 :
            customer.view_menu(mamar_restaurent)

        elif choice == 2 :
            item_name = input("Enter item name : ")
            item_quantity = int(input("Enter quantity : "))
            customer.add_to_cart(mamar_restaurent,item_name=item_name,quantity=item_quantity)

        elif choice == 3 :
            customer.view_cart()

        elif choice == 4 :
            customer.pay_bill(mamar_restaurent)

        elif choice == 5 :
            break

        else :
            print("Invalid Input")
                               
def admin_menu():
    name=input('Enter your name : ')
    email=input('Enter your email : ')
    phone = input('Enter your Phone : ')
    address = input('Enter your Address : ')

    admin = Admin(name=name,email=email,phone=phone,address=address)
    
    while True :
        print(f'Welcome {admin.name}')
        print("1. Add new item ")
        print("2. Add new employee ")
        print("3. View employee ")
        print("4. View items ")
        print("5. Delete item ")
        print("6. Exit ")

        choice = int(input('Enter your Choice : '))

        if choice == 1 :
            item_name = input("Enter item name : ")
            item_quantity = int(input("Enter item quantity : "))
            item_price = int(input("Enter item price : "))
            item = FoodItem(item_name,item_price,item_quantity)

            admin.add_new_item(mamar_restaurent,item=item)


        elif choice == 2 :
            name = input("Enter employee name : ")
            phone = input("Enter Phone : ")
            email = input("Enter employee email : ")
            designation = input("Enter employee designation : ")
            age = input("Enter employee age : ")
            salary = input("Enter employee salary : ")
            address = input("Enter employee adress : ")

            employee = Employee(name=name,phone=phone,email=email,designation=designation,age=age,salary=salary,address=address)
            admin.add_employee(mamar_restaurent,employee=employee)

        elif choice == 3 :
            admin.view_employee(mamar_restaurent)

        elif choice == 4 :
            admin.view_menu(mamar_restaurent)

        elif choice == 5 :
            item_name = input("Enter item name : ")
            admin.remove_item(mamar_restaurent,item_name)

        elif choice == 6:
            break
        else :
            print("Invalid Input")                               


while True : 
    print("Welcome !!")
    print("1. Customer ")
    print("2. Admin ")
    print("3. Exit ")

    choice = int(input('Enter your Choice : '))

    if choice == 1 :
        customer_menu()
    elif choice == 2 :
        admin_menu()
    elif choice == 3 :    
        break      
    else : 
        print("Invalid Input !")   
