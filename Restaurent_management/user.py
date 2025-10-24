from abc import ABC
from restaurent import Restaurent
from orders import Order

class User (ABC) :

    def __init__(self,name,phone,email,address):
        self.name = name 
        self.phone = phone 
        self.email = email 
        self.address = address

class Customer(User):
     
    def __init__(self,name,phone,email,address):
        super().__init__(name,phone,email,address)
        self.cart = Order()

    def view_menu(self,restaurent):
        restaurent.menu.show_menu()

    def add_to_cart(self,restaurent,item_name,quantity):
        item = restaurent.menu.find_item(item_name)    
        if item :
            if quantity > item.quantity :
                print('Item quantity exceeded !!')
            else : 
                self.cart.add_item(item,quantity)
                print('Item ordered')    
        else :
            print('item not find')

    def view_cart(self):
        print("**** Cart ****")
        print("Name\tPrice\tQuantity")
        for item ,quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}") 
        print(f"Total Price : { self.cart.total_price }")                

    def pay_bill(self, restaurent):
        
        for item, quantity in self.cart.items.items():
           
            menu_item = restaurent.menu.find_item(item.name)
            if menu_item:
                if menu_item.quantity >= quantity:
                    menu_item.quantity -= quantity
                else:
                    print(f"Error: Not enough {item.name} in stock. Available: {menu_item.quantity}, Requested: {quantity}")
                    return False  
        
        print(f"Total {self.cart.total_price} paid successfully")
        self.cart.clear()
        return True  


class Employee (User):

    def __init__(self,name,phone,email,address,age,designation,salary):
        super().__init__(name,phone,email,address)
        self.age = age 
        self.designation = designation
        self.salary = salary


class Admin(User):

    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
    
    def add_employee(self,restaurent,employee):
        restaurent.add_employee(employee)

    def view_employee(self,restaurent):
        restaurent.view_employee()
    
    def add_new_item(self,restaurent,item):
        restaurent.menu.add_menu_item(item)

    def remove_item(self,restaurent,item):
        restaurent.menu.remove_item(item)    

    def view_menu (self,restaurent) : 
        restaurent.menu.show_menu()    







  
        





                    


# ad=Admin('Naim',1212,'aaa@gmail.com','Dhaka')
# ad.add_employee("boltu",123123,'boltu@gmail.com','Dinajpur',23,'Chef',30000)
# ad.view_employee()
# mamar_dokan=Restaurent("Mamar Dokan")
# item1=FoodItem('Dal' , 10 , 100)
# item2=FoodItem('vatt' , 10 , 100)
# item3=FoodItem('Murgi' , 100 , 50)
# ad=Admin('Naim',1212,'aaa@gmail.com','Dhaka')
# ad.add_new_item(mamar_dokan,item1)
# ad.add_new_item(mamar_dokan,item2)
# ad.add_new_item(mamar_dokan,item3)

# customer1= Customer('Rahim','rahim@gamil.com',1221221,'Dhaka')
# customer1.view_menu(mamar_dokan)
        
# item_name = input ('Enter item name : ')
# item_quantity = input('Enter item quantity : ')

# customer1.add_to_cart (mamar_dokan,item_name,item_quantity)
# customer1.view_cart() 