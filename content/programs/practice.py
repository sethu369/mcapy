"""Practice questions (60) for MCA 102 A - Programming in Python."""


def Q(title, unit, topic, difficulty, description, hint, solution, sampleInput="", args=None):
    return dict(title=title, unit=unit, topic=topic, difficulty=difficulty,
                description=description, hint=hint, sampleInput=sampleInput,
                args=args or [], solution=solution.strip("\n") + "\n")


PRACTICE = [
# ---------------------------------------------------------------- UNIT 1
Q("Check the Python Major Version", 1, "Introduction to Python", "Beginner",
  "Write a program that uses the sys module to find the major version of the running interpreter. Print 'Python 3 detected' if the major version is 3, otherwise print 'Different major version'.",
  "sys.version_info.major gives the major version number.",
  r'''
import sys

# version_info is a named tuple: (major, minor, micro, ...)
major = sys.version_info.major
if major == 3:
    print("Python 3 detected")
else:
    print("Different major version")
'''),
Q("Dynamic Typing Demonstration", 1, "Features of Python", "Beginner",
  "Write a program to show that Python is dynamically typed. Assign an int, a float, a string and a list to the same variable one after another and print the value together with its type each time.",
  "Use type(x).__name__ to print the type name.",
  r'''
# Python decides the type at run time, so one name can refer to any object
x = 10
print(x, type(x).__name__)
x = 3.5
print(x, type(x).__name__)
x = "Python"
print(x, type(x).__name__)
x = [1, 2, 3]
print(x, type(x).__name__)
'''),
Q("Tokens of a Python Statement", 1, "Components of a Python Program", "Intermediate",
  "Write a program that breaks the statement 'total = price * 2 + 5' into tokens using the tokenize module and prints each token with its type name (NAME, OP, NUMBER).",
  "Use tokenize.generate_tokens with io.StringIO(...).readline and tokenize.tok_name.",
  r'''
import io
import tokenize

statement = "total = price * 2 + 5"

# generate_tokens reads the source line by line and yields token objects
for tok in tokenize.generate_tokens(io.StringIO(statement).readline):
    kind = tokenize.tok_name[tok.type]
    # skip the end-of-line / end-of-file helper tokens
    if kind in ("NEWLINE", "ENDMARKER", "NL"):
        continue
    print(f"{kind:<8} {tok.string}")
'''),
Q("Peek Inside Bytecode (PVM)", 1, "Python Virtual Machine (PVM)", "Intermediate",
  "Python first compiles source code to bytecode and the PVM executes it. Write a program that compiles the expression 'a + b * 2' with compile(), prints the variable names used in the bytecode, and then executes it with a=3, b=4.",
  "A compiled code object has co_names; eval() can run it with a dictionary of variables.",
  r'''
source = "a + b * 2"

# Step 1: compile the source to a code object (bytecode)
code_obj = compile(source, "<string>", "eval")

# Step 2: inspect what the compiler found
print("Names used:", sorted(code_obj.co_names))
print("Bytecode is bytes:", isinstance(code_obj.co_code, bytes))

# Step 3: the PVM executes the bytecode
print("Result:", eval(code_obj, {"a": 3, "b": 4}))
'''),
Q("Reference Counting of an Object", 1, "Memory Management in Python", "Intermediate",
  "Write a program that shows how Python counts references to an object. Create a list, note its reference count, create two more names referring to it and show the count rises by 2, then delete them and show it falls back.",
  "sys.getrefcount() always includes one temporary reference, so compare differences, not absolute values.",
  r'''
import sys

data = [1, 2, 3]
base = sys.getrefcount(data)

alias1 = data
alias2 = data
print("Increase after two aliases:", sys.getrefcount(data) - base)

del alias1
del alias2
print("Increase after deleting them:", sys.getrefcount(data) - base)
'''),
Q("Object Identity with id()", 1, "Memory Management in Python", "Beginner",
  "Write a program to show that two names bound to the same list share one memory address (id) while a copy gets a different one. Print True/False for each comparison.",
  "Use id() and list.copy().",
  r'''
a = [10, 20, 30]
b = a            # same object, new name
c = a.copy()     # new object with the same contents

print("a and b same object:", id(a) == id(b))
print("a and c same object:", id(a) == id(c))
print("a and c equal values:", a == c)
'''),
Q("Cyclic Garbage Collection", 1, "Garbage Collection in Python", "Advanced",
  "Create two objects that refer to each other (a reference cycle), delete the names pointing to them and use the gc module to prove that the garbage collector reclaims them. Print whether at least one object was collected.",
  "gc.collect() returns the number of unreachable objects found.",
  r'''
import gc


class Node:
    def __init__(self):
        self.other = None


gc.disable()          # stop automatic collection so we control it
gc.collect()          # clean anything already waiting

a = Node()
b = Node()
a.other = b           # a -> b
b.other = a           # b -> a  (cycle: reference counts never reach zero)

del a, b              # no names left, but the cycle keeps them alive
found = gc.collect()  # the cyclic collector breaks the cycle
print("Cycle collected:", found > 0)
gc.enable()
'''),
Q("Weak References and Object Lifetime", 1, "Garbage Collection in Python", "Advanced",
  "Write a program using the weakref module to show that an object is destroyed as soon as its last strong reference is deleted. Print the weak reference's target before and after the deletion.",
  "weakref.ref(obj)() returns the object, or None once it has been freed.",
  r'''
import weakref


class Resource:
    def __init__(self, name):
        self.name = name


r = Resource("file-handle")
weak = weakref.ref(r)          # does not increase the reference count

print("Before delete:", weak().name)
del r                          # reference count becomes zero -> object freed
print("After delete:", weak())
'''),
Q("Check Whether Modules Are Installed", 1, "Verifying Installed Packages", "Beginner",
  "Write a program that checks whether the modules 'json', 'math' and 'not_a_real_package' are available, using importlib.util.find_spec, and prints 'Installed' or 'Not installed' for each.",
  "find_spec returns None when the module cannot be found.",
  r'''
import importlib.util

for name in ["json", "math", "not_a_real_package"]:
    spec = importlib.util.find_spec(name)
    status = "Installed" if spec is not None else "Not installed"
    print(f"{name}: {status}")
'''),
Q("Verify the Python Interpreter Path", 1, "Verifying the Path to Python", "Beginner",
  "Write a program that confirms the interpreter path stored in sys.executable exists on disk and is a file, and that the module search path sys.path is a non-empty list.",
  "Use os.path.isfile() and len().",
  r'''
import os
import sys

print("Interpreter file exists:", os.path.isfile(sys.executable))
print("Module search path is a list:", isinstance(sys.path, list))
print("Search path is not empty:", len(sys.path) > 0)
'''),
Q("Reserved Words in Python", 1, "Python Fundamentals", "Beginner",
  "Write a program that uses the keyword module to test whether each of the words 'if', 'Print', 'class', 'sum' and 'lambda' is a reserved word, and prints the answer for every word.",
  "keyword.iskeyword(word) returns True for reserved words.",
  r'''
import keyword

for word in ["if", "Print", "class", "sum", "lambda"]:
    print(f"{word:<7} reserved: {keyword.iskeyword(word)}")
'''),
Q("Summarise Data with a pandas Series", 1, "Installing pandas", "Intermediate",
  "Write a program that creates a pandas Series of five exam marks indexed by subject names, and prints the Series, its mean, and the subject with the highest mark. (Requires pandas.)",
  "Series.mean() and Series.idxmax() do the work.",
  r'''
# Requires: pip install pandas
import pandas as pd

marks = pd.Series([78, 85, 62, 90, 71],
                  index=["Python", "Maths", "DBMS", "Networks", "OS"])

print(marks)
print("Mean mark:", marks.mean())
print("Best subject:", marks.idxmax())
'''),
# ---------------------------------------------------------------- UNIT 2
Q("Comments and Docstrings", 2, "Comments in Python", "Beginner",
  "Write a program with a single-line comment, a multi-line comment block and a function that has a docstring. Call the function and print its docstring using __doc__.",
  "A docstring is the first string literal inside the function body.",
  r'''
# This is a single-line comment
# Multi-line comments are
# just several lines starting with '#'


def square(n):
    """Return the square of n."""
    return n * n


print(square(7))
print(square.__doc__)
'''),
Q("Identify Data Types", 2, "Data types in Python", "Beginner",
  "Write a program that stores values 25, 3.14, 'MCA', True, 4+2j, None and (1, 2) in a list and prints each value along with its data type name.",
  "Loop over the list and use type(v).__name__.",
  r'''
values = [25, 3.14, "MCA", True, 4 + 2j, None, (1, 2)]

for v in values:
    print(f"{v!r:<8} -> {type(v).__name__}")
'''),
Q("Slicing a Sequence", 2, "Sequences in Python", "Beginner",
  "Write a program that reads a string and prints its first three characters, last three characters, every second character and the string reversed using slicing.",
  "Slicing syntax is s[start:stop:step]; negative indexes count from the end.",
  r'''
text = input("Enter a word: ")

print("First three:", text[:3])
print("Last three :", text[-3:])
print("Every 2nd  :", text[::2])
print("Reversed   :", text[::-1])
''', "programming"),
Q("Set Operations", 2, "Sets", "Intermediate",
  "Two classes have students {'Asha','Ravi','Meena','John'} and {'Ravi','John','Priya'} enrolled. Write a program to print the students in both, in either, only in the first, and in exactly one of the classes (sorted).",
  "Use &, |, - and ^ on sets, and sorted() for stable output.",
  r'''
class_a = {"Asha", "Ravi", "Meena", "John"}
class_b = {"Ravi", "John", "Priya"}

print("In both       :", sorted(class_a & class_b))
print("In either     :", sorted(class_a | class_b))
print("Only in A     :", sorted(class_a - class_b))
print("In exactly one:", sorted(class_a ^ class_b))
'''),
Q("Numeric Literals in Different Bases", 2, "Literals", "Intermediate",
  "Write a program that shows the same number 45 written as decimal, binary (0b), octal (0o) and hexadecimal (0x) literals, and prints the decimal value of each. Also convert 45 back into the three other bases using bin(), oct() and hex().",
  "Literals are 0b101101, 0o55 and 0x2D for 45.",
  r'''
dec = 45
bina = 0b101101
octa = 0o55
hexa = 0x2D

print("All equal 45:", dec == bina == octa == hexa)
print("Binary     :", bin(dec))
print("Octal      :", oct(dec))
print("Hexadecimal:", hex(dec))
'''),
Q("Area of a Circle Using a Constant", 2, "Constants", "Beginner",
  "Python has no true constants, so by convention they are written in capital letters. Write a program that reads a radius, uses the constant PI = 3.14159 and prints the area and circumference to two decimals.",
  "Area = PI * r * r, circumference = 2 * PI * r.",
  r'''
PI = 3.14159   # written in capitals: a constant by convention

radius = float(input("Enter radius: "))
print(f"Area          = {PI * radius ** 2:.2f}")
print(f"Circumference = {2 * PI * radius:.2f}")
''', "5"),
Q("Palindrome and Vowel Count", 2, "Strings and Characters", "Intermediate",
  "Write a program that reads a string and prints the number of vowels in it and whether it is a palindrome (ignore case).",
  "Compare the lowercase string with its reverse s[::-1].",
  r'''
text = input("Enter a string: ").strip().lower()

vowels = sum(1 for ch in text if ch in "aeiou")
print("Vowels:", vowels)

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
''', "Madam"),
Q("A User-defined Data Type Using a Class", 2, "User-defined Data types", "Advanced",
  "Define a user-defined data type Point (with x and y) using a class and an Enum Color with RED, GREEN, BLUE. Create a Point (3, 4), print its distance from the origin and print the name and value of Color.GREEN.",
  "Use enum.Enum and math.hypot or ** 0.5.",
  r'''
from enum import Enum


class Point:
    """A user-defined type representing a point in 2-D."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


p = Point(3, 4)
print("Distance from origin:", p.distance_from_origin())
print(Color.GREEN.name, Color.GREEN.value)
'''),
Q("Valid Identifiers", 2, "Identifiers and Reserved words", "Intermediate",
  "Write a program that reads names (one per line, ending with 'end') and reports for each one whether it is a valid Python identifier and not a reserved word.",
  "str.isidentifier() checks the naming rules; keyword.iskeyword() checks reserved words.",
  r'''
import keyword

while True:
    name = input()
    if name == "end":
        break
    if name.isidentifier() and not keyword.iskeyword(name):
        print(f"{name}: valid")
    else:
        print(f"{name}: invalid")
''', "total_marks\n2ndYear\nclass\n_temp\nmy-var\nend"),
Q("Arithmetic Operators Calculator", 2, "Arithmetic Operators", "Beginner",
  "Write a program that reads two integers and prints their sum, difference, product, true division, floor division, remainder and the first raised to the power of the second.",
  "Operators are + - * / // % **.",
  r'''
a = int(input("First number : "))
b = int(input("Second number: "))

print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * b  =", a * b)
print("a / b  =", a / b)
print("a // b =", a // b)
print("a % b  =", a % b)
print("a ** b =", a ** b)
''', "17\n5"),
Q("Assignment and Unary Minus Operators", 2, "Assignment Operators", "Beginner",
  "Start with x = 20 and apply +=, -=, *=, //=, %= and **= (with suitable operands), printing x after each. Finally use the unary minus operator to print -x.",
  "x += 5 is shorthand for x = x + 5.",
  r'''
x = 20
x += 5
print("after += 5  :", x)
x -= 3
print("after -= 3  :", x)
x *= 2
print("after *= 2  :", x)
x //= 4
print("after //= 4 :", x)
x %= 7
print("after %= 7  :", x)
x **= 3
print("after **= 3 :", x)
print("unary minus :", -x)
'''),
Q("Swap and Test Using Bitwise Operators", 2, "Bitwise Operators", "Advanced",
  "Write a program that reads two integers, swaps them using only the XOR operator (no temporary variable), and then tells whether the first original number is a power of two using n & (n - 1).",
  "a ^= b; b ^= a; a ^= b swaps without a temp.",
  r'''
a = int(input("a: "))
b = int(input("b: "))
original_a = a

# XOR swap
a = a ^ b
b = a ^ b
a = a ^ b
print("After swap: a =", a, "b =", b)

# A power of two has exactly one bit set, so n & (n-1) is 0
if original_a > 0 and original_a & (original_a - 1) == 0:
    print(original_a, "is a power of two")
else:
    print(original_a, "is not a power of two")
''', "16\n7"),
# ---------------------------------------------------------------- UNIT 3
Q("Sum and Average of Three Numbers", 3, "Input Statements", "Beginner",
  "Write a program that reads three numbers using input() and prints their sum and average (to 2 decimal places).",
  "input() returns text, so convert with float().",
  r'''
n1 = float(input("Enter first number : "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number : "))

total = n1 + n2 + n3
print("Sum     =", total)
print(f"Average = {total / 3:.2f}")
''', "12\n15.5\n20"),
Q("Formatted Output Using print()", 3, "Output statements", "Beginner",
  "Write a program that prints the values 1, 2, 3 on one line separated by hyphens, then prints 'Hello' and 'World' on the same line using the end parameter, and finally prints a price of 99.5 formatted to two decimals in a width of 10.",
  "print() has sep and end arguments; use an f-string format spec like :10.2f.",
  r'''
print(1, 2, 3, sep="-")
print("Hello", end=" ")
print("World")
price = 99.5
print(f"Price: {price:10.2f}")
'''),
Q("Add Numbers Passed on the Command Line", 3, "Command Line Arguments", "Intermediate",
  "Write a program that reads integers given as command-line arguments and prints their count and sum. If no arguments are given, print a usage message.",
  "Arguments are in sys.argv[1:] as strings.",
  r'''
import sys

numbers = sys.argv[1:]
if not numbers:
    print("Usage: python prog.py num1 num2 ...")
else:
    values = [int(n) for n in numbers]
    print("Count:", len(values))
    print("Sum  :", sum(values))
''', "", ["10", "20", "30", "40"]),
Q("Leap Year Checker", 3, "if … else Statement", "Beginner",
  "Write a program that reads a year and prints whether it is a leap year. A year is a leap year if it is divisible by 400, or divisible by 4 but not by 100.",
  "Combine conditions with and / or.",
  r'''
year = int(input("Enter a year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
''', "2024"),
Q("Grade Calculator", 3, "if … elif … else Statement", "Beginner",
  "Write a program that reads marks (0-100) and prints the grade: O for 90 and above, A for 80-89, B for 70-79, C for 60-69, D for 50-59 and F for below 50. Print 'Invalid marks' if the input is out of range.",
  "Test the invalid range first, then check the grades from highest to lowest.",
  r'''
marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade O")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 50:
    print("Grade D")
else:
    print("Grade F")
''', "83"),
Q("Reverse a Number and Sum Its Digits", 3, "The while Loop", "Intermediate",
  "Write a program that reads a positive integer and uses a while loop to print the sum of its digits and the number with its digits reversed.",
  "Use % 10 to take the last digit and // 10 to drop it.",
  r'''
n = int(input("Enter a positive integer: "))

digit_sum = 0
reversed_num = 0
while n > 0:
    digit = n % 10
    digit_sum += digit
    reversed_num = reversed_num * 10 + digit
    n //= 10

print("Sum of digits:", digit_sum)
print("Reversed     :", reversed_num)
''', "12345"),
Q("Multiplication Table and Prime Test", 3, "The for Loop", "Beginner",
  "Write a program that reads a number n and prints its multiplication table from 1 to 10 using a for loop.",
  "Use range(1, 11).",
  r'''
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} x {i:2} = {n * i}")
''', "7"),
Q("Prime Numbers Using the else Suite", 3, "The else Suite", "Intermediate",
  "Write a program that prints all prime numbers between 2 and a limit read from the user. Use the else clause of the inner for loop to detect primes.",
  "A loop's else block runs only if the loop finished without break.",
  r'''
limit = int(input("Print primes up to: "))

for num in range(2, limit + 1):
    for d in range(2, int(num ** 0.5) + 1):
        if num % d == 0:
            break          # found a divisor -> not prime
    else:
        # runs only when the for loop was never broken
        print(num, end=" ")
print()
''', "30"),
Q("Number Pyramid Pattern", 3, "Nested Loops", "Intermediate",
  "Write a program that reads the number of rows n and prints a pyramid of numbers such that row i contains the numbers 1 to i, centered with spaces.",
  "Use an outer loop for rows and an inner loop for the numbers; str.center() or leading spaces help.",
  r'''
rows = int(input("Number of rows: "))

for i in range(1, rows + 1):
    line = " ".join(str(j) for j in range(1, i + 1))
    print(line.center(rows * 2 - 1))
''', "5"),
Q("Guessing Game with break and continue", 3, "The break Statement", "Intermediate",
  "A secret number is 42. Write a program that reads guesses until the correct number is entered (use while True and break). Ignore negative guesses with continue and tell the user 'higher' or 'lower' otherwise. Finally print the number of valid attempts.",
  "continue skips the rest of the loop body; break leaves the loop.",
  r'''
SECRET = 42
attempts = 0

while True:
    guess = int(input("Guess: "))
    if guess < 0:
        print("Negative numbers are ignored")
        continue            # do not count this attempt
    attempts += 1
    if guess == SECRET:
        print("Correct!")
        break               # leave the infinite loop
    elif guess < SECRET:
        print("higher")
    else:
        print("lower")

print("Valid attempts:", attempts)
''', "10\n-5\n60\n42"),
Q("Function Returning a Result with Early Exit", 3, "The return Statement", "Intermediate",
  "Write a function first_negative(numbers) that returns the first negative number in a list or None if there is none, using return inside a loop. Test it on two lists and print the results. Also use pass in an empty function stub.",
  "return ends the function immediately.",
  r'''
def first_negative(numbers):
    for n in numbers:
        if n < 0:
            return n        # exit as soon as one is found
    return None


def todo_later():
    pass                    # placeholder: does nothing yet


print(first_negative([4, 9, -3, 8, -1]))
print(first_negative([1, 2, 3]))
todo_later()
'''),
Q("Arrays Using the array Module and NumPy", 3, "Creating an Array", "Advanced",
  "Create an integer array [5, 10, 15, 20] using the array module and append and remove items. Then create a 2 x 3 NumPy array, print its shape, number of dimensions, size and the result of adding 10 to every element. (Requires numpy.)",
  "array('i', [...]) holds one type; ndarray has attributes shape, ndim and size.",
  r'''
# Requires: pip install numpy
import array
import numpy as np

arr = array.array("i", [5, 10, 15, 20])
arr.append(25)
arr.remove(10)
print("array module:", arr.tolist())

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Shape :", matrix.shape)
print("Dims  :", matrix.ndim)
print("Size  :", matrix.size)
print("Plus 10:")
print(matrix + 10)
'''),
# ---------------------------------------------------------------- UNIT 4
Q("List Operations", 4, "Methods to Process Lists", "Beginner",
  "Start with the list [30, 10, 20]. Write a program that appends 40, inserts 5 at the front, removes 20, pops the last element and then prints the list, its length, and the index of 10.",
  "Use append, insert, remove, pop and index.",
  r'''
nums = [30, 10, 20]
nums.append(40)
nums.insert(0, 5)
nums.remove(20)
last = nums.pop()

print("Popped:", last)
print("List  :", nums)
print("Length:", len(nums))
print("Index of 10:", nums.index(10))
'''),
Q("Concatenate, Repeat and Search Lists", 4, "Concatenation of Two Lists", "Beginner",
  "Write a program that joins [1, 2, 3] and [4, 5], repeats [0, 1] three times and checks whether the values 4 and 9 are present in the joined list using the in operator.",
  "Use + for concatenation, * for repetition and in for membership.",
  r'''
joined = [1, 2, 3] + [4, 5]
repeated = [0, 1] * 3

print("Joined  :", joined)
print("Repeated:", repeated)
print("4 in joined:", 4 in joined)
print("9 in joined:", 9 in joined)
'''),
Q("Sort Students by Marks", 4, "Sorting", "Intermediate",
  "A list of (name, marks) tuples is given. Write a program to print the list sorted by marks in descending order and, for equal marks, by name in ascending order.",
  "Use sorted() with key=lambda s: (-s[1], s[0]).",
  r'''
students = [("Ravi", 78), ("Asha", 92), ("Meena", 78), ("John", 85)]

ranked = sorted(students, key=lambda s: (-s[1], s[0]))
for position, (name, marks) in enumerate(ranked, start=1):
    print(position, name, marks)
'''),
Q("Matrix Addition with Nested Lists", 4, "Nested Lists", "Intermediate",
  "Write a program that adds two 3x3 matrices stored as nested lists and prints the resulting matrix row by row.",
  "Use two nested loops or a nested list comprehension.",
  r'''
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result = [[A[i][j] + B[i][j] for j in range(3)] for i in range(3)]

for row in result:
    print(row)
'''),
Q("Tuple Operations", 4, "Operations on Tuples", "Beginner",
  "Write a program that creates the tuple (4, 8, 15, 16, 23, 42), prints its first and last elements, a slice of the middle four, and shows that a tuple cannot be modified by catching the resulting error. Also print its max, min and sum.",
  "Assigning to t[0] raises TypeError.",
  r'''
t = (4, 8, 15, 16, 23, 42)

print("First:", t[0], "Last:", t[-1])
print("Middle four:", t[1:5])
print("max/min/sum:", max(t), min(t), sum(t))

try:
    t[0] = 100
except TypeError as error:
    print("Tuples are immutable:", error)
'''),
Q("Nested Tuples and Unpacking", 4, "Nested Tuples", "Intermediate",
  "Given the nested tuple (('Asha', (80, 90)), ('Ravi', (70, 60))), write a program that unpacks every student's name and two marks and prints the name with the average mark.",
  "Unpack directly in the for statement: for name, (m1, m2) in data.",
  r'''
data = (("Asha", (80, 90)), ("Ravi", (70, 60)))

for name, (m1, m2) in data:
    print(f"{name}: average = {(m1 + m2) / 2}")
'''),
Q("Word Frequency Counter", 4, "Operations on Dictionaries", "Intermediate",
  "Write a program that reads a sentence and prints how many times each word occurs (case-insensitive), in alphabetical order of the words.",
  "Use dict.get(word, 0) + 1 to count.",
  r'''
sentence = input("Enter a sentence: ").lower()

freq = {}
for word in sentence.split():
    freq[word] = freq.get(word, 0) + 1

for word in sorted(freq):
    print(word, freq[word])
''', "the cat and the dog and the bird"),
Q("Dictionary Methods Tour", 4, "Dictionary Methods", "Intermediate",
  "Create the dictionary {'name': 'Asha', 'age': 21}. Write a program that adds 'city' with update(), prints keys, values and items, removes 'age' with pop() and uses setdefault() to add 'country' with value 'India'.",
  "keys(), values(), items(), update(), pop(), setdefault().",
  r'''
student = {"name": "Asha", "age": 21}
student.update({"city": "Pune"})

print("Keys  :", list(student.keys()))
print("Values:", list(student.values()))
print("Items :", list(student.items()))

removed = student.pop("age")
print("Removed age:", removed)
student.setdefault("country", "India")
print(student)
'''),
Q("Pass a Dictionary to a Function", 4, "Passing Dictionaries to Functions", "Intermediate",
  "Write a function apply_discount(prices, percent) that receives a dictionary of item prices and reduces every price by the given percent in place. Show that the caller's dictionary changes.",
  "Dictionaries are mutable, so changes inside the function are visible outside.",
  r'''
def apply_discount(prices, percent):
    for item in prices:
        prices[item] = round(prices[item] * (100 - percent) / 100, 2)


shop = {"pen": 10.0, "book": 250.0, "bag": 800.0}
print("Before:", shop)
apply_discount(shop, 10)
print("After :", shop)
'''),
Q("Ordered Dictionary Operations", 4, "Ordered Dictionaries", "Advanced",
  "Using collections.OrderedDict, store the keys 'a', 'b', 'c', 'd' with values 1-4. Move 'a' to the end, pop the first item with popitem(last=False), and print the dictionary after each step. Also show that two OrderedDicts with the same items in a different order are not equal.",
  "OrderedDict has move_to_end() and popitem(last=False); equality between OrderedDicts considers order.",
  r'''
from collections import OrderedDict

od = OrderedDict([("a", 1), ("b", 2), ("c", 3), ("d", 4)])
print("Start    :", list(od.items()))

od.move_to_end("a")
print("Move a   :", list(od.items()))

first = od.popitem(last=False)
print("Popped   :", first)
print("Remaining:", list(od.items()))

x = OrderedDict([("p", 1), ("q", 2)])
y = OrderedDict([("q", 2), ("p", 1)])
print("Order matters in equality:", x != y)
'''),
Q("Function with Default Arguments", 4, "Defining a Function", "Beginner",
  "Define a function simple_interest(principal, rate=8, years=1) and call it with one, two and three arguments, and once using keyword arguments in a different order.",
  "Parameters with default values must come after those without.",
  r'''
def simple_interest(principal, rate=8, years=1):
    return principal * rate * years / 100


print(simple_interest(10000))
print(simple_interest(10000, 10))
print(simple_interest(10000, 10, 3))
print(simple_interest(years=2, principal=5000, rate=6))
'''),
Q("Return Multiple Values", 4, "Returning Multiple Values from a Function", "Intermediate",
  "Write a function stats(numbers) that returns the minimum, maximum and average of a list as three values. Call it and unpack the result into three variables.",
  "A function can return a tuple; the caller can unpack it.",
  r'''
def stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)


low, high, avg = stats([12, 45, 7, 33, 21])
print("Minimum:", low)
print("Maximum:", high)
print("Average:", avg)
'''),
# ---------------------------------------------------------------- UNIT 5
Q("Class and Objects: Student", 5, "Classes and Objects", "Beginner",
  "Define a class Student with name and marks attributes, an __init__ method and a method display(). Create two objects and call display() on each.",
  "Self refers to the object on which the method is called.",
  r'''
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")


s1 = Student("Asha", 88)
s2 = Student("Ravi", 74)
s1.display()
s2.display()
'''),
Q("Encapsulation with a Bank Account", 5, "Encapsulation", "Intermediate",
  "Write a BankAccount class with a private balance, and methods deposit(), withdraw() and get_balance(). Withdrawal beyond the balance must be refused with a message. Perform a few operations and print the balance.",
  "Prefix the attribute with double underscore to make it private (name mangling).",
  r'''
class BankAccount:
    def __init__(self, opening):
        self.__balance = opening      # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
acc.withdraw(5000)
print("Balance:", acc.get_balance())
'''),
Q("Single and Multilevel Inheritance", 5, "Inheritance", "Intermediate",
  "Create a base class Person (name), a class Employee derived from Person (adds salary) and a class Manager derived from Employee (adds department). Use super() to initialise parents and print the details of a manager.",
  "Call super().__init__(...) in each child constructor.",
  r'''
class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show(self):
        print(f"{self.name} manages {self.department} and earns {self.salary}")


m = Manager("Kavya", 90000, "Sales")
m.show()
print(isinstance(m, Person))
'''),
Q("Method Overriding and Polymorphism", 5, "Polymorphism", "Intermediate",
  "Write classes Circle and Rectangle that both define area(). Put objects of both in a list, loop through it and print each area using the same call, showing polymorphism.",
  "Different classes, same method name; Python picks the right one at run time.",
  r'''
class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return round(3.14159 * self.r ** 2, 2)


class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


shapes = [Circle(3), Rectangle(4, 5), Circle(1)]
for s in shapes:
    print(type(s).__name__, "area =", s.area())
'''),
Q("Abstract Base Class for Shapes", 5, "Abstract Classes and Interfaces", "Advanced",
  "Using the abc module, define an abstract class Shape with an abstract method area() and subclasses Square and Triangle. Show that Shape itself cannot be instantiated by catching the error, and print the areas of the concrete shapes.",
  "Use ABC and @abstractmethod; instantiating an abstract class raises TypeError.",
  r'''
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        """Every shape must implement this."""


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


try:
    Shape()
except TypeError:
    print("Cannot instantiate abstract class Shape")

print("Square  :", Square(4).area())
print("Triangle:", Triangle(6, 3).area())
'''),
Q("Exception Handling and Custom Exception", 5, "Exceptions", "Intermediate",
  "Write a program that reads an age and raises a custom exception InvalidAgeError if it is negative or above 120. Handle ValueError for non-numeric input as well, and always print 'Done' using finally. Read several lines from the input and process each.",
  "Define class InvalidAgeError(Exception) and use try / except / finally.",
  r'''
class InvalidAgeError(Exception):
    pass


def check_age(text):
    age = int(text)                      # may raise ValueError
    if age < 0 or age > 120:
        raise InvalidAgeError(f"{age} is not a realistic age")
    return age


for line in ["25", "abc", "-4", "130"]:
    try:
        print("Valid age:", check_age(line))
    except ValueError:
        print(f"'{line}' is not a number")
    except InvalidAgeError as error:
        print("Error:", error)
    finally:
        print("Done")
'''),
Q("Singly Linked List", 5, "Linked list", "Advanced",
  "Implement a singly linked list with a Node class and methods add_at_end(value), delete(value) and display(). Add 10, 20, 30, 40, delete 20 and display the list as 10 -> 30 -> 40.",
  "Keep a head pointer and walk node.next until it is None.",
  r'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_end(self, value):
        new = Node(value)
        if self.head is None:
            self.head = new
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new

    def delete(self, value):
        cur, prev = self.head, None
        while cur:
            if cur.data == value:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                return True
            prev, cur = cur, cur.next
        return False

    def display(self):
        items, cur = [], self.head
        while cur:
            items.append(str(cur.data))
            cur = cur.next
        print(" -> ".join(items))


ll = LinkedList()
for v in [10, 20, 30, 40]:
    ll.add_at_end(v)
ll.delete(20)
ll.display()
'''),
Q("Stack: Balanced Brackets", 5, "stacks", "Advanced",
  "Write a program that uses a list as a stack to check whether the brackets in an expression read from input are balanced. Handle (), [] and {}.",
  "Push opening brackets, and on a closing bracket pop and compare.",
  r'''
expr = input("Enter expression: ")

pairs = {")": "(", "]": "[", "}": "{"}
stack = []
balanced = True

for ch in expr:
    if ch in "([{":
        stack.append(ch)                 # push
    elif ch in pairs:
        if not stack or stack.pop() != pairs[ch]:
            balanced = False
            break

if stack:
    balanced = False

print("Balanced" if balanced else "Not balanced")
''', "{[a + (b * c)] - d}"),
Q("Queue Simulation Using a List Class", 5, "Queues", "Intermediate",
  "Implement a Queue class with enqueue(), dequeue(), is_empty() and size() using a list. Add three customers, serve one, and print who is next and how many are waiting.",
  "FIFO: add at the end, remove from index 0.",
  r'''
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


q = Queue()
for customer in ["Asha", "Ravi", "Meena"]:
    q.enqueue(customer)

print("Serving:", q.dequeue())
print("Next   :", q.items[0])
print("Waiting:", q.size())
'''),
Q("Double-ended Queue with deque", 5, "Dequeues", "Intermediate",
  "Use collections.deque to add 2 and 3 at the right end, 1 at the left end, then remove one element from each end. Print the deque after each operation. Then rotate [1, 2, 3, 4, 5] by 2 positions.",
  "append, appendleft, pop, popleft and rotate.",
  r'''
from collections import deque

d = deque()
d.append(2)
d.append(3)
d.appendleft(1)
print("After adds    :", list(d))

print("Popped right  :", d.pop())
print("Popped left   :", d.popleft())
print("Remaining     :", list(d))

r = deque([1, 2, 3, 4, 5])
r.rotate(2)
print("Rotated by 2  :", list(r))
'''),
Q("Date Difference and Formatting", 5, "Date and Time", "Intermediate",
  "Write a program using the datetime module that, for the fixed date 15 August 2024, prints the date in DD-MM-YYYY format, the weekday name, the date 30 days later, and the number of days between this date and 1 January 2025.",
  "Use datetime.date, strftime and timedelta.",
  r'''
from datetime import date, timedelta

d = date(2024, 8, 15)
print("Formatted:", d.strftime("%d-%m-%Y"))
print("Weekday  :", d.strftime("%A"))
print("+30 days :", d + timedelta(days=30))
print("Days to 1 Jan 2025:", (date(2025, 1, 1) - d).days)
'''),
Q("Student Records with SQLite", 5, "Python’s Database Connectivity", "Advanced",
  "Write a program that creates an in-memory SQLite database with a table student(roll, name, marks), inserts three records using a parameterised query, and then prints all students who scored above 75 ordered by marks (highest first).",
  "Use sqlite3.connect(':memory:'), executemany with ? placeholders, and ORDER BY ... DESC.",
  r'''
import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("CREATE TABLE student (roll INTEGER PRIMARY KEY, name TEXT, marks INTEGER)")

records = [(1, "Asha", 88), (2, "Ravi", 72), (3, "Meena", 81)]
cur.executemany("INSERT INTO student VALUES (?, ?, ?)", records)
conn.commit()

cur.execute("SELECT roll, name, marks FROM student WHERE marks > ? ORDER BY marks DESC", (75,))
for roll, name, marks in cur.fetchall():
    print(roll, name, marks)

conn.close()
'''),
]
