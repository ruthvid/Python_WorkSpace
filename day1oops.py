# Question 1 – Zomato Food Ordering
# Create a class Restaurant to simulate Zomato’s restaurant system.
# Requirements:
# 1. The constructor should accept restaurant_name and menu (dictionary of items → price).
# 2. Define a method showMenu() that displays all items with prices.
# o Example: Pizza - ₹200, Burger - ₹120
# 3. Define a method orderFood(item, qty) that:
# o Checks if the item is available in the menu.
# o If available → prints the bill (price * qty).
# o If not available → prints "Item not available".
# 4. Create two restaurant objects (Dominos, KFC) with different menus.
# 5. Place orders from both restaurants.



# class restraunt:
#     def __init__(self,name,menu):
#         self.name = name
#         self.menu = menu
    
#     def showmenu(self):
#         print(self.menu)
#         print(f"-----------{self.name} Menu---------")
#         for fooditems in self.menu.items():
#             print(fooditems)
#     def orderFood(self,item,quantity):
#         if item in self.menu:
#             price = self.menu[item] * quantity
#             print(f"You oredred {item} * {quantity} from {self.name} and total is {price}")
#         else:
#             print("Item not available")
    
# dominos = restraunt("dominos",
#           {
#               "Pizza":200,
#               "Burger":120,
#               "Garlic Bread":220,
#           })

# kfc = restraunt("KFC",
#           {
#               "firedchicken":450,
#               "wings":250,
#               "strips":200,
#               "coke":60
#           })


# dominos.showmenu()
# kfc.showmenu()

# dominos.orderFood("Pizza",4)







# Question 2 – Uber Ride Booking
# Create a class Driver to simulate Uber driver details.
# Requirements:
# 1.  The constructor should accept driver_name, car_model, and per_km_rate.
# 2. Define a method showDriver() that prints driver details.
# o Example: Driver: Raj, Car: Swift, Rate: ₹20/km
# 3. Define a method calculateFare(distance) that calculates and prints the fare.
# o Example: Distance: 10 km, Fare: ₹200
# 4. Create 3 driver objects with different details.
# 5. For each driver, calculate fare for a trip (e.g., 8 km, 12 km, 15 km).


# class Driver:
#     def __init__(self,driver_name,car_model,per_km_rate):
#         self.driver_name = driver_name
#         self.car_model=car_model
#         self.per_km_rate=per_km_rate
#     def showDriver(self):
#         print(self.driver_name)
#         print(self.car_model)
#         print(self.per_km_rate)
#     def fareCalculation(self,distance):
#         Fare = distance * self.per_km_rate
#         print(f"your price is {Fare}")
        
#         pass
    
# driver1 = Driver("ramu","swift",20)
# driver2 = Driver("kumar","ertiga",30)
# driver3 = Driver("raju","innova",40)


# driver2.showDriver()

# driver2.fareCalculation(10)








# Question 3 – Flipkart Shopping Cart
# Create a class Product to simulate shopping on Flipkart.
# Requirements:
# 1. The constructor should accept product_name, price, and stock.
# 2. Define a method showDetails() that displays product details.
# o Example: Laptop - ₹50000, Stock: 10
# 3. Define a method buyProduct(qty) that:
# o If enough stock → reduces stock and prints total cost.
# o If not enough stock → print "Out of Stock".
# 4. Create 3 product objects (Laptop, Phone, Shoes) with different stock and price.
# 5. Simulate a shopping cart by:
# o Buying 2 items from Laptop.
# o Buying 1 item from Phone.
# o Trying to buy more Shoes than available stock.


class Product:
    def __init__(self,product_name,price,stock):
        self.product_name = product_name
        self.price = price
        self.stock = stock
        
    def showDetails(self):
        print(self.product_name)
        print(self.price)
        print(self.stock)
        
    def productQuantity(self,qty):
        if qty <= self.stock:
            self.stock -= 1
            final_price = self.price * qty
            print(f"You are buying {qty}{self.product_name} and your bill will be {final_price}")
        else:
            print("Item Out of Stock..")
        pass
    
lap = Product("laptop",50000,20)
mob = Product("mobile",20000,35)
tv = Product("TV",30000,0)
fridge = Product("Fridge",40000,5)


# Product.showDetails(mob)

fridge.productQuantity(5)




