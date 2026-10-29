import sys; sys.path.insert(0, __file__.rsplit("/", 2)[0])   # so `schema` imports
from schema import P

PROGRAMS = []

# ---------------------------------------------------------------- Input and Output (1-9)
PROGRAMS += [
P(title="Input and Output Using input()", category="Input and Output", difficulty="Beginner",
  description="Reads a name and an age from the keyboard with input() and displays a greeting.",
  concepts=["input()", "print()", "int()", "try/except"], filename="input_output_basic.py", kind="Interactive",
  code=r'''
# Reading data with input() and showing it with print()
name = input("Enter your name: ")          # input() always returns a string

try:
    age = int(input("Enter your age: "))   # convert the text to an integer
except ValueError:
    print("Age must be a whole number.")
else:
    print("Hello,", name + "!")
    print("You are", age, "years old.")
    print("Next year you will be", age + 1)
''',
  algorithm=["Display a prompt and read the name with input()", "Read the age as text and convert it with int()",
             "If conversion fails, show an error message", "Otherwise print the greeting using print()"],
  explanation="input() shows a prompt, waits for the user to type a line and returns it as a string. The age is converted to an integer with int() so arithmetic can be done; a try/except block handles non-numeric text. print() then displays the results on the screen, separating the items with spaces.",
  sample_input="Asha\n21", tags=["input", "print", "int", "validation"], topics=["Input Statements", "Output statements"]),

P(title="Output Using print()", category="Input and Output", difficulty="Beginner",
  description="Shows the different ways print() can be used: sep, end, multiple values and escape characters.",
  concepts=["print()", "sep", "end", "escape sequences"], filename="print_output.py",
  code=r'''
# Different ways of using print()
print("Hello, World!")
print("Python", "is", "fun")                 # items separated by a space
print("Python", "is", "fun", sep="-")        # custom separator
print("Loading", end="...")                  # no newline at the end
print("done")
print("Line 1\nLine 2")                      # \n = new line
print("Name:\tAsha")                         # \t = tab
print("She said \"Hi\"")                     # escaped quotes
print('It\'s Python')
print("Repeat " * 3)                         # string repetition
print(10 + 5)                                # expression result
print()                                      # blank line
print("End of demo")
''',
  algorithm=["Call print() with a single string", "Pass several values and change sep", "Change end to avoid the newline",
             "Use escape sequences \\n, \\t and \\\"", "Print expressions and a blank line"],
  explanation="print() writes values to the screen. By default it separates the values with a space (sep) and finishes with a new line (end); both can be changed with keyword arguments. Escape sequences such as \\n and \\t insert special characters inside strings. Any expression can be printed, and it is evaluated first.",
  tags=["print", "sep", "end", "escape"], topics=["Output statements"]),

P(title="Display Formatted Output", category="Input and Output", difficulty="Beginner",
  description="Formats numbers and text using the % operator, str.format() and format specifiers.",
  concepts=["format()", "% formatting", "alignment", "precision"], filename="formatted_output.py",
  code=r'''
# Formatted output: three classic techniques
name = "Ravi"
marks = 87.456
rank = 3

# 1. old style % formatting
print("Name: %s, Marks: %.2f, Rank: %d" % (name, marks, rank))

# 2. str.format()
print("Name: {}, Marks: {:.1f}, Rank: {}".format(name, marks, rank))
print("{0} scored {1:.2f}; {0} is rank {2}".format(name, marks, rank))

# 3. width and alignment with format specifiers
print("{:<10}|{:^10}|{:>10}".format("left", "centre", "right"))
print("{:08.2f}".format(marks))        # zero padded width 8
print("{:,}".format(1234567))          # thousands separator
print("{:b} {:o} {:x}".format(10, 10, 255))   # binary, octal, hex

# a small table
print("-" * 24)
for item, price in [("Pen", 10.5), ("Notebook", 45), ("Bag", 899.99)]:
    print("{:<12}{:>10.2f}".format(item, price))
''',
  algorithm=["Store sample values in variables", "Print them using % formatting", "Print them using str.format()",
             "Apply width, alignment and precision specifiers", "Print a small aligned table"],
  explanation="Formatted output makes results neat and readable. %s, %d and %f are placeholders in the old style, while {} placeholders are used with str.format(). Inside the braces, a specifier such as :<10 or :.2f controls width, alignment and decimal places. The loop at the end shows how alignment produces a clean table.",
  tags=["format", "alignment", "precision", "output"], topics=["Output statements"]),

P(title="Demonstrate f-Strings", category="Input and Output", difficulty="Beginner",
  description="Uses f-strings to embed variables, expressions, function calls and format specifiers directly in text.",
  concepts=["f-string", "expressions", "format specifiers"], filename="fstring_demo.py",
  code=r'''
# f-strings (formatted string literals) - available since Python 3.6
name = "Meena"
price = 249.5
qty = 3

print(f"Hello, {name}!")
print(f"Total = {price * qty}")                      # expressions allowed
print(f"Price: {price:.2f}  Qty: {qty:03d}")         # format specifiers
print(f"Name in capitals: {name.upper()}")           # method calls
print(f"{name:>10}|{name:^10}|{name:<10}|")          # alignment
print(f"{1234567.891:,.2f}")                         # thousands separator
print(f"{0.256:.1%}")                                # percentage
print(f"{name=}  {qty=}")                            # self-documenting (3.8+)
print(f"Braces: {{literal}}")                        # escaping braces
width = 12
print(f"{'dynamic':>{width}}")                       # nested field
''',
  algorithm=["Create some variables", "Embed them in strings prefixed with f", "Use expressions and method calls inside {}",
             "Add format specifiers after a colon", "Show {name=} debugging form and brace escaping"],
  explanation="An f-string starts with the letter f and can contain expressions inside curly braces which are evaluated at run time. After a colon you can add the same format specifiers used by format(), for example .2f for two decimals. The {name=} form prints both the expression and its value, and doubling the braces prints a literal brace. f-strings are shorter and faster than older formatting methods.",
  tags=["f-string", "format", "output"], topics=["Output statements"]),

P(title="Demonstrate Multiple Input Values", category="Input and Output", difficulty="Beginner",
  description="Reads several values from one line using split() and map(), and also reads a list of numbers.",
  concepts=["split()", "map()", "multiple assignment", "list"], filename="multiple_input.py", kind="Interactive",
  code=r'''
# Reading multiple values from a single line of input
try:
    a, b = map(int, input("Enter two integers separated by space: ").split())
    print("Sum =", a + b)

    name, city = input("Enter name and city separated by comma: ").split(",")
    print(f"{name.strip()} lives in {city.strip()}")

    numbers = list(map(float, input("Enter any number of values: ").split()))
    print("Numbers:", numbers)
    print("Count  :", len(numbers))
    print("Total  :", sum(numbers))
except ValueError:
    print("Invalid input - please enter the values in the requested format.")
''',
  algorithm=["Read one line and split it into pieces", "Convert each piece with map(int, ...)", "Unpack the pieces into variables",
             "Read a comma separated line and split on ','", "Read many numbers into a list and process them"],
  explanation="input() returns one string, so split() is used to break it into separate words. map() applies int or float to every piece, and the result is unpacked into variables or turned into a list with list(). If the user types the wrong number of values or non-numeric text, a ValueError is raised and handled by the except block.",
  sample_input="15 27\nAsha, Mumbai\n1.5 2.5 3 4", tags=["input", "split", "map", "multiple"], topics=["Input Statements"]),

P(title="Demonstrate Command-Line Arguments Using sys.argv", category="Input and Output", difficulty="Beginner",
  description="Displays the script name, the number of arguments and each argument supplied on the command line.",
  concepts=["sys.argv", "len()", "enumerate()"], filename="sys_argv_demo.py", args=["hello", "42", "python"],
  code=r'''
# Run as:  python sys_argv_demo.py hello 42 python
import sys

print("Script name        :", sys.argv[0])
print("Total arguments    :", len(sys.argv))
print("Arguments (excl. script):", sys.argv[1:])

for position, value in enumerate(sys.argv[1:], start=1):
    print(f"Argument {position}: {value!r} (type {type(value).__name__})")

# every argument is a string - convert when numbers are needed
if len(sys.argv) > 2:
    print("Second argument + 1 =", int(sys.argv[2]) + 1)
''',
  algorithm=["Import the sys module", "Print sys.argv[0], the script name", "Print the number of items in sys.argv",
             "Loop over sys.argv[1:] and print each value with its type", "Convert one argument to int to show conversion"],
  explanation="Command-line arguments are the extra words typed after the script name. Python stores them in the list sys.argv: element 0 is the script name and the remaining elements are the arguments, always as strings. The program lists them with enumerate() and converts one to an integer to show that explicit conversion is required.",
  tags=["sys.argv", "command line", "arguments"], topics=["Command Line Arguments"]),

P(title="Add Two Numbers Using Command-Line Arguments", category="Input and Output", difficulty="Beginner",
  description="Takes two numbers from the command line and prints their sum.",
  concepts=["sys.argv", "float()", "len()"], filename="add_two_cmdline.py", args=["12", "30.5"],
  code=r'''
# Run as:  python add_two_cmdline.py 12 30.5
import sys

if len(sys.argv) != 3:
    print("Usage: python add_two_cmdline.py <number1> <number2>")
else:
    first = float(sys.argv[1])
    second = float(sys.argv[2])
    print(f"{first} + {second} = {first + second}")
''',
  algorithm=["Check that exactly two arguments are supplied", "Convert sys.argv[1] and sys.argv[2] to float", "Add the numbers",
             "Print the result"],
  explanation="The two numbers arrive in sys.argv[1] and sys.argv[2] as text. The program first checks the length of sys.argv so that it can show a usage message when arguments are missing. float() converts the text to numbers, which are then added and displayed.",
  tags=["sys.argv", "add", "command line"], topics=["Command Line Arguments"]),

P(title="Calculate the Sum of Command-Line Arguments", category="Input and Output", difficulty="Beginner",
  description="Adds any number of numeric command-line arguments using a loop.",
  concepts=["sys.argv", "for loop", "float()"], filename="sum_cmdline_args.py", args=["5", "10", "15.5", "20"],
  code=r'''
# Run as:  python sum_cmdline_args.py 5 10 15.5 20
import sys

numbers = sys.argv[1:]            # ignore the script name
if not numbers:
    print("Please supply at least one number.")
else:
    total = 0
    for text in numbers:
        total += float(text)
    print("Arguments :", numbers)
    print("Sum       :", total)
    print("Average   :", total / len(numbers))
''',
  algorithm=["Take the slice sys.argv[1:]", "If it is empty, print a message", "Set total to 0", "Loop over each argument, convert it and add it to total",
             "Print the sum and the average"],
  explanation="sys.argv[1:] gives only the user supplied arguments. A for loop converts each text value with float() and accumulates the total. The average is obtained by dividing by the number of arguments. The program works for any count of numbers.",
  tags=["sys.argv", "sum", "loop"], topics=["Command Line Arguments"]),

P(title="Handle Invalid Command-Line Arguments", category="Input and Output", difficulty="Intermediate",
  description="Shows how to detect missing or non-numeric command-line arguments and report them gracefully (run here with an invalid value).",
  concepts=["sys.argv", "try/except", "ValueError", "sys.exit()"], filename="invalid_cmdline_args.py", args=["10", "abc", "5"],
  code=r'''
# Run as:  python invalid_cmdline_args.py 10 abc 5     ("abc" is invalid)
import sys

def main():
    if len(sys.argv) < 2:
        print("Error: no arguments given.")
        print("Usage: python invalid_cmdline_args.py <num1> <num2> ...")
        return

    valid, invalid = [], []
    for text in sys.argv[1:]:
        try:
            valid.append(float(text))
        except ValueError:
            invalid.append(text)

    if invalid:
        print("Invalid arguments ignored:", invalid)
    if valid:
        print("Valid numbers :", valid)
        print("Sum of valid  :", sum(valid))
    else:
        print("No valid numbers were supplied.")

main()
''',
  algorithm=["Check whether any argument exists and show usage if not", "Loop through the arguments", "Try to convert each one with float()",
             "Collect failures in an invalid list", "Report invalid values and compute the sum of the valid ones"],
  explanation="Users can easily type wrong arguments, so the program never trusts them. Each argument is converted inside try/except; a ValueError means it is not a number and it is stored in a separate list instead of crashing the program. At the end the program reports the ignored values and works with the valid ones. A usage message is displayed when no argument is given.",
  tags=["sys.argv", "validation", "exception", "error handling"], topics=["Command Line Arguments"]),
]

