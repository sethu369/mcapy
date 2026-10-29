import sys; sys.path.insert(0, __file__.rsplit("/", 2)[0])   # so `schema` imports
from schema import P


def Q(title, cat, diff, desc, concepts, fn, code, algo, expl, topics, tags, si="", kind="Demonstration"):
    return P(title=title, category=cat, difficulty=diff, description=desc, concepts=concepts,
             filename=fn, code=code, algorithm=algo, explanation=expl, sample_input=si,
             tags=tags, topics=topics, kind=kind)


DT = ["Data types in Python"]

PROGRAMS = [
Q("Display Integer Data Type", "Data Types", "Beginner",
  "Creates integers in decimal, binary, octal and hex form and shows their type.",
  ["int", "type()", "big integers"], "integer_data_type.py",
  r'''
# Integers in Python have unlimited size.
age = 25
negative = -40
big = 2 ** 100
binary = 0b1010      # binary literal = 10
octal = 0o17         # octal literal = 15
hexa = 0xFF          # hexadecimal literal = 255

for name, value in [("age", age), ("negative", negative), ("big", big),
                    ("binary", binary), ("octal", octal), ("hexa", hexa)]:
    print(f"{name:9} = {value}  -> {type(value)}")
''',
  ["Create integer variables using decimal, binary, octal and hex literals", "Create a very big integer with 2 ** 100", "Loop over the variables", "Print each value with its type"],
  "An int is a whole number with no fractional part. Python integers can be as large as memory allows, so 2 ** 100 works without overflow. Prefixes 0b, 0o and 0x write numbers in binary, octal and hexadecimal. The type() function reports <class 'int'> for each of them.",
  DT, ["int", "integer", "type", "whole number"]),

Q("Display Float Data Type", "Data Types", "Beginner",
  "Shows floating point numbers, scientific notation and rounding behaviour.",
  ["float", "scientific notation", "round()"], "float_data_type.py",
  r'''
price = 99.75
pi = 3.14159
small = 1.5e-4        # scientific notation = 0.00015
large = 2.5e6         # 2500000.0

print("price:", price, type(price))
print("small:", small)
print("large:", large)

# Floats are stored in binary, so some decimals are approximate.
print("0.1 + 0.2 =", 0.1 + 0.2)
print("rounded   =", round(0.1 + 0.2, 2))
print("10 / 4    =", 10 / 4, type(10 / 4))
''',
  ["Create floats using decimal point and e-notation", "Print them with their type", "Add 0.1 and 0.2 to show approximation", "Use round() to tidy the result"],
  "A float holds numbers with a fractional part and is stored as a 64-bit binary value. Because many decimals cannot be stored exactly, 0.1 + 0.2 gives 0.30000000000000004. The round() function fixes the display. Note that the / operator always returns a float.",
  DT, ["float", "decimal", "real number", "precision"]),

Q("Display Complex Data Type", "Data Types", "Beginner",
  "Creates complex numbers and reads their real and imaginary parts.",
  ["complex", "real", "imag", "conjugate()"], "complex_data_type.py",
  r'''
z1 = 3 + 4j
z2 = complex(1, -2)

print("z1 =", z1, type(z1))
print("z2 =", z2)
print("Real part of z1     :", z1.real)
print("Imaginary part of z1:", z1.imag)
print("Conjugate of z1     :", z1.conjugate())
print("Magnitude of z1     :", abs(z1))
print("z1 + z2 =", z1 + z2)
print("z1 * z2 =", z1 * z2)
''',
  ["Create complex numbers with j suffix and complex()", "Print type and the real/imag attributes", "Find conjugate and magnitude", "Add and multiply two complex numbers"],
  "A complex number has a real and an imaginary part and is written with the letter j, for example 3 + 4j. The attributes .real and .imag give each part, and abs() returns the magnitude (5.0 for 3+4j). Complex numbers support the normal arithmetic operators.",
  DT, ["complex", "imaginary", "j", "number"]),

Q("Demonstrate String Data Type", "Data Types", "Beginner",
  "Shows string creation with different quotes and common string properties.",
  ["str", "quotes", "len()", "immutability"], "string_data_type.py",
  r'''
single = 'Hello'
double = "Python's great"
multi = """This is a
multi-line string"""

print(single, type(single))
print(double)
print(multi)
print("Length of single:", len(single))
print("Upper:", single.upper())
print("Repeat:", single * 2)

# Strings are immutable: item assignment is an error.
try:
    single[0] = "J"
except TypeError as error:
    print("Error:", error)
''',
  ["Create strings with single, double and triple quotes", "Print type and length", "Apply upper() and repetition", "Try to modify a character and catch TypeError"],
  "A string (str) is a sequence of characters written in single, double or triple quotes. Triple quotes allow several lines. Strings are immutable, so you cannot change one character in place; Python raises a TypeError, which the program catches and prints.",
  DT, ["string", "str", "quotes", "text"]),

Q("Demonstrate Boolean Data Type", "Data Types", "Beginner",
  "Shows True/False values, comparison results and truthy/falsy values.",
  ["bool", "True/False", "bool()", "truthy"], "boolean_data_type.py",
  r'''
is_open = True
is_closed = False
print(is_open, type(is_open))
print("5 > 3 :", 5 > 3)
print("5 == 3:", 5 == 3)

# bool is a subclass of int: True is 1 and False is 0.
print("True + True =", True + True)

# Truthy and falsy values
for value in [0, 1, -5, 0.0, "", "text", [], [0], None]:
    print(f"bool({value!r}) = {bool(value)}")
''',
  ["Create True and False values", "Print comparison results", "Show that bool behaves like int", "Convert various values with bool()"],
  "The bool type has only two values, True and False, and is produced by comparisons. Internally True equals 1 and False equals 0. The bool() function tells whether a value is truthy or falsy: zero, empty containers, empty strings and None are False; almost everything else is True.",
  DT, ["bool", "boolean", "true", "false", "truthy"]),

Q("Demonstrate Type Conversion", "Data Types", "Beginner",
  "Converts values between int, float, str, list, tuple and set.",
  ["int()", "float()", "str()", "list()"], "type_conversion.py",
  r'''
print("int('42')      =", int("42"))
print("float('3.5')   =", float("3.5"))
print("str(100)       =", str(100), type(str(100)))
print("int(9.99)      =", int(9.99), "(decimal part is cut off)")
print("list('abc')    =", list("abc"))
print("tuple([1,2,3]) =", tuple([1, 2, 3]))
print("set([1,1,2])   =", set([1, 1, 2]))
print("bool(0)        =", bool(0))
print("chr(65), ord('A') =", chr(65), ord("A"))
''',
  ["Call conversion functions on sample values", "Print each result", "Note that int() truncates floats", "Convert between sequences and sets"],
  "Type conversion changes a value from one data type to another by calling the type as a function: int(), float(), str(), list(), tuple(), set() and bool(). Converting a float to int removes the decimal part, it does not round. chr() and ord() convert between characters and their numeric codes.",
  DT, ["conversion", "casting", "int", "float", "str"]),

Q("Demonstrate Implicit Type Conversion", "Data Types", "Beginner",
  "Shows Python automatically promoting int to float to complex in mixed expressions.",
  ["implicit conversion", "type promotion"], "implicit_type_conversion.py",
  r'''
whole = 10
decimal = 2.5
result = whole + decimal      # int is promoted to float automatically
print(result, type(result))

print(True + 5, type(True + 5))          # bool -> int
print(3 + (2 + 1j), type(3 + (2 + 1j)))  # int -> complex
print(7 / 2, type(7 / 2))                # true division gives float

# No implicit conversion between str and int:
try:
    print("Age: " + 25)
except TypeError as error:
    print("TypeError:", error)
''',
  ["Add an int and a float", "Observe the result type is float", "Mix bool, int and complex", "Show that str + int is not converted automatically"],
  "Implicit conversion is done automatically by Python to avoid losing information. The hierarchy is bool to int to float to complex, so a mixed expression gets the 'wider' type. Python never converts between text and numbers on its own, so adding a str and an int raises a TypeError.",
  DT, ["implicit", "coercion", "promotion", "conversion"]),

Q("Demonstrate Explicit Type Conversion", "Data Types", "Beginner",
  "Uses int(), float(), str() to convert values deliberately, including from user text.",
  ["explicit conversion", "int()", "float()", "str()"], "explicit_type_conversion.py",
  r'''
text_a = input("Enter first number : ")
text_b = input("Enter second number: ")

# input() always returns str, so convert explicitly.
try:
    a = float(text_a)
    b = float(text_b)
    print("Sum        =", a + b)
    print("As integer =", int(a + b))
    print("As text    =", "Total is " + str(a + b))
except ValueError:
    print("Please enter valid numbers.")
''',
  ["Read two strings with input()", "Convert them to float using float()", "Add them and convert the result to int and str", "Handle ValueError for bad input"],
  "Explicit conversion (type casting) is when the programmer calls a conversion function. Since input() returns a string, we must convert it with float() before doing arithmetic. str() converts the result back so it can be joined with other text. A try-except block handles non-numeric input.",
  DT, ["explicit", "casting", "input", "float"], si="12.5\n7", kind="Interactive"),

Q("Demonstrate the type() Function", "Data Types", "Beginner",
  "Prints the type of values of every common built-in kind.",
  ["type()", "built-in types"], "type_function.py",
  r'''
samples = [42, 3.14, 2 + 3j, "hi", True, None, [1, 2], (1, 2), {1, 2},
           {"a": 1}, range(3), b"bytes", print]

for item in samples:
    print(f"{item!s:>20}  ->  {type(item).__name__}")

# type() can be used to compare types
x = 10
print("type(x) == int:", type(x) == int)
print("type(x) is str:", type(x) is str)
''',
  ["Make a list of values of different kinds", "Loop over the list", "Print type(item).__name__", "Compare a type with int and str"],
  "The type() function returns the class of an object, such as int, str or list. Using .__name__ gives only the short name. Comparing type(x) with a class lets you test what kind of value a variable holds. Python variables have no fixed type; the type belongs to the value.",
  DT, ["type", "built-in", "class", "name"]),

Q("Demonstrate isinstance()", "Data Types", "Beginner",
  "Checks object types with isinstance(), including tuples of types and inheritance.",
  ["isinstance()", "type checking", "bool is int"], "isinstance_demo.py",
  r'''
value = 25
print(isinstance(value, int))               # True
print(isinstance(value, float))             # False
print(isinstance(value, (int, float)))      # True: any one of the types
print(isinstance("text", str))              # True

# bool is a subclass of int, so isinstance sees it as an int
print(isinstance(True, int))                # True
print(type(True) == int)                    # False

def describe(item):
    if isinstance(item, (int, float)):
        return "a number"
    if isinstance(item, (list, tuple)):
        return "a sequence of items"
    if isinstance(item, str):
        return "text"
    return "something else"

for thing in [5, 2.5, [1], (2,), "hey", None]:
    print(repr(thing), "is", describe(thing))
''',
  ["Call isinstance() with single types", "Pass a tuple of types", "Show that bool is a subclass of int", "Write describe() using isinstance and test it"],
  "isinstance(obj, type) returns True if obj is an instance of that type or of a subclass. A tuple of types checks several at once. It is preferred over type(x) == T because it respects inheritance, which is why isinstance(True, int) is True. The describe() function shows a typical use.",
  DT, ["isinstance", "type check", "subclass"]),

Q("Check Whether User Input Is an Integer", "Data Types", "Beginner",
  "Reads input and uses try-except with int() to decide whether it is an integer.",
  ["input()", "int()", "try-except", "ValueError"], "check_integer_input.py",
  r'''
user_text = input("Enter a value: ").strip()

try:
    number = int(user_text)       # raises ValueError if not an integer
    print(f"'{user_text}' is an integer. Value = {number}")
except ValueError:
    print(f"'{user_text}' is NOT an integer.")
''',
  ["Read the input as text and strip spaces", "Try to convert it with int()", "If conversion works, report an integer", "If ValueError occurs, report not an integer"],
  "Everything typed through input() is a string, so we cannot just check its type. Instead we try int(text). If the text looks like a whole number (for example 42 or -7) it works; otherwise Python raises ValueError and the except block reports the input is not an integer. Values like 3.5 or abc fail the test.",
  DT, ["integer", "validation", "try except", "int"], si="42", kind="Interactive"),

Q("Check Whether User Input Is a Float", "Data Types", "Beginner",
  "Tests input with float() and separates true decimals from whole numbers.",
  ["float()", "try-except", "is_integer()"], "check_float_input.py",
  r'''
user_text = input("Enter a value: ").strip()

try:
    number = float(user_text)
except ValueError:
    print(f"'{user_text}' is not a valid float.")
else:
    if "." in user_text or "e" in user_text.lower():
        print(f"'{user_text}' is a float. Value = {number}")
    else:
        print(f"'{user_text}' is a whole number, usable as float {number}")
''',
  ["Read input as text", "Try float(text)", "On ValueError print an error", "On success check for a decimal point or exponent", "Report float or whole number"],
  "float() accepts both whole numbers and decimals, so a successful conversion alone does not show the user typed a decimal. The program therefore also looks for a '.' or an exponent letter in the text. The try-except-else structure keeps the error handling separate from the normal path.",
  DT, ["float", "validation", "decimal", "try except"], si="3.75", kind="Interactive"),

Q("Check Whether User Input Is Numeric", "Data Types", "Intermediate",
  "Uses int() and float() attempts and isdigit() to classify input as integer, float or non-numeric.",
  ["isdigit()", "int()", "float()", "functions"], "check_numeric_input.py",
  r'''
def classify(text):
    """Return a description of what kind of number text is."""
    text = text.strip()
    try:
        int(text)
        return "an integer"
    except ValueError:
        pass
    try:
        float(text)
        return "a float"
    except ValueError:
        return "not numeric"

for _ in range(4):
    entry = input("Enter something: ")
    print(f"{entry!r} is {classify(entry)}")
    print("   str.isdigit() says:", entry.isdigit())
''',
  ["Define classify() with two try-except blocks", "First try int(), then float()", "Return the matching description", "Read four inputs and print the result", "Compare with str.isdigit()"],
  "A value is numeric if it can be converted by int() or float(). The function tries int first, then float, and otherwise reports non-numeric. The built-in isdigit() is shown for comparison: it fails for negative numbers and decimals, which is why try-except is more reliable.",
  DT, ["numeric", "isdigit", "validation", "input"], si="25\n-3.5\nhello\n1e3", kind="Interactive"),

Q("Demonstrate User-Defined Data Types Using Classes", "Data Types", "Intermediate",
  "Creates a Student class as a new data type and builds objects from it.",
  ["class", "__init__", "methods", "objects"], "user_defined_data_type.py",
  r'''
class Student:
    """A user-defined data type that groups related data."""

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def percentage(self):
        return sum(self.marks) / len(self.marks)

    def __str__(self):
        return f"Student({self.name}, Roll {self.roll_no})"


s1 = Student("Asha", 101, [80, 90, 85])
s2 = Student("Ravi", 102, [70, 65, 75])

print(s1, type(s1))
print("Average of", s1.name, "=", s1.percentage())
print("Average of", s2.name, "=", s2.percentage())
print("Is s1 a Student?", isinstance(s1, Student))
''',
  ["Define class Student with __init__ to store data", "Add percentage() method and __str__", "Create two Student objects", "Print them, call the method, check with isinstance"],
  "A class lets you define your own data type that bundles data (attributes) with behaviour (methods). __init__ runs when an object is created and sets its attributes. __str__ controls how the object prints. Each object such as s1 is an instance of the new type Student.",
  ["User-defined Data types", "Data types in Python"], ["class", "object", "user defined", "oop"]),

Q("Demonstrate Literals", "Data Types", "Beginner",
  "Shows numeric, string, boolean, special (None) and collection literals.",
  ["literals", "int", "str", "None"], "literals_demo.py",
  r'''
# Numeric literals
decimal, binary, octal, hexa = 100, 0b101, 0o17, 0x1F
floating, exponent, imaginary = 10.5, 1.5e3, 2j
print("Numeric :", decimal, binary, octal, hexa, floating, exponent, imaginary)

# String literals
single, double = 'single', "double"
multi = """line one
line two"""
raw = r"C:\new\table"
print("String  :", single, double, repr(multi), raw)

# Boolean and special literal
print("Boolean :", True, False)
print("Special :", None)

# Collection literals
print("List    :", [1, 2, 3])
print("Tuple   :", (1, 2, 3))
print("Dict    :", {"a": 1})
print("Set     :", {1, 2, 3})
''',
  ["Write numeric literals in different bases", "Write string literals with several quote styles and a raw string", "Show boolean and None literals", "Show list, tuple, dict and set literals"],
  "A literal is a fixed value written directly in the source code. Python has numeric, string, boolean, special (None) and collection literals. A raw string with the r prefix keeps backslashes as they are. Printing each group shows how the literal is displayed.",
  ["Literals", "Data types in Python"], ["literal", "constant value", "raw string", "none"]),

Q("Demonstrate Constants", "Data Types", "Beginner",
  "Uses UPPER_CASE names, math constants, tuples and Final to model constants.",
  ["constants", "convention", "math.pi", "Final"], "constants_demo.py",
  r'''
import math
from typing import Final

# Python has no true constants; by convention we use UPPER_CASE names.
PI = 3.14159
MAX_USERS: Final = 100          # Final tells type checkers not to reassign
WEEK_DAYS = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")   # immutable tuple

radius = 5
print("Area using PI       :", PI * radius ** 2)
print("math.pi             :", math.pi)
print("math.e              :", math.e)
print("Max users           :", MAX_USERS)
print("First day of week   :", WEEK_DAYS[0])

# Tuples really are protected from change:
try:
    WEEK_DAYS[0] = "Sunday"
except TypeError as error:
    print("Cannot change tuple:", error)
''',
  ["Define UPPER_CASE names for constants", "Use math.pi and math.e", "Annotate a name with Final", "Try to modify an immutable tuple and catch the error"],
  "Python does not enforce constants; programmers write names in capital letters to show a value should not change. The math module provides real constants like pi and e. typing.Final warns type checkers against reassignment, and an immutable tuple actually prevents modification.",
  ["Constants"], ["constant", "final", "upper case", "math"]),

Q("Demonstrate Identifiers", "Data Types", "Beginner",
  "Tests which names are valid identifiers and shows case sensitivity.",
  ["identifiers", "isidentifier()", "naming rules"], "identifiers_demo.py",
  r'''
candidates = ["student_name", "_hidden", "total2", "2total", "my-var",
              "class", "naïve", "Total", "first name"]

for name in candidates:
    print(f"{name!r:15} valid identifier? {name.isidentifier()}")

# Identifiers are case-sensitive
marks = 50
Marks = 90
print("marks =", marks, " Marks =", Marks)

# Naming conventions
student_count = 30          # snake_case for variables and functions
class StudentRecord: pass   # CamelCase for classes
MAX_MARKS = 100             # UPPER_CASE for constants
''',
  ["List sample names", "Use str.isidentifier() on each", "Show that marks and Marks are different", "Show the usual naming conventions"],
  "An identifier is the name of a variable, function, class or module. It must start with a letter or underscore, contain only letters, digits and underscores, and cannot contain spaces or symbols like '-'. isidentifier() checks the rules (it still says True for the keyword 'class', which is separately reserved). Names are case sensitive.",
  ["Identifiers and Reserved words"], ["identifier", "naming", "variable names", "isidentifier"]),

Q("Demonstrate Reserved Keywords", "Data Types", "Beginner",
  "Lists Python keywords with the keyword module and checks names against them.",
  ["keyword module", "kwlist", "iskeyword()"], "reserved_keywords.py",
  r'''
import keyword

print("Python version keyword count:", len(keyword.kwlist))
print("Keywords:")
for i, word in enumerate(keyword.kwlist, start=1):
    print(f"{word:10}", end="\n" if i % 6 == 0 else "")
print()

for name in ["if", "while", "print", "True", "total", "match"]:
    print(f"{name:6} is keyword? {keyword.iskeyword(name)}")

print("Soft keywords:", keyword.softkwlist)

# A keyword cannot be used as a variable name:
try:
    exec("class = 5")
except SyntaxError as error:
    print("SyntaxError:", error.msg)
''',
  ["Import the keyword module", "Print keyword.kwlist in rows", "Check sample names with iskeyword()", "Show soft keywords", "Try to assign to a keyword and catch SyntaxError"],
  "Reserved words (keywords) have special meaning to Python and cannot be used as identifiers. The keyword module gives the full list in kwlist and iskeyword() tests a single word. print is a built-in function, not a keyword. Assigning to a keyword gives a SyntaxError, which we trigger safely with exec().",
  ["Identifiers and Reserved words"], ["keyword", "reserved words", "kwlist", "syntax"]),

Q("Demonstrate Python Comments", "Data Types", "Beginner",
  "Shows single-line, inline, multi-line comments and docstrings.",
  ["#", "docstring", "__doc__"], "comments_demo.py",
  r'''
# This is a single-line comment.
print("Line 1")      # This is an inline comment

# Several single-line comments
# can be used together to
# make a multi-line comment.

"""
A triple-quoted string that is not assigned to anything
is ignored at run time, so it is often used as a block comment.
"""
print("Line 2")

def add(a, b):
    """Return the sum of a and b.   <- this is a docstring"""
    return a + b   # print(a - b) would be ignored if commented

print(add(2, 3))
print("Docstring:", add.__doc__)
''',
  ["Write a single-line comment with #", "Add an inline comment after code", "Use consecutive # lines and a triple-quoted block", "Write a docstring and print it with __doc__"],
  "Comments are notes for humans and are ignored by Python. Anything after # on a line is a comment. Python has no special multi-line comment, so people use several # lines or an unassigned triple-quoted string. A docstring placed first in a function is stored in __doc__ and can be read at run time.",
  ["Comments in Python"], ["comment", "docstring", "hash", "documentation"]),

Q("Demonstrate String and Character Handling", "Data Types", "Beginner",
  "Treats a character as a 1-length string and uses ord(), chr() and common character tests.",
  ["characters", "ord()", "chr()", "isalpha()"], "string_character_handling.py",
  r'''
word = "Python 3!"

# Python has no separate char type: a character is a string of length 1.
for ch in word:
    kind = ("letter" if ch.isalpha() else
            "digit" if ch.isdigit() else
            "space" if ch.isspace() else "symbol")
    print(f"{ch!r} code={ord(ch):3} {kind}")

print("chr(97)  =", chr(97))
print("Next letter after 'a':", chr(ord("a") + 1))

letters = sum(c.isalpha() for c in word)
print("Letters count:", letters)
print("Swapcase:", word.swapcase())
print("Reversed:", word[::-1])
''',
  ["Loop through each character of the string", "Classify it with isalpha(), isdigit(), isspace()", "Show its code with ord() and convert back using chr()", "Count letters, swap case and reverse"],
  "Python has no char type; a character is simply a string of length one. ord() gives a character's Unicode code and chr() does the opposite. Methods like isalpha() and isdigit() classify characters. Slicing with [::-1] reverses the string.",
  ["Strings and Characters"], ["string", "character", "ord", "chr"]),
]

