import sys; sys.path.insert(0, __file__.rsplit("/", 2)[0])   # so `schema` imports
from schema import P

OOP = "Object-Oriented Programming"
EXC = "Exceptions"
DS = "Data Structures"
DT = "Date and Time"
DB = "Database Connectivity"
DBT = "Python’s Database Connectivity"

PROGRAMS = [
# ---------------------------------------------------------------- OOP 1-26
P(title="Create a Class", category=OOP, difficulty="Beginner",
  description="Defines a simple Car class with attributes and a method.",
  concepts=["class", "self", "method"], filename="create_class.py",
  code=r'''
# A class is a blueprint that groups data (attributes) and behaviour (methods).
class Car:
    """A very small class describing a car."""

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def describe(self):
        return f"This car is a {self.brand} {self.model}."


# Using the class
print("Class name:", Car.__name__)
my_car = Car("Toyota", "Innova")
print(my_car.describe())
''',
  algorithm=["Use the class keyword and a name in CapWords style", "Add __init__ to store brand and model", "Add a describe() method that returns text", "Create an object and call describe()"],
  explanation="A class is written with the class keyword. Inside it, __init__ runs automatically when an object is made and stores the data on self. Methods are ordinary functions whose first parameter is self. The program defines Car, creates one object and prints its description.",
  tags=["class", "oop", "blueprint", "self"], topics=["Object Oriented Programming System (OOPS)", "Classes and Objects"]),

P(title="Create an Object", category=OOP, difficulty="Beginner",
  description="Creates several objects from one class and shows that each has its own data.",
  concepts=["object", "instance", "id()"], filename="create_object.py",
  code=r'''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")


# Each call to Dog(...) creates a new object (instance)
dog1 = Dog("Tommy", 3)
dog2 = Dog("Bruno", 5)

dog1.bark()
dog2.bark()
print("dog1 attributes:", dog1.__dict__)
print("dog2 attributes:", dog2.__dict__)
print("Same object?", dog1 is dog2)
print("Type of dog1:", type(dog1))
''',
  algorithm=["Define class Dog with __init__ and bark()", "Call Dog(...) twice to build two objects", "Call methods through each object", "Print __dict__ to show separate data"],
  explanation="Calling the class like a function creates an object (an instance). Every object keeps its own copy of the instance attributes, which you can see in __dict__. The 'is' operator proves the two objects are different. Methods are called with dot notation, e.g. dog1.bark().",
  tags=["object", "instance", "dict", "class"], topics=["Classes and Objects"]),

P(title="Demonstrate Constructors", category=OOP, difficulty="Beginner",
  description="Shows __init__ with required, default and keyword arguments, plus a destructor.",
  concepts=["__init__", "default arguments", "__del__"], filename="constructors.py",
  code=r'''
class Student:
    # Constructor: runs automatically when an object is created
    def __init__(self, name, course="MCA", semester=1):
        self.name = name
        self.course = course
        self.semester = semester
        print(f"Constructor called for {self.name}")

    # Destructor: runs when the object is destroyed
    def __del__(self):
        print(f"Destructor called for {self.name}")

    def show(self):
        print(f"{self.name} - {self.course} - Semester {self.semester}")


s1 = Student("Asha")                       # uses defaults
s2 = Student("Ravi", "MBA", 2)             # positional arguments
s3 = Student(name="Meena", semester=3)     # keyword arguments
for s in (s1, s2, s3):
    s.show()
del s1                                     # explicitly delete one object
print("End of program")
''',
  algorithm=["Define __init__ with default values for course and semester", "Create objects using defaults, positional and keyword arguments", "Show each object", "Delete an object to trigger __del__"],
  explanation="__init__ is the constructor; Python calls it right after creating an object. Python has only one constructor per class, so default values are used to allow different ways of calling it. __del__ is the destructor and is called when no reference to the object remains. The remaining objects are destroyed when the program ends.",
  tags=["constructor", "__init__", "__del__", "default"], topics=["Classes and Objects"]),

P(title="Demonstrate Instance Variables", category=OOP, difficulty="Beginner",
  description="Shows that instance variables belong to each object separately.",
  concepts=["instance variable", "self", "attribute"], filename="instance_variables.py",
  code=r'''
class Rectangle:
    def __init__(self, length, width):
        # Instance variables - created per object using self
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


r1 = Rectangle(5, 3)
r2 = Rectangle(10, 2)
print("r1:", r1.length, r1.width, "area =", r1.area())
print("r2:", r2.length, r2.width, "area =", r2.area())

# Changing one object does not affect the other
r1.length = 50
print("After change -> r1 area:", r1.area(), "| r2 area:", r2.area())

# Instance variables can also be added later
r2.color = "red"
print("r2 variables:", vars(r2))
print("r1 variables:", vars(r1))
''',
  algorithm=["Create instance variables inside __init__ using self", "Create two Rectangle objects", "Modify a variable of one object", "Display vars() of both objects"],
  explanation="Variables created with self.name inside methods are instance variables; every object gets its own copy. Changing r1.length does not affect r2. Python even lets you add a new attribute to a single object later, as done with r2.color. vars() shows the dictionary of attributes held by an object.",
  tags=["instance", "variable", "self", "attribute"], topics=["Classes and Objects"]),

P(title="Demonstrate Class Variables", category=OOP, difficulty="Beginner",
  description="Shows a class variable shared by all objects of a class.",
  concepts=["class variable", "shared data", "counter"], filename="class_variables.py",
  code=r'''
class Employee:
    company = "TechSoft Ltd"     # class variable (shared by all objects)
    count = 0                    # counts how many objects are created

    def __init__(self, name):
        self.name = name         # instance variable
        Employee.count += 1


e1 = Employee("Arun")
e2 = Employee("Divya")
print("Company seen by e1:", e1.company)
print("Company seen by e2:", e2.company)
print("Employees created:", Employee.count)

# Changing through the class affects every object
Employee.company = "NewTech Pvt Ltd"
print("After class change:", e1.company, "|", e2.company)

# Assigning through an object creates a new instance variable that hides the class one
e1.company = "Freelancer"
print("e1:", e1.company, "| e2:", e2.company, "| class:", Employee.company)
''',
  algorithm=["Declare variables directly inside the class body", "Increase the counter in __init__ using the class name", "Read the variable through objects", "Change it via the class and then via one object"],
  explanation="A variable declared in the class body (outside methods) is a class variable and is shared by all objects. Employee.count is incremented every time an object is created. Changing the value through the class changes it for everyone, but assigning through an object only creates a separate instance variable that hides the shared one.",
  tags=["class variable", "shared", "counter", "static data"], topics=["Classes and Objects"]),

P(title="Demonstrate Instance Methods", category=OOP, difficulty="Beginner",
  description="Defines instance methods that read and change the state of an object.",
  concepts=["instance method", "self", "state"], filename="instance_methods.py",
  code=r'''
class Counter:
    def __init__(self, start=0):
        self.value = start

    # Instance methods receive the object as the first argument (self)
    def increment(self, step=1):
        self.value += step

    def decrement(self, step=1):
        self.value -= step

    def show(self):
        print("Current value:", self.value)


c = Counter(10)
c.show()
c.increment()
c.increment(5)
c.show()
c.decrement(3)
c.show()

# c.show() is the same as Counter.show(c)
Counter.show(c)
''',
  algorithm=["Define a class with a value attribute", "Write increment, decrement and show methods using self", "Create an object and call the methods", "Call a method through the class to see self explicitly"],
  explanation="Instance methods work on one particular object, which Python passes automatically as self. They can read and modify the instance variables, so the object remembers changes between calls. The last line shows that obj.method() is just shorthand for Class.method(obj).",
  tags=["instance method", "self", "state"], topics=["Classes and Objects"]),

P(title="Demonstrate Class Methods", category=OOP, difficulty="Intermediate",
  description="Uses @classmethod as alternative constructor and to access class data.",
  concepts=["@classmethod", "cls", "alternative constructor"], filename="class_methods.py",
  code=r'''
class Person:
    species = "Homo sapiens"
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1

    # The first parameter is cls (the class), not self
    @classmethod
    def from_string(cls, text):
        """Alternative constructor: 'Name-Age' -> Person object"""
        name, age = text.split("-")
        return cls(name, int(age))

    @classmethod
    def get_population(cls):
        return cls.population


p1 = Person("Kiran", 21)
p2 = Person.from_string("Sneha-23")
print(p2.name, p2.age)
print("Population:", Person.get_population())
print("Called via object:", p1.get_population())
''',
  algorithm=["Decorate a method with @classmethod", "Receive the class as cls", "Use cls(...) to build objects in from_string", "Call the methods using the class name"],
  explanation="A class method is marked with @classmethod and receives the class itself (cls) instead of an object. It is used for work that concerns the whole class, such as reading class variables or creating objects in different ways (alternative constructors). Here from_string builds a Person from the text 'Sneha-23'.",
  tags=["classmethod", "cls", "decorator"], topics=["Classes and Objects"]),

P(title="Demonstrate Static Methods", category=OOP, difficulty="Intermediate",
  description="Uses @staticmethod for a utility function placed inside a class.",
  concepts=["@staticmethod", "utility function"], filename="static_methods.py",
  code=r'''
class MathUtils:
    # Static methods take neither self nor cls
    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def square(n):
        return n * n

    @staticmethod
    def celsius_to_fahrenheit(c):
        return c * 9 / 5 + 32


# No object is required
print("Is 10 even?", MathUtils.is_even(10))
print("Square of 7:", MathUtils.square(7))
print("37 C in F:", MathUtils.celsius_to_fahrenheit(37))

# They can also be called through an object
m = MathUtils()
print("Is 7 even?", m.is_even(7))
''',
  algorithm=["Decorate functions with @staticmethod", "Do not use self or cls", "Call them directly with the class name", "Optionally call through an object"],
  explanation="A static method is a normal function that lives inside a class for organisation only. It cannot see the object or the class automatically, so it only uses its own parameters. It is called using ClassName.method() and no object is needed.",
  tags=["staticmethod", "utility", "decorator"], topics=["Classes and Objects"]),

P(title="Demonstrate Encapsulation", category=OOP, difficulty="Intermediate",
  description="Hides data using private attributes and exposes it through getters, setters and a property.",
  concepts=["encapsulation", "private attribute", "@property"], filename="encapsulation.py",
  code=r'''
class Account:
    def __init__(self, owner, balance):
        self.owner = owner          # public
        self._bank = "SBI"          # protected (convention)
        self.__balance = balance    # private (name mangled)

    # Controlled access through methods
    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit must be positive")

    # Property gives attribute-like access with validation
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value


acc = Account("Latha", 5000)
acc.deposit(1500)
print("Balance:", acc.get_balance())
print("Property:", acc.balance)

try:
    print(acc.__balance)            # direct access fails
except AttributeError as err:
    print("Cannot access directly:", err)

print("Name-mangled name still exists:", acc._Account__balance)
try:
    acc.balance = -10
except ValueError as err:
    print("Setter rejected value:", err)
''',
  algorithm=["Store the balance in a private attribute (double underscore)", "Provide get_balance and deposit methods", "Add a property with a validating setter", "Try to access the private attribute directly and handle the error"],
  explanation="Encapsulation means bundling data with the methods that work on it and controlling access to it. A name starting with __ is private: Python renames it to _Class__name so it cannot be reached by accident. A single underscore is only a convention for protected. The @property decorator allows validation while still using simple attribute syntax. Python does not enforce privacy strictly; it relies on conventions.",
  tags=["encapsulation", "private", "property", "getter", "setter"], topics=["Encapsulation"]),

P(title="Demonstrate Abstraction", category=OOP, difficulty="Intermediate",
  description="Hides complex internal steps of a coffee machine behind a simple method.",
  concepts=["abstraction", "hiding details", "public interface"], filename="abstraction.py",
  code=r'''
class CoffeeMachine:
    """The user only calls make_coffee(); the details are hidden."""

    def make_coffee(self):
        self.__boil_water()
        self.__grind_beans()
        self.__brew()
        print("Your coffee is ready!")

    # Internal steps (implementation details)
    def __boil_water(self):
        print("  Boiling water...")

    def __grind_beans(self):
        print("  Grinding beans...")

    def __brew(self):
        print("  Brewing coffee...")


machine = CoffeeMachine()
print("Pressing the button:")
machine.make_coffee()
''',
  algorithm=["Create private helper methods for internal steps", "Create one public method that calls them in order", "The user calls only the public method"],
  explanation="Abstraction means showing only what is necessary and hiding how it is done. The user of CoffeeMachine just calls make_coffee(); boiling, grinding and brewing are hidden private methods. Later the internal steps can change without changing the code that uses the class. Formal abstract classes are shown in the abc programs.",
  tags=["abstraction", "hiding", "interface"], topics=["Abstraction"]),

P(title="Demonstrate Inheritance", category=OOP, difficulty="Beginner",
  description="A child class reuses and extends the members of a parent class.",
  concepts=["inheritance", "super()", "reuse"], filename="inheritance.py",
  code=r'''
class Animal:                      # parent / base / super class
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):                 # child / derived / sub class
    def __init__(self, name, breed):
        super().__init__(name)     # call the parent constructor
        self.breed = breed

    def bark(self):
        print(f"{self.name} the {self.breed} barks")


d = Dog("Tommy", "Labrador")
d.eat()      # inherited from Animal
d.bark()     # defined in Dog
print("Is Dog a subclass of Animal?", issubclass(Dog, Animal))
''',
  algorithm=["Define the parent class Animal", "Define Dog(Animal) giving the parent in brackets", "Call super().__init__ to initialise parent data", "Use inherited and new methods on a Dog object"],
  explanation="Inheritance lets a new class (child) take over the attributes and methods of an existing class (parent), which avoids repeating code. The parent is written in brackets after the child name. super() gives access to the parent so its constructor can be reused. The Dog object can call eat() even though it is only defined in Animal.",
  tags=["inheritance", "super", "parent", "child"], topics=["Inheritance"]),

P(title="Demonstrate Single Inheritance", category=OOP, difficulty="Beginner",
  description="One child class derived from exactly one parent class.",
  concepts=["single inheritance", "super()"], filename="single_inheritance.py",
  code=r'''
class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

    def info(self):
        print("Number of wheels:", self.wheels)


class Bike(Vehicle):               # exactly one parent
    def __init__(self):
        super().__init__(2)

    def ring_bell(self):
        print("Ting-ting!")


b = Bike()
b.info()
b.ring_bell()
print("Parent of Bike:", Bike.__bases__)
''',
  algorithm=["Create base class Vehicle", "Create Bike with only one parent", "Create a Bike object", "Use inherited info() and own ring_bell()"],
  explanation="In single inheritance a child class has exactly one parent. Bike gets the wheels attribute and info() method from Vehicle and adds ring_bell(). The __bases__ attribute lists the parent classes of a class.",
  tags=["single", "inheritance", "bases"], topics=["Inheritance"]),

P(title="Demonstrate Multilevel Inheritance", category=OOP, difficulty="Intermediate",
  description="A chain of classes: grandparent, parent and child.",
  concepts=["multilevel inheritance", "MRO"], filename="multilevel_inheritance.py",
  code=r'''
class Grandfather:
    def property_info(self):
        print("Grandfather owns land")


class Father(Grandfather):
    def business_info(self):
        print("Father runs a business")


class Son(Father):
    def study_info(self):
        print("Son is studying MCA")


s = Son()
s.property_info()    # from Grandfather
s.business_info()    # from Father
s.study_info()       # own method
print("Method Resolution Order:", [c.__name__ for c in Son.__mro__])
''',
  algorithm=["Define Grandfather", "Define Father inheriting Grandfather", "Define Son inheriting Father", "Call methods from all three levels through one Son object", "Print the MRO"],
  explanation="In multilevel inheritance a class is derived from a class that is itself derived from another. The Son object can use methods of Father and Grandfather. Python searches for a method in the order shown by __mro__ (Method Resolution Order): Son, Father, Grandfather, object.",
  tags=["multilevel", "inheritance", "mro"], topics=["Inheritance"]),

P(title="Demonstrate Multiple Inheritance", category=OOP, difficulty="Intermediate",
  description="A class inheriting from two parent classes, with MRO and the diamond case.",
  concepts=["multiple inheritance", "MRO", "super()"], filename="multiple_inheritance.py",
  code=r'''
class Father:
    def skills(self):
        print("Father: gardening")


class Mother:
    def skills(self):
        print("Mother: painting")

    def cooking(self):
        print("Mother: cooking")


class Child(Father, Mother):       # two parents
    def skills(self):
        super().skills()           # first in MRO -> Father
        Mother.skills(self)        # call the other explicitly
        print("Child: coding")


c = Child()
c.skills()
c.cooking()
print("MRO:", [cls.__name__ for cls in Child.__mro__])


# Diamond problem: Python resolves it with C3 linearisation
class A:
    def who(self): print("A")
class B(A):
    def who(self): print("B"); super().who()
class C(A):
    def who(self): print("C"); super().who()
class D(B, C):
    def who(self): print("D"); super().who()

D().who()
print("D MRO:", [cls.__name__ for cls in D.__mro__])
''',
  algorithm=["Define two parent classes with a same-named method", "Create Child(Father, Mother)", "Call both parent versions using super() and the class name", "Show the MRO", "Demonstrate the diamond shape with A, B, C and D"],
  explanation="Python allows a class to have several parents. When a method exists in more than one parent, the order of the parents decides which is found first, shown by __mro__. In the diamond example, super() follows the MRO D, B, C, A so every class runs exactly once.",
  tags=["multiple", "inheritance", "diamond", "mro"], topics=["Inheritance"]),

P(title="Demonstrate Hierarchical Inheritance", category=OOP, difficulty="Beginner",
  description="Several child classes derived from the same parent class.",
  concepts=["hierarchical inheritance", "shared parent"], filename="hierarchical_inheritance.py",
  code=r'''
class Shape:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Shape:", self.name)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def area(self):
        return self.side ** 2


for shape in (Circle(7), Square(4)):
    shape.display()
    print("Area:", round(shape.area(), 2))
print("Children of Shape:", [c.__name__ for c in Shape.__subclasses__()])
''',
  algorithm=["Create base class Shape", "Derive Circle and Square from Shape", "Each child adds its own data and area()", "Use both objects with the common display()"],
  explanation="In hierarchical inheritance one parent has more than one child. Circle and Square both reuse display() from Shape but have their own area() calculation. __subclasses__() lists the direct children of a class.",
  tags=["hierarchical", "inheritance", "subclasses"], topics=["Inheritance"]),

P(title="Demonstrate Polymorphism", category=OOP, difficulty="Beginner",
  description="Same method name gives different behaviour for different objects (duck typing).",
  concepts=["polymorphism", "duck typing", "common interface"], filename="polymorphism.py",
  code=r'''
class Cat:
    def speak(self):
        return "Meow"


class Dog:
    def speak(self):
        return "Woof"


class Duck:
    def speak(self):
        return "Quack"


# One function works with any object that has a speak() method
def make_it_speak(animal):
    print(f"{animal.__class__.__name__} says {animal.speak()}")


for pet in (Cat(), Dog(), Duck()):
    make_it_speak(pet)

# Built-in polymorphism: the same operator/function on different types
print(3 + 4, "|", "3" + "4", "|", [1] + [2])
print(len("hello"), len([1, 2, 3]), len({"a": 1}))
''',
  algorithm=["Create classes that all define speak()", "Write a function that just calls animal.speak()", "Pass different objects to it", "Show + and len() on built-in types"],
  explanation="Polymorphism means many forms: the same call behaves differently depending on the object. Python uses duck typing, so any object with a speak() method works, even if the classes are unrelated. Built-in operators such as + and functions such as len() are also polymorphic.",
  tags=["polymorphism", "duck typing", "speak"], topics=["Polymorphism"]),

P(title="Demonstrate Method Overriding", category=OOP, difficulty="Beginner",
  description="A child class replaces a method of its parent and can still call the parent version.",
  concepts=["method overriding", "super()"], filename="method_overriding.py",
  code=r'''
class Bank:
    def interest_rate(self):
        return 4.0

    def describe(self):
        print("General bank, interest:", self.interest_rate(), "%")


class SBI(Bank):
    def interest_rate(self):          # overrides the parent method
        return 6.5


class HDFC(Bank):
    def interest_rate(self):
        base = super().interest_rate()   # reuse the parent version
        return base + 3.0


for bank in (Bank(), SBI(), HDFC()):
    bank.describe()
''',
  algorithm=["Define interest_rate() in the parent", "Define a method with the same name in each child", "In HDFC call super().interest_rate() and add to it", "Call describe() on all three objects"],
  explanation="Overriding means a child class provides its own version of a method that the parent already has. Python picks the version belonging to the object's real class. super() lets the child reuse the parent's logic. Note that describe() written once in Bank automatically uses the overridden interest_rate().",
  tags=["overriding", "super", "polymorphism"], topics=["Polymorphism", "Inheritance"]),

P(title="Demonstrate Method Overloading Using Python Techniques", category=OOP, difficulty="Intermediate",
  description="Python has no Java-style overloading; this program simulates it with default arguments, *args and singledispatchmethod.",
  concepts=["default arguments", "*args", "singledispatch"], filename="method_overloading.py",
  code=r'''
from functools import singledispatchmethod

# NOTE: Python does NOT support Java-style method overloading.
# If you define two methods with the same name, the last one replaces the first.
# These are the Pythonic techniques instead.

class Calculator:
    # Technique 1: default arguments
    def add(self, a, b=0, c=0):
        return a + b + c

    # Technique 2: variable number of arguments
    def total(self, *numbers):
        return sum(numbers)

    # Technique 3: behaviour based on the argument type
    @singledispatchmethod
    def describe(self, value):
        return f"Something else: {value!r}"

    @describe.register
    def _(self, value: int):
        return f"Integer {value}"

    @describe.register
    def _(self, value: str):
        return f"String '{value}' of length {len(value)}"

    @describe.register
    def _(self, value: list):
        return f"List with {len(value)} items"


calc = Calculator()
print("add(5):", calc.add(5))
print("add(5, 6):", calc.add(5, 6))
print("add(5, 6, 7):", calc.add(5, 6, 7))
print("total(1, 2, 3, 4, 5):", calc.total(1, 2, 3, 4, 5))
print(calc.describe(42))
print(calc.describe("Python"))
print(calc.describe([1, 2, 3]))
print(calc.describe(3.5))
''',
  algorithm=["Explain that the last definition of a name wins in Python", "Use default arguments so add() accepts 1 to 3 values", "Use *numbers for any count of values", "Use singledispatchmethod to choose code by argument type", "Call each version and print the results"],
  explanation="Python does not allow several methods with the same name and different parameter lists as Java does. Instead, default arguments let one method be called with different numbers of values, *args accepts any number of values, and functools.singledispatchmethod selects an implementation based on the type of the first argument. The program calls each technique with different inputs.",
  tags=["overloading", "default args", "args", "singledispatch"], topics=["Polymorphism"]),

P(title="Demonstrate Abstract Classes", category=OOP, difficulty="Intermediate",
  description="Uses the abc module to create an abstract base class that cannot be instantiated.",
  concepts=["abc", "ABC", "instantiation error"], filename="abstract_classes.py",
  code=r'''
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract class: cannot be instantiated."""

    @abstractmethod
    def area(self):
        pass

    # Concrete method shared by all shapes
    def show(self):
        print(f"{self.__class__.__name__} area = {self.area():.2f}")


class Rectangle(Shape):
    def __init__(self, l, b):
        self.l, self.b = l, b

    def area(self):
        return self.l * self.b


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14159 * self.r ** 2


try:
    s = Shape()
except TypeError as err:
    print("Cannot create object:", err)

Rectangle(4, 5).show()
Circle(3).show()
''',
  algorithm=["Import ABC and abstractmethod from abc", "Make Shape inherit ABC with an abstract area()", "Add a normal method show() that uses area()", "Create concrete subclasses", "Show that Shape() raises TypeError"],
  explanation="An abstract class is a class that is meant to be inherited, not instantiated. In Python it is made by inheriting from abc.ABC and marking methods with @abstractmethod. Trying to create an object of Shape raises TypeError. Child classes become concrete by implementing all abstract methods, and can then use the shared show() method.",
  tags=["abc", "abstract class", "abstractmethod"], topics=["Abstract Classes and Interfaces", "Abstraction"]),

P(title="Demonstrate Abstract Methods", category=OOP, difficulty="Intermediate",
  description="Shows that a subclass must override every abstract method before objects can be created.",
  concepts=["abstractmethod", "abc", "contract"], filename="abstract_methods.py",
  code=r'''
from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        """Every payment type must implement pay()."""

    @abstractmethod
    def refund(self, amount):
        """Every payment type must implement refund()."""


class UPI(Payment):
    def pay(self, amount):
        print(f"Paid Rs.{amount} using UPI")

    def refund(self, amount):
        print(f"Refunded Rs.{amount} to UPI")


class Cash(Payment):
    def pay(self, amount):          # refund() is missing!
        print(f"Paid Rs.{amount} in cash")


print("Abstract methods of Payment:", sorted(Payment.__abstractmethods__))

upi = UPI()
upi.pay(500)
upi.refund(200)

try:
    cash = Cash()
except TypeError as err:
    print("Error:", err)
''',
  algorithm=["Declare pay() and refund() as abstract methods", "Implement both in UPI and create an object", "Implement only pay() in Cash", "Creating Cash() raises TypeError because refund() is missing"],
  explanation="An abstract method has a name and a signature but no real body; it forces subclasses to supply the implementation. A subclass that leaves any abstract method unimplemented is itself abstract, so Python refuses to create its objects. This works like a contract between the base class and its children.",
  tags=["abstract method", "abc", "contract"], topics=["Abstract Classes and Interfaces"]),

P(title="Demonstrate Interfaces Using Python Techniques", category=OOP, difficulty="Intermediate",
  description="Python has no interface keyword; shows an ABC-based interface and a typing.Protocol.",
  concepts=["interface", "ABC", "Protocol"], filename="interfaces.py",
  code=r'''
from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable

# Python has no 'interface' keyword. Two common techniques:

# 1) An abstract class that contains ONLY abstract methods
class Flyable(ABC):
    @abstractmethod
    def fly(self): ...

    @abstractmethod
    def land(self): ...


class Swimmable(ABC):
    @abstractmethod
    def swim(self): ...


# A class can "implement" many interfaces through multiple inheritance
class Duck(Flyable, Swimmable):
    def fly(self):
        print("Duck flies")

    def land(self):
        print("Duck lands")

    def swim(self):
        print("Duck swims")


d = Duck()
d.fly(); d.land(); d.swim()
print("Duck is Flyable?", isinstance(d, Flyable))


# 2) Protocol: structural typing (no inheritance needed)
@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> None: ...


class Circle:                      # does not inherit Drawable
    def draw(self):
        print("Drawing a circle")


class Table:
    pass


for obj in (Circle(), Table()):
    print(type(obj).__name__, "is Drawable?", isinstance(obj, Drawable))
Circle().draw()
''',
  algorithm=["Create abstract classes with only abstract methods as interfaces", "Implement two interfaces in one class", "Define a Protocol with a draw() method", "Check objects with isinstance against the interface and the protocol"],
  explanation="Languages such as Java have an interface keyword, but Python does not. The usual approach is an abstract class containing only abstract methods; a class implements several interfaces by inheriting from them. Protocol (from typing) describes an interface by structure, so any class having draw() counts as Drawable without inheriting anything.",
  tags=["interface", "protocol", "abc", "typing"], topics=["Abstract Classes and Interfaces"]),

P(title="Demonstrate isinstance()", category=OOP, difficulty="Beginner",
  description="Checks the type of values and objects with isinstance() and issubclass().",
  concepts=["isinstance", "issubclass", "type checking"], filename="isinstance_demo.py",
  code=r'''
class Animal:
    pass


class Dog(Animal):
    pass


a = Animal()
d = Dog()

print("isinstance(d, Dog):", isinstance(d, Dog))
print("isinstance(d, Animal):", isinstance(d, Animal))   # True for parent too
print("isinstance(a, Dog):", isinstance(a, Dog))
print("type(d) == Animal:", type(d) == Animal)           # type() ignores inheritance

# Checking built-in types, also with a tuple of types
for value in (10, 3.5, "hello", [1, 2], True):
    print(repr(value), "is number?", isinstance(value, (int, float)))

print("issubclass(Dog, Animal):", issubclass(Dog, Animal))
print("bool is a subclass of int:", issubclass(bool, int))
''',
  algorithm=["Create a parent and a child class", "Test objects with isinstance against child and parent", "Compare with type()", "Test built-in values against a tuple of types", "Use issubclass() for classes"],
  explanation="isinstance(obj, cls) returns True if obj belongs to cls or to any class derived from it, which makes it better than type() for checking. A tuple of classes can be given to test several types at once. Note that True is also an int because bool is a subclass of int. issubclass() does the same check between two classes.",
  tags=["isinstance", "issubclass", "type"], topics=["Classes and Objects", "Inheritance"]),

P(title="Create a Student Class", category=OOP, difficulty="Beginner",
  description="A Student class that stores marks, computes the average and assigns a grade.",
  concepts=["class", "methods", "__str__"], filename="student_class.py",
  code=r'''
class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.marks = {}

    def add_marks(self, subject, mark):
        if 0 <= mark <= 100:
            self.marks[subject] = mark
        else:
            print("Invalid mark for", subject)

    def average(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 75:
            return "Distinction"
        elif avg >= 60:
            return "First Class"
        elif avg >= 40:
            return "Pass"
        return "Fail"

    def __str__(self):
        return f"[{self.roll_no}] {self.name} - Avg: {self.average():.2f} - {self.grade()}"


s1 = Student(101, "Anita")
s1.add_marks("Python", 88)
s1.add_marks("Maths", 76)
s1.add_marks("DBMS", 91)
s1.add_marks("Networks", 120)    # rejected
print(s1)
print("Marks:", s1.marks)

s2 = Student(102, "Bala")
s2.add_marks("Python", 35)
s2.add_marks("Maths", 42)
print(s2)
''',
  algorithm=["Store roll number, name and an empty marks dictionary", "add_marks validates the range 0-100", "average() computes the mean of the marks", "grade() decides the class from the average", "__str__ gives a readable line"],
  explanation="The Student class keeps the details of one student and the marks of each subject in a dictionary. Methods validate marks, calculate the average and return a grade. The special method __str__ controls what print() shows for the object. Two student objects are created to show different results.",
  tags=["student", "class", "marks", "grade"], topics=["Classes and Objects"]),

P(title="Create a Bank Account Class", category=OOP, difficulty="Intermediate",
  description="A BankAccount class with deposit, withdraw, balance checks and a transaction history.",
  concepts=["encapsulation", "custom exception", "history list"], filename="bank_account_class.py",
  code=r'''
class InsufficientFunds(Exception):
    pass


class BankAccount:
    def __init__(self, acc_no, holder, balance=0):
        self.acc_no = acc_no
        self.holder = holder
        self.__balance = balance
        self.history = []

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        self.history.append(("Deposit", amount))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise InsufficientFunds(f"Balance {self.__balance} is less than {amount}")
        self.__balance -= amount
        self.history.append(("Withdraw", amount))

    def statement(self):
        print(f"Statement for {self.holder} (A/C {self.acc_no})")
        for kind, amount in self.history:
            print(f"  {kind:<9} {amount:>8.2f}")
        print(f"  Closing balance: {self.__balance:.2f}")


acct = BankAccount(1001, "Meera", 1000)
acct.deposit(2500)
acct.withdraw(700)
for action, amt in (("withdraw", 10000), ("deposit", -5)):
    try:
        getattr(acct, action)(amt)
    except (InsufficientFunds, ValueError) as err:
        print("Transaction failed:", err)
acct.statement()
''',
  algorithm=["Keep the balance private and expose it via a property", "deposit() and withdraw() validate the amount", "Raise InsufficientFunds when balance is too low", "Record every successful transaction in a list", "Print a statement"],
  explanation="BankAccount protects its balance by making it private and changing it only through deposit() and withdraw(). Wrong amounts raise exceptions, which the calling code catches with try/except. Each successful operation is added to a history list used by statement().",
  tags=["bank", "account", "deposit", "withdraw"], topics=["Classes and Objects", "Encapsulation"]),

P(title="Create an Employee Management Class", category=OOP, difficulty="Intermediate",
  description="Employee base class, a Manager subclass and a Company class that manages them.",
  concepts=["inheritance", "composition", "list of objects"], filename="employee_management_class.py",
  code=r'''
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def __str__(self):
        return f"{self.emp_id:<4}{self.name:<10}{'Employee':<10}{self.salary:>9.2f}"


class Manager(Employee):
    def __init__(self, emp_id, name, salary, bonus):
        super().__init__(emp_id, name, salary)
        self.bonus = bonus

    def annual_salary(self):                 # overridden
        return super().annual_salary() + self.bonus

    def __str__(self):
        return f"{self.emp_id:<4}{self.name:<10}{'Manager':<10}{self.salary:>9.2f}"


class Company:
    def __init__(self):
        self.employees = []

    def hire(self, employee):
        self.employees.append(employee)

    def fire(self, emp_id):
        before = len(self.employees)
        self.employees = [e for e in self.employees if e.emp_id != emp_id]
        return len(self.employees) < before

    def give_raise(self, emp_id, percent):
        for e in self.employees:
            if e.emp_id == emp_id:
                e.salary += e.salary * percent / 100

    def report(self):
        print(f"{'ID':<4}{'Name':<10}{'Role':<10}{'Salary':>9}")
        for e in self.employees:
            print(e)
        total = sum(e.annual_salary() for e in self.employees)
        print("Total yearly payroll:", total)


company = Company()
company.hire(Employee(1, "Ravi", 30000))
company.hire(Employee(2, "Sita", 35000))
company.hire(Manager(3, "Kumar", 60000, 50000))
company.give_raise(1, 10)
company.report()
print("Removing ID 2:", company.fire(2))
print("Removing ID 9:", company.fire(9))
company.report()
''',
  algorithm=["Create Employee with salary and annual_salary()", "Derive Manager with a bonus and override annual_salary()", "Company stores a list of employee objects", "Add methods hire, fire and give_raise", "Print a payroll report before and after changes"],
  explanation="This small management system uses inheritance (Manager is an Employee) and composition (a Company has employees). Because annual_salary() is overridden, the payroll total works for both kinds of employees without checking the type. Hiring, firing and raising salaries are methods of Company that operate on its list of objects.",
  tags=["employee", "management", "company", "payroll"], topics=["Classes and Objects", "Inheritance", "Polymorphism"], kind="Application"),

P(title="Create a Library Management Class", category=OOP, difficulty="Advanced",
  description="Library, Book and Member classes supporting add, issue, return and search.",
  concepts=["classes", "dictionary", "composition"], filename="library_management_class.py",
  code=r'''
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"{self.book_id:<4}{self.title:<26}{self.author:<18}{status}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}          # book_id -> Book
        self.issued = {}         # book_id -> member name

    def add_book(self, book):
        self.books[book.book_id] = book

    def issue_book(self, book_id, member):
        book = self.books.get(book_id)
        if book is None:
            return "Book not found"
        if book.is_issued:
            return f"'{book.title}' is already issued to {self.issued[book_id]}"
        book.is_issued = True
        self.issued[book_id] = member
        return f"'{book.title}' issued to {member}"

    def return_book(self, book_id):
        if book_id not in self.issued:
            return "This book was not issued"
        member = self.issued.pop(book_id)
        self.books[book_id].is_issued = False
        return f"'{self.books[book_id].title}' returned by {member}"

    def search(self, keyword):
        keyword = keyword.lower()
        return [b for b in self.books.values()
                if keyword in b.title.lower() or keyword in b.author.lower()]

    def show_all(self):
        print(f"--- {self.name} ---")
        for book in self.books.values():
            print(book)


lib = Library("City Central Library")
lib.add_book(Book(1, "Python Crash Course", "Eric Matthes"))
lib.add_book(Book(2, "Learning Python", "Mark Lutz"))
lib.add_book(Book(3, "Data Structures in C", "Reema Thareja"))
lib.show_all()
print(lib.issue_book(2, "Anil"))
print(lib.issue_book(2, "Beena"))
print(lib.issue_book(9, "Beena"))
lib.show_all()
print(lib.return_book(2))
print(lib.return_book(2))
print("Search 'python':", [b.title for b in lib.search("python")])
''',
  algorithm=["Book stores id, title, author and issue status", "Library keeps dictionaries of books and issued records", "issue_book() checks existence and availability", "return_book() clears the issue record", "search() matches title or author", "Run a sample scenario"],
  explanation="Book objects are kept in a dictionary inside the Library for fast lookup by id. issue_book() and return_book() check every rule (missing book, already issued, not issued) and return a message. search() uses a list comprehension for case-insensitive matching. The final part simulates issuing, returning and searching.",
  tags=["library", "management", "books", "issue"], topics=["Classes and Objects", "Encapsulation"], kind="Application"),

# ---------------------------------------------------------------- Exceptions 27-39
P(title="Demonstrate try-except", category=EXC, difficulty="Beginner",
  description="Catches a runtime error so the program continues instead of crashing.",
  concepts=["try", "except", "error handling"], filename="try_except.py",
  code=r'''
# Without try-except, an error stops the program.
# With try-except, we handle it and continue.
numbers = [10, 5, 0, 2]

for n in numbers:
    try:
        result = 100 / n
        print(f"100 / {n} = {result}")
    except ZeroDivisionError:
        print(f"Cannot divide 100 by {n}")

print("Program continues after the error")
''',
  algorithm=["Put risky code inside try", "Write the expected error type after except", "If an error occurs, the except block runs and the loop continues", "Print a final message to show the program did not crash"],
  explanation="Code that might fail is placed in the try block. If an exception of the named type occurs, Python jumps to the matching except block instead of stopping. Here dividing by 0 raises ZeroDivisionError, which is handled, and the loop moves on to the next number.",
  tags=["try", "except", "exception"], topics=["Exceptions"]),

P(title="Demonstrate Multiple Exceptions", category=EXC, difficulty="Beginner",
  description="Handles different exception types with separate except blocks and a combined tuple.",
  concepts=["multiple except", "tuple of exceptions", "as err"], filename="multiple_exceptions.py",
  code=r'''
def risky(index, divisor):
    data = [10, 20, 30]
    return data[index] / divisor


tests = [(1, 2), (5, 1), (0, 0), ("a", 1), (2, 3)]

for index, divisor in tests:
    try:
        print(f"risky({index!r}, {divisor}) =", round(risky(index, divisor), 2))
    except IndexError:
        print(f"risky({index!r}, {divisor}) -> IndexError: index out of range")
    except ZeroDivisionError:
        print(f"risky({index!r}, {divisor}) -> ZeroDivisionError")
    except (TypeError, ValueError) as err:         # several types in one block
        print(f"risky({index!r}, {divisor}) -> {type(err).__name__}: {err}")

# Catch-all (use only as the last block)
try:
    int("abc")
except Exception as err:
    print("Generic handler caught:", repr(err))
''',
  algorithm=["Write one try block", "Add an except for each expected error type", "Use a tuple to share one handler", "Put a generic Exception handler last"],
  explanation="A try block may be followed by many except blocks; Python runs the first one that matches the error. Several types can share a handler by writing them in a tuple. 'as err' gives access to the error object. The broad Exception handler should always be the last one.",
  tags=["multiple", "except", "exceptions"], topics=["Exceptions"]),

P(title="Demonstrate finally", category=EXC, difficulty="Beginner",
  description="Shows that the finally block always runs, even after errors or return.",
  concepts=["finally", "cleanup"], filename="finally_demo.py",
  code=r'''
def divide(a, b):
    try:
        print(f"Dividing {a} by {b}")
        return a / b
    except ZeroDivisionError:
        print("Error: division by zero")
        return None
    finally:
        # always executed - good for cleanup such as closing files
        print("finally block executed\n")


print("Result:", divide(10, 2))
print("Result:", divide(10, 0))

# finally with a file: ensure it is closed
f = open("temp_demo.txt", "w")
try:
    f.write("Hello")
    print("Written to file")
finally:
    f.close()
    print("File closed:", f.closed)

import os
os.remove("temp_demo.txt")
''',
  algorithm=["Write try/except/finally in a function", "Call it with valid and invalid values", "Observe that finally runs in both cases, even with return", "Use finally to close a file"],
  explanation="The finally block runs whether or not an exception happened, and even when the try block uses return. That makes it ideal for cleanup such as closing files or connections. The output shows 'finally block executed' for both calls of divide().",
  tags=["finally", "cleanup", "try"], topics=["Exceptions"]),

P(title="Demonstrate else with try-except", category=EXC, difficulty="Beginner",
  description="Uses the else block, which runs only when no exception occurs.",
  concepts=["try-else", "input validation"], filename="try_except_else.py",
  code=r'''
for text in ["25", "abc", "7"]:
    try:
        number = int(text)
    except ValueError:
        print(f"'{text}' is not a valid integer")
    else:
        # runs only if the try block succeeded
        print(f"'{text}' converted successfully; its square is {number ** 2}")
    finally:
        print("-- done with", repr(text))
''',
  algorithm=["Place the risky conversion in try", "Handle the failure in except", "Place the follow-up code in else", "Optionally add finally"],
  explanation="The else block is executed only when the try block finishes without any exception. It keeps the code that depends on success separate from the risky statement, so errors in it are not caught by mistake. The order is try, except, else, finally.",
  tags=["else", "try", "except"], topics=["Exceptions"]),

P(title="Handle ZeroDivisionError", category=EXC, difficulty="Beginner",
  description="Reads two numbers and divides them, handling division by zero.",
  concepts=["ZeroDivisionError", "input", "float"], filename="handle_zero_division.py",
  code=r'''
try:
    a = float(input("Enter numerator: "))
    b = float(input("Enter denominator: "))
    print("Result =", a / b)
except ZeroDivisionError:
    print("Error: denominator cannot be zero")
except ValueError:
    print("Error: please enter numbers only")

# Other operations also raise it
for expression in ("10 // 0", "10 % 0", "0 ** -1"):
    try:
        eval(expression)
    except ZeroDivisionError as err:
        print(f"{expression:<8} -> {err}")
''',
  algorithm=["Read two numbers", "Divide inside try", "Catch ZeroDivisionError and print a friendly message", "Show that //, % and negative powers of 0 raise it too"],
  explanation="Dividing by zero raises ZeroDivisionError. The program reads two numbers, tries the division and prints an error message when the denominator is 0. The sample input uses 0 as denominator so the handler runs; the loop shows other operations that raise the same error.",
  sample_input="10\n0", kind="Interactive", tags=["zerodivisionerror", "divide"], topics=["Exceptions"]),

P(title="Handle ValueError", category=EXC, difficulty="Beginner",
  description="Keeps asking for an integer until a valid value is typed.",
  concepts=["ValueError", "while loop", "int()"], filename="handle_value_error.py",
  code=r'''
while True:
    text = input("Enter your age: ")
    try:
        age = int(text)
        if age < 0:
            raise ValueError("age cannot be negative")
    except ValueError as err:
        print("Invalid input:", err)
    else:
        print("Your age is", age)
        break
''',
  algorithm=["Loop until valid input is received", "Convert text with int() inside try", "Raise ValueError for a negative age", "Print the error and ask again; break on success"],
  explanation="int('abc') raises ValueError because the text is not a number. The loop catches it and asks again until a good value arrives. We also raise ValueError ourselves for negative ages. The sample input tries 'abc', -5 and finally 21.",
  sample_input="abc\n-5\n21", kind="Interactive", tags=["valueerror", "int", "validation"], topics=["Exceptions"]),

P(title="Handle TypeError", category=EXC, difficulty="Beginner",
  description="Shows common causes of TypeError and how to handle them.",
  concepts=["TypeError", "type conversion"], filename="handle_type_error.py",
  code=r'''
# 1) Mixing incompatible types
try:
    print("Age: " + 25)
except TypeError as err:
    print("TypeError 1:", err)
    print("Fixed:", "Age: " + str(25))

# 2) Calling something that is not callable
try:
    x = 10
    x()
except TypeError as err:
    print("TypeError 2:", err)

# 3) Wrong number of arguments
def add(a, b):
    return a + b

try:
    add(1)
except TypeError as err:
    print("TypeError 3:", err)

# 4) Unsupported operand types
for a, b in [(5, 3), (5, "3"), ([1], (2,))]:
    try:
        print(a, "+", b, "=", a + b)
    except TypeError as err:
        print("TypeError 4:", err)
''',
  algorithm=["Try an operation that mixes str and int", "Convert with str() to fix it", "Try calling an int and calling a function with a missing argument", "Loop over several operand pairs and catch the failures"],
  explanation="TypeError is raised when an operation is applied to a value of the wrong type, such as adding a string to an integer or calling a function with the wrong number of arguments. The message printed by Python explains what went wrong. The usual fix is to convert the type or correct the call.",
  tags=["typeerror", "types", "exception"], topics=["Exceptions"]),

P(title="Handle IndexError", category=EXC, difficulty="Beginner",
  description="Handles access to a list position that does not exist.",
  concepts=["IndexError", "list index", "len()"], filename="handle_index_error.py",
  code=r'''
fruits = ["apple", "banana", "cherry"]

for position in (0, 2, 3, -1, -4):
    try:
        print(f"fruits[{position}] = {fruits[position]}")
    except IndexError as err:
        print(f"fruits[{position}] -> IndexError: {err}")

# Prevent the error by checking the length first
position = 5
if 0 <= position < len(fruits):
    print(fruits[position])
else:
    print(f"Valid positions are 0 to {len(fruits) - 1}")

# Popping from an empty list also raises IndexError
try:
    [].pop()
except IndexError as err:
    print("pop():", err)
''',
  algorithm=["Create a list of 3 items", "Access valid and invalid positions inside try", "Catch IndexError", "Show prevention by checking len()", "Show pop() on an empty list"],
  explanation="A list with 3 items has valid indexes 0 to 2 (or -1 to -3). Asking for any other position raises IndexError. The program catches the error, and also shows how checking the length beforehand avoids it. Popping from an empty list raises the same error.",
  tags=["indexerror", "list", "range"], topics=["Exceptions"]),

P(title="Handle KeyError", category=EXC, difficulty="Beginner",
  description="Handles a missing dictionary key and shows the safer get() method.",
  concepts=["KeyError", "dict.get", "in operator"], filename="handle_key_error.py",
  code=r'''
student = {"name": "Priya", "course": "MCA", "year": 1}

for key in ("name", "email"):
    try:
        print(f"{key}: {student[key]}")
    except KeyError as err:
        print("KeyError - missing key:", err)

# Safer alternatives
print("get() with default:", student.get("email", "not provided"))
if "year" in student:
    print("year is present:", student["year"])

# setdefault adds the key if it is missing
student.setdefault("email", "priya@example.com")
print(student)
''',
  algorithm=["Create a dictionary", "Access existing and missing keys in try", "Catch KeyError", "Use get() with a default", "Use the in operator and setdefault()"],
  explanation="Reading a key that is not in a dictionary with square brackets raises KeyError. You can catch the error, or avoid it by using get() which returns a default value, or by testing 'key in dict' first. setdefault() inserts a value when the key is missing.",
  tags=["keyerror", "dictionary", "get"], topics=["Exceptions"]),

P(title="Handle FileNotFoundError", category=EXC, difficulty="Beginner",
  description="Tries to open a file that does not exist and handles the error.",
  concepts=["FileNotFoundError", "open()", "os.path.exists"], filename="handle_file_not_found.py",
  code=r'''
import os

filename = "missing_file.txt"

try:
    with open(filename) as f:
        print(f.read())
except FileNotFoundError:
    print(f"The file '{filename}' was not found.")
except PermissionError:
    print("You do not have permission to read this file.")

# Check first with os.path
print("Exists?", os.path.exists(filename))

# Create the file when it is missing, then read it again
if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("File created by the program.\n")

with open(filename) as f:
    print("Now reading:", f.read().strip())

os.remove(filename)       # clean up
''',
  algorithm=["Open a non-existing file inside try", "Catch FileNotFoundError and print a message", "Check existence using os.path.exists", "Create the file and read it", "Delete the file at the end"],
  explanation="open() in read mode raises FileNotFoundError when the file is missing. The program catches it and prints a friendly message instead of crashing. It then creates the file, reads it successfully and removes it so nothing is left behind.",
  tags=["filenotfounderror", "file", "open"], topics=["Exceptions"]),

P(title="Demonstrate raise", category=EXC, difficulty="Beginner",
  description="Raises built-in exceptions on purpose, re-raises and chains exceptions.",
  concepts=["raise", "re-raise", "raise from"], filename="raise_demo.py",
  code=r'''
def set_percentage(value):
    if not isinstance(value, (int, float)):
        raise TypeError("percentage must be a number")
    if not 0 <= value <= 100:
        raise ValueError(f"percentage must be 0-100, got {value}")
    return value


for v in (85, 120, "high"):
    try:
        print("Accepted:", set_percentage(v))
    except (TypeError, ValueError) as err:
        print(f"Rejected {v!r}: {type(err).__name__} - {err}")


# Re-raising: log and pass the error upward
def process():
    try:
        return 1 / 0
    except ZeroDivisionError:
        print("process(): logging the error and re-raising")
        raise


try:
    process()
except ZeroDivisionError as err:
    print("Caught outside:", err)


# Exception chaining with 'from'
try:
    try:
        int("x1")
    except ValueError as original:
        raise RuntimeError("Could not read configuration") from original
except RuntimeError as err:
    print(err, "| caused by:", repr(err.__cause__))
''',
  algorithm=["Write a function that validates and raises with raise", "Catch the raised errors in the caller", "Use bare raise inside except to re-raise", "Use raise ... from ... to chain a cause"],
  explanation="The raise statement creates an exception deliberately, which is how functions report invalid input. A bare raise inside an except block passes the same error to the caller after doing something such as logging. 'raise X from Y' links a new error to the original cause, which helps with debugging.",
  tags=["raise", "exception", "validation"], topics=["Exceptions"]),

P(title="Create a User-Defined Exception", category=EXC, difficulty="Intermediate",
  description="Defines custom exception classes for an ATM withdrawal scenario.",
  concepts=["custom exception", "Exception class", "inheritance"], filename="user_defined_exception.py",
  code=r'''
class BankError(Exception):
    """Base class for all bank related errors."""


class InsufficientBalanceError(BankError):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw {amount}; available balance is {balance}")


class InvalidAmountError(BankError):
    pass


def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountError("Amount must be greater than zero")
    if amount > balance:
        raise InsufficientBalanceError(balance, amount)
    return balance - amount


balance = 5000
for amount in (1500, -20, 9000):
    try:
        balance = withdraw(balance, amount)
        print(f"Withdrew {amount}. New balance: {balance}")
    except InsufficientBalanceError as err:
        print("Insufficient:", err, "| short by", err.amount - err.balance)
    except BankError as err:              # catches InvalidAmountError
        print("Bank error:", err)
''',
  algorithm=["Create BankError by inheriting Exception", "Derive specific errors from BankError", "Store extra data inside the exception object", "Raise them in withdraw()", "Catch specific and general errors in order"],
  explanation="A user-defined exception is simply a class that inherits from Exception. Making a base class (BankError) lets callers catch all related errors together or each one separately. The exception object can carry extra information, such as the balance and amount, for the handler to use.",
  tags=["custom exception", "user-defined", "class"], topics=["Exceptions", "Inheritance"]),

P(title="Input Validation Using Exceptions", category=EXC, difficulty="Intermediate",
  description="Reads name, age and email with validation rules enforced through exceptions.",
  concepts=["validation", "raise", "loop until valid"], filename="input_validation_exceptions.py",
  code=r'''
def read_name(text):
    text = text.strip()
    if not text.replace(" ", "").isalpha():
        raise ValueError("name must contain only letters")
    return text.title()


def read_age(text):
    age = int(text)                       # may raise ValueError
    if not 1 <= age <= 120:
        raise ValueError("age must be between 1 and 120")
    return age


def read_email(text):
    text = text.strip()
    if "@" not in text or "." not in text.split("@")[-1]:
        raise ValueError("email must look like name@domain.com")
    return text.lower()


def ask(prompt, converter):
    """Keep asking until the converter accepts the input."""
    while True:
        try:
            return converter(input(prompt))
        except ValueError as err:
            print("  Invalid:", err)


name = ask("Name  : ", read_name)
age = ask("Age   : ", read_age)
email = ask("Email : ", read_email)
print(f"\nRegistered: {name}, {age} years, {email}")
''',
  algorithm=["Write one validator function per field that raises ValueError", "Write ask() which loops until the validator succeeds", "Read name, age and email using ask()", "Print the cleaned values"],
  explanation="Each validator returns a cleaned value or raises ValueError with a helpful message. The generic ask() function repeats the question until no exception occurs, so the main program stays short. The sample input contains several bad answers before the good ones, showing the retry messages.",
  sample_input="R2D2\nravi kumar\nabc\n150\n22\nravi.com\nRavi@Example.com", kind="Interactive",
  tags=["validation", "input", "exceptions", "loop"], topics=["Exceptions"]),

# ---------------------------------------------------------------- DATA STRUCTURES 40-52
P(title="Implement a Linked List", category=DS, difficulty="Intermediate",
  description="Builds a singly linked list from Node and LinkedList classes.",
  concepts=["Node class", "references", "append"], filename="linked_list_implementation.py",
  code=r'''
class Node:
    """One element of the list: a value and a link to the next node."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:   # walk to the last node
            current = current.next
        current.next = new_node

    def to_list(self):
        items, current = [], self.head
        while current is not None:
            items.append(current.data)
            current = current.next
        return items


numbers = LinkedList()
for value in (10, 20, 30, 40):
    numbers.append(value)
print("Linked list :", " -> ".join(map(str, numbers.to_list())) + " -> None")
print("Head value  :", numbers.head.data)
''',
  algorithm=["Create a Node class holding data and a next reference", "Create a LinkedList class with a head pointer", "append(): if empty make the new node the head, else walk to the last node", "Link the last node to the new node", "Print values by following the next links"],
  explanation="A linked list stores items in separate Node objects, each pointing to the next one. The LinkedList object only remembers the head. To append, we walk along the next links until we reach the node whose next is None and attach the new node there. Unlike a Python list, items are not stored side by side in memory.",
  tags=["linked list", "node", "data structure"], topics=["Linked list"]),

P(title="Insert a Node into a Linked List", category=DS, difficulty="Intermediate",
  description="Inserts nodes at the beginning, at the end and at a given position.",
  concepts=["insert at head", "insert at position", "pointer update"], filename="linked_list_insert.py",
  code=r'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def insert_at_position(self, position, data):
        if position == 0:
            self.insert_at_beginning(data)
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                break
            current = current.next
        if current is None:
            raise IndexError("position out of range")
        node = Node(data)
        node.next = current.next
        current.next = node

    def show(self):
        items, current = [], self.head
        while current:
            items.append(str(current.data))
            current = current.next
        print(" -> ".join(items) if items else "(empty)")


ll = LinkedList()
ll.insert_at_end(20)
ll.insert_at_end(40)
ll.show()
ll.insert_at_beginning(10)
ll.show()
ll.insert_at_position(2, 30)
ll.show()
try:
    ll.insert_at_position(10, 99)
except IndexError as err:
    print("Error:", err)
''',
  algorithm=["Insert at beginning: new node points to old head, head becomes new node", "Insert at end: walk to last node and link the new node", "Insert at position: stop at the node before the position", "Point new node to the next node, then point the previous node to the new node", "Raise IndexError if the position is beyond the list"],
  explanation="Insertion only needs pointer changes, no shifting of elements. At the head we make the new node point to the old head. In the middle we find the previous node, set new.next to previous.next and then previous.next to the new node; the order matters or the rest of the list would be lost. A position beyond the end raises IndexError.",
  tags=["linked list", "insert", "node"], topics=["Linked list"]),

P(title="Delete a Node from a Linked List", category=DS, difficulty="Intermediate",
  description="Deletes a node by value, handling head, middle and missing values.",
  concepts=["delete node", "head handling", "pointer bypass"], filename="linked_list_delete.py",
  code=r'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, values=()):
        self.head = None
        for value in values:
            self.append(value)

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def delete(self, value):
        """Delete the first node holding value. Return True if found."""
        if self.head is None:
            return False
        if self.head.data == value:        # deleting the head
            self.head = self.head.next
            return True
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next   # bypass the node
                return True
            current = current.next
        return False

    def show(self):
        items, current = [], self.head
        while current:
            items.append(str(current.data))
            current = current.next
        print(" -> ".join(items) if items else "(empty)")


ll = LinkedList([5, 10, 15, 20, 25])
ll.show()
for target in (5, 15, 25, 99):
    done = ll.delete(target)
    print(f"Delete {target}:", "deleted" if done else "not found")
    ll.show()
''',
  algorithm=["If the list is empty return False", "If the head holds the value, move head to head.next", "Otherwise walk with current looking at current.next", "When current.next matches, set current.next = current.next.next", "Return False if the end is reached without a match"],
  explanation="To delete a node we make the previous node skip over it by linking to the node after it. The head is a special case because it has no previous node, so we just move head forward. Python's garbage collector frees the unlinked node automatically. The function returns True or False so the caller knows whether the value existed.",
  tags=["linked list", "delete", "remove"], topics=["Linked list"]),

P(title="Search a Linked List", category=DS, difficulty="Intermediate",
  description="Searches a linked list for a value and reports its position.",
  concepts=["traversal", "linear search", "index"], filename="linked_list_search.py",
  code=r'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def build(values):
    head = None
    tail = None
    for value in values:
        node = Node(value)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head


def search(head, key):
    """Return the 0-based position of key, or -1 if absent."""
    position = 0
    current = head
    while current is not None:
        if current.data == key:
            return position
        current = current.next
        position += 1
    return -1


head = build([8, 3, 12, 7, 20])
for key in (12, 20, 5):
    pos = search(head, key)
    if pos == -1:
        print(f"{key} is not in the list")
    else:
        print(f"{key} found at position {pos}")
''',
  algorithm=["Start at the head with position 0", "Compare current.data with the key", "If equal return the position", "Otherwise move to the next node and increase the position", "Return -1 when the end (None) is reached"],
  explanation="Searching a linked list is a linear search: we must follow the links one by one because there is no index to jump to. build() creates the list while keeping a tail pointer so each append is quick. search() counts how many nodes were passed and returns that count when the key is found, or -1 if the whole list is checked.",
  tags=["linked list", "search", "traversal"], topics=["Linked list"]),

P(title="Display Linked List Elements", category=DS, difficulty="Beginner",
  description="Traverses a linked list using an iterator so it can be printed or looped over.",
  concepts=["__iter__", "generator", "traversal"], filename="linked_list_display.py",
  code=r'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.size += 1

    def __iter__(self):
        """Allows: for value in linked_list"""
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __str__(self):
        return " -> ".join(str(v) for v in self) + " -> None"


colors = LinkedList()
for color in ("red", "green", "blue"):
    colors.append(color)

print("List     :", colors)
print("Size     :", colors.size)
for index, color in enumerate(colors, start=1):
    print(f"Element {index}: {color}")
''',
  algorithm=["Store nodes in a LinkedList with a size counter", "Define __iter__ as a generator that walks the nodes", "Define __str__ to join the values with arrows", "Print the list, its size and loop through it with enumerate()"],
  explanation="Defining __iter__ with yield turns the linked list into an iterable, so ordinary for loops, enumerate() and join() work on it. The generator remembers where it stopped between values. __str__ builds the readable arrow format used by print().",
  tags=["linked list", "display", "iterator", "generator"], topics=["Linked list"]),

P(title="Implement a Stack", category=DS, difficulty="Beginner",
  description="Creates a Stack class (LIFO) on top of a Python list.",
  concepts=["LIFO", "list", "class"], filename="stack_implementation.py",
  code=r'''
class Stack:
    """Last In, First Out container."""
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def __str__(self):
        return "Stack(bottom -> top): " + str(self._items)


stack = Stack()
for book in ("Python", "Java", "C", "SQL"):
    stack.push(book)
print(stack)
print("Top item :", stack.peek())
print("Size     :", stack.size())
print("Empty?   :", stack.is_empty())
''',
  algorithm=["Keep the items in a private list", "push(): append at the end (top)", "pop(): remove from the end", "peek(): look at the last item without removing it", "Provide is_empty() and size() helpers"],
  explanation="A stack follows Last In, First Out: the newest item is removed first, like a pile of plates. A Python list is ideal because append() and pop() work at the end in constant time. The list is kept private (leading underscore) so users only change the stack through push and pop.",
  tags=["stack", "lifo", "push", "pop"], topics=["stacks"]),

P(title="Push and Pop Operations on a Stack", category=DS, difficulty="Beginner",
  description="Shows the order in which items come out after several push and pop calls.",
  concepts=["push", "pop", "LIFO order"], filename="stack_push_pop.py",
  code=r'''
stack = []

print("--- PUSH ---")
for value in (10, 20, 30, 40):
    stack.append(value)
    print(f"Pushed {value:>2} -> {stack}")

print("--- POP ---")
while stack:
    removed = stack.pop()
    print(f"Popped {removed:>2} -> {stack}")
''',
  algorithm=["Start with an empty list as the stack", "Push values using append() and show the stack after each push", "Pop with pop() until the stack is empty", "Observe that values come out in reverse order"],
  explanation="append() acts as push and pop() acts as pop because both work at the end of the list. After pushing 10, 20, 30, 40 the first value popped is 40, the last pushed. The while stack: loop runs until the list is empty since an empty list is False.",
  tags=["stack", "push", "pop"], topics=["stacks"]),

P(title="Stack Overflow and Underflow Check", category=DS, difficulty="Intermediate",
  description="A fixed-capacity stack that reports overflow and underflow conditions.",
  concepts=["capacity", "overflow", "underflow", "custom exception"], filename="stack_overflow_underflow.py",
  code=r'''
class StackOverflowError(Exception):
    pass


class StackUnderflowError(Exception):
    pass


class BoundedStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def is_full(self):
        return len(self.items) == self.capacity

    def is_empty(self):
        return not self.items

    def push(self, item):
        if self.is_full():
            raise StackOverflowError(f"cannot push {item}: stack is full")
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise StackUnderflowError("cannot pop: stack is empty")
        return self.items.pop()


stack = BoundedStack(3)
for value in (1, 2, 3, 4):
    try:
        stack.push(value)
        print("Pushed", value, "->", stack.items)
    except StackOverflowError as err:
        print("Overflow:", err)

for _ in range(4):
    try:
        print("Popped", stack.pop())
    except StackUnderflowError as err:
        print("Underflow:", err)
''',
  algorithm=["Create a stack with a fixed capacity", "push(): if length equals capacity raise overflow error", "pop(): if the list is empty raise underflow error", "Push one more item than the capacity and catch the overflow", "Pop one more item than present and catch the underflow"],
  explanation="Python lists grow automatically, so overflow does not happen naturally; we simulate a fixed-size stack by checking the capacity ourselves. Overflow means pushing into a full stack and underflow means popping from an empty one. Both are reported with small custom exceptions that the caller handles with try-except.",
  tags=["stack", "overflow", "underflow", "capacity"], topics=["stacks"]),

P(title="Implement a Queue", category=DS, difficulty="Beginner",
  description="Creates a FIFO Queue class using a list.",
  concepts=["FIFO", "list", "class"], filename="queue_implementation.py",
  code=r'''
class Queue:
    """First In, First Out container (simple list version)."""
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)       # add at the rear

    def dequeue(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        return self._items.pop(0)      # remove from the front

    def front(self):
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def __str__(self):
        return "Queue(front -> rear): " + str(self._items)


line = Queue()
for customer in ("Asha", "Bala", "Chitra"):
    line.enqueue(customer)
print(line)
print("Front :", line.front())
print("Size  :", line.size())
''',
  algorithm=["Store items in a private list", "enqueue(): append at the rear", "dequeue(): remove the first item with pop(0)", "front(): view the first item", "Raise an error when dequeuing from an empty queue"],
  explanation="A queue is First In, First Out like a ticket line: the person who came first is served first. Items are added at the rear and removed from the front. pop(0) on a list has to shift every other item, which is slow for big queues, so real programs use collections.deque (shown in a later program).",
  tags=["queue", "fifo", "enqueue", "dequeue"], topics=["Queues"]),

P(title="Enqueue and Dequeue Operations", category=DS, difficulty="Beginner",
  description="Shows the FIFO order of enqueue and dequeue using collections.deque.",
  concepts=["deque", "append", "popleft"], filename="queue_enqueue_dequeue.py",
  code=r'''
from collections import deque

queue = deque()

print("--- ENQUEUE ---")
for task in ("print report", "send email", "backup data"):
    queue.append(task)
    print("Enqueued:", task, "| queue:", list(queue))

print("--- DEQUEUE ---")
while queue:
    task = queue.popleft()
    print("Dequeued:", task, "| queue:", list(queue))

print("Queue empty now:", len(queue) == 0)
''',
  algorithm=["Create an empty deque", "Enqueue tasks with append() (rear)", "Dequeue with popleft() (front)", "Repeat until the queue is empty"],
  explanation="collections.deque gives fast operations at both ends. append() adds to the right (rear) and popleft() removes from the left (front), both in constant time, so it is the recommended way to build a queue. The tasks come out in exactly the order they went in.",
  tags=["queue", "deque", "enqueue", "dequeue"], topics=["Queues"]),

P(title="Implement a Circular Queue", category=DS, difficulty="Advanced",
  description="A fixed-size circular queue where the rear wraps around to the start of the array.",
  concepts=["circular buffer", "modulo", "front/rear"], filename="circular_queue.py",
  code=r'''
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0          # index of the first item
        self.count = 0          # number of stored items

    def is_full(self):
        return self.count == self.capacity

    def is_empty(self):
        return self.count == 0

    def enqueue(self, item):
        if self.is_full():
            print(f"Queue full, cannot add {item}")
            return
        rear = (self.front + self.count) % self.capacity   # wrap around
        self.data[rear] = item
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue empty")
            return None
        item = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return item

    def show(self):
        print("Slots:", self.data, "| front index:", self.front, "| items:", self.count)


cq = CircularQueue(4)
for x in (10, 20, 30, 40):
    cq.enqueue(x)
cq.show()
cq.enqueue(50)                       # full
print("Dequeued:", cq.dequeue())
print("Dequeued:", cq.dequeue())
cq.show()
cq.enqueue(50)                       # reuses freed slot at index 0
cq.enqueue(60)                       # reuses slot at index 1
cq.show()
''',
  algorithm=["Create a list of fixed size and track front and count", "Rear index = (front + count) % capacity", "enqueue(): refuse if full, else store at rear and increase count", "dequeue(): read at front, clear it and move front forward with modulo", "Show how freed slots at the start are reused"],
  explanation="A circular queue treats the fixed-size list as a ring. The modulo operator % brings an index that passes the end back to 0, so slots freed by dequeue are reused instead of wasted. We track the front index and the number of items; the rear position is calculated from them. The demo fills the queue, removes two items and then adds two more into the freed slots.",
  tags=["circular queue", "ring buffer", "modulo"], topics=["Queues"]),

P(title="Implement a Deque", category=DS, difficulty="Intermediate",
  description="A double-ended queue class built from scratch on a list.",
  concepts=["double-ended queue", "list", "class"], filename="deque_implementation.py",
  code=r'''
class Deque:
    """Double-ended queue: add/remove at both front and rear."""
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if not self.items:
            raise IndexError("deque is empty")
        return self.items.pop(0)

    def remove_rear(self):
        if not self.items:
            raise IndexError("deque is empty")
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        return "Deque(front -> rear): " + str(self.items)


d = Deque()
d.add_rear(20)
d.add_rear(30)
d.add_front(10)
print(d)
print("Removed from rear :", d.remove_rear())
print("Removed from front:", d.remove_front())
print(d)
print("Size:", d.size())
''',
  algorithm=["Store items in a list", "add_front(): insert at index 0", "add_rear(): append at the end", "remove_front(): pop(0)", "remove_rear(): pop()"],
  explanation="A deque (double-ended queue, pronounced deck) allows insertion and removal at both ends, so it can behave as a stack or as a queue. This teaching version uses a list, where operations at the front are slow because items shift. The next program shows the efficient built-in collections.deque.",
  tags=["deque", "dequeue", "double ended queue"], topics=["Dequeues"]),

P(title="Deque Operations Using collections.deque", category=DS, difficulty="Intermediate",
  description="Uses the built-in deque with appendleft, popleft, rotate, maxlen and more.",
  concepts=["collections.deque", "rotate", "maxlen"], filename="collections_deque_operations.py",
  code=r'''
from collections import deque

d = deque([2, 3, 4])
print("Start        :", d)

d.append(5)               # add right
d.appendleft(1)           # add left
print("After adds   :", d)

print("pop()        :", d.pop())         # remove right
print("popleft()    :", d.popleft())     # remove left
print("Now          :", d)

d.extend([6, 7])
d.extendleft([0, -1])     # each item goes to the left one by one
print("After extend :", d)

d.rotate(2)               # rotate right by 2
print("rotate(2)    :", d)
d.rotate(-2)              # rotate back
print("rotate(-2)   :", d)

print("Index of 4   :", d.index(4))
print("Count of 4   :", d.count(4))
d.reverse()
print("Reversed     :", d)

recent = deque(maxlen=3)  # keeps only the latest 3 items
for page in ("home", "about", "blog", "contact", "faq"):
    recent.append(page)
print("Last 3 pages :", list(recent))
''',
  algorithm=["Import deque from collections", "Use append/appendleft and pop/popleft at both ends", "Use extend, extendleft and rotate", "Use index, count and reverse like a list", "Create a deque with maxlen to keep only recent items"],
  explanation="collections.deque is implemented as a doubly linked block structure, so adding or removing at either end is fast. rotate(n) moves items around the ring and maxlen automatically discards old items from the opposite end, which is handy for 'recent history' features. extendleft() reverses the order of the given items because each is placed on the left one at a time.",
  tags=["deque", "collections", "rotate", "maxlen"], topics=["Dequeues", "Queues"]),

# ---------------------------------------------------------------- DATE AND TIME 53-62
P(title="Display the Current Date", category=DT, difficulty="Beginner",
  description="Shows today's date using date.today() and its parts.",
  concepts=["datetime.date", "today()", "attributes"], filename="display_current_date.py",
  code=r'''
from datetime import date

today = date.today()
print("Today's date :", today)
print("Year         :", today.year)
print("Month        :", today.month)
print("Day          :", today.day)
print("Weekday name :", today.strftime("%A"))
print("ISO format   :", today.isoformat())
''',
  algorithm=["Import date from datetime", "Call date.today()", "Print the date object", "Print year, month and day attributes", "Format the weekday name with strftime()"],
  explanation="date.today() returns a date object for the computer's current local date. The object has year, month and day attributes, and strftime('%A') converts it to the weekday name. The output changes every day because it reads the system clock.",
  tags=["date", "today", "datetime"], topics=["Date and Time"]),

P(title="Display the Current Time", category=DT, difficulty="Beginner",
  description="Shows the current clock time using datetime.now().time().",
  concepts=["datetime.now()", "time()", "strftime"], filename="display_current_time.py",
  code=r'''
from datetime import datetime

now = datetime.now()
current_time = now.time()
print("Current time (full)  :", current_time)
print("Hour                 :", now.hour)
print("Minute               :", now.minute)
print("Second               :", now.second)
print("24-hour format       :", now.strftime("%H:%M:%S"))
print("12-hour format       :", now.strftime("%I:%M:%S %p"))
''',
  algorithm=["Import datetime", "Get the current moment with datetime.now()", "Extract the time part with .time()", "Print hour, minute and second", "Format the time in 24-hour and 12-hour styles"],
  explanation="datetime.now() returns the current local date and time; calling .time() keeps only the time-of-day part. strftime() builds text from format codes: %H is the 24-hour hour, %I the 12-hour hour, %M minutes, %S seconds and %p AM/PM. The values depend on when the program runs.",
  tags=["time", "now", "strftime"], topics=["Date and Time"]),

P(title="Display Date and Time Together", category=DT, difficulty="Beginner",
  description="Prints the current date and time as one datetime object.",
  concepts=["datetime.now()", "isoformat", "combine"], filename="display_date_and_time.py",
  code=r'''
from datetime import datetime, date, time

now = datetime.now()
print("Date and time :", now)
print("Without micro :", now.replace(microsecond=0))
print("ISO format    :", now.isoformat(sep=" ", timespec="seconds"))

# Build a datetime from separate date and time objects
combined = datetime.combine(date(2025, 1, 26), time(9, 30))
print("Combined      :", combined)
''',
  algorithm=["Call datetime.now()", "Print it, and print again with microseconds removed", "Print the ISO form using isoformat()", "Create a fixed datetime by combining a date and a time"],
  explanation="A datetime object holds both the date and the time. replace(microsecond=0) removes the fractional seconds for neater output and isoformat() gives the standard YYYY-MM-DD HH:MM:SS text. datetime.combine() joins separate date and time objects, which is useful when they come from different sources.",
  tags=["datetime", "now", "combine"], topics=["Date and Time"]),

P(title="Format Date and Time", category=DT, difficulty="Beginner",
  description="Formats a fixed datetime with strftime and parses text back with strptime.",
  concepts=["strftime", "strptime", "format codes"], filename="format_date_time.py",
  code=r'''
from datetime import datetime

moment = datetime(2025, 8, 15, 14, 5, 9)

formats = {
    "%d-%m-%Y": "day-month-year",
    "%d/%m/%y": "short year",
    "%B %d, %Y": "month name",
    "%A, %d %b %Y": "weekday + short month",
    "%H:%M:%S": "24-hour time",
    "%I:%M %p": "12-hour time",
    "%j": "day of the year",
}
for code, label in formats.items():
    print(f"{code:<15} {label:<22} -> {moment.strftime(code)}")

# strptime: text -> datetime
text = "26-01-2025 18:45"
parsed = datetime.strptime(text, "%d-%m-%Y %H:%M")
print("\nParsed text :", parsed)
print("Month name  :", parsed.strftime("%B"))
print(f"f-string    : {moment:%d %B %Y}")
''',
  algorithm=["Create a fixed datetime object", "Loop through a dictionary of format codes", "Use strftime() to convert the datetime to text", "Use strptime() to convert text back to a datetime", "Show formatting inside an f-string"],
  explanation="strftime (string from time) turns a datetime into text using % codes such as %d day, %m month, %Y four-digit year and %B month name. strptime (string parse time) does the reverse and needs a format that exactly matches the text. A fixed date is used so the output is always the same.",
  tags=["strftime", "strptime", "format"], topics=["Date and Time"]),

P(title="Calculate the Difference Between Dates", category=DT, difficulty="Beginner",
  description="Subtracts two dates to find the number of days, weeks and the time left to an event.",
  concepts=["date subtraction", "timedelta", "input"], filename="date_difference.py",
  code=r'''
from datetime import datetime

DATE_FORMAT = "%d-%m-%Y"


def read_date(prompt):
    while True:
        text = input(prompt)
        try:
            return datetime.strptime(text.strip(), DATE_FORMAT).date()
        except ValueError:
            print("  Please enter a valid date as DD-MM-YYYY")


start = read_date("Enter first date  (DD-MM-YYYY): ")
end = read_date("Enter second date (DD-MM-YYYY): ")

difference = end - start                 # a timedelta object
days = abs(difference.days)
print(f"\nDifference : {days} days")
print(f"In weeks   : {days // 7} weeks and {days % 7} days")
if end < start:
    print("(The second date is earlier than the first)")
''',
  algorithm=["Read two dates in DD-MM-YYYY format and validate with strptime", "Subtract the first date from the second", "Take abs() of the .days value", "Show the result in days, then weeks and days"],
  explanation="Subtracting two date objects gives a timedelta whose .days attribute is the whole number of days between them. The read_date() function keeps asking until strptime accepts the input, so invalid dates like 31-02-2025 are rejected. abs() makes the answer positive whichever date is earlier.",
  sample_input="31-02-2025\n01-01-2025\n15-08-2025", kind="Interactive",
  tags=["date difference", "timedelta", "days"], topics=["Date and Time"]),

P(title="Calculate Age from Date of Birth", category=DT, difficulty="Beginner",
  description="Computes age in years, months and days from a birth date.",
  concepts=["date", "age calculation", "tuple comparison"], filename="age_from_date_of_birth.py",
  code=r'''
from datetime import date


def calculate_age(birth, today):
    years = today.year - birth.year
    # not yet had the birthday this year?
    if (today.month, today.day) < (birth.month, birth.day):
        years -= 1
    last_birthday_year = birth.year + years
    try:
        last_birthday = date(last_birthday_year, birth.month, birth.day)
    except ValueError:                       # born on 29 February
        last_birthday = date(last_birthday_year, 3, 1)
    extra_days = (today - last_birthday).days
    return years, extra_days


reference_day = date(2025, 6, 15)             # fixed so the output is repeatable
for name, dob in (("Asha", date(2003, 9, 21)), ("Ravi", date(2000, 6, 15)), ("Meena", date(1999, 12, 31))):
    years, days = calculate_age(dob, reference_day)
    print(f"{name:<6} born {dob}  ->  {years} years and {days} days old on {reference_day}")

print("\nToday's reference using date.today():", date.today())
''',
  algorithm=["Subtract birth year from the current year", "Subtract one if the birthday has not yet occurred this year (compare (month, day) tuples)", "Find the date of the last birthday", "Count the days from that birthday to today"],
  explanation="Age is the difference in years, minus one if this year's birthday has not happened yet. Comparing the tuples (month, day) does this check neatly. A fixed reference date is used so the sample output never changes; replace it with date.today() to get a real age. A try-except handles people born on 29 February.",
  tags=["age", "birthday", "date of birth"], topics=["Date and Time"]),

P(title="Demonstrate timedelta", category=DT, difficulty="Intermediate",
  description="Uses timedelta to add and subtract durations from dates and datetimes.",
  concepts=["timedelta", "date arithmetic", "total_seconds"], filename="timedelta_demo.py",
  code=r'''
from datetime import date, datetime, timedelta

start = date(2025, 1, 31)
print("Start date        :", start)
print("+ 7 days          :", start + timedelta(days=7))
print("- 31 days         :", start - timedelta(days=31))
print("+ 2 weeks         :", start + timedelta(weeks=2))

meeting = datetime(2025, 3, 10, 9, 0)
print("\nMeeting           :", meeting)
print("+ 90 minutes      :", meeting + timedelta(minutes=90))
print("- 5 hours         :", meeting - timedelta(hours=5))

duration = timedelta(days=2, hours=3, minutes=30)
print("\nDuration          :", duration)
print("Days / seconds    :", duration.days, "/", duration.seconds)
print("Total seconds     :", duration.total_seconds())
print("Total hours       :", duration.total_seconds() / 3600)
print("Doubled           :", duration * 2)
print("Compare           :", timedelta(hours=25) > timedelta(days=1))
''',
  algorithm=["Create timedelta objects with days, weeks, hours or minutes", "Add them to or subtract them from a date", "Do the same with a datetime", "Inspect .days, .seconds and total_seconds()", "Multiply and compare timedeltas"],
  explanation="A timedelta represents a length of time, not a point in time. Adding it to a date or datetime moves that value forward, subtracting moves it back. total_seconds() converts the whole duration to seconds, while .days and .seconds give only the separate parts. Timedeltas can also be multiplied and compared.",
  tags=["timedelta", "duration", "date arithmetic"], topics=["Date and Time"]),

P(title="Demonstrate datetime", category=DT, difficulty="Intermediate",
  description="Explores the datetime, date and time classes: creation, attributes, replace and comparison.",
  concepts=["datetime class", "attributes", "replace", "weekday"], filename="datetime_demo.py",
  code=r'''
from datetime import datetime, date, time

dt = datetime(2025, 8, 15, 10, 30, 45)
print("datetime object :", dt)
print("date part       :", dt.date())
print("time part       :", dt.time())
print("year/month/day  :", dt.year, dt.month, dt.day)
print("hour/min/sec    :", dt.hour, dt.minute, dt.second)
print("weekday() (Mon=0):", dt.weekday())
print("isoweekday()     :", dt.isoweekday())
print("Day name         :", dt.strftime("%A"))

changed = dt.replace(year=2030, hour=0, minute=0, second=0)
print("replace()        :", changed)

a = datetime(2025, 1, 1)
b = datetime(2025, 12, 31)
print("a < b            :", a < b)
print("b - a            :", b - a)

print("Unix timestamp   :", datetime(2025, 1, 1, 0, 0, 0).timestamp() > 0)
print("From string      :", datetime.fromisoformat("2025-08-15T10:30:45"))
print("Max date (date)  :", date.max)
print("Midnight (time)  :", time.min)
''',
  algorithm=["Create a datetime with year, month, day, hour, minute, second", "Read its attributes and split it into date() and time()", "Find the weekday with weekday() and strftime()", "Use replace() to create a modified copy", "Compare and subtract datetimes and parse an ISO string"],
  explanation="The datetime class combines date and time in one object. Objects are immutable, so replace() returns a new object instead of changing the old one. weekday() gives Monday as 0 while isoweekday() gives Monday as 1. Datetimes can be compared with < and > and subtracted to get a timedelta.",
  tags=["datetime", "weekday", "replace", "fromisoformat"], topics=["Date and Time"]),

P(title="Demonstrate the time Module", category=DT, difficulty="Intermediate",
  description="Uses time.time(), sleep(), perf_counter(), localtime() and strftime().",
  concepts=["time module", "sleep", "perf_counter", "struct_time"], filename="time_module_demo.py",
  code=r'''
import time

# 1. Seconds since the epoch (1 Jan 1970 UTC)
seconds = time.time()
print("Seconds since epoch is a float:", isinstance(seconds, float))

# 2. struct_time for a fixed moment (gmtime is the same everywhere)
fixed = time.gmtime(1700000000)
print("gmtime(1700000000):", fixed.tm_year, fixed.tm_mon, fixed.tm_mday, fixed.tm_hour, fixed.tm_min)
print("Formatted         :", time.strftime("%Y-%m-%d %H:%M:%S", fixed))
print("asctime           :", time.asctime(fixed))
print("mktime round trip :", time.mktime(time.localtime(seconds)) > 0)

# 3. Pause and measure
start = time.perf_counter()
time.sleep(0.3)
elapsed = time.perf_counter() - start
print(f"sleep(0.3) took about {elapsed:.1f} seconds")

# 4. Count down using sleep
for n in (3, 2, 1):
    print("Countdown", n)
    time.sleep(0.1)
print("Lift off!")
''',
  algorithm=["Read time.time() to get seconds since the epoch", "Convert a fixed timestamp with gmtime() and format it with strftime()", "Pause the program with sleep()", "Measure elapsed time with perf_counter()", "Run a short countdown"],
  explanation="The time module works with plain seconds. time.time() returns seconds since 1 January 1970, gmtime()/localtime() convert such seconds to a struct_time, and strftime() formats it. time.sleep() pauses the program and perf_counter() is the best clock for measuring how long code takes. gmtime on a fixed number gives the same output on every computer.",
  tags=["time", "sleep", "perf_counter", "timestamp"], topics=["Date and Time"]),

P(title="Demonstrate the calendar Module", category=DT, difficulty="Beginner",
  description="Prints a month, a year summary and answers leap-year and weekday questions with calendar.",
  concepts=["calendar.month", "isleap", "weekday", "monthrange"], filename="calendar_demo.py",
  code=r'''
import calendar

print(calendar.month(2025, 8))                 # text calendar of one month

print("Is 2024 a leap year? ", calendar.isleap(2024))
print("Is 2025 a leap year? ", calendar.isleap(2025))
print("Leap years 2000-2030 :", calendar.leapdays(2000, 2031))

# weekday(): Monday = 0 ... Sunday = 6
day_number = calendar.weekday(2025, 8, 15)
print("15 Aug 2025 is a     :", calendar.day_name[day_number])

first_weekday, days_in_month = calendar.monthrange(2024, 2)
print("February 2024 starts on", calendar.day_name[first_weekday], "and has", days_in_month, "days")

print("Month names          :", list(calendar.month_abbr)[1:])

cal = calendar.TextCalendar(firstweekday=calendar.SUNDAY)
print(cal.formatmonth(2025, 1))
''',
  algorithm=["Import calendar", "Print a month with calendar.month()", "Check leap years with isleap() and leapdays()", "Find a weekday with calendar.weekday() and day_name", "Use monthrange() for the days in a month", "Create a TextCalendar that starts on Sunday"],
  explanation="The calendar module knows the layout of months and leap-year rules. calendar.month(year, month) returns a ready-to-print text calendar, weekday() tells which day a date falls on and monthrange() returns the first weekday and the number of days of a month. TextCalendar lets you choose which day the week starts on.",
  tags=["calendar", "leap year", "month", "weekday"], topics=["Date and Time"]),

# ---------------------------------------------------------------- Database Connectivity

P(title="Connect to an SQLite Database", category=DB, difficulty="Beginner",
  description="Opens a connection to an SQLite database file, checks the SQLite version and closes the connection.",
  concepts=["sqlite3.connect", "cursor", "close"], filename="sqlite_connect.py",
  code=r'''
import os
import sqlite3

DB_FILE = "connect_demo.db"

# sqlite3.connect() opens the file; if it does not exist SQLite creates it.
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# SQL: SELECT sqlite_version();
cursor.execute("SELECT sqlite_version()")
version = cursor.fetchone()[0]

print("Connected to database :", DB_FILE)
print("SQLite library version:", "available" if version else "unknown")
print("Python sqlite3 module :", "loaded")

connection.close()                       # always release the connection
print("Connection closed.")

os.remove(DB_FILE)                       # clean up the demo file
print("Demo file removed     :", not os.path.exists(DB_FILE))
''',
  algorithm=["Import sqlite3", "Call sqlite3.connect() with a file name", "Create a cursor from the connection", "Run SELECT sqlite_version()", "Close the connection", "Delete the demo file"],
  explanation="sqlite3 is built into Python, so no installation is needed. connect() returns a Connection object and creates the database file when it is missing. A cursor is used to send SQL statements and fetch results. The connection is closed at the end and the demo file is deleted so the program leaves nothing behind.",
  tags=["sqlite", "connect", "database", "cursor"], topics=[DBT]),

P(title="Create a Database", category=DB, difficulty="Beginner",
  description="Creates a new SQLite database file and an in-memory database, and confirms that the file exists.",
  concepts=["sqlite3.connect", ":memory:", "os.path.exists"], filename="sqlite_create_database.py",
  code=r'''
import os
import sqlite3

DB_FILE = "college.db"

print("Before connect, file exists:", os.path.exists(DB_FILE))

# Connecting to a name that does not exist creates a new database file.
connection = sqlite3.connect(DB_FILE)
connection.execute("CREATE TABLE IF NOT EXISTS dummy (id INTEGER)")   # forces file creation
connection.commit()
connection.close()

print("After connect,  file exists:", os.path.exists(DB_FILE))
print("File size is more than 0   :", os.path.getsize(DB_FILE) > 0)

# ':memory:' creates a temporary database that lives only in RAM.
memory_db = sqlite3.connect(":memory:")
print("In-memory database created :", isinstance(memory_db, sqlite3.Connection))
memory_db.close()

os.remove(DB_FILE)
print("After remove,   file exists:", os.path.exists(DB_FILE))
''',
  algorithm=["Check that the file does not exist", "Connect to a new file name", "Execute a statement so SQLite writes the file", "Commit and close", "Confirm the file now exists", "Create an in-memory database and delete the file"],
  explanation="In SQLite a database is just a file, so creating a database means connecting to a new file name. SQLite writes the file when the first statement is committed. The special name ':memory:' gives a fast temporary database that vanishes when closed, which is useful for tests and practice.",
  tags=["sqlite", "create database", "memory", "file"], topics=[DBT]),

P(title="Create a Table", category=DB, difficulty="Beginner",
  description="Creates a students table with CREATE TABLE and lists its columns using PRAGMA table_info.",
  concepts=["CREATE TABLE", "PRIMARY KEY", "PRAGMA"], filename="sqlite_create_table.py",
  code=r'''
import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

# SQL:
#   CREATE TABLE IF NOT EXISTS students (
#       roll_no INTEGER PRIMARY KEY,
#       name    TEXT NOT NULL,
#       course  TEXT,
#       marks   REAL DEFAULT 0
#   );
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        roll_no INTEGER PRIMARY KEY,
        name    TEXT NOT NULL,
        course  TEXT,
        marks   REAL DEFAULT 0
    )
""")
connection.commit()

# SQL: PRAGMA table_info(students);
print("Column details of table 'students'")
print(f"{'No':<4}{'Name':<10}{'Type':<8}{'NotNull':<9}{'Default':<9}{'PK'}")
for cid, name, col_type, not_null, default, pk in cursor.execute("PRAGMA table_info(students)"):
    print(f"{cid:<4}{name:<10}{col_type:<8}{not_null:<9}{str(default):<9}{pk}")

# SQL: SELECT name FROM sqlite_master WHERE type = 'table';
tables = cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'").fetchall()
print("Tables in database:", [t[0] for t in tables])

connection.close()
''',
  algorithm=["Connect to an in-memory database", "Write the CREATE TABLE statement with column types", "Execute it and commit", "Read column details with PRAGMA table_info", "List tables from sqlite_master"],
  explanation="CREATE TABLE defines the columns, their data types and rules such as PRIMARY KEY, NOT NULL and DEFAULT. IF NOT EXISTS stops an error if the table is already there. PRAGMA table_info returns one row per column, and sqlite_master is SQLite's own catalogue of all tables.",
  tags=["sqlite", "create table", "pragma", "schema"], topics=[DBT]),

P(title="Insert Records into a Table", category=DB, difficulty="Beginner",
  description="Inserts one record with execute() and several records with executemany(), then reports the row count.",
  concepts=["INSERT INTO", "execute", "executemany", "commit"], filename="sqlite_insert_records.py",
  code=r'''
import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
cursor.execute("CREATE TABLE students (roll_no INTEGER PRIMARY KEY, name TEXT, course TEXT, marks REAL)")

# SQL: INSERT INTO students (roll_no, name, course, marks) VALUES (?, ?, ?, ?);
cursor.execute("INSERT INTO students (roll_no, name, course, marks) VALUES (?, ?, ?, ?)",
               (1, "Asha", "MCA", 82.5))
print("Inserted one record, rowcount =", cursor.rowcount)

more_students = [
    (2, "Ravi", "MCA", 74.0),
    (3, "Meena", "MBA", 91.0),
    (4, "John", "MCA", 66.5),
]
cursor.executemany("INSERT INTO students VALUES (?, ?, ?, ?)", more_students)
print("Inserted many records, rowcount =", cursor.rowcount)

connection.commit()                      # make the changes permanent

# SQL: SELECT COUNT(*) FROM students;
total = cursor.execute("SELECT COUNT(*) FROM students").fetchone()[0]
print("Total records in table:", total)

connection.close()
''',
  algorithm=["Create the table", "Insert one row using placeholders", "Insert a list of rows with executemany()", "Commit the transaction", "Count rows with SELECT COUNT(*)"],
  explanation="INSERT INTO adds a row. The question marks are placeholders that sqlite3 fills with the values from a tuple, which is safer than building SQL text by hand. executemany() repeats the same statement for each tuple in a list. commit() saves the inserted data permanently.",
  tags=["sqlite", "insert", "executemany", "records"], topics=[DBT]),

P(title="Display Records from a Table", category=DB, difficulty="Beginner",
  description="Reads rows with SELECT and shows fetchall(), fetchone() and iteration over the cursor.",
  concepts=["SELECT", "fetchall", "fetchone", "ORDER BY"], filename="sqlite_display_records.py",
  code=r'''
import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
cursor.execute("CREATE TABLE students (roll_no INTEGER PRIMARY KEY, name TEXT, course TEXT, marks REAL)")
cursor.executemany("INSERT INTO students VALUES (?, ?, ?, ?)", [
    (1, "Asha", "MCA", 82.5), (2, "Ravi", "MCA", 74.0),
    (3, "Meena", "MBA", 91.0), (4, "John", "MCA", 66.5),
])

# SQL: SELECT * FROM students;
print("All records (fetchall):")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print("  ", row)

# SQL: SELECT name, marks FROM students ORDER BY marks DESC;
print("\nRanked by marks (iterating the cursor):")
for name, marks in cursor.execute("SELECT name, marks FROM students ORDER BY marks DESC"):
    print(f"   {name:<8}{marks:>6.1f}")

# SQL: SELECT * FROM students LIMIT 1;
cursor.execute("SELECT * FROM students LIMIT 1")
print("\nFirst record (fetchone):", cursor.fetchone())

connection.close()
''',
  algorithm=["Create and fill the table", "Run SELECT * and call fetchall()", "Loop over the rows and print them", "Use ORDER BY to sort the output", "Use fetchone() to read a single row"],
  explanation="SELECT retrieves rows. After execute(), fetchall() returns every row as a list of tuples, fetchone() returns the next single row, and the cursor itself can be used in a for loop. ORDER BY sorts the result and LIMIT restricts how many rows come back.",
  tags=["sqlite", "select", "fetchall", "display"], topics=[DBT]),

P(title="Update Records in a Table", category=DB, difficulty="Beginner",
  description="Changes existing rows with UPDATE and WHERE and reports how many rows were affected.",
  concepts=["UPDATE", "WHERE", "rowcount"], filename="sqlite_update_records.py",
  code=r'''
import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
cursor.execute("CREATE TABLE students (roll_no INTEGER PRIMARY KEY, name TEXT, course TEXT, marks REAL)")
cursor.executemany("INSERT INTO students VALUES (?, ?, ?, ?)", [
    (1, "Asha", "MCA", 82.5), (2, "Ravi", "MCA", 74.0),
    (3, "Meena", "MBA", 91.0), (4, "John", "MCA", 66.5),
])

def show(title):
    print(title)
    for row in cursor.execute("SELECT * FROM students ORDER BY roll_no"):
        print("  ", row)

show("Before update:")

# SQL: UPDATE students SET marks = ? WHERE roll_no = ?;
cursor.execute("UPDATE students SET marks = ? WHERE roll_no = ?", (80.0, 2))
print("\nRows changed by first update :", cursor.rowcount)

# SQL: UPDATE students SET marks = marks + 5 WHERE course = ?;
cursor.execute("UPDATE students SET marks = marks + 5 WHERE course = ?", ("MCA",))
print("Rows changed by second update:", cursor.rowcount)
connection.commit()

print()
show("After update:")
connection.close()
''',
  algorithm=["Create and fill the table", "Run UPDATE ... WHERE for one student", "Run UPDATE ... WHERE for a whole course", "Check cursor.rowcount", "Commit and display the table again"],
  explanation="UPDATE changes column values of existing rows. The WHERE clause chooses which rows are changed; without it every row would be modified. cursor.rowcount tells how many rows were affected. Values are passed as parameters and commit() saves the change.",
  tags=["sqlite", "update", "where", "rowcount"], topics=[DBT]),

P(title="Delete Records from a Table", category=DB, difficulty="Beginner",
  description="Removes selected rows with DELETE and WHERE and shows the remaining records.",
  concepts=["DELETE", "WHERE", "rowcount"], filename="sqlite_delete_records.py",
  code=r'''
import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
cursor.execute("CREATE TABLE students (roll_no INTEGER PRIMARY KEY, name TEXT, course TEXT, marks REAL)")
cursor.executemany("INSERT INTO students VALUES (?, ?, ?, ?)", [
    (1, "Asha", "MCA", 82.5), (2, "Ravi", "MCA", 74.0),
    (3, "Meena", "MBA", 91.0), (4, "John", "MCA", 36.5),
])

# SQL: DELETE FROM students WHERE roll_no = ?;
cursor.execute("DELETE FROM students WHERE roll_no = ?", (3,))
print("Deleted by roll number:", cursor.rowcount)

# SQL: DELETE FROM students WHERE marks < ?;
cursor.execute("DELETE FROM students WHERE marks < ?", (40,))
print("Deleted failing marks :", cursor.rowcount)

# Deleting a record that does not exist changes nothing.
cursor.execute("DELETE FROM students WHERE roll_no = ?", (99,))
print("Deleted roll no 99    :", cursor.rowcount)
connection.commit()

print("\nRemaining records:")
for row in cursor.execute("SELECT * FROM students"):
    print("  ", row)

connection.close()
''',
  algorithm=["Create and fill the table", "Delete one row by primary key", "Delete rows that match a condition", "Try deleting a missing row and see rowcount 0", "Commit and list the remaining rows"],
  explanation="DELETE FROM removes rows that satisfy the WHERE condition. Always include WHERE, otherwise the whole table is emptied. rowcount shows how many rows were removed, and it is 0 when nothing matched. Parameters keep the statement safe.",
  tags=["sqlite", "delete", "where", "remove"], topics=[DBT]),

P(title="Search Database Records", category=DB, difficulty="Intermediate",
  description="Searches a table by exact match, LIKE pattern, range and combined conditions.",
  concepts=["WHERE", "LIKE", "BETWEEN", "AND/OR"], filename="sqlite_search_records.py",
  code=r'''
import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
cursor.execute("CREATE TABLE students (roll_no INTEGER PRIMARY KEY, name TEXT, course TEXT, marks REAL)")
cursor.executemany("INSERT INTO students VALUES (?, ?, ?, ?)", [
    (1, "Asha", "MCA", 82.5), (2, "Ravi", "MCA", 74.0),
    (3, "Meena", "MBA", 91.0), (4, "John", "MCA", 66.5),
    (5, "Anil", "MBA", 58.0),
])

def search(title, sql, params=()):
    print(title)
    rows = cursor.execute(sql, params).fetchall()
    if not rows:
        print("   no records found")
    for row in rows:
        print("  ", row)
    print()

# SQL: SELECT * FROM students WHERE roll_no = ?;
search("1. Exact match, roll_no = 3", "SELECT * FROM students WHERE roll_no = ?", (3,))

# SQL: SELECT * FROM students WHERE name LIKE ?;   ('A%' = starts with A)
search("2. Names starting with A", "SELECT * FROM students WHERE name LIKE ?", ("A%",))

# SQL: SELECT * FROM students WHERE marks BETWEEN ? AND ?;
search("3. Marks between 70 and 90", "SELECT * FROM students WHERE marks BETWEEN ? AND ?", (70, 90))

# SQL: SELECT * FROM students WHERE course = ? AND marks >= ?;
search("4. MCA students with marks >= 70", "SELECT * FROM students WHERE course = ? AND marks >= ?", ("MCA", 70))

search("5. Search that finds nothing", "SELECT * FROM students WHERE name = ?", ("Zara",))
connection.close()
''',
  algorithm=["Create and fill the table", "Write a helper that runs a query and prints rows", "Search with equality", "Search with LIKE and a pattern", "Search with BETWEEN and with AND", "Handle the case of no result"],
  explanation="The WHERE clause filters rows. '=' matches exactly, LIKE matches patterns where % means any characters, BETWEEN selects a range and AND/OR combine conditions. The helper function takes the SQL and its parameters, runs the query and prints a message when nothing is found.",
  tags=["sqlite", "search", "like", "where"], topics=[DBT]),

P(title="Parameterized SQL Queries", category=DB, difficulty="Intermediate",
  description="Compares placeholders with string formatting and shows how parameters stop SQL injection.",
  concepts=["? placeholders", "named parameters", "SQL injection"], filename="sqlite_parameterized_queries.py",
  code=r'''
import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")
cursor.executemany("INSERT INTO users VALUES (?, ?)", [("admin", "s3cret"), ("asha", "pass123")])

# Positional placeholders (?)
# SQL: SELECT * FROM users WHERE username = ?;
print("Positional :", cursor.execute("SELECT * FROM users WHERE username = ?", ("asha",)).fetchall())

# Named placeholders (:name) with a dictionary
# SQL: SELECT * FROM users WHERE username = :user AND password = :pwd;
print("Named      :", cursor.execute(
    "SELECT * FROM users WHERE username = :user AND password = :pwd",
    {"user": "admin", "pwd": "s3cret"}).fetchall())

# A malicious input that tries to bypass the password check
evil = "x' OR '1'='1"

# UNSAFE: building SQL text by joining strings - NEVER do this
unsafe_sql = "SELECT * FROM users WHERE username = '" + evil + "'"
print("\nUnsafe SQL text:", unsafe_sql)
print("Unsafe result  :", cursor.execute(unsafe_sql).fetchall(), " <- leaks every user!")

# SAFE: the value is passed separately and is treated only as data
safe_rows = cursor.execute("SELECT * FROM users WHERE username = ?", (evil,)).fetchall()
print("Safe result    :", safe_rows, " <- nothing leaked")

connection.close()
''',
  algorithm=["Create a users table with two rows", "Query using ? placeholders and a tuple", "Query using :name placeholders and a dictionary", "Build an unsafe query by joining strings", "Run the same malicious input as a parameter", "Compare the two results"],
  explanation="A parameterized query keeps the SQL text and the values apart. sqlite3 sends the values separately, so they can never change the structure of the statement. The unsafe version joins the user's text into the SQL, so the trick input x' OR '1'='1 makes the condition always true and returns every user. Always use ? or :name placeholders.",
  tags=["sqlite", "parameters", "placeholder", "sql injection"], topics=[DBT]),

P(title="Student Database Management Program", category=DB, difficulty="Advanced",
  description="A menu-driven SQLite application to add, view, search, update and delete student records.",
  concepts=["sqlite3", "CRUD", "menu loop", "input validation"], filename="student_database_management.py",
  code=r'''
import os
import sqlite3

DB_FILE = "students.db"

# SQL: CREATE TABLE IF NOT EXISTS students (roll_no INTEGER PRIMARY KEY, name TEXT NOT NULL, course TEXT, marks REAL);
def setup(connection):
    connection.execute("""CREATE TABLE IF NOT EXISTS students (
        roll_no INTEGER PRIMARY KEY, name TEXT NOT NULL, course TEXT, marks REAL)""")
    connection.commit()

def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")

def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")

def add_student(connection):
    roll = read_int("Roll no : ")
    name = input("Name    : ").strip()
    course = input("Course  : ").strip()
    marks = read_float("Marks   : ")
    try:
        # SQL: INSERT INTO students VALUES (?, ?, ?, ?);
        connection.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (roll, name, course, marks))
        connection.commit()
        print("Student added.")
    except sqlite3.IntegrityError:
        print("Error: roll number", roll, "already exists.")

def view_students(connection):
    # SQL: SELECT * FROM students ORDER BY roll_no;
    rows = connection.execute("SELECT * FROM students ORDER BY roll_no").fetchall()
    print(f"{'Roll':<6}{'Name':<10}{'Course':<8}{'Marks':>6}")
    for roll, name, course, marks in rows:
        print(f"{roll:<6}{name:<10}{course:<8}{marks:>6.1f}")
    print("Total:", len(rows))

def search_student(connection):
    text = input("Name to search: ").strip()
    # SQL: SELECT * FROM students WHERE name LIKE ?;
    rows = connection.execute("SELECT * FROM students WHERE name LIKE ?", ("%" + text + "%",)).fetchall()
    print(rows if rows else "No matching student.")

def update_marks(connection):
    roll = read_int("Roll no to update: ")
    marks = read_float("New marks: ")
    # SQL: UPDATE students SET marks = ? WHERE roll_no = ?;
    cursor = connection.execute("UPDATE students SET marks = ? WHERE roll_no = ?", (marks, roll))
    connection.commit()
    print("Updated." if cursor.rowcount else "Roll number not found.")

def delete_student(connection):
    roll = read_int("Roll no to delete: ")
    # SQL: DELETE FROM students WHERE roll_no = ?;
    cursor = connection.execute("DELETE FROM students WHERE roll_no = ?", (roll,))
    connection.commit()
    print("Deleted." if cursor.rowcount else "Roll number not found.")

def main():
    connection = sqlite3.connect(DB_FILE)
    setup(connection)
    actions = {"1": add_student, "2": view_students, "3": search_student,
               "4": update_marks, "5": delete_student}
    while True:
        print("\n1.Add  2.View  3.Search  4.Update marks  5.Delete  6.Exit")
        choice = input("Choice: ").strip()
        if choice == "6":
            break
        action = actions.get(choice)
        if action:
            action(connection)
        else:
            print("Invalid choice.")
    connection.close()
    os.remove(DB_FILE)                   # demo only: remove the file
    print("Goodbye.")

main()
''',
  sample_input="1\n101\nAsha\nMCA\n82.5\n1\n102\nRavi\nMCA\n74\n1\n101\nDup\nMCA\n50\n1\nabc\n103\nMeena\nMBA\n91\n2\n3\nrav\n4\n102\n80\n5\n101\n5\n999\n2\n9\n6\n",
  algorithm=["Open the database and create the table", "Show a menu in a loop", "Add: read and validate input, INSERT with parameters", "View: SELECT and print a table", "Search with LIKE, update with UPDATE, delete with DELETE", "Exit: close the connection"],
  explanation="Each menu option is a small function that runs one SQL statement with parameters. Dictionary dispatch maps the typed choice to the function. read_int and read_float repeat until valid input is given, and a duplicate roll number is caught as sqlite3.IntegrityError. commit() is called after every change, and the file is removed at the end because this is only a demo.",
  tags=["student", "crud", "sqlite", "menu", "application"], topics=[DBT], kind="Application"),

P(title="Employee Database Management Program", category=DB, difficulty="Advanced",
  description="A SQLite employee application with add, list, department report, raise salary and delete operations.",
  concepts=["sqlite3", "AUTOINCREMENT", "GROUP BY", "aggregate functions"], filename="employee_database_management.py",
  code=r'''
import os
import sqlite3

DB_FILE = "employees.db"

class EmployeeDatabase:
    """Small wrapper class around an SQLite employees table."""

    def __init__(self, file_name):
        self.connection = sqlite3.connect(file_name)
        # SQL: CREATE TABLE IF NOT EXISTS employees (
        #          emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
        #          name TEXT NOT NULL, department TEXT, salary REAL CHECK (salary >= 0));
        self.connection.execute("""CREATE TABLE IF NOT EXISTS employees (
            emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL, department TEXT, salary REAL CHECK (salary >= 0))""")

    def add(self, name, department, salary):
        # SQL: INSERT INTO employees (name, department, salary) VALUES (?, ?, ?);
        try:
            cursor = self.connection.execute(
                "INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
                (name, department, salary))
            self.connection.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError as error:
            print("Could not add", name, "->", error)
            return None

    def list_all(self):
        # SQL: SELECT * FROM employees ORDER BY emp_id;
        print(f"{'ID':<4}{'Name':<10}{'Dept':<8}{'Salary':>10}")
        for emp_id, name, dept, salary in self.connection.execute("SELECT * FROM employees ORDER BY emp_id"):
            print(f"{emp_id:<4}{name:<10}{dept:<8}{salary:>10,.2f}")

    def department_report(self):
        # SQL: SELECT department, COUNT(*), AVG(salary), MAX(salary) FROM employees GROUP BY department;
        print(f"{'Dept':<8}{'Count':>6}{'Average':>12}{'Highest':>12}")
        query = "SELECT department, COUNT(*), AVG(salary), MAX(salary) FROM employees GROUP BY department"
        for dept, count, average, highest in self.connection.execute(query):
            print(f"{dept:<8}{count:>6}{average:>12,.2f}{highest:>12,.2f}")

    def give_raise(self, department, percent):
        # SQL: UPDATE employees SET salary = salary * (1 + ? / 100.0) WHERE department = ?;
        cursor = self.connection.execute(
            "UPDATE employees SET salary = salary * (1 + ? / 100.0) WHERE department = ?",
            (percent, department))
        self.connection.commit()
        return cursor.rowcount

    def remove(self, emp_id):
        # SQL: DELETE FROM employees WHERE emp_id = ?;
        cursor = self.connection.execute("DELETE FROM employees WHERE emp_id = ?", (emp_id,))
        self.connection.commit()
        return cursor.rowcount

    def close(self):
        self.connection.close()

db = EmployeeDatabase(DB_FILE)
db.add("Kiran", "IT", 55000)
db.add("Sunita", "HR", 48000)
db.add("Vikram", "IT", 72000)
db.add("Priya", "Sales", 40000)
db.add("Bad", "IT", -100)                  # rejected by the CHECK rule

print("All employees")
db.list_all()
print("\nDepartment report")
db.department_report()

print("\n10% raise for IT, employees changed:", db.give_raise("IT", 10))
print("Removing employee 4, rows deleted   :", db.remove(4))

print("\nAfter changes")
db.list_all()

db.close()
os.remove(DB_FILE)
''',
  algorithm=["Create an EmployeeDatabase class that opens the file and creates the table", "Add employees with parameterized INSERT", "Reject invalid salary through the CHECK constraint", "List all rows and build a GROUP BY report", "Give a percentage raise with UPDATE", "Delete an employee, show the result and clean up"],
  explanation="The class hides all SQL inside methods, so the main program only calls add(), list_all(), give_raise() and so on. AUTOINCREMENT creates employee ids automatically and lastrowid returns the new id. A CHECK constraint refuses negative salaries, raising IntegrityError that the program catches. GROUP BY with COUNT, AVG and MAX gives a department summary.",
  tags=["employee", "sqlite", "group by", "class", "application"], topics=[DBT], kind="Application"),

P(title="Demonstrate Database Transactions", category=DB, difficulty="Advanced",
  description="Transfers money between two accounts as one all-or-nothing transaction using SQLite.",
  concepts=["transaction", "atomicity", "with connection", "IntegrityError"], filename="sqlite_transactions.py",
  code=r'''
import sqlite3

connection = sqlite3.connect(":memory:")
connection.execute("CREATE TABLE accounts (name TEXT PRIMARY KEY, balance REAL CHECK (balance >= 0))")
connection.executemany("INSERT INTO accounts VALUES (?, ?)", [("Asha", 1000.0), ("Ravi", 500.0)])
connection.commit()

def show(title):
    print(title, dict(connection.execute("SELECT name, balance FROM accounts")))

def transfer(sender, receiver, amount):
    """Move money as ONE transaction: both updates succeed or neither does."""
    try:
        # 'with connection' = BEGIN ... COMMIT, or ROLLBACK if an error occurs
        with connection:
            # SQL: UPDATE accounts SET balance = balance - ? WHERE name = ?;
            connection.execute("UPDATE accounts SET balance = balance - ? WHERE name = ?", (amount, sender))
            # SQL: UPDATE accounts SET balance = balance + ? WHERE name = ?;
            connection.execute("UPDATE accounts SET balance = balance + ? WHERE name = ?", (amount, receiver))
        print(f"Transfer of {amount} from {sender} to {receiver}: SUCCESS")
    except sqlite3.IntegrityError as error:
        print(f"Transfer of {amount} from {sender} to {receiver}: FAILED ({error})")

show("Start          :")
transfer("Asha", "Ravi", 300)
show("After success  :")
transfer("Ravi", "Asha", 5000)            # Ravi cannot pay: CHECK fails, whole transfer undone
show("After failure  :")
print("Total money is still", connection.execute("SELECT SUM(balance) FROM accounts").fetchone()[0])

connection.close()
''',
  algorithm=["Create an accounts table with a CHECK on balance", "Write transfer() with two UPDATE statements", "Wrap them in 'with connection' so they form one transaction", "Run a valid transfer", "Run a transfer that violates the CHECK", "Show that the failed transfer changed nothing"],
  explanation="A transaction groups several SQL statements into one unit that follows all-or-nothing (atomicity). Using the connection as a context manager commits when the block ends normally and rolls back when an exception occurs. In the failed transfer the first UPDATE succeeds inside the transaction, the second makes the balance negative, SQLite raises IntegrityError and the first UPDATE is undone, so the total money never changes.",
  tags=["transaction", "atomic", "sqlite", "bank transfer"], topics=[DBT]),

P(title="Demonstrate Commit and Rollback", category=DB, difficulty="Intermediate",
  description="Shows that commit() saves changes permanently while rollback() cancels uncommitted changes.",
  concepts=["commit", "rollback", "in_transaction"], filename="sqlite_commit_rollback.py",
  code=r'''
import os
import sqlite3

DB_FILE = "commit_demo.db"
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
cursor.execute("CREATE TABLE items (id INTEGER PRIMARY KEY, name TEXT)")
connection.commit()

def count_with_new_connection():
    """Another connection only sees data that was really committed."""
    other = sqlite3.connect(DB_FILE)
    total = other.execute("SELECT COUNT(*) FROM items").fetchone()[0]
    other.close()
    return total

# 1. COMMIT
# SQL: INSERT INTO items (name) VALUES (?);
cursor.execute("INSERT INTO items (name) VALUES (?)", ("Pen",))
print("Inserted Pen, not yet committed")
print("  In a transaction      :", connection.in_transaction)
print("  Rows seen by others   :", count_with_new_connection())
connection.commit()
print("After commit() -> rows seen by others:", count_with_new_connection())

# 2. ROLLBACK
cursor.execute("INSERT INTO items (name) VALUES (?)", ("Book",))
cursor.execute("INSERT INTO items (name) VALUES (?)", ("Bag",))
print("\nInserted Book and Bag, rows seen by this connection:",
      cursor.execute("SELECT COUNT(*) FROM items").fetchone()[0])
connection.rollback()
print("After rollback() -> rows in table             :",
      cursor.execute("SELECT COUNT(*) FROM items").fetchone()[0])

print("\nFinal records:", cursor.execute("SELECT * FROM items").fetchall())

connection.close()
os.remove(DB_FILE)
''',
  algorithm=["Create a table in a file database and commit", "Insert a row and check that another connection cannot see it", "Call commit() and check that it is now visible", "Insert two more rows", "Call rollback() to cancel them", "Display the final table and delete the file"],
  explanation="Changes made with INSERT, UPDATE or DELETE are held in an open transaction until you decide. commit() writes them permanently so every connection can see them. rollback() throws away everything since the last commit. A second connection is used to prove that uncommitted data is invisible to others.",
  tags=["commit", "rollback", "sqlite", "transaction"], topics=[DBT]),
]
