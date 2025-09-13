# Multiple Inheritance in Uber  

# 1. Create Parent Class 1 → Person 
# o Attributes: name, contact. 
# o Example values: "Rahul", "9876543210". 
# 2. Create Parent Class 2 → Driver 
# o Attributes: license_no, rating. 
# o Example values: "DLX12345", 4.9. 
# 3. Create Child Class → UberDriver (inherits from Person + Driver) 
# o Extra Attribute: car. 
# o Example value: "Hyundai i20". 
# 4. Constructor & Data Passing 
# o When creating an UberDriver object, pass all attributes: 
# ▪ name, contact (for Person) 
# ▪ license_no, rating (for Driver) 
# ▪ car (for UberDriver). 
# 5. Object Creation Example 
# 6. d1 = UberDriver("Rahul", "9876543210", "DLX12345", 4.9, "Hyundai i20") 
# 7. Display Details 
# o Calling a method like d1.show() should print: 
# o Name: Rahul, Contact: 9876543210 
# o License No: DLX12345, Rating: 4.9 
# Car: Hyundai i20 

class Person:
    def __init__(self,name,contact):
        self.name = name
        self.contact = contact
        
    def details(self):
        print(f"driver name is {self.name} and his contact is {self.contact}")
class Driver:
    def __init__(self,licence_no,rating):
        self.licence_no = licence_no
        self.rating = rating
    def licence_details(self):
        print(f"His licence number is {self.licence_no} and his rating is {self.rating}")
    
class uberDriver(Person,Driver):
    def __init__(self,car,name,contact,licence_no,rating):
        self.car = car
        self.name = name
        self.contact = contact
        self.licence_no = licence_no
        self.rating = rating
        Person.__init__(self,name,contact)
        Person.details(self)
        Driver.__init__(self,licence_no,rating)
        Driver.licence_details(self)
        print(self.car)
        
drive1 = uberDriver("Suzuki Ertiga","Rohith","9945672213","DLX13425",4.6)
    





# Multiple Inheritance in Blinkit  

# 1. Create Parent Class 1 → Person 
# o Attributes: name, contact. 
# o Example values: "Anil", "9876543210". 
# 2. Create Parent Class 2 → Employee 
# o Attributes: emp_id, salary. 
# o Example values: "BKP101", 12000. 
# 3. Create Child Class → DeliveryPartner (inherits from Person + Employee) 
# o Extra Attribute: vehicle. 
# o Example value: "Scooter". 
# 4. Constructor & Data Passing 
# o When creating a DeliveryPartner object, pass all attributes: 
# ▪ name, contact (from Person) 
# ▪ emp_id, salary (from Employee) 
# ▪ vehicle (from DeliveryPartner). 
# 5. Object Creation Example 
# 6. dp1 = DeliveryPartner("Anil", "9876543210", "BKP101", 12000, "Scooter") 
# 7. Display Details 
# o Calling dp1.show() should print: 
# o Name: Anil, Contact: 9876543210 
# o Employee ID: BKP101, Salary: 12000 
# Vehicle: Scooter

class Person:
    def __init__(self,name,contact):
        self.name = name
        self.contact = contact
        print(f"The rider name is {self.name} and his contact is {self.contact}")

class Employee:
    def __init__(self,emp_id,salary):
        self.emp_id = emp_id
        self.salary = salary
        print(f"His employee id is {self.emp_id} and his salary is {self.salary}")
    
class DeliveryPartner(Person,Employee):
    def __init__(self,name,contact,emp_id,salary,vehicle):
        self.vehicle = vehicle
        Person.__init__(self,name,contact)
        Employee.__init__(self,emp_id,salary)
        print(f"The rider is using {self.vehicle}")
    def show(self):
        print(f"Name : {self.name} , contact : {self.contact}")
        print(f"Employye ID : {self.emp_id} , Salary : {self.salary}")
        print(f"Vehicle : {self.vehicle}")

ride1 = DeliveryPartner("Rahul","9977552231","BLK101X",15000,"Scooty")


ride1.show()