# ---------------------------------------------------------------- Conditional Statements (10-23)
PROGRAMS += [
P(title="Check Whether a Number Is Positive or Negative", category="Conditional Statements", difficulty="Beginner",
  description="Reads a number and tells whether it is positive, negative or zero using if statements.",
  concepts=["if statement", "comparison", "float()"], filename="positive_negative.py", kind="Interactive",
  code=r'''
try:
    number = float(input("Enter a number: "))
    if number > 0:
        print(number, "is positive")
    if number < 0:
        print(number, "is negative")
except ValueError:
    print("Please enter a valid number.")
''',
  algorithm=["Read the number", "If number > 0 print positive", "If number < 0 print negative", "Handle invalid input with except"],
  explanation="The simple if statement executes its block only when the condition is True. Two separate if statements test for positive and negative values. A zero value satisfies neither, so nothing is printed for it (the next programs handle zero). float() allows decimal numbers.",
  sample_input="-7.5", tags=["if", "positive", "negative"], topics=["if Statement"]),

P(title="Check Whether a Number Is Even or Odd", category="Conditional Statements", difficulty="Beginner",
  description="Uses the modulus operator with if-else to decide whether an integer is even or odd.",
  concepts=["if-else", "% operator", "int()"], filename="even_odd.py", kind="Interactive",
  code=r'''
try:
    number = int(input("Enter an integer: "))
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")
except ValueError:
    print("Please enter a whole number.")
''',
  algorithm=["Read an integer", "Compute number % 2", "If the remainder is 0 print even", "Otherwise print odd"],
  explanation="An even number is exactly divisible by 2, so number % 2 gives 0. The if-else statement chooses one of two blocks depending on that test. Negative integers work too because Python's % result for 2 is always 0 or 1.",
  sample_input="37", tags=["even", "odd", "modulus"], topics=["if … else Statement"]),

P(title="Check Whether a Number Is Zero", category="Conditional Statements", difficulty="Beginner",
  description="Tests if the entered number equals zero using the == operator.",
  concepts=["if-else", "== operator"], filename="check_zero.py", kind="Interactive",
  code=r'''
try:
    number = float(input("Enter a number: "))
    if number == 0:
        print("The number is zero")
    else:
        print("The number is not zero")
except ValueError:
    print("Invalid number.")
''',
  algorithm=["Read the number", "Compare it with 0 using ==", "Print 'zero' if equal", "Else print 'not zero'"],
  explanation="The equality operator == compares two values and returns True or False. The if-else statement uses this result to print the proper message. Note the difference between = (assignment) and == (comparison).",
  sample_input="0", tags=["zero", "equality", "if-else"], topics=["if … else Statement"]),

P(title="Find the Largest of Two Numbers", category="Conditional Statements", difficulty="Beginner",
  description="Compares two numbers and prints the larger one.",
  concepts=["if-elif-else", "comparison operators"], filename="largest_of_two.py", kind="Interactive",
  code=r'''
try:
    a = float(input("Enter first number : "))
    b = float(input("Enter second number: "))
    if a > b:
        print(a, "is the largest")
    elif b > a:
        print(b, "is the largest")
    else:
        print("Both numbers are equal")
except ValueError:
    print("Please enter valid numbers.")
''',
  algorithm=["Read two numbers a and b", "If a > b, a is largest", "Else if b > a, b is largest", "Otherwise they are equal"],
  explanation="The program uses comparison operators inside an if-elif-else chain. Checking for equality separately gives a correct answer even when both numbers are the same. Only one block of the chain runs.",
  sample_input="45\n67", tags=["largest", "maximum", "compare"], topics=["if … elif … else Statement"]),

P(title="Find the Largest of Three Numbers", category="Conditional Statements", difficulty="Beginner",
  description="Finds the greatest of three numbers using logical operators in an if-elif-else chain.",
  concepts=["and operator", "if-elif-else"], filename="largest_of_three.py", kind="Interactive",
  code=r'''
try:
    a = float(input("Enter first number : "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number : "))

    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c
    print("Largest number is", largest)
    print("Check using max():", max(a, b, c))
except ValueError:
    print("Please enter valid numbers.")
''',
  algorithm=["Read three numbers", "If a is >= both others, a is largest", "Else if b is >= both others, b is largest", "Otherwise c is largest",
             "Print the result"],
  explanation="The and operator joins two comparisons so that a number is chosen only when it is at least as big as both others. Using >= handles ties correctly. The built-in max() function is printed as a cross-check.",
  sample_input="12\n78\n45", tags=["largest", "three numbers", "and"], topics=["if … elif … else Statement"]),

P(title="Find the Smallest of Three Numbers", category="Conditional Statements", difficulty="Beginner",
  description="Finds the smallest of three numbers using nested comparisons.",
  concepts=["nested if", "comparison"], filename="smallest_of_three.py", kind="Interactive",
  code=r'''
try:
    a = float(input("Enter first number : "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number : "))

    if a <= b:
        if a <= c:
            smallest = a
        else:
            smallest = c
    else:
        if b <= c:
            smallest = b
        else:
            smallest = c
    print("Smallest number is", smallest)
    print("Check using min():", min(a, b, c))
except ValueError:
    print("Please enter valid numbers.")
''',
  algorithm=["Read three numbers", "Compare a with b", "Compare the winner with c", "Store the smallest value", "Print it"],
  explanation="First a and b are compared; the smaller one is then compared with c, so only two comparisons are needed. The nested if statements show how one decision leads to another. min() is used to verify the result.",
  sample_input="34\n9\n21", tags=["smallest", "minimum", "nested if"], topics=["if Statement", "if … else Statement"]),

P(title="Check Whether a Year Is a Leap Year", category="Conditional Statements", difficulty="Beginner",
  description="Applies the Gregorian leap year rules using logical operators.",
  concepts=["and / or", "% operator", "if-else"], filename="leap_year.py", kind="Interactive",
  code=r'''
try:
    year = int(input("Enter a year: "))
    # divisible by 4 and not by 100, OR divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")
except ValueError:
    print("Please enter a valid year.")
''',
  algorithm=["Read the year", "Test (year % 4 == 0 and year % 100 != 0)", "Or test year % 400 == 0", "Print leap year if either is True", "Otherwise print not a leap year"],
  explanation="A year is a leap year when it is divisible by 4, except century years, which must be divisible by 400. The condition combines three modulus tests with and/or. For example 2024 and 2000 are leap years but 1900 is not.",
  sample_input="2024", tags=["leap year", "logical operators"], topics=["if … else Statement"]),

P(title="Check Whether a Person Is Eligible to Vote", category="Conditional Statements", difficulty="Beginner",
  description="Checks whether the age entered is 18 or above and tells how many years remain otherwise.",
  concepts=["if-else", "int()", "validation"], filename="voting_eligibility.py", kind="Interactive",
  code=r'''
try:
    age = int(input("Enter your age: "))
    if age < 0:
        print("Age cannot be negative.")
    elif age >= 18:
        print("You are eligible to vote.")
    else:
        print(f"Not eligible. You can vote after {18 - age} year(s).")
except ValueError:
    print("Please enter a valid age.")
''',
  algorithm=["Read the age", "Reject negative ages", "If age >= 18 print eligible", "Otherwise print the years remaining"],
  explanation="Voting eligibility depends on the age being at least 18. The program also validates the input: negative ages and non-numeric text are rejected. For under-age users it calculates how many years they must wait.",
  sample_input="16", tags=["voting", "age", "eligibility"], topics=["if … elif … else Statement"]),

P(title="Calculate Student Grades", category="Conditional Statements", difficulty="Beginner",
  description="Calculates total, percentage and grade of a student from marks in three subjects.",
  concepts=["if-elif-else", "arithmetic", "validation"], filename="student_grade.py", kind="Interactive",
  code=r'''
try:
    marks = []
    for subject in ("Maths", "Physics", "Python"):
        score = float(input(f"Enter marks in {subject} (0-100): "))
        if not 0 <= score <= 100:
            raise ValueError("marks out of range")
        marks.append(score)

    total = sum(marks)
    percentage = total / len(marks)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F (Fail)"

    print(f"Total      : {total}")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Grade      : {grade}")
except ValueError:
    print("Invalid marks entered. Marks must be numbers from 0 to 100.")
''',
  algorithm=["Read marks for each subject and validate the range", "Add the marks and compute the percentage", "Compare the percentage with grade limits from top to bottom",
             "Pick the first matching grade", "Print total, percentage and grade"],
  explanation="After reading and validating the marks, the percentage is calculated. An if-elif-else ladder tests the highest grade first and stops at the first condition that is true. A raised ValueError is used to reject marks outside 0-100.",
  sample_input="85\n78\n92", tags=["grade", "percentage", "elif"], topics=["if … elif … else Statement"]),

P(title="Demonstrate Nested if Statements", category="Conditional Statements", difficulty="Intermediate",
  description="Uses an if statement inside another if to decide loan eligibility based on age and salary.",
  concepts=["nested if", "indentation", "and"], filename="nested_if.py", kind="Interactive",
  code=r'''
try:
    age = int(input("Enter age: "))
    salary = float(input("Enter monthly salary: "))

    if age >= 21:                         # outer if
        print("Age requirement satisfied.")
        if salary >= 25000:               # inner if
            print("Salary requirement satisfied.")
            if salary >= 100000:          # inner-most if
                print("Loan approved with premium interest rate.")
            else:
                print("Loan approved with standard interest rate.")
        else:
            print("Loan rejected: salary too low.")
    else:
        print("Loan rejected: you must be at least 21.")
except ValueError:
    print("Invalid input.")
''',
  algorithm=["Read age and salary", "Outer if checks the age", "Inner if checks the salary", "A third level checks for a premium salary", "Print the matching decision"],
  explanation="A nested if is an if statement placed inside the block of another if. The inner condition is tested only when the outer condition is True. Indentation shows which block each statement belongs to, so it must be consistent.",
  sample_input="28\n45000", tags=["nested if", "indentation", "decision"], topics=["if Statement", "if … else Statement"]),

P(title="Demonstrate if-else", category="Conditional Statements", difficulty="Beginner",
  description="A two-way decision that checks whether a password is correct.",
  concepts=["if-else", "string comparison"], filename="if_else_demo.py", kind="Interactive",
  code=r'''
secret = "python123"
attempt = input("Enter the password: ")

if attempt == secret:
    print("Access granted")
else:
    print("Access denied")

# conditional expression (one-line if-else)
message = "Welcome!" if attempt == secret else "Try again."
print(message)
''',
  algorithm=["Store the correct password", "Read the user's attempt", "If both match print granted", "Else print denied", "Show the one-line conditional expression"],
  explanation="if-else executes exactly one of two blocks: the if block when the condition is True and the else block otherwise. Strings are compared with ==. The last lines show the compact conditional expression value_if_true if condition else value_if_false.",
  sample_input="python123", tags=["if-else", "password", "two-way"], topics=["if … else Statement"]),

P(title="Demonstrate if-elif-else", category="Conditional Statements", difficulty="Beginner",
  description="Multi-way decision that prints the name of the day from its number.",
  concepts=["if-elif-else", "multi-way branching"], filename="if_elif_else_demo.py", kind="Interactive",
  code=r'''
try:
    day = int(input("Enter day number (1-7): "))
    if day == 1:
        print("Monday")
    elif day == 2:
        print("Tuesday")
    elif day == 3:
        print("Wednesday")
    elif day == 4:
        print("Thursday")
    elif day == 5:
        print("Friday")
    elif day == 6:
        print("Saturday")
    elif day == 7:
        print("Sunday")
    else:
        print("Invalid day number")
except ValueError:
    print("Please enter a number.")
''',
  algorithm=["Read the day number", "Test it against 1, 2, 3 ... using elif", "Print the name for the first matching test", "Else print an invalid message"],
  explanation="if-elif-else tests the conditions one after another and runs only the block of the first True condition. The else block is the default when nothing matches. This structure is used whenever there are more than two possible outcomes.",
  sample_input="5", tags=["elif", "multi-way", "day"], topics=["if … elif … else Statement"]),

P(title="Simple Calculator Using Conditional Statements", category="Conditional Statements", difficulty="Beginner",
  description="Performs +, -, *, / and % on two numbers chosen by the user with an if-elif ladder.",
  concepts=["if-elif-else", "arithmetic operators", "ZeroDivisionError"], filename="simple_calculator.py", kind="Interactive",
  code=r'''
try:
    num1 = float(input("Enter first number : "))
    operator = input("Enter operator (+ - * / %): ").strip()
    num2 = float(input("Enter second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            result = "Error: division by zero"
        else:
            result = num1 / num2
    elif operator == "%":
        result = num1 % num2 if num2 != 0 else "Error: division by zero"
    else:
        result = "Error: unknown operator"
    print("Result:", result)
except ValueError:
    print("Please enter valid numbers.")
''',
  algorithm=["Read two numbers and the operator", "Compare the operator with each symbol using elif", "Perform the matching calculation",
             "Guard division and modulus against zero", "Print the result or an error message"],
  explanation="The operator typed by the user decides which calculation is performed. An if-elif ladder checks each symbol; the final else catches unknown operators. Division by zero is tested before dividing so the program never crashes.",
  sample_input="15\n/\n4", tags=["calculator", "operators", "elif"], topics=["if … elif … else Statement"]),

P(title="Check Whether a Number Is Divisible by Another Number", category="Conditional Statements", difficulty="Beginner",
  description="Checks whether the first number is exactly divisible by the second using the remainder.",
  concepts=["% operator", "if-else", "zero check"], filename="divisibility_check.py", kind="Interactive",
  code=r'''
try:
    dividend = int(input("Enter the number: "))
    divisor = int(input("Enter the divisor: "))
    if divisor == 0:
        print("Divisor cannot be zero.")
    elif dividend % divisor == 0:
        print(f"{dividend} is divisible by {divisor} (quotient {dividend // divisor})")
    else:
        print(f"{dividend} is NOT divisible by {divisor} (remainder {dividend % divisor})")
except ValueError:
    print("Please enter whole numbers.")
''',
  algorithm=["Read the dividend and divisor", "Reject a zero divisor", "Compute dividend % divisor", "If the remainder is 0 it is divisible", "Print quotient or remainder"],
  explanation="A number is divisible by another when the remainder of the division is zero. The % operator gives the remainder and // gives the quotient. A zero divisor is checked first, since division by zero is not allowed.",
  sample_input="144\n12", tags=["divisible", "modulus", "remainder"], topics=["if … elif … else Statement"]),
]