SQ = ["Sequences in Python"]
ST = ["Sets"]

PROGRAMS += [
Q("Demonstrate Strings as Sequences", "Sequences", "Beginner",
  "Shows that a string is an ordered, immutable sequence with common methods.",
  ["str", "sequence", "methods", "len()"], "strings_sequence.py",
  r'''
text = "Programming in Python"
print("Text      :", text)
print("Length    :", len(text))
print("Upper     :", text.upper())
print("Title     :", text.title())
print("Replace   :", text.replace("Python", "Java"))
print("Split     :", text.split())
print("Join      :", "-".join(["a", "b", "c"]))
print("Find 'in' :", text.find("in"))
print("Count 'n' :", text.count("n"))
print("Starts with 'Prog':", text.startswith("Prog"))
print("Strip     :", "   padded   ".strip())
for index, ch in enumerate(text[:5]):
    print(index, ch)
''',
  ["Create a string", "Apply common methods such as upper(), replace(), split(), join()", "Search with find() and count()", "Loop through the first characters with enumerate()"],
  "A string is an ordered sequence of characters that cannot be changed after creation, so every method returns a new string. The program shows case change, replacement, splitting into a list, joining a list, searching and counting. enumerate() gives each character together with its position.",
  SQ, ["string", "sequence", "methods", "text"]),

Q("Demonstrate Lists", "Sequences", "Beginner",
  "Creates a list and uses append, insert, remove, pop, sort and more.",
  ["list", "append()", "sort()", "mutable"], "lists_demo.py",
  r'''
fruits = ["apple", "banana", "cherry"]
print("Original:", fruits)

fruits.append("mango")            # add at end
fruits.insert(1, "orange")        # add at position 1
print("After adds:", fruits)

fruits.remove("banana")           # remove by value
last = fruits.pop()               # remove and return last
print("Popped:", last, "->", fruits)

fruits.sort()
print("Sorted:", fruits)
fruits.reverse()
print("Reversed:", fruits)

fruits[0] = "grape"               # lists are mutable
print("Changed:", fruits, "length", len(fruits))
mixed = [1, "two", 3.0, [4, 5]]
print("Mixed list:", mixed)
''',
  ["Create a list", "Add items with append() and insert()", "Remove with remove() and pop()", "Sort and reverse", "Change an element by index"],
  "A list is an ordered, mutable sequence that can hold items of any type. Methods like append(), insert(), remove() and pop() change the list in place. sort() and reverse() also modify the list itself. Because lists are mutable, assigning to an index replaces that element.",
  SQ, ["list", "append", "mutable", "sequence"]),

Q("Demonstrate Tuples", "Sequences", "Beginner",
  "Shows tuple creation, immutability, packing/unpacking and methods.",
  ["tuple", "immutable", "unpacking"], "tuples_demo.py",
  r'''
point = (10, 20, 30)
single = (5,)                  # comma makes it a tuple
print(point, type(point), single, type(single))

# Packing and unpacking
x, y, z = point
print("x, y, z =", x, y, z)
first, *rest = point
print("first =", first, "rest =", rest)

print("Length:", len(point), "Max:", max(point), "Sum:", sum(point))
print("Count of 10:", point.count(10), "Index of 20:", point.index(20))

# Tuples are immutable
try:
    point[0] = 99
except TypeError as error:
    print("Error:", error)

# Swapping with tuples
a, b = 1, 2
a, b = b, a
print("Swapped:", a, b)
''',
  ["Create tuples including a one-item tuple", "Unpack into variables", "Use len, max, sum, count, index", "Try to modify it and catch TypeError", "Swap two variables"],
  "A tuple is an ordered sequence like a list, but it cannot be changed after it is created. A single-item tuple needs a trailing comma. Tuple unpacking assigns each item to a variable, and a starred name collects the rest. Tuples are handy for fixed data such as coordinates.",
  SQ, ["tuple", "immutable", "unpacking", "sequence"]),

Q("Demonstrate Indexing", "Sequences", "Beginner",
  "Accesses elements of a string, list and tuple by positive and negative index.",
  ["indexing", "negative index", "IndexError"], "indexing_demo.py",
  r'''
word = "PYTHON"
numbers = [10, 20, 30, 40, 50]
colors = ("red", "green", "blue")

print("word[0]   =", word[0])
print("word[5]   =", word[5])
print("word[-1]  =", word[-1], "(last)")
print("word[-6]  =", word[-6], "(first)")
print("numbers[2] =", numbers[2])
print("colors[-2] =", colors[-2])

# Change an item in a list using its index
numbers[1] = 99
print("Modified list:", numbers)

# Index out of range
try:
    print(numbers[10])
except IndexError as error:
    print("IndexError:", error)
''',
  ["Create a string, a list and a tuple", "Access items by positive index starting at 0", "Access items by negative index from the end", "Assign to a list index", "Catch IndexError for a bad index"],
  "Indexing selects a single element of a sequence by its position. The first item has index 0 and the last has index -1. Negative indices count from the end. Using an index beyond the length raises IndexError, which is handled with try-except.",
  SQ, ["index", "negative index", "sequence", "position"]),

Q("Demonstrate Slicing", "Sequences", "Beginner",
  "Uses start:stop:step slices on lists and strings, including reversing.",
  ["slicing", "start:stop:step"], "slicing_demo.py",
  r'''
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
text = "Hello, World"

print("numbers[2:6]   =", numbers[2:6])      # stop is excluded
print("numbers[:4]    =", numbers[:4])
print("numbers[6:]    =", numbers[6:])
print("numbers[::2]   =", numbers[::2])      # every 2nd item
print("numbers[1::3]  =", numbers[1::3])
print("numbers[-3:]   =", numbers[-3:])
print("numbers[::-1]  =", numbers[::-1])     # reversed
print("text[0:5]      =", text[0:5])
print("text[-5:]      =", text[-5:])
print("text[::-1]     =", text[::-1])
copy = numbers[:]                            # shallow copy
print("copy is numbers?", copy is numbers)
''',
  ["Create a list and a string", "Slice with start and stop", "Use omitted bounds, step and negative values", "Reverse with [::-1]", "Make a copy with [:]"],
  "A slice sequence[start:stop:step] returns a new sequence from start up to, but not including, stop. Leaving out a value uses the default: the beginning, the end, or step 1. A negative step walks backwards, so [::-1] reverses. Slicing never raises IndexError for out-of-range limits.",
  SQ, ["slice", "slicing", "step", "reverse"]),

Q("Demonstrate Sequence Concatenation", "Sequences", "Beginner",
  "Joins strings, lists and tuples with + and shows the type-mixing error.",
  ["concatenation", "+ operator", "join()"], "sequence_concatenation.py",
  r'''
first_name, last_name = "Ada", "Lovelace"
print("String :", first_name + " " + last_name)
print("List   :", [1, 2, 3] + [4, 5])
print("Tuple  :", (1, 2) + (3, 4))

# Different sequence types cannot be mixed with +
try:
    print([1, 2] + (3, 4))
except TypeError as error:
    print("TypeError:", error)

# Convert first, then concatenate
print("Fixed  :", [1, 2] + list((3, 4)))

# Many strings: join() is better than repeated +
words = ["Python", "is", "fun"]
print("Joined :", " ".join(words))

# Extending a list in place
items = [1, 2]
items += [3, 4]
items.extend([5])
print("Extended:", items)
''',
  ["Add two strings, two lists and two tuples with +", "Try adding a list and a tuple and catch TypeError", "Convert types before adding", "Use join() and extend() as alternatives"],
  "The + operator joins two sequences of the same type into a new one. Mixing types such as list and tuple raises TypeError, so one must be converted first. For many strings, join() is faster than repeated +. += and extend() add to an existing list in place.",
  SQ, ["concatenation", "plus", "join", "sequence"]),

Q("Demonstrate Sequence Repetition", "Sequences", "Beginner",
  "Repeats strings, lists and tuples with * and warns about shared references.",
  ["repetition", "* operator"], "sequence_repetition.py",
  r'''
print("ab" * 3)
print("-" * 30)
print([0] * 5)
print((1, 2) * 3)
print("Python " * 2)

# 0 or negative counts give an empty sequence
print(repr("hi" * 0), [1] * -1)

# Careful: repeating a list of lists copies the SAME inner list
grid = [[0] * 3] * 2
grid[0][0] = 9
print("Shared rows  :", grid)

# Safe way: build each row separately
grid = [[0] * 3 for _ in range(2)]
grid[0][0] = 9
print("Separate rows:", grid)
''',
  ["Repeat a string, list and tuple with *", "Show that count 0 gives empty", "Show the shared-reference pitfall with nested lists", "Use a list comprehension for independent rows"],
  "The * operator repeats a sequence a given number of times and returns a new sequence. It is handy for drawing lines of characters or creating a list of zeros. When a list that contains another list is repeated, all copies refer to the same inner list, so a change appears in every row; a comprehension avoids this.",
  SQ, ["repetition", "multiply", "star", "sequence"]),

Q("Demonstrate Membership Operators in Sequences", "Sequences", "Beginner",
  "Uses in and not in on strings, lists, tuples and ranges.",
  ["in", "not in", "membership"], "sequence_membership.py",
  r'''
word = "programming"
numbers = [2, 4, 6, 8]
colors = ("red", "green")

print("'gram' in word        :", "gram" in word)       # substring test
print("'z' in word           :", "z" in word)
print("6 in numbers          :", 6 in numbers)
print("5 not in numbers      :", 5 not in numbers)
print("'Red' in colors       :", "Red" in colors)      # case-sensitive
print("7 in range(0, 10, 7)  :", 7 in range(0, 10, 7))

# Typical use: validate a choice
choice = "green"
if choice in colors:
    print(choice, "is an allowed colour")
''',
  ["Create a string, list, tuple and range", "Test items with in", "Test absence with not in", "Use membership inside an if statement"],
  "The in operator returns True if a value is found in a sequence, and not in returns True if it is missing. For strings it checks for a substring. The check is case-sensitive. Membership tests are commonly used to validate input choices.",
  SQ + ["Membership Operators"], ["membership", "in", "not in", "sequence"]),

# ------------------------------ Sets ------------------------------
Q("Create a Set", "Sets", "Beginner",
  "Creates sets using braces, set() and comprehension; shows empty-set pitfall.",
  ["set", "set()", "unordered", "unique"], "create_set.py",
  r'''
colors = {"red", "green", "blue"}
numbers = set([1, 2, 3, 2, 1])        # duplicates removed
letters = set("hello")                # unique characters
squares = {n * n for n in range(1, 6)}   # set comprehension

print(colors, type(colors))
print(numbers)
print(sorted(letters))
print(squares)

empty_wrong = {}                      # this is a dict!
empty_set = set()
print(type(empty_wrong), type(empty_set))
print("Length:", len(colors))
print("Sets are unordered, so there is no indexing:")
try:
    print(colors[0])
except TypeError as error:
    print("TypeError:", error)
''',
  ["Create a set with braces", "Create sets using set() from a list and a string", "Use a set comprehension", "Create an empty set correctly", "Show that indexing is not allowed"],
  "A set is an unordered collection of unique items. Duplicates are dropped automatically. Curly braces with no items make a dict, so an empty set must be created with set(). Because sets have no order they cannot be indexed.",
  ST, ["set", "unique", "create", "unordered"]),

Q("Add Elements to a Set", "Sets", "Beginner",
  "Uses add() and update() to put items into a set.",
  ["add()", "update()", "set"], "set_add_elements.py",
  r'''
languages = {"Python", "C"}
print("Start :", sorted(languages))

languages.add("Java")                       # one item
languages.add("Python")                     # already present - no change
print("add   :", sorted(languages))

languages.update(["Go", "Rust"])            # many items from a list
languages.update({"C++"}, ("Ruby",))        # several iterables at once
print("update:", sorted(languages))

# Set items must be hashable (immutable)
try:
    languages.add(["a", "list"])
except TypeError as error:
    print("TypeError:", error)
''',
  ["Create a small set", "Add a single item with add()", "Add duplicate and see nothing changes", "Add many items with update()", "Show that lists cannot be set items"],
  "add() inserts one element and update() inserts every element of any iterable. Adding something already present does nothing, because sets keep only unique items. Elements must be hashable, so a list cannot be added but a tuple can. sorted() is used only to print in a stable order.",
  ST, ["set", "add", "update", "insert"]),

Q("Remove Elements from a Set", "Sets", "Beginner",
  "Compares remove(), discard(), pop() and clear().",
  ["remove()", "discard()", "pop()", "KeyError"], "set_remove_elements.py",
  r'''
nums = {1, 2, 3, 4, 5, 6}

nums.remove(2)                 # raises KeyError if missing
print("remove(2)  :", sorted(nums))

nums.discard(10)               # silently ignores missing items
nums.discard(3)
print("discard    :", sorted(nums))

try:
    nums.remove(99)
except KeyError as error:
    print("KeyError for missing item:", error)

popped = nums.pop()            # removes an arbitrary item
print("pop() removed one item; left:", len(nums))

nums.clear()
print("after clear:", nums)
''',
  ["Remove an existing item with remove()", "Use discard() for safe removal", "Show KeyError from remove() on a missing item", "Use pop() and clear()"],
  "remove() deletes an element but raises KeyError if it is absent, while discard() does nothing in that case. pop() removes and returns an arbitrary element because sets are unordered. clear() empties the whole set.",
  ST, ["set", "remove", "discard", "pop"]),

Q("Demonstrate Set Union", "Sets", "Beginner",
  "Combines two sets with | and union().",
  ["union", "|", "set operations"], "set_union.py",
  r'''
python_club = {"Asha", "Ravi", "Meena", "John"}
java_club = {"Ravi", "Kiran", "John"}

print("Using |        :", sorted(python_club | java_club))
print("Using union()  :", sorted(python_club.union(java_club)))
print("Three sets     :", sorted(python_club | java_club | {"Zoya"}))
print("Total unique members:", len(python_club | java_club))

# update with |= changes the left-hand set
python_club |= {"Nina"}
print("After |=       :", sorted(python_club))
''',
  ["Create two sets", "Find union with | and union()", "Combine more than two sets", "Count the unique members", "Use |= for in-place union"],
  "The union of two sets contains every element that is in either set, with duplicates removed. It can be written as a | b or a.union(b). The |= operator updates the left set in place. In the club example, people in both clubs are listed only once.",
  ST, ["union", "set", "or", "combine"]),

Q("Demonstrate Set Intersection", "Sets", "Beginner",
  "Finds common elements with & and intersection().",
  ["intersection", "&", "isdisjoint()"], "set_intersection.py",
  r'''
python_club = {"Asha", "Ravi", "Meena", "John"}
java_club = {"Ravi", "Kiran", "John"}

print("Using &              :", sorted(python_club & java_club))
print("Using intersection() :", sorted(python_club.intersection(java_club)))
print("Common count         :", len(python_club & java_club))

others = {"Tom", "Jerry"}
print("Any common with others?", bool(python_club & others))
print("isdisjoint           :", python_club.isdisjoint(others))

python_club &= java_club          # in-place intersection
print("After &=             :", sorted(python_club))
''',
  ["Create two sets", "Find common elements with & and intersection()", "Test for no overlap with isdisjoint()", "Use &= to keep only common items"],
  "The intersection of two sets holds only the elements present in both. It is written a & b or a.intersection(b). isdisjoint() answers whether two sets have nothing in common. The &= form modifies the first set so it keeps only the shared items.",
  ST, ["intersection", "set", "and", "common"]),

Q("Demonstrate Set Difference", "Sets", "Beginner",
  "Finds items in one set but not another using - and difference().",
  ["difference", "-", "issubset()"], "set_difference.py",
  r'''
all_students = {"Asha", "Ravi", "Meena", "John", "Kiran"}
present = {"Asha", "John", "Kiran"}

absent = all_students - present
print("Absent (using -)       :", sorted(absent))
print("Absent (difference())  :", sorted(all_students.difference(present)))

# Difference is NOT symmetric
print("present - all_students :", present - all_students)

print("present is subset of all?", present.issubset(all_students))
all_students -= {"Kiran"}
print("After -= :", sorted(all_students))
''',
  ["Create a set of all students and a set of present students", "Compute all - present", "Show that reversing the order gives a different result", "Check issubset() and use -="],
  "The difference a - b contains the elements that are in a but not in b. Unlike union and intersection, the order matters: present - all_students is empty here. difference() is the method form. issubset() confirms present is fully inside the whole class.",
  ST, ["difference", "set", "minus", "subset"]),

Q("Demonstrate Symmetric Difference", "Sets", "Beginner",
  "Finds items that are in exactly one of two sets using ^.",
  ["symmetric_difference", "^"], "set_symmetric_difference.py",
  r'''
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("a ^ b                      :", sorted(a ^ b))
print("a.symmetric_difference(b)  :", sorted(a.symmetric_difference(b)))

# Same result using other operations
print("(a | b) - (a & b)          :", sorted((a | b) - (a & b)))
print("(a - b) | (b - a)          :", sorted((a - b) | (b - a)))

a ^= {1, 9}
print("After a ^= {1, 9}          :", sorted(a))
''',
  ["Create two overlapping sets", "Apply ^ and symmetric_difference()", "Verify with union minus intersection", "Use ^= to update a set"],
  "Symmetric difference returns elements that are in either set but not in both. It can be written a ^ b. The program proves the result by computing (a | b) - (a & b) and (a - b) | (b - a), which are equal. ^= updates the left set in place.",
  ST, ["symmetric difference", "xor", "set", "caret"]),

Q("Remove Duplicate Elements Using Sets", "Sets", "Beginner",
  "Removes duplicates from a list with set(), and also keeps the original order.",
  ["set()", "dict.fromkeys()", "duplicates"], "remove_duplicates_set.py",
  r'''
numbers = [4, 2, 7, 2, 4, 9, 7, 1, 4]
print("Original       :", numbers)

unique_unordered = list(set(numbers))
print("Using set()    :", sorted(unique_unordered), "(order not guaranteed, so sorted here)")

# Keep first-appearance order using dict.fromkeys()
unique_ordered = list(dict.fromkeys(numbers))
print("Keep order     :", unique_ordered)

# Same idea with a seen-set
seen = set()
result = []
for n in numbers:
    if n not in seen:
        seen.add(n)
        result.append(n)
print("Seen-set loop  :", result)
print(f"Removed {len(numbers) - len(result)} duplicates")
''',
  ["Start with a list that has repeated values", "Convert to set and back to list", "Keep order using dict.fromkeys()", "Or use a loop with a seen set", "Report how many duplicates were removed"],
  "Converting a list to a set removes duplicates because a set holds each value once, but the original order is lost. dict.fromkeys() or a loop with a seen set removes duplicates and keeps the first-appearance order. The count of removed items is the length difference.",
  ST, ["duplicates", "unique", "set", "list"]),
]

