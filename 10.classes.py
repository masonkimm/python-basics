# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return (f'My name is {self.name} and I am {self.age}')

    def hasBirthday(self):
        self.age += 1

# Extend class


class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return (f'My name is {self.name} and I am {self.age} and my balance is {self.balance}')


# Init user object
brad = User('Brad Pitt', 'pitt@bull.com', 32)
print(brad.name)
print(brad.greeting())
brad.hasBirthday()  # age +1
print(brad.greeting())

# Init customer object
angelina = Customer('Angelina Jolie', 'jolie@agel.com', 32)
angelina.set_balance(500)
print(angelina.greeting())