# ---------------------------------------------------------------- Loops (24-42)
PROGRAMS += [
P(title="Demonstrate while Loop", category="Loops", difficulty="Beginner",
  description="Repeats a block while a condition is True, using a counter and a running total.",
  concepts=["while loop", "counter", "condition"], filename="while_loop_demo.py",
  code=r'''
# while loop: repeat as long as the condition is True
count = 1
while count <= 5:
    print("Count is", count)
    count += 1              # update the variable, otherwise the loop never ends
print("Loop finished, count =", count)

# countdown
n = 3
while n > 0:
    print(n, end=" ")
    n -= 1
print("Lift off!")

# sum digits entered from a list until a negative value appears
values = [4, 8, 15, -1, 16]
index, total = 0, 0
while values[index] >= 0:
    total += values[index]
    index += 1
print("Total before negative number:", total)
''',
  algorithm=["Initialise the loop variable", "Test the condition before every iteration", "Execute the body", "Update the variable", "Stop when the condition becomes False"],
  explanation="The while loop checks its condition before every pass and runs the body while it is True. The loop variable must change inside the body, otherwise the loop would never stop. The examples show a counter, a countdown and a loop that ends when a negative value is found.",
  tags=["while", "loop", "counter"], topics=["The while Loop"]),

P(title="Demonstrate for Loop", category="Loops", difficulty="Beginner",
  description="Iterates over a range, a string, a list and a dictionary using the for loop.",
  concepts=["for loop", "range()", "iterables"], filename="for_loop_demo.py",
  code=r'''
# for loop: iterate over any sequence
print("range(5):", end=" ")
for i in range(5):
    print(i, end=" ")
print()

print("range(2, 10, 3):", end=" ")
for i in range(2, 10, 3):          # start, stop, step
    print(i, end=" ")
print()

for letter in "Python":            # string
    print(letter, end="-")
print()

for fruit in ["apple", "banana", "cherry"]:   # list
    print("I like", fruit)

marks = {"Asha": 80, "Ravi": 72}
for name, score in marks.items():  # dictionary
    print(name, "scored", score)

for i in range(5, 0, -1):          # reverse counting
    print(i, end=" ")
print()
''',
  algorithm=["Pick an iterable such as range(), a string or a list", "For each element assign it to the loop variable", "Run the body", "Repeat until the sequence is exhausted"],
  explanation="The for loop in Python walks over the items of any iterable and assigns each item to the loop variable. range(start, stop, step) produces numbers, where stop is excluded. The loop works equally well on strings, lists and dictionaries, and a negative step counts downwards.",
  tags=["for", "range", "iteration"], topics=["The for Loop"]),

P(title="Print Numbers from 1 to N", category="Loops", difficulty="Beginner",
  description="Prints all numbers from 1 up to a limit N entered by the user.",
  concepts=["for loop", "range()", "input"], filename="print_1_to_n.py", kind="Interactive",
  code=r'''
try:
    n = int(input("Enter N: "))
    if n < 1:
        print("N must be at least 1.")
    else:
        for number in range(1, n + 1):      # n + 1 because stop is excluded
            print(number, end=" ")
        print()
except ValueError:
    print("Please enter a whole number.")
''',
  algorithm=["Read N", "Validate N >= 1", "Loop with range(1, N + 1)", "Print each number on the same line"],
  explanation="range(1, n + 1) produces 1, 2, ..., n because the stop value is never included. The end=\" \" argument keeps the numbers on one line. Invalid or non-positive input is rejected before the loop starts.",
  sample_input="10", tags=["range", "for", "1 to n"], topics=["The for Loop"]),

P(title="Print Multiplication Tables", category="Loops", difficulty="Beginner",
  description="Prints the multiplication table of a number up to 10.",
  concepts=["for loop", "f-string", "arithmetic"], filename="multiplication_table.py", kind="Interactive",
  code=r'''
try:
    number = int(input("Enter a number: "))
    print(f"Multiplication table of {number}")
    for i in range(1, 11):
        print(f"{number} x {i:2d} = {number * i}")
except ValueError:
    print("Please enter a whole number.")
''',
  algorithm=["Read the number", "Loop i from 1 to 10", "Compute number * i", "Print one line of the table each time"],
  explanation="The for loop runs ten times with i = 1 to 10. In each pass the product number * i is calculated and printed using an f-string; the :2d specifier aligns the multiplier for neat output.",
  sample_input="7", tags=["table", "multiplication", "for"], topics=["The for Loop"]),

P(title="Calculate the Sum of Natural Numbers", category="Loops", difficulty="Beginner",
  description="Adds the natural numbers 1 to N using a loop and verifies the result with the formula n(n+1)/2.",
  concepts=["while loop", "accumulator", "formula"], filename="sum_natural_numbers.py", kind="Interactive",
  code=r'''
try:
    n = int(input("Enter N: "))
    if n < 1:
        print("N must be a natural number (1, 2, 3, ...).")
    else:
        total = 0
        i = 1
        while i <= n:
            total += i
            i += 1
        print(f"Sum of first {n} natural numbers = {total}")
        print("Using formula n(n+1)/2          =", n * (n + 1) // 2)
except ValueError:
    print("Please enter a whole number.")
''',
  algorithm=["Read N and validate it", "Set total = 0 and i = 1", "While i <= N add i to total and increase i", "Print the total", "Compare with n(n+1)/2"],
  explanation="The variable total is an accumulator that grows by i in every iteration. The loop ends when i exceeds N. The closed-form formula n(n+1)/2 is printed to confirm that the loop gives the correct answer.",
  sample_input="100", tags=["sum", "natural numbers", "while"], topics=["The while Loop"]),

P(title="Calculate Factorial", category="Loops", difficulty="Beginner",
  description="Finds n! by multiplying the numbers from 1 to n in a loop.",
  concepts=["for loop", "accumulator", "validation"], filename="factorial_loop.py", kind="Interactive",
  code=r'''
try:
    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        print(f"{n}! = {factorial}")
except ValueError:
    print("Please enter a whole number.")
''',
  algorithm=["Read n and reject negatives", "Start with factorial = 1", "Multiply by each i from 2 to n", "Print the result"],
  explanation="The factorial of n is 1 x 2 x ... x n, and 0! is defined as 1. The result variable starts at 1 and is multiplied by every number in the loop. For n = 0 or 1 the loop does not run, so 1 is printed correctly. Python integers have no size limit, so large factorials work.",
  sample_input="6", tags=["factorial", "loop", "multiplication"], topics=["The for Loop"]),

P(title="Generate Fibonacci Series", category="Loops", difficulty="Beginner",
  description="Prints the first N terms of the Fibonacci series.",
  concepts=["while loop", "tuple assignment"], filename="fibonacci_series.py", kind="Interactive",
  code=r'''
try:
    terms = int(input("How many terms? "))
    if terms <= 0:
        print("Enter a positive number.")
    else:
        a, b = 0, 1
        count = 0
        while count < terms:
            print(a, end=" ")
            a, b = b, a + b        # shift the pair forward
            count += 1
        print()
except ValueError:
    print("Please enter a whole number.")
''',
  algorithm=["Read the number of terms", "Start with a = 0 and b = 1", "Print a", "Replace (a, b) by (b, a + b)", "Repeat until the required count is reached"],
  explanation="Each Fibonacci number is the sum of the previous two. The two variables a and b hold consecutive terms, and the statement a, b = b, a + b updates both at the same time. A counter controls how many terms are printed.",
  sample_input="10", tags=["fibonacci", "series", "while"], topics=["The while Loop"]),

P(title="Check Whether a Number Is Prime", category="Loops", difficulty="Intermediate",
  description="Tests for primality by trying divisors up to the square root, using break and loop else.",
  concepts=["for-else", "break", "square root"], filename="prime_check.py", kind="Interactive",
  code=r'''
try:
    number = int(input("Enter a number: "))
    if number < 2:
        print(number, "is not prime")
    else:
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                print(number, "is not prime; divisible by", divisor)
                break
        else:                       # runs only if the loop was not broken
            print(number, "is prime")
except ValueError:
    print("Please enter a whole number.")
''',
  algorithm=["Read the number; numbers below 2 are not prime", "Try each divisor from 2 to sqrt(number)", "If one divides exactly, report not prime and break",
             "If the loop finishes without break, the number is prime"],
  explanation="A prime number has no divisors other than 1 and itself. It is enough to test divisors up to the square root, because larger factors pair with smaller ones. The else clause of the for loop runs only when no break occurred, which means no divisor was found.",
  sample_input="97", tags=["prime", "break", "for-else"], topics=["The for Loop", "The else Suite"]),

P(title="Print Prime Numbers in a Range", category="Loops", difficulty="Intermediate",
  description="Prints all prime numbers between a start and an end value using nested loops.",
  concepts=["nested loops", "break", "range()"], filename="primes_in_range.py", kind="Interactive",
  code=r'''
try:
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range  : "))
    primes = []
    for number in range(max(start, 2), end + 1):
        is_prime = True
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    print(f"Prime numbers between {start} and {end}:")
    print(primes)
    print("Count:", len(primes))
except ValueError:
    print("Please enter whole numbers.")
''',
  algorithm=["Read the start and end values", "Outer loop visits every number in the range", "Inner loop tests divisors up to sqrt(number)",
             "A flag records whether a divisor was found", "Collect and print the primes"],
  explanation="An outer for loop picks each candidate number and an inner for loop searches for a divisor. A Boolean flag is_prime starts as True and becomes False when a divisor is found; break then leaves the inner loop early. The primes are stored in a list and printed with their count.",
  sample_input="10\n50", tags=["prime", "range", "nested loop"], topics=["Nested Loops", "The break Statement"]),

P(title="Reverse a Number", category="Loops", difficulty="Beginner",
  description="Reverses the digits of an integer using the remainder and floor-division operators.",
  concepts=["while loop", "% and //", "digits"], filename="reverse_number.py", kind="Interactive",
  code=r'''
try:
    number = int(input("Enter a number: "))
    original = abs(number)
    reversed_number = 0
    while original > 0:
        digit = original % 10                         # last digit
        reversed_number = reversed_number * 10 + digit
        original //= 10                               # drop last digit
    if number < 0:
        reversed_number = -reversed_number
    print("Reversed number:", reversed_number)
except ValueError:
    print("Please enter a whole number.")
''',
  algorithm=["Read the number", "Extract the last digit with % 10", "Append it to the reversed number: reversed * 10 + digit", "Remove the last digit with // 10",
             "Repeat until no digits remain"],
  explanation="Taking number % 10 gives the last digit and number // 10 removes it. Multiplying the reversed value by 10 shifts its digits left to make room for the new digit. The loop continues until the original number becomes 0.",
  sample_input="12345", tags=["reverse", "digits", "while"], topics=["The while Loop"]),

P(title="Check Palindrome Number", category="Loops", difficulty="Beginner",
  description="Reverses a number digit by digit and compares it with the original to decide if it is a palindrome.",
  concepts=["while loop", "comparison"], filename="palindrome_number.py", kind="Interactive",
  code=r'''
try:
    number = int(input("Enter a number: "))
    if number < 0:
        print("Negative numbers are not treated as palindromes.")
    else:
        temp, reverse = number, 0
        while temp > 0:
            reverse = reverse * 10 + temp % 10
            temp //= 10
        if reverse == number:
            print(number, "is a palindrome")
        else:
            print(number, "is not a palindrome (reverse is", str(reverse) + ")")
except ValueError:
    print("Please enter a whole number.")
''',
  algorithm=["Read the number", "Copy it into temp and build the reverse", "Compare the reverse with the original", "Print palindrome or not palindrome"],
  explanation="A palindrome number reads the same from both directions, e.g. 1221. The digits are reversed with the usual remainder technique and the result is compared with the original number using ==. A copy of the number is used so the original is not lost.",
  sample_input="12321", tags=["palindrome", "reverse", "number"], topics=["The while Loop"]),

P(title="Demonstrate Infinite Loops Safely", category="Loops", difficulty="Intermediate",
  description="Shows while True loops that are always terminated safely with break and a counter.",
  concepts=["while True", "break", "safe exit"], filename="infinite_loop_safe.py",
  code=r'''
# An infinite loop never ends by itself: while True: ...
# To use one safely, ALWAYS provide a way out (break / return / counter).

counter = 0
while True:                       # condition is always True
    counter += 1
    print("Iteration", counter)
    if counter == 5:              # exit condition
        print("Limit reached - leaving the infinite loop.")
        break

# Typical real-life use: keep asking until valid data arrives
attempts = ["abc", "-4", "25"]    # simulated user input
position = 0
while True:
    text = attempts[position]
    position += 1
    if text.isdigit():
        print("Accepted:", text)
        break
    print("Rejected:", text)

# Safety net: a maximum number of loops
safety_limit = 1000
steps = 0
while True:
    steps += 1
    if steps >= safety_limit:
        print("Safety limit stopped the loop after", steps, "steps")
        break
# NOTE: pressing Ctrl+C also stops a runaway loop in the terminal.
''',
  algorithm=["Write while True so the condition never becomes False", "Update a counter inside the loop", "Test an exit condition with if", "Use break to leave the loop",
             "Add a maximum-step safety limit"],
  explanation="while True creates a loop that would run forever. It is safe only when the body contains a reachable break statement, as in the counter and validation examples. A safety limit protects against logic mistakes, and Ctrl+C can stop a runaway loop in the terminal.",
  tags=["infinite loop", "while True", "break"], topics=["Infinite Loops", "The break Statement"]),

P(title="Demonstrate Nested Loops", category="Loops", difficulty="Beginner",
  description="Uses a loop inside another loop to print a multiplication grid and coordinate pairs.",
  concepts=["nested for", "range()", "formatting"], filename="nested_loops_demo.py",
  code=r'''
# Nested loop: the inner loop completes fully for every pass of the outer loop
for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row},{col})", end=" ")
    print()                           # new line after each row

print("\nMultiplication grid 1-5")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:4d}", end="")
    print()

# nested while inside for
print()
for i in range(1, 4):
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
''',
  algorithm=["Start the outer loop", "For each outer value start the inner loop", "Run the inner loop completely", "Print a new line after the inner loop", "Continue with the next outer value"],
  explanation="In nested loops the inner loop is repeated completely for each iteration of the outer loop, so 3 x 3 loops give 9 pairs. The inner print uses end=\"\" to stay on the same line and the outer loop prints the line break. Different loop types, such as while inside for, can be mixed.",
  tags=["nested loops", "grid", "rows columns"], topics=["Nested Loops"]),

P(title="Demonstrate break", category="Loops", difficulty="Beginner",
  description="Leaves a loop early using break when a search item is found.",
  concepts=["break", "for loop", "search"], filename="break_demo.py",
  code=r'''
# break terminates the nearest enclosing loop immediately
for number in range(1, 11):
    if number == 6:
        print("Found 6 - stopping the loop")
        break
    print("Checking", number)
print("Loop ended")

# linear search that stops at the first match
names = ["Asha", "Ravi", "Meena", "John"]
target = "Meena"
for position, name in enumerate(names):
    if name == target:
        print(f"{target} found at index {position}")
        break
''',
  algorithm=["Start a loop", "Test a condition inside the loop", "When it is true execute break", "Control jumps to the first statement after the loop"],
  explanation="break stops the loop at once, skipping any remaining iterations. It is useful for searching because there is no need to continue after the item is found. Statements after the loop run normally.",
  tags=["break", "loop control", "search"], topics=["The break Statement"]),

P(title="Demonstrate continue", category="Loops", difficulty="Beginner",
  description="Skips selected iterations with continue, e.g. printing only odd numbers and skipping a name.",
  concepts=["continue", "for loop"], filename="continue_demo.py",
  code=r'''
# continue skips the rest of the current iteration and starts the next one
print("Odd numbers from 1 to 10:")
for number in range(1, 11):
    if number % 2 == 0:
        continue                  # skip even numbers
    print(number, end=" ")
print()

print("Skipping a name:")
for name in ["Asha", "Ravi", "Skip", "Meena"]:
    if name == "Skip":
        continue
    print("Hello", name)

# skipping bad data
total = 0
for item in [10, "x", 20, None, 30]:
    if not isinstance(item, int):
        continue
    total += item
print("Total of valid integers:", total)
''',
  algorithm=["Start a loop", "Check a condition at the top of the body", "Execute continue when the item should be skipped", "The loop jumps to its next iteration", "Remaining items are processed normally"],
  explanation="continue ends only the current iteration and moves to the next one; the loop itself keeps running. Here it skips even numbers, a special name and invalid data items. Compare this with break, which leaves the loop completely.",
  tags=["continue", "skip", "loop control"], topics=["The continue Statement"]),

P(title="Demonstrate pass", category="Loops", difficulty="Beginner",
  description="Uses the pass statement as a placeholder in loops, if blocks, functions and classes.",
  concepts=["pass", "placeholder", "empty block"], filename="pass_demo.py",
  code=r'''
# pass does nothing - it is a placeholder where a statement is required

for number in range(1, 6):
    if number == 3:
        pass                      # TODO: handle 3 later
    else:
        print("Number", number)

def future_feature():
    pass                          # function to be written later

class EmptyClass:
    pass                          # class with no members yet

future_feature()
obj = EmptyClass()
print("Created object:", type(obj).__name__)

# difference from continue
for i in range(3):
    if i == 1:
        pass                      # does nothing, remaining code still runs
    print("pass version, i =", i)
''',
  algorithm=["Write a block that needs a statement but has no logic yet", "Insert pass as the body", "Run the program - no error occurs", "Replace pass with real code later"],
  explanation="Python does not allow empty blocks, so pass is used as a do-nothing placeholder in loops, conditions, functions and classes. It lets a program structure be written first and filled in later. Unlike continue, pass does not skip anything; the statements after it still execute.",
  tags=["pass", "placeholder", "empty"], topics=["The pass Statement"]),

P(title="Demonstrate Loop else", category="Loops", difficulty="Intermediate",
  description="Shows the else suite of for and while loops, which runs only when the loop ends without break.",
  concepts=["for-else", "while-else", "break"], filename="loop_else_demo.py",
  code=r'''
# else on a loop runs when the loop finishes normally (no break)

# 1. search that FAILS - else runs
for n in [3, 5, 7]:
    if n % 2 == 0:
        print("Even number found")
        break
else:
    print("No even number found")

# 2. search that SUCCEEDS - break skips else
for n in [3, 4, 7]:
    if n % 2 == 0:
        print("Even number found:", n)
        break
else:
    print("No even number found")

# 3. while-else
count = 0
while count < 3:
    print("count =", count)
    count += 1
else:
    print("while loop completed normally")
''',
  algorithm=["Write a for or while loop with a break inside an if", "Add an else block aligned with the loop", "If the loop is never broken, the else block runs", "If break executes, the else block is skipped"],
  explanation="The else suite attached to a loop executes after the loop is exhausted. If the loop is terminated by break, the else suite is skipped. This is handy for searches: else means 'not found'. The same rule applies to while loops.",
  tags=["loop else", "for-else", "while-else"], topics=["The else Suite"]),

P(title="Print Patterns Using Nested Loops", category="Loops", difficulty="Intermediate",
  description="Prints star triangle, number triangle, pyramid and square patterns with nested loops.",
  concepts=["nested loops", "string repetition", "patterns"], filename="patterns_nested_loops.py", kind="Interactive",
  code=r'''
try:
    rows = int(input("Enter number of rows: "))
    if rows < 1:
        print("Rows must be at least 1.")
    else:
        print("\nRight triangle:")
        for i in range(1, rows + 1):
            for j in range(i):
                print("*", end=" ")
            print()

        print("\nNumber triangle:")
        for i in range(1, rows + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

        print("\nPyramid:")
        for i in range(1, rows + 1):
            print(" " * (rows - i) + "* " * i)

        print("\nInverted triangle:")
        for i in range(rows, 0, -1):
            print("* " * i)
except ValueError:
    print("Please enter a whole number.")
''',
  algorithm=["Read the number of rows", "Outer loop controls the row number", "Inner loop prints the symbols of that row", "Print a newline after each row",
             "Use spaces and string repetition for the pyramid"],
  explanation="In pattern programs the outer loop represents rows and the inner loop represents the columns of each row. The number of inner iterations depends on the row number i, which makes triangles. The pyramid uses leading spaces (rows - i) to centre the stars.",
  sample_input="5", tags=["pattern", "star", "pyramid", "nested loops"], topics=["Nested Loops"]),

P(title="Demonstrate the return Statement in a Function", category="Loops", difficulty="Beginner",
  description="Shows functions that return a value, several values, and exit early using return.",
  concepts=["def", "return", "tuple", "early exit"], filename="return_statement_demo.py",
  code=r'''
def square(x):
    return x * x                  # sends a value back to the caller

def min_max(values):
    return min(values), max(values)   # returns a tuple of two values

def first_negative(values):
    for v in values:
        if v < 0:
            return v              # return exits the function immediately
    return None                   # reached only if no negative value exists

def greet(name):
    print("Hello", name)          # no return statement -> returns None

result = square(7)
print("square(7) =", result)

low, high = min_max([4, 9, -2, 15])
print("Minimum:", low, " Maximum:", high)

print("First negative:", first_negative([3, 8, -5, -1]))
print("First negative:", first_negative([3, 8]))

print("greet returns:", greet("Asha"))
''',
  algorithm=["Define functions with def", "Use return to send a result to the caller", "Return several values as a tuple and unpack them", "Use return inside a loop to exit early",
             "Show that a function without return gives None"],
  explanation="The return statement ends the function and hands a value back to the place where it was called. Returning a comma separated list really returns a tuple, which can be unpacked into variables. A function that never executes return gives None. Statements after a return in the same path are never executed.",
  tags=["return", "function", "def", "tuple"], topics=["The return Statement"]),
]