BIT = ["Bitwise Operators"]

PROGRAMS += [
Q("Arithmetic Operators", "Operators", "Beginner",
  "Applies +, -, *, /, //, % and ** to two numbers read from the user.",
  ["arithmetic operators", "//", "%", "**"], "arithmetic_operators.py",
  r'''
try:
    a = float(input("Enter first number : "))
    b = float(input("Enter second number: "))
    print(f"{a} + {b}  = {a + b}")
    print(f"{a} - {b}  = {a - b}")
    print(f"{a} * {b}  = {a * b}")
    print(f"{a} ** {b} = {a ** b}")
    if b == 0:
        print("Division, floor division and modulus by zero are not allowed.")
    else:
        print(f"{a} / {b}  = {a / b}")
        print(f"{a} // {b} = {a // b}")
        print(f"{a} % {b}  = {a % b}")
except ValueError:
    print("Invalid number entered.")
''',
  ["Read two numbers", "Apply +, -, *, ** and print", "Check the second number for zero", "Apply /, // and % when safe", "Handle invalid input"],
  "Arithmetic operators perform maths: + - * for the basics, / for true division, // for floor division (rounds down), % for the remainder and ** for power. Division, // and % by zero raise ZeroDivisionError, so the program checks b first. Input is converted with float() inside a try-except.",
  ["Arithmetic Operators"], ["arithmetic", "operators", "modulus", "power"], si="17\n5", kind="Interactive"),

Q("Assignment Operators", "Operators", "Beginner",
  "Shows =, augmented assignment operators and multiple assignment.",
  ["assignment", "+=", "//=", "walrus"], "assignment_operators.py",
  r'''
x = 10
print("x = 10          ->", x)
x += 5;  print("x += 5          ->", x)
x -= 3;  print("x -= 3          ->", x)
x *= 2;  print("x *= 2          ->", x)
x /= 4;  print("x /= 4          ->", x)
x //= 2; print("x //= 2         ->", x)
x **= 3; print("x **= 3         ->", x)
x %= 5;  print("x %= 5          ->", x)

n = 12
n &= 10; print("n &= 10         ->", n)
n |= 3;  print("n |= 3          ->", n)
n ^= 5;  print("n ^= 5          ->", n)
n <<= 2; print("n <<= 2         ->", n)
n >>= 1; print("n >>= 1         ->", n)

a = b = c = 7                    # chained assignment
p, q = 1, 2                      # multiple assignment
print(a, b, c, p, q)
if (length := len("Python")) > 5:   # walrus operator
    print("Length is", length)
''',
  ["Assign a value with =", "Apply each arithmetic augmented operator", "Apply bitwise augmented operators", "Show chained and multiple assignment", "Use the walrus operator"],
  "The = operator stores a value in a variable. Augmented operators such as += combine an operation with assignment, so x += 5 means x = x + 5. The same pattern works for bitwise operators. Python also allows chained assignment (a = b = c) and, since 3.8, the walrus operator := for assigning inside an expression.",
  ["Assignment Operators"], ["assignment", "augmented", "+=", "walrus"]),

Q("Unary Minus Operator", "Operators", "Beginner",
  "Negates numbers, variables and expressions with the unary minus.",
  ["unary minus", "negation", "abs()"], "unary_minus_operator.py",
  r'''
a = 15
b = -8
print("-a      =", -a)
print("-b      =", -b)           # negative of a negative is positive
print("--a     =", --a)          # two minuses cancel
print("-(a+b)  =", -(a + b))
print("-3.5    =", -3.5)
print("-0      =", -0)

# Precedence: ** binds tighter than unary minus
print("-2 ** 2   =", -2 ** 2)
print("(-2) ** 2 =", (-2) ** 2)

# Unary minus vs binary minus
print("5 - -3  =", 5 - -3)
print("abs(b)  =", abs(b))
print("Unary plus +b =", +b)
''',
  ["Create positive and negative numbers", "Apply the unary minus", "Show double negation and expressions", "Explain precedence with **", "Compare with binary minus and abs()"],
  "The unary minus has one operand and changes its sign. Applying it twice returns the original number. It has lower precedence than **, so -2 ** 2 is -(2 ** 2) = -4, while (-2) ** 2 is 4. A unary plus also exists but normally changes nothing.",
  ["Unary Minus Operator"], ["unary", "minus", "negative", "sign"]),

Q("Relational Operators", "Operators", "Beginner",
  "Compares two numbers with ==, !=, >, <, >= and <=, and shows chained comparison.",
  ["relational", "comparison", "chained"], "relational_operators.py",
  r'''
try:
    a = int(input("Enter first integer : "))
    b = int(input("Enter second integer: "))
except ValueError:
    print("Please enter integers only.")
else:
    print(f"{a} == {b} : {a == b}")
    print(f"{a} != {b} : {a != b}")
    print(f"{a} >  {b} : {a > b}")
    print(f"{a} <  {b} : {a < b}")
    print(f"{a} >= {b} : {a >= b}")
    print(f"{a} <= {b} : {a <= b}")
    print("Chained 0 < a < 100:", 0 < a < 100)
    print("String compare 'apple' < 'banana':", "apple" < "banana")
''',
  ["Read two integers safely", "Apply the six relational operators", "Print each True/False result", "Show a chained comparison and string comparison"],
  "Relational (comparison) operators compare two values and return a boolean. Python allows chained comparisons like 0 < a < 100, which is a neat shortcut for two tests joined by and. Strings are compared alphabetically using character codes.",
  ["Relational Operators"], ["relational", "comparison", "equal", "greater"], si="25\n40", kind="Interactive"),

Q("Logical Operators", "Operators", "Beginner",
  "Uses and, or, not with a truth table and in a real eligibility check.",
  ["and", "or", "not", "truth table"], "logical_operators.py",
  r'''
print(" A      B     A and B   A or B   not A")
for a in (True, False):
    for b in (True, False):
        print(f"{a!s:6} {b!s:6} {a and b!s:8} {a or b!s:8} {not a}")

age = 22
has_id = True
print("Can vote?", age >= 18 and has_id)
print("Free entry?", age < 5 or age > 60)
print("Not a minor?", not age < 18)

# and/or return one of the operands (short-circuit)
print("0 or 'default'   ->", 0 or "default")
print("5 and 10         ->", 5 and 10)
print("'' and 10        ->", repr("" and 10))
''',
  ["Print a truth table with nested loops", "Apply and, or, not to real conditions", "Show that and/or return operands and short-circuit"],
  "and is True only if both sides are True, or is True if at least one side is True, and not reverses a boolean. The truth table lists all four combinations. Python's and/or do not always return True/False: they return one of the operands and stop evaluating as soon as the answer is known (short-circuit).",
  ["Logical Operators"], ["logical", "and", "or", "not"]),

Q("Boolean Operations", "Operators", "Beginner",
  "Combines booleans with and/or/not, all(), any() and boolean operators on sets of conditions.",
  ["boolean operations", "all()", "any()", "bool()"], "boolean_operations.py",
  r'''
is_raining = True
has_umbrella = False

print("Go out without worry?", (not is_raining) or has_umbrella)
print("Stay home?", is_raining and not has_umbrella)

marks = [72, 85, 90, 66]
print("All passed (>=40)?", all(m >= 40 for m in marks))
print("Any distinction (>=85)?", any(m >= 85 for m in marks))
print("All empty list ->", all([]), "| any empty list ->", any([]))

# bool and bitwise operators on booleans
print("True & False :", True & False)
print("True | False :", True | False)
print("True ^ True  :", True ^ True)
print("True == 1    :", True == 1)
print("bool('False'):", bool("False"), "(non-empty string is True)")

# De Morgan's law
a, b = True, False
print("De Morgan holds:", (not (a and b)) == ((not a) or (not b)))
''',
  ["Combine boolean variables with and/or/not", "Use all() and any() on a list of conditions", "Use & | ^ on boolean values", "Verify De Morgan's law"],
  "Boolean operations combine True/False values. all() is True when every item is true and any() is True when at least one is true; both accept generator expressions. The bitwise operators &, | and ^ also work on booleans. De Morgan's law, not (a and b) == (not a) or (not b), is confirmed in the last line.",
  ["Boolean Operators", "Logical Operators"], ["boolean", "all", "any", "de morgan"]),

Q("Bitwise AND", "Operators", "Intermediate",
  "Applies & to numbers and shows binary working, plus an odd/even and bit-mask use.",
  ["&", "bin()", "bit mask"], "bitwise_and.py",
  r'''
a, b = 12, 10
print(f"a = {a:04b} ({a})")
print(f"b = {b:04b} ({b})")
print(f"a & b = {a & b:04b} ({a & b})")

# Use 1: odd/even test - the last bit of an odd number is 1
for n in (6, 7):
    print(n, "is", "odd" if n & 1 else "even")

# Use 2: bit mask - keep only the lowest 4 bits
value = 0b10110111
print("Lowest 4 bits:", bin(value & 0b1111))
''',
  ["Choose two integers", "Show their binary form", "Apply & bit by bit", "Use & 1 to find odd/even", "Use a mask to extract bits"],
  "Bitwise AND compares two numbers bit by bit and gives 1 only where both bits are 1. 12 (1100) & 10 (1010) is 1000, which is 8. Because the last bit of an odd number is 1, n & 1 tests odd or even. AND with a mask keeps only the chosen bits.",
  BIT, ["bitwise", "and", "mask", "binary"]),

Q("Bitwise OR", "Operators", "Intermediate",
  "Applies | to numbers and uses it to set bits and combine flags.",
  ["|", "set bit", "flags"], "bitwise_or.py",
  r'''
a, b = 12, 10
print(f"a = {a:04b} ({a})")
print(f"b = {b:04b} ({b})")
print(f"a | b = {a | b:04b} ({a | b})")

# Set a particular bit (bit 0) of a number
number = 0b1000
print("Set bit 0:", bin(number | (1 << 0)))

# Combine permission flags
READ, WRITE, EXECUTE = 1, 2, 4
permission = READ | WRITE
print("Permission value:", permission)
print("Can write?  ", bool(permission & WRITE))
print("Can execute?", bool(permission & EXECUTE))
''',
  ["Choose two integers", "Apply | and print the binary result", "Set a single bit using 1 << n", "Combine READ/WRITE flags and test them"],
  "Bitwise OR gives 1 in each position where at least one of the two bits is 1. 12 | 10 is 1110 = 14. OR with (1 << n) turns bit n on. Programmers use OR to combine flags into one number and AND to test them.",
  BIT, ["bitwise", "or", "flags", "set bit"]),

Q("Bitwise XOR", "Operators", "Intermediate",
  "Applies ^ and uses it for toggling bits, swapping and simple encryption.",
  ["^", "toggle", "swap"], "bitwise_xor.py",
  r'''
a, b = 12, 10
print(f"a = {a:04b} ({a})")
print(f"b = {b:04b} ({b})")
print(f"a ^ b = {a ^ b:04b} ({a ^ b})")

# XOR with itself is 0; XOR with 0 gives the same number
print("a ^ a =", a ^ a, "| a ^ 0 =", a ^ 0)

# Toggle a bit
print("Toggle bit 1 of 0b1010:", bin(0b1010 ^ 0b10))

# Swap two numbers without a temporary variable
x, y = 5, 9
x ^= y
y ^= x
x ^= y
print("Swapped:", x, y)

# Simple XOR cipher - applying it twice restores the text
key = 42
secret = [ord(c) ^ key for c in "Hello"]
print("Encrypted codes:", secret)
print("Decrypted      :", "".join(chr(code ^ key) for code in secret))
''',
  ["Apply ^ to two integers", "Show XOR with itself and zero", "Toggle a bit", "Swap two numbers using XOR", "Encrypt and decrypt text with a key"],
  "Bitwise XOR gives 1 where the two bits are different. XOR-ing a number with itself gives 0 and XOR-ing twice with the same value restores the original. This allows toggling bits, swapping without a temporary variable and a toy cipher.",
  BIT, ["bitwise", "xor", "toggle", "cipher"]),

Q("Bitwise NOT", "Operators", "Intermediate",
  "Applies ~ and explains why ~n equals -(n+1) using two's complement.",
  ["~", "two's complement", "masking"], "bitwise_not.py",
  r'''
for n in (0, 5, -5, 255):
    print(f"~{n:<4} = {~n:<5}  (same as -({n}+1) = {-(n + 1)})")

# Python integers are unlimited, so to see an 8-bit NOT we mask the result
n = 0b00001111
inverted = ~n & 0xFF
print(f"8-bit NOT of {n:08b} is {inverted:08b} ({inverted})")
''',
  ["Apply ~ to several numbers", "Compare with -(n+1)", "Mask with & 0xFF to see the 8-bit inversion"],
  "The bitwise NOT operator ~ flips every bit. For Python's signed, unlimited integers this always equals -(n + 1), so ~5 is -6. To see a fixed-width inversion, such as 8 bits, we mask the result with 0xFF.",
  BIT, ["bitwise", "not", "tilde", "complement"]),

Q("Left Shift Operator", "Operators", "Intermediate",
  "Uses << to shift bits left, which multiplies by powers of two.",
  ["<<", "shift", "powers of 2"], "left_shift.py",
  r'''
number = 5
print(f"Binary of {number}: {number:08b}")
for shift in range(1, 4):
    result = number << shift
    print(f"{number} << {shift} = {result:3}  binary {result:08b}   ({number} * 2**{shift})")

# Quick way to compute powers of two
print("1 << 10 =", 1 << 10)
''',
  ["Pick a number and show its binary form", "Shift it left by 1, 2 and 3 places", "Show the result equals number * 2**shift", "Compute a power of two with 1 << n"],
  "Left shift x << n moves the bits of x n places to the left and fills with zeros, which multiplies x by 2**n. So 5 << 2 is 20. The expression 1 << n is a fast way to get 2 to the power n.",
  BIT, ["left shift", "<<", "bitwise", "multiply"]),

Q("Right Shift Operator", "Operators", "Intermediate",
  "Uses >> to shift bits right, which floor-divides by powers of two.",
  [">>", "shift", "floor division"], "right_shift.py",
  r'''
number = 100
print(f"Binary of {number}: {number:08b}")
for shift in range(1, 4):
    result = number >> shift
    print(f"{number} >> {shift} = {result:3}  binary {result:08b}   ({number} // 2**{shift})")

print("25 >> 1 =", 25 >> 1, "(odd numbers lose the last bit)")
print("-16 >> 2 =", -16 >> 2, "(sign is preserved)")
''',
  ["Pick a number and show binary", "Shift right by 1, 2 and 3", "Compare with floor division by 2**n", "Show behaviour for odd and negative numbers"],
  "Right shift x >> n moves the bits n places right, dropping the lowest bits. It equals floor division by 2**n, so 25 >> 1 is 12. For negative numbers Python keeps the sign (arithmetic shift), so -16 >> 2 is -4.",
  BIT, ["right shift", ">>", "bitwise", "divide"]),

Q("Membership Operators", "Operators", "Beginner",
  "Applies in and not in to a list, string, dictionary and set, reading a value from the user.",
  ["in", "not in", "dict keys"], "membership_operators.py",
  r'''
vowels = "aeiou"
students = ["Asha", "Ravi", "Meena"]
marks = {"Asha": 90, "Ravi": 75}
primes = {2, 3, 5, 7}

letter = input("Enter a single letter: ").lower()
print(f"'{letter}' in vowels      :", letter in vowels)
print(f"'{letter}' not in vowels  :", letter not in vowels)
print("'Ravi' in students   :", "Ravi" in students)
print("'Ravi' in marks      :", "Ravi" in marks, "(checks keys)")
print("75 in marks          :", 75 in marks)
print("75 in marks.values() :", 75 in marks.values())
print("7 in primes          :", 7 in primes)
''',
  ["Create a string, list, dictionary and set", "Read a letter from the user", "Test it with in and not in", "Show that dict membership tests keys, not values"],
  "The membership operators in and not in test whether a value is present in a container. For a dictionary they look at the keys, so values need .values(). Sets and dictionaries do this check very quickly. Here the user's letter is tested against a string of vowels.",
  ["Membership Operators"], ["membership", "in", "not in", "dictionary"], si="e", kind="Interactive"),

Q("Identity Operators", "Operators", "Intermediate",
  "Uses is and is not with id() to compare object identity, including None checks.",
  ["is", "is not", "id()", "None"], "identity_operators.py",
  r'''
a = [1, 2, 3]
b = a                # same object
c = [1, 2, 3]        # equal but a different object

print("a is b     :", a is b)
print("a is c     :", a is c)
print("a == c     :", a == c)
print("a is not c :", a is not c)
print("id(a) == id(b):", id(a) == id(b))

b.append(4)
print("a after b.append(4):", a)

# Recommended use: compare with None
result = None
if result is None:
    print("result is None")
print("x is not None:", 5 is not None)
''',
  ["Create a list and a second name for it", "Create an equal but separate list", "Compare using is, is not and ==", "Show id() values agree and mutation is shared", "Use is None"],
  "The identity operators is and is not test whether two names point to the very same object in memory, which id() confirms. a and b are the same list, so changing b also changes a. c has equal contents but is a separate object. Use is for None and == for values.",
  ["Identity Operators"], ["identity", "is", "id", "none"]),

Q("Operator Precedence", "Operators", "Intermediate",
  "Evaluates expressions to show which operators run first and how parentheses change it.",
  ["precedence", "associativity", "parentheses"], "operator_precedence.py",
  r'''
print("2 + 3 * 4        =", 2 + 3 * 4)          # * before +
print("(2 + 3) * 4      =", (2 + 3) * 4)
print("2 ** 3 ** 2      =", 2 ** 3 ** 2)        # ** is right-associative
print("(2 ** 3) ** 2    =", (2 ** 3) ** 2)
print("-3 ** 2          =", -3 ** 2)
print("10 - 4 - 3       =", 10 - 4 - 3)         # left-associative
print("100 / 10 * 2     =", 100 / 10 * 2)
print("7 // 2 * 2 + 7 % 2 =", 7 // 2 * 2 + 7 % 2)
print("5 > 3 and 2 < 1 or True =", 5 > 3 and 2 < 1 or True)
print("not True or True =", not True or True)
print("1 | 2 & 3 ^ 4    =", 1 | 2 & 3 ^ 4)
print("1 + 2 << 3       =", 1 + 2 << 3)         # + before <<
print("5 == 5 == True   =", 5 == 5 == True)

print("Order (high to low): ** , unary -, * / // %, + -, << >>, &, ^, |, comparisons, not, and, or")
''',
  ["Write expressions that mix several operators", "Print the result of each", "Compare with parenthesised versions", "Show right-associative ** and left-associative -", "Print the precedence order"],
  "Operator precedence decides which operator is applied first. Multiplication runs before addition, ** runs before unary minus and is right-associative, and comparison operators bind tighter than not, and, or. Parentheses always override the default order and make code easier to read.",
  ["Arithmetic Operators", "Logical Operators", "Bitwise Operators"], ["precedence", "associativity", "parentheses", "order"]),

Q("Demonstrate == Versus is", "Operators", "Intermediate",
  "Explains value equality (==) versus object identity (is) with lists, strings and small ints.",
  ["==", "is", "id()", "copy"], "equals_vs_is.py",
  r'''
list1 = [10, 20, 30]
list2 = [10, 20, 30]
list3 = list1
list4 = list1.copy()

print("list1 == list2 :", list1 == list2, "(same values)")
print("list1 is list2 :", list1 is list2, "(different objects)")
print("list1 is list3 :", list1 is list3, "(same object)")
print("list1 is list4 :", list1 is list4, "(copy is a new object)")

# Numbers: equal values may or may not be the same object
x = 1000
y = int("1000")
print("x == y :", x == y)
print("x is y :", x is y, "(do not rely on this!)")

# 1 == 1.0 but they are different types
print("1 == 1.0 :", 1 == 1.0, "| 1 is 1.0 :", 1 is 1.0 if False else False)
print("Rule: use == to compare values, use is only for None/True/False.")
''',
  ["Create lists with equal values", "Compare with == and is", "Create an alias and a copy", "Show int equality versus identity", "State the rule of thumb"],
  "== asks whether two objects have equal values, while is asks whether they are the very same object. Two separate lists with the same items are == but not is. An alias is the same object, a copy is not. Because Python may reuse small objects, never rely on is to compare numbers or strings.",
  ["Identity Operators", "Relational Operators"], ["equality", "identity", "is", "compare"]),

Q("Demonstrate in Versus not in", "Operators", "Beginner",
  "Contrasts in and not in to validate choices and find missing items.",
  ["in", "not in", "validation"], "in_vs_not_in.py",
  r'''
allowed_commands = ["start", "stop", "pause"]
banned_words = {"spam", "scam"}

command = input("Enter command: ").strip().lower()
if command in allowed_commands:
    print(f"'{command}' accepted")
if command not in allowed_commands:
    print(f"'{command}' is not a valid command")

sentence = "free spam offer"
clean = [w for w in sentence.split() if w not in banned_words]
print("Cleaned sentence:", " ".join(clean))

required = {"name", "email", "phone"}
provided = {"name", "email"}
missing = [field for field in sorted(required) if field not in provided]
print("Missing fields:", missing)
print("not (x in y) is the same as x not in y:", (not ("a" in "xyz")) == ("a" not in "xyz"))
''',
  ["Read a command from the user", "Accept it if in the allowed list, reject if not in", "Filter banned words using not in", "List missing fields with not in", "Show that not (x in y) equals x not in y"],
  "in is True when a value is found and not in is True when it is absent; they are exact opposites. The program uses in to accept valid commands and not in to reject, to filter out unwanted words and to find missing form fields. x not in y is the preferred, more readable form of not (x in y).",
  ["Membership Operators"], ["in", "not in", "membership", "validation"], si="Pause", kind="Interactive"),
]
