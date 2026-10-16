''' CLASS
    (1) What is class
    (2) ordinary vs static properties
    (3) special/magic methods
'''


print("===== What is class ====_")
# class - blueprint for object creation!
# structure > state constructor method


class Person():

    # state
    message = "class state property"

# constructor


def __init__(self, name, age):
    self.name = name
    self. age = age
# method


def introduce(self):
    print(f"{self. name} says: How do you do!")


def say_age(self):
    print(f"{self. name} says I am {self. age}!")


# bu yerda classsmethod static method deyiladi. bu asosiy clas.  nomi bilan chaqiriladi.
@classmethod
def explain(cls):
    print("static method property executed!")


person1 = Person("Justin", 25)
person2 = Person("Martin", 35)
person3 = Person("John", 22)

# ordinary state
print("person1. name:", person1. name)

# ordinary method
person1. introduce()
person2. say_age()


print("===== ordinary vs static properties =====")

#  bu yerda static state ni ishlatdik
new_message = Person.message
print("new_message:", new_message)

# static method ni ishlatdik
Person.explain()


print("==== special/magic methods=====")
# Python's most common special methods are below:
# _init_ _new _str_ _call_ _getitem_ _eq_ _len_ ...


class Car():
    # state
    description = "This class makes cars"
# constructor

    def __new__(cls, *args):
        print("*__new__*")
        return super().__new__(cls)

    def _init_(self, name, year):
        self. name = name
        self. year = year
# method

    def start_engine(self):
        print(f"the {self.name} started engine!")

    def stop_engine(self):
        print(f"the {self.name} stopped engine!")

    def __str__(self):
        return f"{self.name} was produced in {self.year} year!"

    def __call__(self):
        print("Object called as function!")
        return True


my_car = Car("Ferrari", 2025)
my_car.start_engine()
my_car.stop_engine()


print("-------")
your_car = Car("Toyota", 2026)
print(your_car)
#  bu yerda call methodi orqali objectni function usulida call qildik
your_car()

response = your_car()  # CALL
print("response:", response)
