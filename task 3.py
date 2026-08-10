class Address:
    def __init__(self, door_no, street, city, pincode):
        self.door_no = door_no
        self.street = street
        self.city = city
        self.pincode = pincode

class Customer:
    def __init__(self, customer_id, name, email, door_no, street, city, pincode):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.address = Address(door_no, street, city, pincode)

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

class Order:
    def __init__(self, order_id, customer, products):
        self.order_id = order_id
        self.customer = customer
        self.products = products

customer1 = Customer(
    1, "riya", "riya@gmail.com",
    101, "Anna Salai", "Chennai", 600002)
customer2 = Customer(
    2, "john", "john@gmail.com",
    202, "MG Road", "Coimbatore", 641001)
customer3 = Customer(
    3, "Priya", "priya@gmail.com",
    303, "Gandhi Road", "Madurai", 625001)

product1 = Product(101, "Laptop", 50000, 1)
product2 = Product(102, "Mouse", 800, 2)
product3 = Product(103, "Keyboard", 1500, 1)
products = [product1, product2, product3]
order1 = Order(1001, customer1, products)
order2 = Order(1002, customer2, products)
order3 = Order(1003, customer3, products)

print("Order 1")
print("Customer:", order1.customer.name)
print("City:", order1.customer.address.city)
for product in order1.products:
    print("Product:", product.name)

print("\nOrder 2")
print("Customer:", order2.customer.name)
print("City:", order2.customer.address.city)
for product in order2.products:
    print("Product:", product.name)

print("\nOrder 3")
print("Customer:", order3.customer.name)
print("City:", order3.customer.address.city)
for product in order3.products:
    print("Product:", product.name)