import sys; sys.path.insert(0, __file__.rsplit("/", 2)[0])   # so `schema` imports
from schema import P

PROGRAMS = [
# 1
P(title="Print Hello World", category="Getting Started", difficulty="Beginner",
  description="The first Python program: print a greeting on the screen using print().",
  concepts=["print()", "string literal"], filename="hello_world.py",
  code=r'''
# The classic first program
print("Hello, World!")
print("Welcome to Python Programming - MCA 102 A")
''',
  algorithm=["Start the program", "Call print() with the text Hello, World!", "Call print() with a welcome line", "End the program"],
  explanation="print() is a built-in function that writes text to the screen. The text inside quotes is a string literal. Each print() call ends with a new line, so the two messages appear on separate lines. No input is needed; the output is the two lines of text.",
  tags=["hello", "print", "first program"], topics=["Introduction to Python"]),
# 2
P(title="Display Student Details", category="Getting Started", difficulty="Beginner",
  description="Store a student's details in variables and display them in a neat format.",
  concepts=["variables", "print()", "f-string"], filename="student_details.py",
  code=r'''
# Display student details using variables and f-strings
name = "Anita Sharma"
roll_no = 101
course = "MCA"
semester = 1
cgpa = 8.6

print("----- STUDENT DETAILS -----")
print(f"Name     : {name}")
print(f"Roll No  : {roll_no}")
print(f"Course   : {course}")
print(f"Semester : {semester}")
print(f"CGPA     : {cgpa}")
''',
  algorithm=["Create variables for name, roll number, course, semester and CGPA", "Print a heading", "Print each detail using an f-string", "End"],
  explanation="Each detail is stored in a variable of a suitable type (str, int, float). An f-string, written as f\"...\", lets us place variable values inside curly braces within the text. print() then shows each formatted line. The output is a small student profile.",
  tags=["student", "variables", "f-string", "details"], topics=["Introduction to Python", "Python Fundamentals"]),
# 3
P(title="Display College Details", category="Getting Started", difficulty="Beginner",
  description="Show college information stored in a dictionary.",
  concepts=["dict", "for loop", "print()"], filename="college_details.py",
  code=r'''
# Display college details stored in a dictionary
college = {
    "Name": "Sunrise Institute of Technology",
    "City": "Pune",
    "Established": 1998,
    "Department": "Master of Computer Applications",
    "Affiliation": "State Technical University",
}

print("===== COLLEGE DETAILS =====")
for field, value in college.items():
    print(f"{field:<12}: {value}")
''',
  algorithm=["Create a dictionary of college fields and values", "Print a heading", "Loop over the key-value pairs", "Print each pair aligned in columns"],
  explanation="A dictionary stores data as key-value pairs, which suits records like college details. The items() method gives each key with its value in a for loop. The format spec :<12 left-aligns the field name in 12 characters so the colons line up.",
  tags=["college", "dictionary", "loop"], topics=["Introduction to Python", "Python Fundamentals"]),
# 4
P(title="Display MCA Student Information (Interactive)", category="Getting Started", difficulty="Beginner",
  description="Read an MCA student's information from the keyboard and print a summary.",
  concepts=["input()", "int()", "try/except", "f-string"], filename="mca_student_info.py",
  code=r'''
# Read MCA student information from the user and display it
name = input("Enter student name: ").strip()
specialisation = input("Enter specialisation: ").strip()

try:
    year = int(input("Enter year of admission: "))
    semester = int(input("Enter current semester (1-4): "))
    if not 1 <= semester <= 4:
        raise ValueError("semester must be between 1 and 4")
except ValueError as error:
    print("Invalid input:", error)
else:
    print("\n--- MCA STUDENT INFORMATION ---")
    print(f"Name           : {name}")
    print(f"Programme      : MCA")
    print(f"Specialisation : {specialisation}")
    print(f"Admission Year : {year}")
    print(f"Semester       : {semester}")
''',
  algorithm=["Read name and specialisation as text", "Read admission year and semester and convert to int", "Validate that the semester is between 1 and 4", "If invalid, show an error message", "Otherwise print the information summary"],
  explanation="input() always returns a string, so numeric values are converted with int(). The try/except block catches wrong input such as letters, and the manual check raises ValueError for an out-of-range semester. The else block runs only when no error occurred and prints the formatted summary.",
  sample_input="Rahul Verma\nData Science\n2025\n1", tags=["input", "student", "validation"], kind="Interactive",
  topics=["Introduction to Python", "Python Fundamentals"]),
# 5
P(title="Basic Arithmetic Calculations", category="Fundamentals", difficulty="Beginner",
  description="Perform addition, subtraction, multiplication, division and more on two numbers.",
  concepts=["arithmetic operators", "input()", "float()", "try/except"], filename="basic_arithmetic.py",
  code=r'''
# Basic arithmetic on two numbers entered by the user
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
except ValueError:
    print("Please enter valid numbers.")
else:
    print(f"{a} + {b}  = {a + b}")
    print(f"{a} - {b}  = {a - b}")
    print(f"{a} * {b}  = {a * b}")
    if b != 0:
        print(f"{a} / {b}  = {a / b}")
        print(f"{a} // {b} = {a // b}   (floor division)")
        print(f"{a} % {b}  = {a % b}   (remainder)")
    else:
        print("Division by zero is not allowed.")
    print(f"{a} ** {b} = {a ** b}   (power)")
''',
  algorithm=["Read two numbers as float", "Print sum, difference and product", "If the second number is not zero print division, floor division and remainder", "Print a raised to the power b"],
  explanation="The operators +, -, *, /, //, % and ** perform the basic arithmetic operations. The program converts input to float so decimals are allowed and guards against division by zero. try/except handles non-numeric input.",
  sample_input="17\n5", tags=["arithmetic", "operators", "calculator"], kind="Interactive",
  topics=["Python Fundamentals"]),
# 6
P(title="Demonstrate Python Variables", category="Fundamentals", difficulty="Beginner",
  description="Show how variables are created, reassigned, multiply assigned and swapped.",
  concepts=["variables", "dynamic typing", "multiple assignment"], filename="python_variables.py",
  code=r'''
# Variables in Python: no declaration needed, type comes from the value
age = 21
name = "Meera"
height = 5.4
print(name, age, height)

# Dynamic typing: the same name can refer to a different type later
age = "twenty-one"
print("age is now:", age, "->", type(age))

# Multiple assignment
x, y, z = 1, 2, 3
print("x, y, z =", x, y, z)

# Same value to many variables
p = q = r = 100
print("p, q, r =", p, q, r)

# Swapping two variables without a temporary variable
x, y = y, x
print("after swap: x =", x, ", y =", y)

# Naming rules: letters, digits, underscore; cannot start with a digit
student_count = 40
_private_value = 7
print(student_count, _private_value)

# Constants are written in UPPER CASE by convention
PI = 3.14159
print("PI =", PI)
''',
  algorithm=["Create variables of different types", "Reassign a variable to a new type", "Use multiple assignment and chained assignment", "Swap two variables", "Show naming conventions and constants"],
  explanation="A Python variable is a name that refers to an object; no type declaration is needed. Assigning a new value can change the type, which is called dynamic typing. Tuple-style assignment lets us assign several variables at once and swap values in one line. Constants are only a naming convention in UPPER CASE.",
  tags=["variable", "assignment", "dynamic typing"], topics=["Python Fundamentals"]),
# 7
P(title="Demonstrate Python Data Types", category="Fundamentals", difficulty="Beginner",
  description="Create a value of each built-in data type and display its type.",
  concepts=["int", "float", "str", "list", "tuple", "dict", "set", "bool", "type()"], filename="python_data_types.py",
  code=r'''
# Demonstrate the built-in data types
values = [
    42,                      # int
    3.14,                    # float
    2 + 3j,                  # complex
    "Python",                # str
    True,                    # bool
    [1, 2, 3],               # list (mutable)
    (1, 2, 3),               # tuple (immutable)
    {"a": 1, "b": 2},        # dict
    {1, 2, 3},               # set
    frozenset({1, 2}),       # frozenset
    b"bytes",                # bytes
    range(5),                # range
    None,                    # NoneType
]

for value in values:
    print(f"{value!r:<22} -> {type(value).__name__}")

# isinstance() checks the type
print("isinstance(42, int):", isinstance(42, int))
# Type conversion
print("int('15') + 5 =", int("15") + 5)
print("str(99) + '!' =", str(99) + "!")
''',
  algorithm=["Build a list containing one value of each data type", "Loop through the list", "Print each value with its type name using type()", "Show isinstance() and simple type conversion"],
  explanation="Python has numeric (int, float, complex), text (str), boolean, sequence (list, tuple, range), mapping (dict), set and binary types. type() returns the class of a value and __name__ gives a readable name. isinstance() tests the type, and int()/str() convert between types.",
  tags=["data types", "type", "int", "list"], topics=["Python Fundamentals"]),
# 8
P(title="Demonstrate Python Comments", category="Components of a Program", difficulty="Beginner",
  description="Show single-line comments, inline comments, multi-line comments and docstrings.",
  concepts=["# comment", "docstring", "__doc__"], filename="python_comments.py",
  code=r'''
# This is a single-line comment
print("Line 1")   # This is an inline comment

# Python has no special multi-line comment syntax.
# Several single-line comments are used instead.

"""
A string that is not assigned to anything is ignored,
so it is sometimes used as a multi-line comment.
"""

def area_of_square(side):
    """Return the area of a square (this is a docstring)."""
    return side * side

print("Area:", area_of_square(4))

# Docstrings are stored and can be read at run time
print("Docstring:", area_of_square.__doc__)

# print("This line is commented out, so it will not run")
print("Comments are ignored by the interpreter.")
''',
  algorithm=["Write single-line and inline comments", "Write consecutive comment lines as a multi-line comment", "Define a function with a docstring", "Read the docstring through __doc__", "Comment out a line of code to disable it"],
  explanation="A comment starts with # and runs to the end of the line; Python ignores it. There is no real block-comment syntax, so we use several # lines or a bare string. A docstring is the first string in a function, class or module and is kept in __doc__, which is why it differs from an ordinary comment.",
  tags=["comment", "docstring", "hash"], topics=["Components of a Python Program"]),
# 9
P(title="Demonstrate Multiple Statements", category="Components of a Program", difficulty="Beginner",
  description="Write several statements on one line with semicolons and split one statement over lines.",
  concepts=["semicolon", "line continuation", "statements"], filename="multiple_statements.py",
  code=r'''
# Several statements on ONE line separated by semicolons
a = 10; b = 20; c = a + b
print("a, b, c =", a, b, c)

# One statement over MANY lines using a backslash
total = a + \
        b + \
        c
print("total =", total)

# Brackets allow a statement to continue without a backslash
numbers = [
    1, 2, 3,
    4, 5, 6,
]
print("numbers =", numbers)

message = ("Python allows long statements "
           "to be split inside parentheses.")
print(message)

# A compound statement on a single line
for i in range(3): print("i =", i)
''',
  algorithm=["Put three assignments on one line using semicolons", "Split an expression with a backslash", "Split a list and a string inside brackets", "Write a one-line for loop"],
  explanation="Normally one line holds one statement, but a semicolon lets us write several statements on a line. A long statement can continue on the next line with a backslash or inside (), [] or {}. Semicolons are rarely used because separate lines are easier to read.",
  tags=["statements", "semicolon", "line continuation"], topics=["Components of a Python Program"]),
# 10
P(title="Demonstrate Python Indentation", category="Components of a Program", difficulty="Beginner",
  description="Show how indentation defines blocks in if, for and function bodies.",
  concepts=["indentation", "blocks", "if", "for"], filename="python_indentation.py",
  code=r'''
# Python uses indentation (4 spaces by convention) to define blocks
marks = 72

if marks >= 40:
    print("Result: Pass")
    if marks >= 60:
        print("Class: First Class")
    else:
        print("Class: Second Class")
else:
    print("Result: Fail")

print("This line is outside the if block")

for number in range(1, 4):
    square = number ** 2
    print(f"Square of {number} is {square}")
print("Loop finished")

def greet(person):
    message = "Hello, " + person
    return message

print(greet("Student"))

# Wrong indentation raises IndentationError. We can demonstrate it safely:
bad_code = "if True:\nprint('no indent')"
try:
    compile(bad_code, "<demo>", "exec")
except IndentationError as error:
    print("IndentationError caught:", error.msg)
''',
  algorithm=["Write an if/else with nested if using consistent indentation", "Show a statement outside the block", "Write a for loop and a function body with indentation", "Compile badly indented code to show IndentationError"],
  explanation="Unlike languages that use braces, Python groups statements by indentation. Every line in a block must have the same indentation, normally four spaces. Dedenting ends the block. The last part compiles faulty code inside try/except to show the IndentationError without crashing the program.",
  tags=["indentation", "block", "if else"], topics=["Components of a Python Program"]),
# 11
P(title="Demonstrate Python Functions", category="Components of a Program", difficulty="Beginner",
  description="Define and call functions with parameters, default values and return values.",
  concepts=["def", "return", "default argument", "*args"], filename="python_functions.py",
  code=r'''
# A function without parameters
def say_hello():
    print("Hello from a function!")

# A function with parameters and a return value
def add(a, b):
    return a + b

# A function with a default argument
def power(base, exponent=2):
    return base ** exponent

# A function with variable number of arguments
def total_of(*numbers):
    return sum(numbers)

# A function returning multiple values (as a tuple)
def min_max(values):
    return min(values), max(values)

say_hello()
print("add(3, 4)       =", add(3, 4))
print("power(5)        =", power(5))
print("power(2, 10)    =", power(2, 10))
print("power(exponent=3, base=2) =", power(exponent=3, base=2))
print("total_of(1,2,3,4) =", total_of(1, 2, 3, 4))
lowest, highest = min_max([7, 2, 9, 4])
print("min, max        =", lowest, highest)
''',
  algorithm=["Define functions using def", "Add parameters, a default value and *args", "Return values using return", "Call each function and print the result"],
  explanation="A function is a reusable block defined with def. Parameters receive values, default arguments make parameters optional, and *args collects any number of positional arguments. return sends a result back; returning several values gives a tuple that can be unpacked. Keyword arguments let us pass values by name.",
  tags=["function", "def", "return", "arguments"], topics=["Components of a Python Program"]),
# 12
P(title="Demonstrate Python Modules", category="Components of a Program", difficulty="Beginner",
  description="Import standard modules in different ways and use their functions.",
  concepts=["import", "from ... import", "alias", "dir()"], filename="python_modules.py",
  code=r'''
# A module is a file of Python code that can be imported
import math
from random import seed, randint
import datetime as dt
from statistics import mean

print("math.sqrt(49)  =", math.sqrt(49))
print("math.pi        =", round(math.pi, 4))
print("math.factorial(5) =", math.factorial(5))

seed(1)                      # fixed seed gives repeatable output
print("randint(1, 6)  =", randint(1, 6))

print("fixed date     =", dt.date(2025, 7, 1).strftime("%d %B %Y"))
print("mean([2,4,6])  =", mean([2, 4, 6]))

# Find out what a module contains
print("Some names in math:", [n for n in dir(math) if not n.startswith("_")][:6])
print("Module name:", math.__name__)

# Creating our own module: this very file is a module too.
print("This file's __name__ is:", __name__)
''',
  algorithm=["Import whole modules with import", "Import specific names with from ... import", "Give a module an alias with as", "Call functions from the modules", "List module contents using dir()"],
  explanation="A module is a .py file whose functions and variables can be reused by importing it. import math gives access as math.sqrt(); from random import randint imports a single name; 'as' creates a short alias. dir() lists the names inside a module. Running a file directly sets its __name__ to __main__.",
  tags=["module", "import", "math", "random"], topics=["Components of a Python Program"]),
# 13
P(title="Demonstrate Python Features", category="Introduction", difficulty="Beginner",
  description="Small examples of key Python features: simplicity, dynamic typing, interpreted, OOP, and rich libraries.",
  concepts=["dynamic typing", "OOP", "list comprehension", "standard library"], filename="python_features.py",
  code=r'''
import sys

# 1. Simple and readable syntax
print("1. Simple syntax: sum =", sum([1, 2, 3]))

# 2. Dynamically typed
value = 10
value = "ten"
print("2. Dynamic typing:", value, type(value).__name__)

# 3. Interpreted: code runs line by line, no separate compile step by the user
print("3. Interpreted: running under", sys.implementation.name)

# 4. Object oriented
class Student:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return "Hi, I am " + self.name

print("4. Object oriented:", Student("Neha").greet())

# 5. Multiple paradigms: functional style
squares = list(map(lambda n: n * n, range(1, 6)))
print("5. Functional style:", squares)

# 6. Powerful built-in data structures and comprehensions
evens = [n for n in range(10) if n % 2 == 0]
print("6. Comprehension:", evens)

# 7. Large standard library
import json
print("7. Standard library (json):", json.dumps({"language": "Python"}))

# 8. Portable and free: same code runs on Windows, Linux and macOS
print("8. Platform independent: running on", sys.platform)

# 9. Automatic memory management
print("9. Garbage collected: no manual free() needed")

# 10. Extensible with third-party packages (pip install pandas, numpy ...)
print("10. Extensible: thousands of packages on PyPI")
''',
  algorithm=["Show readable syntax with a simple call", "Show dynamic typing", "Show a class (object orientation)", "Show functional style and comprehension", "Use the standard library", "Print platform information to show portability"],
  explanation="Python is simple, interpreted, dynamically typed, object oriented and portable, with a big standard library and automatic memory management. Each numbered line demonstrates one feature with a tiny example. The output labels each feature so students can match it with the theory.",
  tags=["features", "dynamic typing", "oop", "portable"], topics=["Introduction to Python", "Features of Python"]),
# 14
P(title="Demonstrate Python Memory Concepts", category="Memory Management", difficulty="Intermediate",
  description="Explore object identity, size in memory, small-integer caching and mutable versus immutable objects.",
  concepts=["id()", "sys.getsizeof()", "is vs ==", "mutable/immutable"], filename="memory_concepts.py",
  code=r'''
import sys

# Every object lives in the private heap managed by Python
# id() gives the identity of an object (its address in CPython)
a = 256
b = 256
print("a is b (256)       :", a is b, "- small integers are cached and shared")

x = [1, 2, 3]
y = [1, 2, 3]
print("x == y             :", x == y, "(equal values)")
print("x is y             :", x is y, "(different objects)")

# Size of objects in bytes
print("size of int 0      :", sys.getsizeof(0), "bytes")
print("size of 'a'        :", sys.getsizeof("a"), "bytes")
print("size of []         :", sys.getsizeof([]), "bytes")
print("size of [1,2,3]    :", sys.getsizeof([1, 2, 3]), "bytes")

# Immutable object: a new object is created on change
number = 10
old_id = id(number)
number += 1
print("int changed, same id?  ", id(number) == old_id)

# Mutable object: modified in place
items = [1, 2]
old_id = id(items)
items.append(3)
print("list changed, same id? ", id(items) == old_id)

# Memory grows as a list grows (over-allocation)
data = []
previous = sys.getsizeof(data)
print("\nList growth (size changes only at certain lengths):")
for count in range(1, 11):
    data.append(count)
    current = sys.getsizeof(data)
    if current != previous:
        print(f"  length {count:2d} -> {current} bytes")
        previous = current
''',
  algorithm=["Compare cached small integers using is", "Compare equal but separate lists using == and is", "Measure object sizes with sys.getsizeof()", "Show that immutable objects get a new id when changed", "Show that mutable objects keep the same id", "Watch a list's allocated size grow"],
  explanation="CPython keeps all objects in a private heap and the memory manager allocates space automatically. id() identifies an object, 'is' compares identity while == compares values, and sys.getsizeof() reports the bytes used. Immutable objects such as int are replaced when changed, while a list is modified in place and over-allocates memory as it grows.",
  tags=["memory", "id", "getsizeof", "mutable"], topics=["Memory Management in Python"]),
# 15
P(title="Demonstrate Object References", category="Memory Management", difficulty="Intermediate",
  description="Show that variables are references to objects, and the difference between aliasing and copying.",
  concepts=["references", "aliasing", "copy", "deepcopy"], filename="object_references.py",
  code=r'''
import copy

# A variable is a name (reference) that points to an object
original = [1, 2, [3, 4]]
alias = original                 # another name for the SAME object
print("id(original) == id(alias):", id(original) == id(alias))

alias.append(5)
print("original after alias.append(5):", original)

# Shallow copy: new outer list, but inner objects are shared
shallow = copy.copy(original)
shallow[2].append(99)
print("\noriginal after shallow[2].append(99):", original)
print("shallow is original            :", shallow is original)
print("shallow[2] is original[2]      :", shallow[2] is original[2])

# Deep copy: everything is copied
deep = copy.deepcopy(original)
deep[2].append(1000)
print("\noriginal after deep[2].append(1000):", original)
print("deep[2]                            :", deep[2])

# Immutable objects: rebinding creates a new reference
s1 = "hello"
s2 = s1
s1 = s1 + " world"
print("\ns1 =", s1, "| s2 =", s2)

# Passing a mutable object to a function passes the reference
def add_item(collection):
    collection.append("new")

names = ["a", "b"]
add_item(names)
print("names after function call:", names)
''',
  algorithm=["Create a list and a second name referring to the same list", "Modify through the alias and observe the original", "Make a shallow copy and show shared inner objects", "Make a deep copy and show full independence", "Show immutable rebinding and passing references to functions"],
  explanation="In Python, assignment never copies the object; it binds another name to it. So changing a mutable list through an alias changes the original. copy.copy() makes a shallow copy that still shares inner objects, whereas copy.deepcopy() copies everything. Functions also receive references, so a mutable argument can be changed inside them.",
  tags=["reference", "alias", "copy", "deepcopy"], topics=["Memory Management in Python"]),
# 16
P(title="Demonstrate Garbage Collection Using the gc Module", category="Memory Management", difficulty="Intermediate",
  description="Create a reference cycle, delete it and let the gc module collect it.",
  concepts=["gc.collect()", "reference cycle", "__del__", "weakref"], filename="garbage_collection_gc.py",
  code=r'''
import gc
import weakref

class Node:
    """A simple node that can point to another node."""
    def __init__(self, name):
        self.name = name
        self.partner = None

    def __del__(self):
        print(f"  Node {self.name} is being destroyed")

print("GC enabled         :", gc.isenabled())
print("GC thresholds      :", gc.get_threshold())

# Reference counting frees objects immediately
print("\n1. Simple object, freed by reference counting:")
temp = Node("temp")
del temp

# Reference cycle: a and b point to each other
print("\n2. Reference cycle (reference count never reaches zero):")
gc.collect()                     # clean start
a = Node("A")
b = Node("B")
a.partner = b
b.partner = a
watcher = weakref.ref(a)         # weak reference does not keep object alive
del a, b
print("  After del, object still alive?", watcher() is not None)

collected = gc.collect()         # the cyclic garbage collector runs
print("  gc.collect() found unreachable objects:", collected > 0)
print("  After gc.collect(), object alive?", watcher() is not None)

print("\nGC counts per generation:", len(gc.get_count()), "generations")
''',
  algorithm=["Show that the garbage collector is enabled and its thresholds", "Delete a simple object and see __del__ run at once", "Create two objects pointing to each other and delete the names", "Observe the cycle is still alive using a weak reference", "Call gc.collect() to free the cycle"],
  explanation="CPython frees most objects immediately when their reference count falls to zero. Objects in a reference cycle keep each other alive, so the cyclic garbage collector in the gc module must find them. gc.collect() forces a collection and returns the number of unreachable objects found. A weakref lets us check if an object is still alive without keeping it alive.",
  tags=["gc", "garbage collection", "cycle", "weakref"], topics=["Garbage Collection in Python", "Memory Management in Python"]),
# 17
P(title="Check Python Version (Windows Commands and Python Check)", category="Installation", difficulty="Beginner",
  description="Windows commands to check the installed Python version, plus the same check in Python code.",
  concepts=["py --version", "sys.version_info", "platform"], filename="check_python_version.py",
  code=r'''
# ---------------------------------------------------------------
# TERMINAL COMMANDS (type these in Command Prompt / PowerShell, not in Python)
# ---------------------------------------------------------------
# TERMINAL: python --version        -> shows the version, e.g. Python 3.13.0
# TERMINAL: python -V               -> same as above
# TERMINAL: py --version            -> Windows Python Launcher, default version
# TERMINAL: py -0                   -> list all Python versions installed
# TERMINAL: py -3.13 --version      -> check one specific version
# ---------------------------------------------------------------
# PYTHON SOURCE CODE below: the same check done from inside Python
# ---------------------------------------------------------------
import sys
import platform

print("Python version (short):", platform.python_version())
print("Python version (full) :", sys.version.split()[0])
print("version_info          :", sys.version_info.major, sys.version_info.minor, sys.version_info.micro)
print("Implementation        :", platform.python_implementation())

if sys.version_info >= (3, 8):
    print("This Python is new enough for the course (3.8 or later).")
else:
    print("Please upgrade Python to 3.8 or later.")
''',
  algorithm=["List the terminal commands that report the version (as comments)", "Import sys and platform", "Print the version string and version_info numbers", "Compare version_info with (3, 8) and print a message"],
  explanation="The commented TERMINAL lines are Windows commands typed in Command Prompt; the rest is real Python code. platform.python_version() and sys.version_info give the same information from inside a program. sys.version_info is a tuple-like object so it can be compared directly with (3, 8).",
  tags=["version", "python --version", "windows", "sys"], kind="Terminal Commands", topics=["Installing Python for Windows"]),
# 18
P(title="Display Python Installation Information", category="Installation", difficulty="Beginner",
  description="Steps and commands for installing Python on Windows, and a script that shows where this Python is installed.",
  concepts=["sys.prefix", "platform", "Windows installer"], filename="python_installation_info.py",
  code=r'''
# ---------------------------------------------------------------
# INSTALLING PYTHON ON WINDOWS - steps
# 1. Download the installer from https://www.python.org/downloads/windows/
# 2. Run the installer and TICK "Add python.exe to PATH" (very important)
# 3. Click "Install Now" and wait for "Setup was successful"
# 4. Open a NEW Command Prompt and verify with the commands below
#
# TERMINAL: python --version
# TERMINAL: py --version
# TERMINAL: pip --version
# TERMINAL: py -m ensurepip --upgrade        (only if pip is missing)
# TERMINAL: py -m pip install --upgrade pip  (update pip)
# Silent install (optional, for IT staff):
# TERMINAL: python-3.13.0-amd64.exe /quiet InstallAllUsers=1 PrependPath=1
# ---------------------------------------------------------------
import sys
import platform

print("=== Python Installation Information ===")
print("Version          :", platform.python_version())
print("Implementation   :", platform.python_implementation())
print("Compiler         :", platform.python_compiler())
print("Build            :", platform.python_build()[0])
print("Install prefix   :", sys.prefix)
print("Base prefix      :", sys.base_prefix)
print("Operating system :", platform.system())
print("Architecture     :", platform.machine(), "/", platform.architecture()[0])
print("Byte order       :", sys.byteorder)
print("Max int size info:", sys.int_info.bits_per_digit, "bits per digit")
''',
  algorithm=["Document the Windows installation steps and commands as comments", "Import sys and platform", "Print version, implementation and compiler", "Print the install prefix and base prefix", "Print operating system and architecture"],
  explanation="The comments list how to install Python on Windows and which commands verify it; they must be typed in a terminal and are marked TERMINAL. The Python code then reads the installation details from the sys and platform modules. sys.prefix is the folder where this Python (or its virtual environment) is installed.",
  tags=["install", "windows", "python installation", "sys.prefix"], kind="Terminal Commands", topics=["Installing Python for Windows"]),
# 19
P(title="Check the Python Executable Path", category="Installation", difficulty="Beginner",
  description="Windows PATH-checking commands and a script that prints the interpreter path and PATH entries.",
  concepts=["sys.executable", "PATH", "shutil.which"], filename="check_python_path.py",
  code=r'''
# ---------------------------------------------------------------
# VERIFYING THE PATH TO PYTHON ON WINDOWS
# TERMINAL: where python                       -> full path(s) of python.exe found on PATH
# TERMINAL: where py
# TERMINAL: echo %PATH%                        -> Command Prompt: show PATH variable
# TERMINAL: $env:Path -split ";"               -> PowerShell: one entry per line
# TERMINAL: python -c "import sys; print(sys.executable)"
# If 'python' is not recognised, add the Python folder and its Scripts folder
# to PATH:  Settings > System > About > Advanced system settings >
#           Environment Variables > Path > Edit > New
# ---------------------------------------------------------------
import os
import shutil
import sys

print("sys.executable      :", sys.executable)
print("Folder of python    :", os.path.dirname(sys.executable))

found = shutil.which("python") or shutil.which("python3")
print("Found on PATH       :", found if found else "python not found on PATH")

folder = os.path.dirname(sys.executable)
path_entries = os.environ.get("PATH", "").split(os.pathsep)
print("Python folder in PATH:", folder in path_entries)
print("Number of PATH entries:", len(path_entries))

print("\nFirst 3 PATH entries:")
for entry in path_entries[:3]:
    print("  ", entry)
''',
  algorithm=["List the Windows commands for checking the PATH (as comments)", "Print sys.executable and its folder", "Use shutil.which() to search for python on PATH", "Split the PATH variable and check whether the Python folder is present", "Print a few PATH entries"],
  explanation="sys.executable gives the full path of the running interpreter. shutil.which() searches the PATH like the 'where' command on Windows. The PATH environment variable is a list of folders separated by os.pathsep, so we split it and check whether Python's folder is in it. If not, the user should add it as described in the comments.",
  tags=["path", "executable", "where python", "environment"], kind="Terminal Commands", topics=["Verifying the Path to Python"]),
# 20
P(title="Display Python Environment Information", category="Installation", difficulty="Intermediate",
  description="Show platform, virtual-environment status, module search path and selected environment variables.",
  concepts=["sys.path", "venv", "os.environ", "platform"], filename="python_environment_info.py",
  code=r'''
# ---------------------------------------------------------------
# VIRTUAL ENVIRONMENT COMMANDS (Windows)
# TERMINAL: python -m venv myenv              -> create environment
# TERMINAL: myenv\Scripts\activate            -> activate (Command Prompt)
# TERMINAL: myenv\Scripts\Activate.ps1        -> activate (PowerShell)
# TERMINAL: deactivate                        -> leave the environment
# TERMINAL: python -m site                    -> show site information
# ---------------------------------------------------------------
import os
import platform
import sys
import site

print("=== Python Environment Information ===")
print("OS               :", platform.platform())
print("Python           :", platform.python_version())
print("Executable       :", sys.executable)

in_venv = sys.prefix != sys.base_prefix
print("Virtual env?     :", "Yes" if in_venv else "No (system Python)")

print("Default encoding :", sys.getdefaultencoding())
print("File system enc. :", sys.getfilesystemencoding())
print("Current folder   :", os.path.basename(os.getcwd()) or os.getcwd())
print("CPU count        :", os.cpu_count() is not None)

print("\nModule search path (sys.path), first 4 entries:")
for entry in sys.path[:4]:
    print("  ", entry if entry else "(current directory)")

print("\nUser site enabled:", site.ENABLE_USER_SITE)
print("Loaded modules   :", len(sys.modules) > 10)
print("Environment variables set:", len(os.environ) > 0)
''',
  algorithm=["List virtual environment commands as comments", "Print OS and Python details", "Compare sys.prefix with sys.base_prefix to detect a virtual environment", "Print encodings and module search path", "Print a few environment flags"],
  explanation="This program summarises the environment a Python program runs in. A virtual environment is detected when sys.prefix differs from sys.base_prefix. sys.path is the list of folders Python searches when importing, and the encodings show how text is handled. The comment block shows the Windows commands to create and activate a venv.",
  tags=["environment", "venv", "sys.path", "platform"], kind="Terminal Commands", topics=["Installing Python for Windows", "Verifying the Path to Python"]),
# 21
P(title="Import and Verify pandas", category="pandas Setup", difficulty="Beginner",
  description="Install pandas with pip on Windows and verify the import with error handling.",
  concepts=["pip install", "import", "ImportError", "importlib"], filename="import_verify_pandas.py",
  deps=["pandas"],
  code=r'''
# Requires: pip install pandas
# ---------------------------------------------------------------
# INSTALLING pandas ON WINDOWS
# TERMINAL: python -m pip install pandas
# TERMINAL: py -m pip install pandas
# TERMINAL: pip install pandas
# TERMINAL: python -m pip install --upgrade pandas      (upgrade)
# TERMINAL: python -m pip install pandas==2.2.2         (specific version)
# ---------------------------------------------------------------
import importlib.util

# Check whether the package can be found without importing it
spec = importlib.util.find_spec("pandas")
print("pandas found by Python:", spec is not None)

try:
    import pandas as pd
except ImportError:
    print("pandas is NOT installed. Run: python -m pip install pandas")
else:
    print("pandas imported successfully as pd")
    print("Module name   :", pd.__name__)
    print("Has DataFrame :", hasattr(pd, "DataFrame"))
    print("Has Series    :", hasattr(pd, "Series"))
''',
  algorithm=["Document the pip install commands as comments", "Check the package with importlib.util.find_spec()", "Try to import pandas inside try/except", "On success print confirmation and check for DataFrame and Series", "On ImportError print the install command"],
  explanation="pandas is installed from the terminal with python -m pip install pandas. In the script, find_spec() checks whether Python can locate the package, and try/except ImportError handles a missing installation. hasattr() confirms that the main classes exist, so the import really worked.",
  tags=["pandas", "import", "pip install", "verify"], kind="Terminal Commands", topics=["Installing pandas"]),
# 22
P(title="Display pandas Version", category="pandas Setup", difficulty="Beginner",
  description="Print the installed pandas version and the interpreter that uses it.",
  concepts=["pandas.__version__", "importlib.metadata"], filename="pandas_version.py",
  deps=["pandas"],
  code=r'''
# Requires: pip install pandas
# TERMINAL: python -c "import pandas; print(pandas.__version__)"
# TERMINAL: python -m pip show pandas
import sys
from importlib import metadata

try:
    import pandas as pd
except ImportError:
    print("pandas is not installed. Run: python -m pip install pandas")
else:
    print("pandas version (pd.__version__)  :", pd.__version__)
    print("pandas version (importlib.metadata):", metadata.version("pandas"))
    print("Python used                      :", sys.version.split()[0])

    major = int(pd.__version__.split(".")[0])
    print("Major version number             :", major)
    print("Version 1 or newer?              :", major >= 1)
''',
  algorithm=["Show terminal commands for version checking as comments", "Try to import pandas", "Print pd.__version__", "Print the same version using importlib.metadata", "Extract the major version number and compare"],
  explanation="Most packages store their version in the __version__ attribute. importlib.metadata reads the version recorded by pip, so both should agree. Splitting the version string at dots lets us read the major number and compare it. If pandas is missing, the program shows the install command instead of crashing.",
  tags=["pandas", "version", "__version__"], kind="Terminal Commands", topics=["Installing pandas", "Verifying Installed Packages"]),
# 23
P(title="Create a Basic pandas Series", category="pandas Setup", difficulty="Beginner",
  description="Create a one-dimensional pandas Series from a list and with a custom index.",
  concepts=["pd.Series", "index", "values", "dtype"], filename="pandas_series_basic.py",
  deps=["pandas"],
  code=r'''
# Requires: pip install pandas
import pandas as pd

# Series from a list (default index 0, 1, 2 ...)
marks = pd.Series([78, 85, 92, 66])
print("Series with default index:")
print(marks)

# Series with a custom index
subjects = pd.Series([78, 85, 92, 66],
                     index=["Python", "DBMS", "Maths", "OS"],
                     name="Marks")
print("\nSeries with custom index:")
print(subjects)

print("\nValue of Python :", subjects["Python"])
print("Data type       :", subjects.dtype)
print("Highest mark    :", subjects.max())
print("Average mark    :", subjects.mean())
print("Marks above 80  :")
print(subjects[subjects > 80])
''',
  algorithm=["Import pandas as pd", "Create a Series from a list", "Create a Series with a custom index and a name", "Access an item by label", "Use max(), mean() and a boolean filter"],
  explanation="A Series is a one-dimensional labelled array. Without an index pandas numbers the items from 0; a custom index lets us look up values by label such as subjects[\"Python\"]. Series have built-in statistics like max() and mean(), and a condition such as subjects > 80 filters the values.",
  tags=["pandas", "series", "index"], topics=["Installing pandas"]),
# 24
P(title="Create a Basic pandas DataFrame", category="pandas Setup", difficulty="Beginner",
  description="Create a two-dimensional DataFrame from a dictionary and explore it.",
  concepts=["pd.DataFrame", "columns", "head()", "shape"], filename="pandas_dataframe_basic.py",
  deps=["pandas"],
  code=r'''
# Requires: pip install pandas
import pandas as pd

students = {
    "Name": ["Anita", "Rahul", "Meera", "Karan"],
    "Course": ["MCA", "MCA", "MCA", "MCA"],
    "Marks": [88, 74, 91, 67],
}

df = pd.DataFrame(students)
print("DataFrame:")
print(df)

print("\nShape (rows, columns):", df.shape)
print("Column names         :", list(df.columns))
print("\nOnly the Name column:")
print(df["Name"])

print("\nStudents with Marks > 80:")
print(df[df["Marks"] > 80])

print("\nAverage marks:", df["Marks"].mean())
print("\nSummary statistics for Marks:")
print(df["Marks"].describe())
''',
  algorithm=["Create a dictionary of equal-length lists", "Build a DataFrame from the dictionary", "Print shape and column names", "Select one column and filter rows by a condition", "Calculate the mean and describe()"],
  explanation="A DataFrame is a table with rows and labelled columns; each dictionary key becomes a column. df.shape gives rows and columns, df[\"Name\"] selects a column and a condition inside df[...] filters rows. mean() and describe() give quick statistics about a column.",
  tags=["pandas", "dataframe", "table"], topics=["Installing pandas"]),
# 25
P(title="Package Installation Verification", category="Installation", difficulty="Intermediate",
  description="Verify installed packages with pip list/show/check commands and with Python code.",
  concepts=["pip list", "pip show", "importlib.metadata", "subprocess"], filename="package_installation_verification.py",
  deps=["pandas"],
  code=r'''
# Requires: pip install pandas
# ---------------------------------------------------------------
# VERIFYING INSTALLED PACKAGES - Windows terminal commands
# TERMINAL: python -m pip list                 -> all installed packages
# TERMINAL: python -m pip show pandas          -> details of one package
# TERMINAL: python -m pip freeze               -> name==version list
# TERMINAL: python -m pip check                -> check for broken dependencies
# TERMINAL: python -m pip list | findstr pandas
# ---------------------------------------------------------------
import subprocess
import sys
from importlib import metadata

# 1. Check a few packages using importlib.metadata
for package in ["pip", "pandas", "numpy", "some_missing_package"]:
    try:
        print(f"{package:<22} installed, version {metadata.version(package)}")
    except metadata.PackageNotFoundError:
        print(f"{package:<22} NOT installed")

# 2. Run 'pip show pandas' from Python and print selected lines
result = subprocess.run([sys.executable, "-m", "pip", "show", "pandas"],
                        capture_output=True, text=True)
if result.returncode == 0:
    print("\nOutput of: python -m pip show pandas")
    for line in result.stdout.splitlines():
        if line.startswith(("Name", "Summary", "Requires")):
            print("  ", line)
else:
    print("\npandas not found by pip. Install it with: python -m pip install pandas")

# 3. Count installed packages
print("\nTotal packages installed:", len(list(metadata.distributions())) > 0)
''',
  algorithm=["List the pip commands as comments", "Loop over package names and query importlib.metadata", "Catch PackageNotFoundError for missing packages", "Run pip show through subprocess and print selected lines", "Confirm that some distributions are installed"],
  explanation="pip list shows every installed package and pip show prints details of one. The Python code does the same with importlib.metadata.version(), which raises PackageNotFoundError if a package is absent. subprocess.run() runs the pip command from within Python using the same interpreter, and the output is filtered to a few useful lines.",
  tags=["pip list", "pip show", "verify", "packages"], kind="Terminal Commands", topics=["Verifying Installed Packages"]),
# 26 extra
P(title="Python Virtual Machine and Bytecode Using dis", category="Python Internals", difficulty="Intermediate",
  description="See how Python compiles source code to bytecode that the PVM executes.",
  concepts=["bytecode", "dis", "compile()", "PVM"], filename="pvm_bytecode_dis.py",
  code=r'''
import dis

# Python compiles source code to bytecode, then the PVM executes it.
# Source -> compiler -> bytecode (.pyc) -> Python Virtual Machine -> output

def add_and_double(a, b):
    total = a + b
    return total * 2

print("Bytecode of add_and_double():")
dis.dis(add_and_double)

# compile() turns source text into a code object
code_object = compile("x = 5\nprint(x * 3)", "<demo>", "exec")
print("\nCode object type   :", type(code_object).__name__)
print("Constants used     :", code_object.co_consts)
print("Variable names     :", code_object.co_names)
print("First bytes of code:", list(code_object.co_code[:6]))

print("\nExecuting the code object on the PVM:")
exec(code_object)
''',
  algorithm=["Define a small function", "Disassemble it with dis.dis() to see the bytecode instructions", "Compile a source string into a code object", "Inspect constants, names and raw bytecode", "Execute the code object with exec()"],
  explanation="The Python Virtual Machine (PVM) is the engine that runs bytecode, the low-level instructions produced when source code is compiled. dis.dis() prints those instructions in readable form, such as loading variables, adding and returning. compile() creates a code object and exec() hands it to the PVM to run.",
  tags=["pvm", "bytecode", "dis", "compile"], topics=["Python Virtual Machine (PVM)"]),
# 27 extra
P(title="Reference Counting with sys.getrefcount", category="Memory Management", difficulty="Intermediate",
  description="Watch an object's reference count rise and fall as names are added and removed.",
  concepts=["sys.getrefcount()", "del", "reference count"], filename="reference_counting.py",
  code=r'''
import sys

# getrefcount() shows how many references point to an object.
# The result is one higher than expected because the argument itself
# is a temporary extra reference.
data = [10, 20, 30]
print("Initial count          :", sys.getrefcount(data))

second_name = data
print("After second_name = data:", sys.getrefcount(data))

container = {"numbers": data}
print("After storing in a dict :", sys.getrefcount(data))

del second_name
print("After del second_name   :", sys.getrefcount(data))

container.clear()
print("After container.clear() :", sys.getrefcount(data))

print("\nId of data:", id(data) > 0)
print("When the count reaches 0, CPython frees the object immediately.")
''',
  algorithm=["Create a list", "Print its reference count", "Add references by assignment and by storing in a dict", "Remove references with del and clear()", "Print the count after each step"],
  explanation="CPython tracks how many references point to every object. sys.getrefcount() reports this number, always one more than expected because passing the object as an argument adds a temporary reference. The count goes up with each assignment or container storage and down with del or clear(); at zero the memory is freed.",
  tags=["reference count", "getrefcount", "memory", "del"], topics=["Memory Management in Python"]),
]