# ---------------------------------------------------------------- Arrays: array module (43-56)
PROGRAMS += [
P(title="Create an Array (array module)", category="Arrays", difficulty="Beginner",
  description="Creates arrays with the array module (library: array) and lists the advantages of arrays over lists.",
  concepts=["array module", "type code", "array()"], filename="array_create.py",
  code=r'''
# Library used: Python's built-in `array` module (no installation needed)
# array.array stores items of ONE type compactly; NumPy ndarray (used later) is for
# fast multi-dimensional maths. A list can mix types and uses more memory.
from array import array
import sys

marks = array("i", [70, 85, 90, 65])        # 'i' = signed int
prices = array("f", [10.5, 20.25, 30.0])    # 'f' = float
empty = array("i")                          # empty integer array
from_range = array("i", range(1, 6))        # build from any iterable

print("marks      :", marks)
print("prices     :", prices)
print("empty      :", empty)
print("from range :", from_range)

# Advantages of arrays: compact memory, same type, fast numeric storage
numbers_list = list(range(1000))
numbers_array = array("i", range(1000))
print("Size of list items  :", sys.getsizeof(numbers_list), "bytes")
print("Size of array items :", sys.getsizeof(numbers_array), "bytes")
''',
  algorithm=["Import array from the array module", "Choose a type code such as 'i' or 'f'", "Call array(typecode, initial_values)", "Create an empty array and one from range()", "Compare memory used by a list and an array"],
  explanation="The array module provides array.array, a sequence that holds items of a single numeric type given by a type code. Because every item has the same type, the data is stored compactly, which is the main advantage over a list, along with type safety and fast numeric storage. The program creates arrays from lists, from range() and as an empty array, then compares memory with a list using sys.getsizeof(). Library used: array (standard library).",
  tags=["array", "create", "typecode", "advantages"], topics=["Creating an Array", "Advantages of Arrays"]),

P(title="Display Array Elements (array module)", category="Arrays", difficulty="Beginner",
  description="Prints the elements of an array using print, a for loop, indexes and join (library: array).",
  concepts=["array module", "for loop", "enumerate()"], filename="array_display.py",
  code=r'''
# Library used: array (standard library)
from array import array

numbers = array("i", [10, 20, 30, 40, 50])

print("Whole array:", numbers)
print("As a list  :", numbers.tolist())

print("Using a for loop:")
for value in numbers:
    print(value, end=" ")
print()

print("Using index positions:")
for index in range(len(numbers)):
    print(f"numbers[{index}] = {numbers[index]}")

print("Using enumerate:")
for position, value in enumerate(numbers, start=1):
    print(f"Element {position}: {value}")

print("Joined:", ", ".join(str(n) for n in numbers))
''',
  algorithm=["Create an integer array", "Print the whole array and its list form", "Loop over the values", "Loop over the indexes", "Join the values into one string"],
  explanation="An array can be displayed directly with print(), which shows the type code and the items. A for loop gives each value in turn, while range(len(...)) gives index positions so each element can be shown with its index. enumerate() supplies both together. tolist() converts the array into an ordinary list. Library used: array.",
  tags=["array", "display", "loop", "print"], topics=["Creating an Array"]),

P(title="Access Array Elements (array module)", category="Arrays", difficulty="Beginner",
  description="Accesses array items with positive and negative indexes and slices, and handles IndexError (library: array).",
  concepts=["indexing", "negative index", "slicing", "IndexError"], filename="array_access.py",
  code=r'''
# Library used: array (standard library)
from array import array

data = array("i", [5, 10, 15, 20, 25, 30])

print("First element   :", data[0])
print("Third element   :", data[2])
print("Last element    :", data[-1])
print("Second last     :", data[-2])
print("Slice [1:4]     :", data[1:4])
print("Slice [::2]     :", data[::2])
print("Reversed slice  :", data[::-1])

try:
    print(data[10])
except IndexError as error:
    print("Error:", error)
''',
  algorithm=["Create an array of six integers", "Access items with positive indexes starting at 0", "Access items with negative indexes from the end", "Use slices to get several items", "Catch IndexError for an invalid index"],
  explanation="Array elements are reached with square brackets and a zero-based index. Negative indexes count from the end, so -1 is the last item. Slicing start:stop:step returns a new array. Using an index outside the array raises IndexError, which the try/except block reports. Library used: array.",
  tags=["array", "index", "slice", "access"], topics=["Creating an Array"]),

P(title="Insert Array Elements (array module)", category="Arrays", difficulty="Beginner",
  description="Adds elements to an array using append(), insert(), extend() and fromlist() (library: array).",
  concepts=["append()", "insert()", "extend()"], filename="array_insert.py",
  code=r'''
# Library used: array (standard library)
from array import array

nums = array("i", [10, 20, 30])
print("Start        :", nums)

nums.append(40)                    # add one item at the end
print("append(40)   :", nums)

nums.insert(1, 15)                 # insert 15 at index 1
print("insert(1,15) :", nums)

nums.extend([50, 60])              # add many items at the end
print("extend       :", nums)

nums.fromlist([70, 80])            # add items from a list
print("fromlist     :", nums)

try:
    nums.append(2.5)               # wrong type for an 'i' array
except TypeError as error:
    print("Error:", error)
''',
  algorithm=["Create an array", "append() adds an item at the end", "insert(index, value) adds an item at a position", "extend() and fromlist() add several items", "Show that a wrong type raises TypeError"],
  explanation="append() puts a new value at the end of the array while insert() places it at a chosen index and shifts later items right. extend() and fromlist() add many values at once. An array accepts only its declared type, so appending a float to an integer array raises TypeError. Library used: array.",
  tags=["array", "insert", "append", "extend"], topics=["Creating an Array"]),

P(title="Remove Array Elements (array module)", category="Arrays", difficulty="Beginner",
  description="Deletes elements using remove(), pop() and del (library: array).",
  concepts=["remove()", "pop()", "del"], filename="array_remove.py",
  code=r'''
# Library used: array (standard library)
from array import array

nums = array("i", [10, 20, 30, 40, 50, 30])
print("Start       :", nums)

nums.remove(30)                    # removes the FIRST value 30
print("remove(30)  :", nums)

last = nums.pop()                  # removes and returns the last item
print("pop()       :", nums, "-> removed", last)

second = nums.pop(1)               # removes the item at index 1
print("pop(1)      :", nums, "-> removed", second)

del nums[0]                        # delete by index
print("del nums[0] :", nums)

try:
    nums.remove(999)
except ValueError:
    print("999 is not in the array")
''',
  algorithm=["Create an array with a repeated value", "remove(value) deletes the first match", "pop() deletes the last item, pop(i) deletes index i", "del deletes by index", "Handle ValueError when the value is missing"],
  explanation="remove() deletes the first item equal to the given value, while pop() deletes by position and also returns the removed value. The del statement removes an item (or slice) by index. After each removal the remaining items move left. Removing a value that is not present raises ValueError. Library used: array.",
  tags=["array", "remove", "pop", "delete"], topics=["Creating an Array"]),

P(title="Update Array Elements (array module)", category="Arrays", difficulty="Beginner",
  description="Changes array elements by index assignment and slice assignment (library: array).",
  concepts=["assignment", "slice assignment", "loop update"], filename="array_update.py",
  code=r'''
# Library used: array (standard library)
from array import array

nums = array("i", [1, 2, 3, 4, 5])
print("Original      :", nums)

nums[0] = 100                      # update one element
print("nums[0]=100   :", nums)

nums[-1] = 500                     # update the last element
print("nums[-1]=500  :", nums)

nums[1:3] = array("i", [20, 30])   # update a slice (same type needed)
print("slice update  :", nums)

for i in range(len(nums)):         # double every element
    nums[i] = nums[i] * 2
print("doubled       :", nums)
''',
  algorithm=["Create an array", "Assign a new value to an index", "Assign to a negative index", "Replace a slice with another array", "Update every element in a loop"],
  explanation="Arrays are mutable, so an element is updated by assigning to its index. A slice can be replaced by another array of the same type code. A loop with range(len(...)) lets every element be modified. Library used: array.",
  tags=["array", "update", "modify", "assignment"], topics=["Creating an Array"]),

P(title="Find Array Length (array module)", category="Arrays", difficulty="Beginner",
  description="Finds how many elements an array holds with len() and shows buffer information (library: array).",
  concepts=["len()", "itemsize", "buffer_info()"], filename="array_length.py",
  code=r'''
# Library used: array (standard library)
from array import array

nums = array("i", [4, 8, 15, 16, 23, 42])
print("Array            :", nums)
print("Length with len():", len(nums))
print("Bytes per item   :", nums.itemsize)
print("Total bytes      :", len(nums) * nums.itemsize)
print("buffer_info()    :", nums.buffer_info()[1], "items")

# length changes when elements are added or removed
nums.append(50)
print("After append     :", len(nums))
nums.pop()
nums.pop()
print("After two pops   :", len(nums))

empty = array("i")
print("Empty array length:", len(empty))
''',
  algorithm=["Create an array", "Call len() to get the number of items", "Use itemsize to compute total bytes", "Change the array and call len() again", "Check an empty array"],
  explanation="len() returns the number of elements stored in the array. The itemsize attribute tells how many bytes one element needs, so length multiplied by itemsize gives the total storage. The length is updated automatically after append() or pop(), and an empty array has length 0. Library used: array.",
  tags=["array", "length", "len", "size"], topics=["Creating an Array"]),

P(title="Demonstrate Array Types (array module)", category="Arrays", difficulty="Intermediate",
  description="Shows the type codes of the array module and the NumPy dtype comparison (libraries: array and NumPy).",
  concepts=["type codes", "itemsize", "typecode"], filename="array_types.py", deps=["numpy"],
  code=r'''
# Requires: pip install numpy
# Libraries used: array (standard library) for the type codes, NumPy for the comparison
from array import array
import numpy as np

print("Type codes of the array module")
print(f"{'Code':<6}{'Python type':<14}{'Bytes':<6}Example")
samples = {
    "b": [1, -2], "B": [1, 255], "h": [1000, -1000], "H": [60000],
    "i": [100000, -5], "l": [123456789], "q": [2 ** 40], "f": [1.5, 2.5], "d": [3.14159, 2.71828],
}
for code, values in samples.items():
    a = array(code, values)
    kind = "float" if code in "fd" else "int"
    print(f"{code:<6}{kind:<14}{a.itemsize:<6}{a}")

nums = array("d", [1, 2, 3])
print("typecode of nums:", nums.typecode)

# 1-D array module vs NumPy: NumPy gives dtype and multi-dimensions
arr = np.array([1, 2, 3])
print("NumPy dtype      :", arr.dtype)
print("Float array dtype:", np.array([1.5, 2]).dtype)
print("Forced int8      :", np.array([1, 2, 3], dtype=np.int8).dtype)
''',
  algorithm=["Import array and NumPy", "Create one array for each common type code", "Print the byte size per item", "Print typecode of an array", "Show NumPy dtype for comparison"],
  explanation="Every array.array has a type code that fixes the kind of values and the storage per item: signed or unsigned integers of different sizes, and float or double. The program prints the item size for each code. NumPy uses dtype instead of type codes and also supports many dimensions, which the standard array module does not. Libraries used: array and NumPy.",
  tags=["array types", "typecode", "dtype", "numpy"], topics=["Types of Arrays"]),

P(title="Find Maximum and Minimum Array Elements (array module)", category="Arrays", difficulty="Beginner",
  description="Finds the largest and smallest elements using max(), min() and a manual loop (library: array).",
  concepts=["max()", "min()", "loop", "index()"], filename="array_max_min.py",
  code=r'''
# Library used: array (standard library)
from array import array

nums = array("i", [34, 7, 89, 21, 56, 3, 72])
print("Array:", nums)

print("Maximum (max):", max(nums))
print("Minimum (min):", min(nums))
print("Max found at index:", nums.index(max(nums)))
print("Min found at index:", nums.index(min(nums)))

# the same logic written with a loop
largest = smallest = nums[0]
for value in nums:
    if value > largest:
        largest = value
    if value < smallest:
        smallest = value
print("Loop result  :", largest, smallest)
''',
  algorithm=["Create an array", "Use max() and min()", "Use index() to find positions", "Assume the first element is both largest and smallest", "Compare every element and update the two values"],
  explanation="The built-ins max() and min() work on arrays just as on lists. index() returns the position of the first occurrence of a value. The loop version keeps two variables and updates them when a bigger or smaller element is met, which shows the logic behind the built-ins. Library used: array.",
  tags=["array", "maximum", "minimum", "max", "min"], topics=["Creating an Array"]),

P(title="Calculate Array Sum (array module)", category="Arrays", difficulty="Beginner",
  description="Adds all array elements using sum() and a loop (library: array).",
  concepts=["sum()", "accumulator", "for loop"], filename="array_sum.py",
  code=r'''
# Library used: array (standard library)
from array import array

nums = array("i", [12, 18, 25, 30, 15])
print("Array:", nums)
print("Sum using sum():", sum(nums))

total = 0
for value in nums:
    total += value
print("Sum using loop :", total)

even_total = sum(n for n in nums if n % 2 == 0)
print("Sum of even elements:", even_total)
''',
  algorithm=["Create an array", "Call sum() for the total", "Start total at 0 and add each element in a loop", "Add only the even elements using a generator"],
  explanation="sum() adds every element of the array. The loop version shows the accumulator pattern: total starts at 0 and each element is added to it. A generator expression with a condition adds only selected elements. Library used: array.",
  tags=["array", "sum", "total", "accumulator"], topics=["Creating an Array"]),

P(title="Calculate Array Average (array module)", category="Arrays", difficulty="Beginner",
  description="Computes the mean of array elements and counts elements above average (library: array).",
  concepts=["sum()", "len()", "average"], filename="array_average.py",
  code=r'''
# Library used: array (standard library)
from array import array

marks = array("f", [72.5, 88.0, 65.5, 91.0, 79.0])
print("Marks:", marks.tolist())

if len(marks) == 0:
    print("Cannot find average of an empty array")
else:
    average = sum(marks) / len(marks)
    print(f"Sum     : {sum(marks):.2f}")
    print(f"Count   : {len(marks)}")
    print(f"Average : {average:.2f}")
    above = [m for m in marks if m > average]
    print("Above average:", above)
''',
  algorithm=["Create an array of marks", "Check that the array is not empty", "Divide sum() by len()", "Print the average", "List the elements above the average"],
  explanation="The average is the sum of all elements divided by their count. The program first guards against an empty array to avoid division by zero. A list comprehension then picks the marks above the average. Library used: array.",
  tags=["array", "average", "mean"], topics=["Creating an Array"]),

P(title="Sort an Array (array module)", category="Arrays", difficulty="Beginner",
  description="Sorts an array in ascending and descending order using sorted() and a manual bubble sort (library: array).",
  concepts=["sorted()", "reverse", "bubble sort"], filename="array_sort.py",
  code=r'''
# Library used: array (standard library)
# array.array has no sort() method, so sorted() is used and the result is rebuilt.
from array import array

nums = array("i", [42, 7, 19, 3, 88, 25])
print("Original  :", nums)

ascending = array("i", sorted(nums))
print("Ascending :", ascending)

descending = array("i", sorted(nums, reverse=True))
print("Descending:", descending)

# manual bubble sort, in place
data = array("i", nums)
n = len(data)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
print("Bubble sort:", data)
''',
  algorithm=["Create an array", "Use sorted() and rebuild an array from the result", "Use reverse=True for descending order", "Copy the array and bubble sort it", "Swap neighbours that are out of order"],
  explanation="Unlike lists, arrays have no sort() method, so sorted() returns a sorted list and array() converts it back. The bubble sort repeatedly compares neighbouring elements and swaps them if they are in the wrong order, so large values move to the end. Library used: array.",
  tags=["array", "sort", "bubble sort", "sorted"], topics=["Creating an Array"]),

P(title="Reverse an Array (array module)", category="Arrays", difficulty="Beginner",
  description="Reverses an array using reverse(), slicing and two-pointer swapping (library: array).",
  concepts=["reverse()", "slicing", "swap"], filename="array_reverse.py",
  code=r'''
# Library used: array (standard library)
from array import array

nums = array("i", [1, 2, 3, 4, 5])
print("Original      :", nums)

copy1 = array("i", nums)
copy1.reverse()                    # in-place reverse
print("reverse()     :", copy1)

print("Slice [::-1]  :", nums[::-1])

# two-pointer swapping
copy2 = array("i", nums)
left, right = 0, len(copy2) - 1
while left < right:
    copy2[left], copy2[right] = copy2[right], copy2[left]
    left += 1
    right -= 1
print("Manual swap   :", copy2)
''',
  algorithm=["Create an array", "Call reverse() on a copy", "Use the slice [::-1]", "Place one pointer at each end", "Swap and move the pointers inward until they meet"],
  explanation="array.reverse() reverses the array in place, while the slice [::-1] returns a new reversed array. The manual method swaps the first and last elements, then the second and second last, and so on until the two pointers meet. Library used: array.",
  tags=["array", "reverse", "swap", "slice"], topics=["Creating an Array"]),

P(title="Search an Array (array module)", category="Arrays", difficulty="Intermediate",
  description="Searches an array using index(), count(), linear search and binary search (library: array).",
  concepts=["index()", "linear search", "binary search"], filename="array_search.py", kind="Interactive",
  code=r'''
# Library used: array (standard library)
from array import array

nums = array("i", [5, 12, 18, 23, 31, 47, 56, 62])
print("Array:", nums)

try:
    key = int(input("Enter the value to search: "))
except ValueError:
    print("Please enter a whole number.")
else:
    # 1. linear search
    found_at = -1
    for i in range(len(nums)):
        if nums[i] == key:
            found_at = i
            break
    print("Linear search :", f"found at index {found_at}" if found_at >= 0 else "not found")

    # 2. built-in methods
    print("Occurrences   :", nums.count(key))
    if key in nums:
        print("index()       :", nums.index(key))

    # 3. binary search (array is sorted)
    low, high, position = 0, len(nums) - 1, -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == key:
            position = mid
            break
        elif nums[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    print("Binary search :", f"found at index {position}" if position >= 0 else "not found")
''',
  algorithm=["Read the key to search", "Linear search: compare each element with the key", "Use count(), in and index()", "Binary search: compare with the middle element", "Discard the half that cannot contain the key", "Report the position or 'not found'"],
  explanation="Linear search checks the elements one by one and works on any array. count(), in and index() are built-in helpers. Binary search needs a sorted array: it compares the key with the middle element and throws away half of the remaining elements each time, so it is much faster for big arrays. Library used: array.",
  sample_input="31", tags=["array", "search", "linear", "binary"], topics=["Creating an Array"]),
]

