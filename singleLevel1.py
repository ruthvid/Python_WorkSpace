# Question 1 (Zepto – Grocery Delivery )
# Parent Class: Order
# • Instance variables: order_id, items, amount (initialize inside __init__)
# • Method:
# o show_order() →
# ▪ Create a local variable tax = 50
# ▪ Print all order details + tax
# Child Class: Delivery
# • Method:
# o show_delivery() →
# ▪ First, call parent method show_order()
# ▪ Then print delivery status
# Object Creation
# • Create an object of Delivery with all details.
# • Call show_delivery() → this will show both order (parent) + delivery (child).

class Order:
    def __init__(self,order_id,items,amount):
        self.order_id = order_id
        self.items = items
        self.amount = amount
        
    def showOrder(self):
        tax = 50
        final_amount = self.amount + tax
        print(f"your order id is {self.order_id} which is having {self.items} and amount to be paid is {self.amount} with an addition of {tax} rupees of Tax...So your final amount is {final_amount}")
        
class Delivery(Order):
    def __init__(self, order_id, items, amount):
        super().__init__(order_id, items, amount)
    
    def showDelivery(self):
        super().showOrder()
        print("Your Order is getting Packed")
        
        
obj1 = Delivery(100,5,500)
obj1.showDelivery()
        






# Question 2 (Amazon – E-commerce )
# Parent Class: Product
# • Instance variables: name, price, category
# • Method:
# o show_product() →
# ▪ Create a local variable platform = "Amazon"
# ▪ Print product details + platform
# Child Class: DiscountedProduct
# • Method:
# o show_discount(discount_percentage) →
# ▪ Call show_product() from parent
# ▪ Create a local variable final_price = price - (price * discount_percentage /
# 100)
# ▪ Print discount details + final price
# Object Creation
# • Create an object of DiscountedProduct.
# • Call show_discount() → this will show product details + discounted price.


class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
    def show_product(self):
        platform = "Amazon"
        print(f"You have Ordered {self.name} in the category {self.category} which is of price {self.price} from the platform {platform}")
        
        
class Discounted_product(Product):
    def __init__(self,name,price,cat):
        super().__init__(name,price,cat)
    def show_discount(self, discounted_percent):
        super().show_product()
        final_price = self.price - (self.price * (discounted_percent/100))
        print(f"Actual price is {self.price} ")
        print(f"you Will get a discount of {discounted_percent}% so your final price will be {final_price}")
        

product1 = Discounted_product("mobile",20000,"electronics")
product1.show_discount(10)   







# Question 3 (Uber – Ride Booking )
# Parent Class: Ride
# • Instance variables: ride_id, pickup, drop
# • Method:
# o show_ride() →
# ▪ Create a local variable distance = 12
# ▪ Print ride details + distance
# Child Class: Driver
# • Method:
# o show_driver() →
# ▪ Call show_ride() from parent
# ▪ Print driver status
# Object Creation
# • Create an object of Driver.
# • Call show_driver() → this will show ride (parent) + driver (child).     


class Ride:
    def __init__(self,ride_id,pickup,drop):
        self.ride_id = ride_id
        self.pickup = pickup
        self.drop = drop
    def show_ride(self):
        distance = 12
        print(f"pickup {self.ride_id} from {self.pickup} and drop at {self.drop} which is of distance {distance}km.")
        
class Driver(Ride):
    def __init__(self,id,pick,drop):
        super().__init__(id,pick,drop)
    def show_driver(self):
        super().show_ride()
        print("Driver is on the Way...!")
        
ride1 = Driver(1001,"Kphb","Madhapur")
ride1.show_driver()



        