# ---------------------------------------------------------------- Arrays: NumPy (57-66)
PROGRAMS += [
P(title="Perform Mathematical Operations on Arrays (NumPy)", category="Arrays (NumPy)", difficulty="Beginner",
  description="Applies arithmetic, universal functions and aggregate functions on NumPy arrays (library: NumPy).",
  concepts=["vectorised operations", "ufuncs", "broadcasting"], filename="numpy_math_operations.py", deps=["numpy"],
  code=r'''
# Requires: pip install numpy
# Library used: NumPy. Operations apply to the WHOLE array at once (no loop needed).
# The array module cannot do this: array("i", [1,2]) + array("i", [3,4]) joins them.
import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * b  =", a * b)
print("a / b  =", a / b)
print("a // 3 =", a // 3)
print("a % 7  =", a % 7)
print("b ** 2 =", b ** 2)
print("a + 5  =", a + 5)             # broadcasting a scalar
print("sqrt(b)=", np.sqrt(b).round(3))
print("sum, mean, max:", a.sum(), a.mean(), a.max())
print("dot product   :", np.dot(a, b))
''',
  algorithm=["Import NumPy as np", "Create two arrays of the same size", "Apply +, -, *, /, //, % and ** element by element", "Add a scalar to show broadcasting", "Use universal and aggregate functions"],
  explanation="NumPy operators work element by element on whole arrays, which is called vectorisation, so no loop is required. A single number is automatically stretched to the array size (broadcasting). Functions such as np.sqrt, sum, mean and dot give mathematical results quickly. Library used: NumPy.",
  tags=["numpy", "math", "vectorised", "operations"], topics=["Mathematical Operations on Arrays"]),

P(title="Demonstrate One-Dimensional Arrays (NumPy)", category="Arrays (NumPy)", difficulty="Beginner",
  description="Creates 1-D NumPy arrays in several ways and uses indexing, slicing and statistics (library: NumPy).",
  concepts=["np.array()", "arange()", "linspace()", "indexing"], filename="numpy_1d_array.py", deps=["numpy"],
  code=r'''
# Requires: pip install numpy
# Library used: NumPy
import numpy as np

a = np.array([3, 6, 9, 12, 15])         # from a list
b = np.arange(0, 10, 2)                 # start, stop, step
c = np.linspace(0, 1, 5)                # 5 evenly spaced values
d = np.zeros(4)
e = np.ones(3, dtype=int)

print("array   :", a)
print("arange  :", b)
print("linspace:", c)
print("zeros   :", d)
print("ones    :", e)

print("a[0], a[-1]:", a[0], a[-1])
print("a[1:4]     :", a[1:4])
print("a > 8      :", a > 8)
print("a[a > 8]   :", a[a > 8])         # boolean indexing
print("dimensions :", a.ndim, " shape:", a.shape)
''',
  algorithm=["Create arrays with array(), arange(), linspace(), zeros() and ones()", "Print each array", "Access items with indexes and slices", "Filter items with a Boolean condition", "Print ndim and shape"],
  explanation="A one-dimensional array is a single row of values. NumPy offers many creation functions: array() from a list, arange() with a step, linspace() with a count, and zeros() or ones() for filled arrays. Indexing and slicing work like lists, and a Boolean condition can select matching elements. Library used: NumPy.",
  tags=["numpy", "1d", "one dimensional", "arange"], topics=["Dimensions of Arrays"]),

P(title="Demonstrate Two-Dimensional Arrays (NumPy)", category="Arrays (NumPy)", difficulty="Beginner",
  description="Creates a 2-D array (matrix) and accesses rows, columns and elements (library: NumPy).",
  concepts=["2-D array", "rows and columns", "reshape()"], filename="numpy_2d_array.py", deps=["numpy"],
  code=r'''
# Requires: pip install numpy
# Library used: NumPy
import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("Matrix:")
print(matrix)

print("Element [1][2]  :", matrix[1][2], "  or matrix[1, 2] =", matrix[1, 2])
print("First row       :", matrix[0])
print("Second column   :", matrix[:, 1])
print("Sub-matrix      :")
print(matrix[:2, 1:])

print("Row sums        :", matrix.sum(axis=1))
print("Column sums     :", matrix.sum(axis=0))
print("Diagonal        :", np.diag(matrix))

grid = np.arange(1, 7).reshape(2, 3)
print("reshape(2, 3):")
print(grid)

print("Looping through rows:")
for row in matrix:
    print(row)
''',
  algorithm=["Create a 2-D array from nested lists", "Access one element with [row, column]", "Slice a row, a column and a sub-matrix", "Use axis to sum rows and columns", "Create a 2-D array with reshape()"],
  explanation="A two-dimensional array is a table of rows and columns, created from a list of lists. matrix[row, column] reaches one element, and slices with a colon select whole rows or columns. The axis argument decides whether a function works down the columns (axis=0) or across the rows (axis=1). reshape() rearranges a 1-D array into 2-D. Library used: NumPy.",
  tags=["numpy", "2d", "matrix", "two dimensional"], topics=["Dimensions of Arrays"]),

P(title="Demonstrate Array Dimensions (NumPy)", category="Arrays (NumPy)", difficulty="Intermediate",
  description="Compares 0-D, 1-D, 2-D and 3-D arrays and changes the number of dimensions (library: NumPy).",
  concepts=["ndim", "0-D to 3-D", "expand_dims", "flatten()"], filename="numpy_dimensions.py", deps=["numpy"],
  code=r'''
# Requires: pip install numpy
# Library used: NumPy
import numpy as np

scalar = np.array(42)                                   # 0-D
vector = np.array([1, 2, 3])                            # 1-D
matrix = np.array([[1, 2, 3], [4, 5, 6]])               # 2-D
cube = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])   # 3-D

for name, arr in [("scalar", scalar), ("vector", vector), ("matrix", matrix), ("cube", cube)]:
    print(f"{name:<7} ndim = {arr.ndim}  shape = {arr.shape}")

# a higher dimension can be forced
five = np.array([1, 2, 3], ndmin=4)
print("ndmin=4 shape:", five.shape)

# changing the number of dimensions
print("expand_dims  :", np.expand_dims(vector, axis=0).shape)
print("flatten cube :", cube.flatten())
print("squeeze      :", np.squeeze(np.array([[[7]]])).shape, "(a 0-D array)")
''',
  algorithm=["Create arrays with 0, 1, 2 and 3 dimensions", "Print ndim and shape of each", "Force a higher dimension with ndmin", "Add a dimension with expand_dims()", "Reduce dimensions with flatten() and squeeze()"],
  explanation="The number of dimensions (ndim) is the number of nested levels: a single value is 0-D, a list is 1-D, a table is 2-D and a stack of tables is 3-D. The shape tuple gives the length along each dimension. expand_dims() adds a dimension, while flatten() and squeeze() remove them. Library used: NumPy.",
  tags=["numpy", "ndim", "dimensions", "3d"], topics=["Dimensions of Arrays"]),

P(title="Demonstrate Array Shape (NumPy)", category="Arrays (NumPy)", difficulty="Intermediate",
  description="Reads and changes the shape of a NumPy array with shape, reshape() and resize (library: NumPy).",
  concepts=["shape", "reshape()", "-1 dimension", "transpose"], filename="numpy_shape.py", deps=["numpy"],
  code=r'''
# Requires: pip install numpy
# Library used: NumPy
import numpy as np

a = np.arange(1, 13)                    # 12 elements
print("a        :", a)
print("a.shape  :", a.shape)

b = a.reshape(3, 4)
print("reshape(3, 4):")
print(b, "-> shape", b.shape)

c = a.reshape(2, 3, 2)
print("reshape(2, 3, 2) -> shape", c.shape)

d = a.reshape(4, -1)                    # -1: NumPy works out the size
print("reshape(4, -1)   -> shape", d.shape)

print("Transpose of b -> shape", b.T.shape)

try:
    a.reshape(5, 3)                     # 15 slots needed, only 12 elements
except ValueError as error:
    print("Error:", error)
''',
  algorithm=["Create a 1-D array of 12 numbers", "Print its shape", "Reshape it to 3x4 and 2x3x2", "Use -1 to let NumPy calculate one size", "Transpose a matrix", "Show the error for an impossible shape"],
  explanation="The shape of an array is a tuple that gives the number of items along each dimension. reshape() gives the same data a new shape provided the total number of elements stays the same. A -1 asks NumPy to calculate that dimension, and .T swaps rows and columns. An impossible shape raises ValueError. Library used: NumPy.",
  tags=["numpy", "shape", "reshape", "transpose"], topics=["Dimensions of Arrays", "Attributes of an Array"]),

P(title="Demonstrate Array Size (NumPy)", category="Arrays (NumPy)", difficulty="Beginner",
  description="Finds the number of elements and memory used by NumPy arrays (library: NumPy).",
  concepts=["size", "len()", "itemsize", "nbytes"], filename="numpy_size.py", deps=["numpy"],
  code=r'''
# Requires: pip install numpy
# Library used: NumPy
import numpy as np

vector = np.array([5, 10, 15, 20])
matrix = np.arange(12).reshape(3, 4)

print("vector.size :", vector.size)
print("matrix.size :", matrix.size, "(rows x columns = 3 x 4)")
print("len(matrix) :", len(matrix), "(length of the first dimension only)")
print("matrix.shape:", matrix.shape)

print("itemsize    :", matrix.itemsize, "bytes per element")
print("nbytes      :", matrix.nbytes, "bytes in total")
print("check       :", matrix.size * matrix.itemsize)

small = np.arange(12, dtype=np.int8)
print("int8 array nbytes:", small.nbytes)
''',
  algorithm=["Create a 1-D and a 2-D array", "Print size for both", "Compare size with len()", "Print itemsize and nbytes", "Show that a smaller dtype needs less memory"],
  explanation="size is the total number of elements in an array, which is the product of all values in the shape. len() only gives the length of the first dimension, so for a 3x4 matrix it is 3 while size is 12. itemsize is the bytes per element and nbytes is the memory for the whole array. Library used: NumPy.",
  tags=["numpy", "size", "nbytes", "len"], topics=["Attributes of an Array"]),

P(title="Demonstrate Array Attributes (NumPy)", category="Arrays (NumPy)", difficulty="Beginner",
  description="Prints the main ndarray attributes: ndim, shape, size, dtype, itemsize, nbytes and T (library: NumPy).",
  concepts=["ndarray attributes", "dtype", "ndim", "shape"], filename="numpy_attributes.py", deps=["numpy"],
  code=r'''
# Requires: pip install numpy
# Library used: NumPy. (array.array only has typecode, itemsize and buffer_info().)
import numpy as np

arr = np.array([[1.5, 2.5, 3.5],
                [4.5, 5.5, 6.5]])

print("Array:")
print(arr)
print("ndim     :", arr.ndim)
print("shape    :", arr.shape)
print("size     :", arr.size)
print("dtype    :", arr.dtype)
print("itemsize :", arr.itemsize)
print("nbytes   :", arr.nbytes)
print("type     :", type(arr))
print("Transpose arr.T:")
print(arr.T)

ints = np.array([1, 2, 3], dtype=np.int16)
print("int16 array dtype:", ints.dtype, "itemsize:", ints.itemsize)
print("astype(float)    :", ints.astype(float))
''',
  algorithm=["Create a 2-D float array", "Print ndim, shape and size", "Print dtype, itemsize and nbytes", "Print the transpose with .T", "Create an int16 array and convert it with astype()"],
  explanation="Attributes describe an ndarray without changing it: ndim gives the dimensions, shape the length of each, size the element count, dtype the data type, itemsize bytes per element, and nbytes the total memory. The attribute T returns the transpose. astype() makes a copy with another dtype. Library used: NumPy.",
  tags=["numpy", "attributes", "dtype", "ndim"], topics=["Attributes of an Array", "Types of Arrays"]),

P(title="Demonstrate Array Slicing (NumPy)", category="Arrays (NumPy)", difficulty="Intermediate",
  description="Slices 1-D and 2-D NumPy arrays and shows that slices are views (library: NumPy).",
  concepts=["slicing", "step", "views vs copies"], filename="numpy_slicing.py", deps=["numpy"],
  code=r'''
# Requires: pip install numpy
# Library used: NumPy
import numpy as np

a = np.arange(10, 100, 10)              # [10 20 ... 90]
print("a          :", a)
print("a[2:6]     :", a[2:6])
print("a[:3]      :", a[:3])
print("a[5:]      :", a[5:])
print("a[::2]     :", a[::2])
print("a[::-1]    :", a[::-1])
print("a[-3:]     :", a[-3:])

m = np.arange(1, 17).reshape(4, 4)
print("Matrix:")
print(m)
print("m[1:3, 1:3]:")
print(m[1:3, 1:3])
print("m[:, 0]    :", m[:, 0])
print("m[-1, :]   :", m[-1, :])

# a slice is a VIEW: changing it changes the original
view = a[:3]
view[0] = 999
print("After view[0]=999, a =", a)

# copy() makes an independent array
safe = a[:3].copy()
safe[0] = -1
print("After copy change, a[0] =", a[0])
''',
  algorithm=["Create a 1-D array and slice with start:stop:step", "Use negative indexes and steps", "Create a 4x4 matrix", "Slice rows and columns with [rows, columns]", "Show that a slice is a view and copy() is independent"],
  explanation="NumPy slicing uses start:stop:step, and for 2-D arrays one slice per dimension separated by a comma. A colon alone selects everything along a dimension. Unlike list slicing, a NumPy slice is a view of the same memory, so changing it changes the original unless copy() is used. Library used: NumPy.",
  tags=["numpy", "slicing", "view", "copy"], topics=["Dimensions of Arrays"]),

P(title="Demonstrate Matrix Addition (NumPy)", category="Arrays (NumPy)", difficulty="Beginner",
  description="Adds two matrices with NumPy and with nested loops for comparison (library: NumPy).",
  concepts=["matrix addition", "np.add()", "nested loops"], filename="numpy_matrix_addition.py", deps=["numpy"],
  code=r'''
# Requires: pip install numpy
# Library used: NumPy
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[9, 8, 7],
              [6, 5, 4]])

print("Matrix A:")
print(A)
print("Matrix B:")
print(B)

if A.shape != B.shape:
    print("Matrices must have the same shape to be added.")
else:
    print("A + B using the + operator:")
    print(A + B)
    print("A + B using np.add():")
    print(np.add(A, B))

    # same result using nested loops
    result = np.zeros(A.shape, dtype=int)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            result[i, j] = A[i, j] + B[i, j]
    print("Using nested loops:")
    print(result)
    print("Both methods equal:", np.array_equal(A + B, result))
''',
  algorithm=["Create two matrices of the same shape", "Check that the shapes match", "Add them with + and np.add()", "Add them element by element with nested loops", "Compare the results"],
  explanation="Two matrices can be added only when they have the same shape; each element is added to the element in the same position. NumPy does this in one step with + or np.add(). The nested loop version shows what happens internally, and array_equal() confirms both give the same answer. Library used: NumPy.",
  tags=["numpy", "matrix", "addition", "2d"], topics=["Mathematical Operations on Arrays", "Dimensions of Arrays"]),

P(title="Demonstrate Matrix Multiplication (NumPy)", category="Arrays (NumPy)", difficulty="Intermediate",
  description="Multiplies matrices with @, np.dot() and nested loops, and contrasts it with element-wise * (library: NumPy).",
  concepts=["matrix multiplication", "@ operator", "np.dot()"], filename="numpy_matrix_multiplication.py", deps=["numpy"],
  code=r'''
# Requires: pip install numpy
# Library used: NumPy
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]])          # 2 x 3
B = np.array([[7, 8],
              [9, 10],
              [11, 12]])           # 3 x 2

print("A (2x3):")
print(A)
print("B (3x2):")
print(B)

if A.shape[1] != B.shape[0]:
    print("Columns of A must equal rows of B.")
else:
    print("A @ B (2x2):")
    print(A @ B)
    print("np.dot(A, B):")
    print(np.dot(A, B))

    # triple nested loop
    result = np.zeros((A.shape[0], B.shape[1]), dtype=int)
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                result[i, j] += A[i, k] * B[k, j]
    print("Using loops:")
    print(result)

# element-wise product is different
C = np.array([[1, 2], [3, 4]])
D = np.array([[5, 6], [7, 8]])
print("C * D (element-wise):")
print(C * D)
print("C @ D (matrix product):")
print(C @ D)
''',
  algorithm=["Create A (2x3) and B (3x2)", "Check columns of A equal rows of B", "Multiply with @ and np.dot()", "Use three nested loops: row of A times column of B", "Show that * multiplies element by element"],
  explanation="In matrix multiplication each result element is the sum of products of a row of the first matrix and a column of the second, so the columns of A must equal the rows of B. NumPy provides the @ operator and np.dot() for this. The triple loop shows the calculation step by step. Note that * on NumPy arrays is element-wise multiplication, which gives a different answer. Library used: NumPy.",
  tags=["numpy", "matrix", "multiplication", "dot"], topics=["Mathematical Operations on Arrays", "Dimensions of Arrays"]),
]
