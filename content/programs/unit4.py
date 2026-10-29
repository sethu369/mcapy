import sys; sys.path.insert(0, __file__.rsplit("/", 2)[0])   # so `schema` imports
from schema import P

PROGRAMS = [
P(title="Create a List", category="Lists", difficulty="Beginner",
  description="Creates lists in several ways: literal, list(), range() and an empty list.",
  concepts=["list", "list()", "range()", "len()"], filename="create_list.py",
  code=r'''
# Different ways of creating a list
fruits = ["apple", "banana", "cherry"]          # list literal
mixed = [10, "Python", 3.14, True]              # a list can hold different types
numbers = list(range(1, 6))                     # from range()
letters = list("MCA")                           # from a string
empty = []                                      # empty list

print("Fruits :", fruits)
print("Mixed  :", mixed)
print("Numbers:", numbers)
print("Letters:", letters)
print("Empty  :", empty, "-> length", len(empty))
print("Type   :", type(fruits))
''',
  algorithm=["Create a list using square brackets", "Create a list holding mixed data types", "Create lists using list() with range() and a string", "Create an empty list", "Print each list and its type"],
  explanation="A list is an ordered, changeable collection written inside square brackets. The program builds lists using a literal, the list() constructor with range() and with a string, and an empty list. Lists may contain items of different types. type() confirms the object is of class list and len() gives the number of items.",
  tags=["list", "create", "range", "basics"], topics=["Creating Lists"]),

P(title="Access List Elements", category="Lists", difficulty="Beginner",
  description="Accesses list items using positive and negative indexes and a for loop.",
  concepts=["indexing", "negative index", "for loop"], filename="access_list_elements.py",
  code=r'''
colors = ["red", "green", "blue", "yellow", "black"]

print("First element :", colors[0])
print("Third element :", colors[2])
print("Last element  :", colors[-1])
print("Second last   :", colors[-2])

print("All elements with their index:")
for index, color in enumerate(colors):
    print(f"  colors[{index}] = {color}")

try:
    print(colors[10])
except IndexError as error:
    print("Error:", error)
''',
  algorithm=["Create a list of colours", "Access items with positive indexes (start at 0)", "Access items with negative indexes (from the end)", "Loop with enumerate() to show index and value", "Catch IndexError for an invalid index"],
  explanation="List items are accessed with an index inside square brackets; the first item has index 0 and the last has index -1. enumerate() gives both the index and the item while looping. Using an index outside the list raises IndexError, which is handled with try/except.",
  tags=["list", "index", "access"], topics=["Creating Lists"]),

P(title="Update List Elements", category="Lists", difficulty="Beginner",
  description="Changes single items and a range of items in a list because lists are mutable.",
  concepts=["mutability", "assignment", "slice assignment"], filename="update_list_elements.py",
  code=r'''
marks = [45, 60, 72, 58, 90]
print("Original :", marks)

marks[0] = 50                 # update one element
print("After marks[0] = 50 :", marks)

marks[-1] = marks[-1] + 5     # update using its current value
print("After adding 5 to last :", marks)

marks[1:3] = [65, 75]         # update a slice (range of elements)
print("After slice update :", marks)

# Update every element: add 2 grace marks
for i in range(len(marks)):
    marks[i] += 2
print("After grace marks :", marks)
''',
  algorithm=["Create a list of marks", "Assign a new value to one index", "Update using the existing value", "Replace a slice with new values", "Loop over indexes to update every item"],
  explanation="Lists are mutable, so an item can be replaced by assigning to its index. A slice on the left side of = replaces several items at once. To update every item the program loops over the indexes using range(len(list)) and modifies each position in place.",
  tags=["list", "update", "mutable"], topics=["Updating the Elements of a List"]),

P(title="Add Elements to a List", category="Lists", difficulty="Beginner",
  description="Adds items using append(), insert() and extend().",
  concepts=["append()", "insert()", "extend()"], filename="add_list_elements.py",
  code=r'''
subjects = ["Python", "Maths"]
print("Start   :", subjects)

subjects.append("DBMS")            # add at the end
print("append  :", subjects)

subjects.insert(1, "Networks")     # add at a given position
print("insert  :", subjects)

subjects.extend(["OS", "Java"])    # add many items
print("extend  :", subjects)

subjects += ["AI"]                 # same effect as extend
print("+=      :", subjects)

subjects.append(["x", "y"])        # append adds the list as ONE item
print("append list :", subjects)
''',
  algorithm=["Start with a small list", "append() one item at the end", "insert() an item at index 1", "extend() with several items", "Show that append(list) adds a nested list"],
  explanation="append() adds one item at the end, insert(index, item) places an item at a chosen position and extend() adds every item of another iterable. The += operator behaves like extend(). Note that append() with a list adds that whole list as a single nested item.",
  tags=["list", "append", "insert", "extend"], topics=["Methods to Process Lists"]),

P(title="Remove List Elements", category="Lists", difficulty="Beginner",
  description="Removes items using remove(), pop(), del and clear().",
  concepts=["remove()", "pop()", "del", "clear()"], filename="remove_list_elements.py",
  code=r'''
items = [10, 20, 30, 40, 50, 20, 60]
print("Start :", items)

items.remove(20)              # removes the first matching value
print("remove(20) :", items)

popped = items.pop()          # removes and returns the last item
print("pop() ->", popped, items)

popped = items.pop(1)         # removes item at index 1
print("pop(1) ->", popped, items)

del items[0]                  # delete by index
print("del items[0] :", items)

del items[1:3]                # delete a slice
print("del items[1:3] :", items)

items.clear()                 # remove everything
print("clear() :", items)

try:
    [1, 2].remove(99)
except ValueError as error:
    print("Error:", error)
''',
  algorithm=["Create a list with a repeated value", "remove() the first occurrence of a value", "pop() the last item and an item by index", "Use del for an index and for a slice", "clear() the list", "Handle ValueError when value is missing"],
  explanation="remove(value) deletes the first matching value, pop(index) deletes by position and returns the removed item (last item by default), and del can delete one index or a slice. clear() empties the list. Removing a value that is not present raises ValueError, which is caught here.",
  tags=["list", "remove", "pop", "del"], topics=["Methods to Process Lists"]),

P(title="Concatenate Two Lists", category="Lists", difficulty="Beginner",
  description="Joins two lists with +, extend() and unpacking.",
  concepts=["+ operator", "extend()", "unpacking"], filename="concatenate_lists.py",
  code=r'''
list1 = [1, 2, 3]
list2 = [4, 5, 6]

joined = list1 + list2            # creates a NEW list
print("list1 + list2 :", joined)
print("list1 unchanged:", list1)

list1.extend(list2)               # modifies list1 itself
print("after extend  :", list1)

a = ["a", "b"]
b = ["c", "d"]
c = [*a, *b, "e"]                 # unpacking
print("unpacking     :", c)
''',
  algorithm=["Create two lists", "Join them with + to get a new list", "Use extend() to add the second list to the first", "Use * unpacking to join lists and extra items", "Print results"],
  explanation="The + operator concatenates two lists and returns a new list, leaving the originals unchanged. extend() adds the items of one list into another in place. The unpacking syntax [*a, *b] is another way to build a combined list.",
  tags=["list", "concatenate", "join", "plus"], topics=["Concatenation of Two Lists"]),

P(title="Repeat a List", category="Lists", difficulty="Beginner",
  description="Repeats a list using the * operator and shows the shared-reference trap with nested lists.",
  concepts=["* operator", "repetition", "nested list"], filename="repeat_list.py",
  code=r'''
pattern = [1, 2, 3]
print("pattern * 3 :", pattern * 3)

zeros = [0] * 8                  # handy way to create a list of zeros
print("zeros       :", zeros)

stars = ["*"] * 5
print("stars       :", stars)

# Trap: repeating a nested list copies the REFERENCE
shared = [[0] * 3] * 2
shared[0][0] = 99
print("shared  (wrong):", shared)

separate = [[0] * 3 for _ in range(2)]
separate[0][0] = 99
print("separate (right):", separate)
''',
  algorithm=["Create a list", "Repeat it with * 3", "Create a list of zeros with [0] * n", "Show the problem with [[0]*3]*2", "Fix it using a list comprehension"],
  explanation="Multiplying a list by an integer repeats its items and gives a new list. This is useful to initialise lists such as [0] * 8. When the item is itself a list, the repetition copies references, so changing one row changes all rows; a list comprehension creates independent rows.",
  tags=["list", "repetition", "multiply"], topics=["Repetition of Lists"]),

P(title="Check Membership in a List", category="Lists", difficulty="Beginner",
  description="Uses the in and not in operators to test whether an item is present in a list.",
  concepts=["in", "not in", "input", "if-else"], filename="list_membership.py", kind="Interactive",
  code=r'''
cities = ["Delhi", "Mumbai", "Chennai", "Kolkata", "Pune"]
print("Cities:", cities)

name = input("Enter a city to search: ").strip().title()

if name in cities:
    print(f"{name} is present in the list.")
else:
    print(f"{name} is NOT present in the list.")

print("'Goa' not in cities ->", "Goa" not in cities)
print("3 in [1, 2, 3]      ->", 3 in [1, 2, 3])
''',
  sample_input="mumbai",
  algorithm=["Create a list of cities", "Read a city name and format it", "Test with the in operator", "Print whether it is present", "Show not in as well"],
  explanation="The in operator returns True when the value is found in the list and not in returns the opposite. The program reads a city name, cleans it using strip() and title(), and checks membership. This is a readable alternative to writing a search loop.",
  tags=["list", "membership", "in", "search"], topics=["Membership in Lists"]),

P(title="Demonstrate List Methods", category="Lists", difficulty="Intermediate",
  description="Shows the commonly used list methods: count, index, copy, sort, reverse and more.",
  concepts=["list methods", "count()", "index()", "copy()"], filename="list_methods.py",
  code=r'''
data = [5, 3, 8, 3, 1]
print("data:", data)

print("len(data)     :", len(data))
print("count(3)      :", data.count(3))
print("index(8)      :", data.index(8))

data.append(7)
data.insert(0, 9)
data.extend([2, 2])
print("after add     :", data)

data.remove(3)
print("remove(3)     :", data)
print("pop()         :", data.pop())

copy_of_data = data.copy()
data.sort()
print("sorted data   :", data)
print("copy (unsorted):", copy_of_data)

data.reverse()
print("reversed      :", data)

data.clear()
print("clear()       :", data)
''',
  algorithm=["Create a list", "Use len(), count() and index() to query it", "Use append(), insert(), extend() to add", "Use remove() and pop() to delete", "Use copy(), sort(), reverse() and clear()"],
  explanation="Lists have many built-in methods that change the list in place: append, insert, extend, remove, pop, sort, reverse and clear. count() and index() only inspect it, and copy() makes a shallow copy. Most of these methods return None, so the list itself is printed after calling them.",
  tags=["list", "methods", "count", "index"], topics=["Methods to Process Lists"]),

P(title="Sort a List", category="Lists", difficulty="Beginner",
  description="Sorts a list using sort() and sorted(), in ascending and descending order and with a key.",
  concepts=["sort()", "sorted()", "reverse=True", "key"], filename="sort_list.py",
  code=r'''
numbers = [42, 7, 19, 3, 88, 25]
print("Original         :", numbers)
print("sorted() ascending:", sorted(numbers))
print("sorted() descending:", sorted(numbers, reverse=True))
print("Original untouched:", numbers)

numbers.sort()                      # sorts in place
print("after sort()     :", numbers)

words = ["banana", "kiwi", "apple", "fig", "cherry"]
print("Alphabetical     :", sorted(words))
print("By length        :", sorted(words, key=len))

# Manual bubble sort to understand the logic
data = [64, 34, 25, 12, 22]
for i in range(len(data) - 1):
    for j in range(len(data) - 1 - i):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
print("Bubble sort      :", data)
''',
  algorithm=["Create a list of numbers", "Use sorted() to get a new sorted list", "Use sort() to sort in place", "Use reverse=True and key=len", "Implement bubble sort manually"],
  explanation="sorted() returns a new sorted list and leaves the original alone, while sort() sorts the list itself. The reverse argument gives descending order and key chooses what to compare, e.g. len. The bubble sort at the end repeatedly swaps neighbouring items that are out of order.",
  tags=["list", "sort", "sorted", "bubble sort"], topics=["Sorting"]),

P(title="Reverse a List", category="Lists", difficulty="Beginner",
  description="Reverses a list using reverse(), slicing and reversed().",
  concepts=["reverse()", "slicing [::-1]", "reversed()"], filename="reverse_list.py",
  code=r'''
nums = [1, 2, 3, 4, 5]
print("Original      :", nums)
print("Slicing [::-1]:", nums[::-1])
print("reversed()    :", list(reversed(nums)))
print("Original kept :", nums)

nums.reverse()                       # in place
print("reverse()     :", nums)

# Manual reversal using two pointers
data = ["a", "b", "c", "d"]
left, right = 0, len(data) - 1
while left < right:
    data[left], data[right] = data[right], data[left]
    left += 1
    right -= 1
print("Manual reverse:", data)
''',
  algorithm=["Create a list", "Reverse with slicing to get a new list", "Use reversed() with list()", "Use reverse() to reverse in place", "Reverse manually by swapping from both ends"],
  explanation="Slicing with step -1 and reversed() produce a reversed copy, while reverse() changes the list itself. The manual method keeps two positions, one at each end, and swaps the items while moving towards the middle.",
  tags=["list", "reverse", "slicing"], topics=["Methods to Process Lists"]),

P(title="Find Maximum and Minimum in a List", category="Lists", difficulty="Beginner",
  description="Finds the largest and smallest values using max()/min() and a manual loop.",
  concepts=["max()", "min()", "loop", "comparison"], filename="list_max_min.py", kind="Interactive",
  code=r'''
text = input("Enter numbers separated by spaces: ")
try:
    numbers = [float(x) for x in text.split()]
    if not numbers:
        raise ValueError("no numbers entered")
except ValueError as error:
    print("Invalid input:", error)
else:
    print("Using built-ins -> max:", max(numbers), " min:", min(numbers))

    # Manual logic
    largest = smallest = numbers[0]
    for n in numbers[1:]:
        if n > largest:
            largest = n
        if n < smallest:
            smallest = n
    print("Using a loop   -> max:", largest, " min:", smallest)
''',
  sample_input="45 12 89 3 67 21",
  algorithm=["Read numbers as a line of text", "Convert to a list of floats with validation", "Print max() and min()", "Repeat the logic with a loop", "Compare each item with the current largest and smallest"],
  explanation="max() and min() return the largest and smallest items. The loop version starts with the first item as both largest and smallest and updates them whenever a bigger or smaller item is found. Input is split into words and converted with float(); bad input is caught by try/except.",
  tags=["list", "max", "min", "largest"], topics=["Methods to Process Lists"]),

P(title="Find Sum and Average of a List", category="Lists", difficulty="Beginner",
  description="Calculates the total and mean of the numbers in a list.",
  concepts=["sum()", "len()", "average"], filename="list_sum_average.py", kind="Interactive",
  code=r'''
text = input("Enter marks separated by spaces: ")
try:
    marks = [float(x) for x in text.split()]
    if not marks:
        raise ValueError("list is empty")
except ValueError as error:
    print("Invalid input:", error)
else:
    total = sum(marks)
    average = total / len(marks)
    print("Marks   :", marks)
    print("Sum     :", total)
    print("Count   :", len(marks))
    print(f"Average : {average:.2f}")

    # Same thing with a loop
    running = 0
    for m in marks:
        running += m
    print("Loop sum:", running)
''',
  sample_input="70 85 90 65 80",
  algorithm=["Read the numbers and convert to floats", "Compute the sum with sum()", "Divide by len() for the average", "Verify the sum with a loop", "Print the results"],
  explanation="sum() adds all numbers and len() counts them, so the average is sum divided by count. The program validates the input to avoid dividing by zero for an empty list. A for loop with a running total shows how sum() works internally.",
  tags=["list", "sum", "average", "mean"], topics=["Methods to Process Lists"]),

P(title="Remove Duplicates from a List", category="Lists", difficulty="Intermediate",
  description="Removes repeated items in three ways, one of which keeps the original order.",
  concepts=["set()", "dict.fromkeys()", "loop"], filename="remove_duplicates.py",
  code=r'''
items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("Original          :", items)

# 1. set() - removes duplicates but loses order
print("Using set()       :", list(set(items)))

# 2. dict.fromkeys() - keeps first-appearance order
print("Using dict.fromkeys:", list(dict.fromkeys(items)))

# 3. Manual loop - keeps order
unique = []
for x in items:
    if x not in unique:
        unique.append(x)
print("Using a loop      :", unique)
''',
  algorithm=["Create a list containing repeated values", "Convert to a set to drop duplicates", "Use dict.fromkeys() to keep order", "Use a loop that appends only unseen items", "Print all results"],
  explanation="A set stores only unique values, so list(set(items)) removes duplicates, but a set does not guarantee order. Dictionary keys are unique and keep insertion order, so dict.fromkeys() preserves the original order. The loop checks with 'not in' before appending.",
  tags=["list", "duplicates", "set", "unique"], topics=["Methods to Process Lists"]),

P(title="Demonstrate Nested Lists", category="Lists", difficulty="Intermediate",
  description="Builds a list of lists (a matrix), accesses and modifies items, and loops through it.",
  concepts=["nested list", "double index", "nested loop"], filename="nested_lists.py",
  code=r'''
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("Whole matrix :", matrix)
print("matrix[1]    :", matrix[1])
print("matrix[1][2] :", matrix[1][2])

matrix[0][0] = 100
matrix[2].append(10)
print("After changes:", matrix)

print("Printing as a table:")
for row in matrix:
    for value in row:
        print(f"{value:4}", end="")
    print()

# Rows may have different lengths
students = [["Asha", 80, 90], ["Ravi", 70], ["Meena", 95, 85, 75]]
for record in students:
    print(record[0], "has", len(record) - 1, "marks")
''',
  algorithm=["Create a list whose items are lists", "Access an item using two indexes", "Modify an inner item and append to an inner list", "Use nested loops to print it as a table", "Show rows of different length"],
  explanation="A nested list is a list that contains other lists, often used for tables and matrices. matrix[row][column] first picks a row and then a column. Nested for loops visit every value, and inner lists can have different lengths.",
  tags=["list", "nested", "matrix", "2d"], topics=["Nested Lists"]),

P(title="Demonstrate List Comprehension", category="Lists", difficulty="Intermediate",
  description="Creates lists compactly using list comprehensions with conditions.",
  concepts=["list comprehension", "condition", "expression"], filename="list_comprehension.py",
  code=r'''
squares = [n * n for n in range(1, 11)]
print("Squares       :", squares)

evens = [n for n in range(1, 21) if n % 2 == 0]
print("Even numbers  :", evens)

words = ["python", "java", "c", "kotlin"]
upper = [w.upper() for w in words]
print("Upper case    :", upper)

lengths = [len(w) for w in words]
print("Lengths       :", lengths)

labels = ["even" if n % 2 == 0 else "odd" for n in range(1, 6)]
print("Even/odd      :", labels)

pairs = [(x, y) for x in range(1, 3) for y in "ab"]
print("Pairs         :", pairs)

# Equivalent loop for the first example
loop_squares = []
for n in range(1, 11):
    loop_squares.append(n * n)
print("Same with loop:", loop_squares == squares)
''',
  algorithm=["Write [expression for item in iterable]", "Add an if condition to filter", "Apply a string method to each item", "Use a conditional expression", "Compare with the equivalent for loop"],
  explanation="A list comprehension builds a new list in one line: [expression for item in iterable if condition]. It replaces a loop that appends to an empty list. The program shows squares, filtering, transforming strings, conditional values and two loops in one comprehension.",
  tags=["list", "comprehension", "loop", "filter"], topics=["Creating Lists"]),

P(title="Search an Element in a List", category="Lists", difficulty="Beginner",
  description="Performs a linear search and reports the position of the element.",
  concepts=["linear search", "enumerate()", "index()"], filename="search_in_list.py", kind="Interactive",
  code=r'''
numbers = [14, 27, 35, 48, 52, 63, 71]
print("List:", numbers)

try:
    target = int(input("Enter the number to search: "))
except ValueError:
    print("Please enter an integer.")
else:
    found_at = -1
    for position, value in enumerate(numbers):
        if value == target:
            found_at = position
            break

    if found_at == -1:
        print(f"{target} was not found.")
    else:
        print(f"{target} found at index {found_at} (position {found_at + 1}).")

    # Built-in way
    if target in numbers:
        print("index() also says:", numbers.index(target))
''',
  sample_input="48",
  algorithm=["Read the number to search", "Loop through the list with enumerate()", "If an item equals the target, save the index and stop", "Report found or not found", "Show the built-in index() method"],
  explanation="Linear search checks the items one by one from the start until the target is found. enumerate() supplies the position along with the value, and break stops the loop at the first match. The same result can be obtained with the in operator and index().",
  tags=["list", "search", "linear search"], topics=["Membership in Lists"]),

P(title="Demonstrate List Slicing", category="Lists", difficulty="Beginner",
  description="Extracts parts of a list using start, stop and step values.",
  concepts=["slicing", "step", "negative index"], filename="list_slicing.py",
  code=r'''
nums = [10, 20, 30, 40, 50, 60, 70, 80]
print("nums         :", nums)
print("nums[2:5]    :", nums[2:5])     # index 2,3,4
print("nums[:3]     :", nums[:3])      # first three
print("nums[5:]     :", nums[5:])      # from index 5
print("nums[-3:]    :", nums[-3:])     # last three
print("nums[::2]    :", nums[::2])     # every second item
print("nums[1:7:3]  :", nums[1:7:3])
print("nums[::-1]   :", nums[::-1])    # reversed
print("nums[:]      :", nums[:], "(a copy)")
print("nums[20:30]  :", nums[20:30], "(out of range gives empty list)")
''',
  algorithm=["Create a list of eight numbers", "Slice with start and stop", "Omit start or stop", "Use negative indexes", "Use a step value, including -1", "Show that slicing never raises IndexError"],
  explanation="The slice list[start:stop:step] returns a new list from start up to but not including stop. Leaving out a value uses the default: the beginning, the end or a step of 1. Negative indexes count from the end and a step of -1 reverses the list. Slices outside the range simply give an empty list.",
  tags=["list", "slice", "step"], topics=["Creating Lists"]),

P(title="Create a Tuple", category="Tuples", difficulty="Beginner",
  description="Creates tuples using parentheses, tuple(), a single-item tuple and packing without brackets.",
  concepts=["tuple", "tuple()", "immutability"], filename="create_tuple.py",
  code=r'''
colors = ("red", "green", "blue")        # tuple literal
mixed = (1, "two", 3.0, True)            # different types
numbers = tuple(range(1, 6))             # from range()
letters = tuple("PYTHON")                # from a string
packed = 10, 20, 30                      # parentheses are optional
single = (5,)                            # comma makes it a tuple
not_tuple = (5)                          # this is just an int
empty = ()

print("colors   :", colors)
print("mixed    :", mixed)
print("numbers  :", numbers)
print("letters  :", letters)
print("packed   :", packed, type(packed))
print("single   :", single, type(single))
print("not_tuple:", not_tuple, type(not_tuple))
print("empty    :", empty, "length", len(empty))

try:
    colors[0] = "pink"
except TypeError as error:
    print("Tuples are immutable ->", error)
''',
  algorithm=["Create tuples with parentheses", "Create tuples with tuple() from range and string", "Create a tuple without brackets (packing)", "Show that a single item needs a trailing comma", "Try to change an item and catch TypeError"],
  explanation="A tuple is an ordered collection written with parentheses. Unlike a list it cannot be changed after creation, so assigning to an item raises TypeError. A tuple with one item needs a trailing comma, otherwise Python treats the brackets as ordinary grouping. tuple() converts other iterables such as range or a string.",
  tags=["tuple", "create", "immutable"], topics=["Creating Tuples"]),

P(title="Access Tuple Elements", category="Tuples", difficulty="Beginner",
  description="Reads tuple items with an index, negative index and a for loop.",
  concepts=["indexing", "enumerate()", "for loop"], filename="access_tuple_elements.py",
  code=r'''
days = ("Mon", "Tue", "Wed", "Thu", "Fri")

print("First  :", days[0])
print("Third  :", days[2])
print("Last   :", days[-1])

print("Using a for loop:")
for day in days:
    print("  ", day)

print("With positions:")
for position, day in enumerate(days, start=1):
    print(f"  {position}. {day}")

try:
    print(days[9])
except IndexError as error:
    print("Error:", error)
''',
  algorithm=["Create a tuple of days", "Access items by positive and negative index", "Loop through the tuple", "Use enumerate() for positions", "Handle IndexError"],
  explanation="Tuple items are read with square brackets exactly like list items; index 0 is the first item and -1 is the last. A for loop visits every item and enumerate() adds a counter. An index beyond the end raises IndexError, which is caught with try/except.",
  tags=["tuple", "access", "index"], topics=["Accessing the Tuple Elements"]),

P(title="Demonstrate Tuple Indexing", category="Tuples", difficulty="Beginner",
  description="Shows positive and negative indexes of a tuple and searches an item with index().",
  concepts=["index", "negative index", "index()"], filename="tuple_indexing.py",
  code=r'''
letters = ("a", "b", "c", "d", "e")

print("Index table:")
for i in range(len(letters)):
    print(f"  letters[{i}] = letters[{i - len(letters)}] = {letters[i]}")

print("index('d')  :", letters.index("d"))
try:
    letters.index("z")
except ValueError as error:
    print("index('z')  : ValueError ->", error)
''',
  algorithm=["Create a tuple of letters", "Print each item with its positive and negative index", "Use index() to find the position of a value", "Catch ValueError when the value is missing"],
  explanation="Every tuple item has two valid indexes: a positive one counting from the start and a negative one counting from the end. The loop prints both for each item. The index() method returns the position of the first matching value and raises ValueError when the value is not present.",
  tags=["tuple", "index", "negative index"], topics=["Accessing the Tuple Elements"]),

P(title="Demonstrate Tuple Slicing", category="Tuples", difficulty="Beginner",
  description="Extracts parts of a tuple using start, stop and step.",
  concepts=["slicing", "step", "reverse"], filename="tuple_slicing.py",
  code=r'''
t = (10, 20, 30, 40, 50, 60, 70)
print("t         :", t)
print("t[1:4]    :", t[1:4])
print("t[:3]     :", t[:3])
print("t[4:]     :", t[4:])
print("t[-3:]    :", t[-3:])
print("t[::2]    :", t[::2])
print("t[::-1]   :", t[::-1])
print("Type of slice:", type(t[1:4]))
''',
  algorithm=["Create a tuple of seven numbers", "Slice with start and stop", "Omit start or stop", "Use negative indexes", "Use steps 2 and -1", "Show that a slice is also a tuple"],
  explanation="The slice t[start:stop:step] returns a new tuple from start up to but not including stop. Omitted values default to the beginning, the end and a step of 1. A step of -1 reverses the tuple. The original tuple is never modified because tuples are immutable.",
  tags=["tuple", "slice", "step"], topics=["Operations on Tuples"]),

P(title="Concatenate Tuples", category="Tuples", difficulty="Beginner",
  description="Joins tuples using the + operator and shows how to 'add' an item to a tuple.",
  concepts=["+ operator", "concatenation"], filename="concatenate_tuples.py",
  code=r'''
t1 = (1, 2, 3)
t2 = (4, 5)
joined = t1 + t2
print("t1 + t2       :", joined)
print("t1 unchanged  :", t1)

# Adding one item: the right side must also be a tuple
t1 = t1 + (99,)
print("t1 + (99,)    :", t1)

try:
    t1 + [4]
except TypeError as error:
    print("Error:", error)
''',
  algorithm=["Create two tuples", "Join them with +", "Show the originals are unchanged", "Add one item using a one-item tuple", "Show the TypeError when joining a tuple and a list"],
  explanation="The + operator creates a new tuple that contains the items of both tuples. Since tuples cannot change, 'adding' an item really builds a new tuple and rebinds the name. Both sides of + must be tuples, otherwise Python raises TypeError.",
  tags=["tuple", "concatenate", "plus"], topics=["Operations on Tuples"]),

P(title="Repeat Tuples", category="Tuples", difficulty="Beginner",
  description="Repeats the items of a tuple using the * operator.",
  concepts=["* operator", "repetition"], filename="repeat_tuples.py",
  code=r'''
t = ("ab", "cd")
print("t * 3     :", t * 3)
print("(0,) * 5  :", (0,) * 5)
print("t * 0     :", t * 0)
print("Original  :", t)

line = ("-",) * 20
print("".join(line))
''',
  algorithm=["Create a tuple", "Repeat it with * 3", "Repeat a one-item tuple to create (0,0,0,0,0)", "Repeat by 0 to get an empty tuple", "Join a repeated tuple to draw a line"],
  explanation="Multiplying a tuple by an integer n repeats its items n times and gives a new tuple. Multiplying by 0 gives an empty tuple. The original tuple is not changed. The join() call at the end turns the repeated dashes into a printable line.",
  tags=["tuple", "repeat", "multiply"], topics=["Operations on Tuples"]),

P(title="Demonstrate Tuple Membership", category="Tuples", difficulty="Beginner",
  description="Checks whether an item is in a tuple using in and not in with user input.",
  concepts=["in", "not in", "input"], filename="tuple_membership.py", kind="Interactive",
  code=r'''
vowels = ("a", "e", "i", "o", "u")
ch = input("Enter a character: ").strip().lower()

if len(ch) != 1:
    print("Please enter exactly one character.")
elif ch in vowels:
    print(f"'{ch}' is a vowel.")
elif ch.isalpha():
    print(f"'{ch}' is a consonant.")
else:
    print(f"'{ch}' is not a letter.")

print("'z' not in vowels ->", "z" not in vowels)
''',
  sample_input="E",
  algorithm=["Create a tuple of vowels", "Read a character and convert to lower case", "Validate that it is a single character", "Test membership using in", "Print the result"],
  explanation="The in operator checks whether a value is present in the tuple and returns True or False. The program reads one character and normalises it with strip() and lower(). If it is in the tuple of vowels it is a vowel; otherwise isalpha() separates consonants from other symbols.",
  tags=["tuple", "membership", "in", "vowel"], topics=["Operations on Tuples"]),

P(title="Demonstrate Tuple Methods", category="Tuples", difficulty="Beginner",
  description="Uses the two tuple methods, count() and index(), plus len().",
  concepts=["count()", "index()", "len()"], filename="tuple_methods.py",
  code=r'''
scores = (7, 3, 9, 3, 5, 3, 8)
print("Tuple        :", scores)
print("len()        :", len(scores))
print("count(3)     :", scores.count(3))
print("count(100)   :", scores.count(100))
print("index(9)     :", scores.index(9))
print("index(3, 2)  :", scores.index(3, 2), "(search starts at index 2)")

print("Methods of a tuple:", [m for m in dir(tuple) if not m.startswith("_")])
''',
  algorithm=["Create a tuple with repeated values", "Use len() to count items", "Use count() to count one value", "Use index() with an optional start position", "List all public tuple methods using dir()"],
  explanation="Because tuples are immutable they have only two methods: count(value) returns how many times a value occurs and index(value) returns its first position. index() accepts an optional start position. dir(tuple) proves that there is no append, remove or sort.",
  tags=["tuple", "methods", "count", "index"], topics=["Functions to Process Tuples"]),

P(title="Find Tuple Maximum and Minimum", category="Tuples", difficulty="Beginner",
  description="Finds the largest and smallest items of a tuple with max(), min() and a loop.",
  concepts=["max()", "min()", "loop"], filename="tuple_max_min.py",
  code=r'''
temperatures = (31.5, 28.0, 35.2, 26.4, 33.9)
print("Tuple   :", temperatures)
print("Maximum :", max(temperatures))
print("Minimum :", min(temperatures))

words = ("banana", "kiwi", "cherry", "fig")
print("Longest word :", max(words, key=len))
print("Shortest word:", min(words, key=len))
print("Alphabetically last:", max(words))

# Manual logic
largest = smallest = temperatures[0]
for value in temperatures:
    if value > largest:
        largest = value
    if value < smallest:
        smallest = value
print("Loop result :", largest, smallest)
''',
  algorithm=["Create a tuple of numbers", "Apply max() and min()", "Use key=len on a tuple of strings", "Repeat with a manual loop", "Print the results"],
  explanation="max() and min() accept any iterable, including a tuple. The key argument changes what is compared, for example len for the longest word. The loop version keeps the current largest and smallest value and updates them while scanning the tuple.",
  tags=["tuple", "max", "min"], topics=["Functions to Process Tuples"]),

P(title="Calculate Tuple Sum", category="Tuples", difficulty="Beginner",
  description="Adds the numbers in a tuple with sum() and with a loop, and finds the average.",
  concepts=["sum()", "loop", "average"], filename="tuple_sum.py",
  code=r'''
prices = (120, 250, 75, 310, 45)
print("Prices :", prices)
print("sum()  :", sum(prices))
print("sum(start=100):", sum(prices, 100))

total = 0
for price in prices:
    total += price
print("Loop   :", total)
print("Average:", total / len(prices))
print("sorted :", sorted(prices), "(sorted() returns a list)")
''',
  algorithm=["Create a tuple of prices", "Add with sum()", "Add using a for loop and a running total", "Divide by len() for the average", "Show sorted() on a tuple"],
  explanation="sum() adds every number in the tuple and has an optional second argument that is the starting value. The loop shows the same logic with a running total. The average is the total divided by the number of items. sorted() works on tuples but always returns a list.",
  tags=["tuple", "sum", "average"], topics=["Functions to Process Tuples"]),

P(title="Convert List to Tuple", category="Tuples", difficulty="Beginner",
  description="Converts a list into a tuple using tuple() and checks the types.",
  concepts=["tuple()", "type conversion"], filename="list_to_tuple.py",
  code=r'''
subjects = ["Python", "DBMS", "Maths"]
fixed = tuple(subjects)

print("List  :", subjects, type(subjects).__name__)
print("Tuple :", fixed, type(fixed).__name__)

subjects.append("OS")          # list can change
print("List after append :", subjects)
print("Tuple is unchanged:", fixed)

# A tuple can be used as a dictionary key, a list cannot
timetable = {fixed: "Room 101"}
print("Dictionary with tuple key:", timetable)
''',
  algorithm=["Create a list", "Convert it with tuple()", "Print both with their types", "Modify the list and show the tuple is unaffected", "Use the tuple as a dictionary key"],
  explanation="tuple(list) creates a new tuple holding the same items. The tuple is a separate object, so later changes to the list do not affect it. Converting to a tuple makes the data read-only and also hashable, which allows it to be used as a dictionary key.",
  tags=["tuple", "list", "convert"], topics=["Creating Tuples"]),

P(title="Convert Tuple to List", category="Tuples", difficulty="Beginner",
  description="Converts a tuple to a list so that it can be modified, then back to a tuple.",
  concepts=["list()", "tuple()", "mutability"], filename="tuple_to_list.py",
  code=r'''
original = (10, 20, 30)
print("Tuple :", original)

temp = list(original)       # tuple -> list
temp.append(40)
temp[0] = 5
temp.remove(20)
print("List  :", temp)

updated = tuple(temp)       # list -> tuple
print("New tuple:", updated)
print("Old tuple is still:", original)
''',
  algorithm=["Create a tuple", "Convert it to a list with list()", "Modify the list by append, assignment and remove", "Convert the list back to a tuple", "Show the original tuple is unchanged"],
  explanation="A tuple cannot be edited, so the usual trick is to convert it into a list, make the changes and convert it back. list() and tuple() each create a new object. The original tuple stays exactly as it was.",
  tags=["tuple", "list", "convert", "modify"], topics=["Operations on Tuples"]),

P(title="Demonstrate Nested Tuples", category="Tuples", difficulty="Intermediate",
  description="Builds a tuple of tuples, accesses inner items and loops through them.",
  concepts=["nested tuple", "double index", "loop"], filename="nested_tuples.py",
  code=r'''
students = (
    ("Asha", 21, (80, 90, 85)),
    ("Ravi", 22, (70, 65, 75)),
    ("Meena", 20, (95, 88, 92)),
)

print("First student   :", students[0])
print("Name of second  :", students[1][0])
print("Marks of third  :", students[2][2])
print("Maths of third  :", students[2][2][1])

for name, age, marks in students:
    print(f"{name:6} age {age}  total {sum(marks)}")

# The outer tuple is fixed, but a list inside a tuple can still change
box = ("label", [1, 2])
box[1].append(3)
print("Tuple holding a list:", box)
''',
  algorithm=["Create a tuple whose items are tuples", "Access items with several indexes", "Unpack each inner tuple in a for loop", "Calculate the total of the innermost tuple", "Show that a list inside a tuple stays mutable"],
  explanation="A nested tuple is a tuple that contains other tuples. Each extra pair of brackets goes one level deeper, for example students[2][2][1]. The loop unpacks each inner tuple into three names. A tuple only protects its own items, so a list stored inside it can still be changed.",
  tags=["tuple", "nested", "unpack"], topics=["Nested Tuples"]),

P(title="Demonstrate Tuple Unpacking", category="Tuples", difficulty="Intermediate",
  description="Unpacks tuples into variables, with the star operator, swapping and in function results.",
  concepts=["unpacking", "star operator", "swap"], filename="tuple_unpacking.py",
  code=r'''
point = (3, 4)
x, y = point
print("x =", x, " y =", y)

first, *middle, last = (1, 2, 3, 4, 5)
print("first:", first, "middle:", middle, "last:", last)

a, b = 10, 20
a, b = b, a                      # swap without a temp variable
print("After swap: a =", a, " b =", b)

name, _, city = ("Asha", 21, "Pune")   # _ ignores a value
print(name, "lives in", city)

try:
    p, q = (1, 2, 3)
except ValueError as error:
    print("Error:", error)
''',
  algorithm=["Unpack a tuple into two variables", "Use * to collect the remaining items", "Swap two variables using tuple assignment", "Ignore a value with _", "Show the ValueError when counts do not match"],
  explanation="Tuple unpacking assigns each item of a tuple to a separate variable in one statement. The number of names must match the number of items unless one name has a star, which collects the extra items into a list. Swapping with a, b = b, a works because the right side is packed into a tuple first.",
  tags=["tuple", "unpacking", "swap", "star"], topics=["Operations on Tuples"]),

P(title="Create a Dictionary", category="Dictionaries", difficulty="Beginner",
  description="Creates dictionaries using braces, dict(), zip() and a comprehension.",
  concepts=["dict", "key-value", "dict()", "zip()"], filename="create_dictionary.py",
  code=r'''
student = {"name": "Asha", "age": 21, "course": "MCA"}   # literal
point = dict(x=3, y=4)                                   # dict() with keywords
pairs = dict([("a", 1), ("b", 2)])                       # from list of pairs
keys = ["one", "two", "three"]
values = [1, 2, 3]
numbers = dict(zip(keys, values))                        # from two lists
squares = {n: n * n for n in range(1, 6)}                # comprehension
empty = {}

for label, d in [("student", student), ("point", point), ("pairs", pairs),
                 ("numbers", numbers), ("squares", squares), ("empty", empty)]:
    print(f"{label:8}:", d)
print("Type:", type(student), " length:", len(student))
''',
  algorithm=["Create a dictionary with braces and key: value pairs", "Create one with dict() keywords", "Create one from a list of pairs", "Combine two lists using zip()", "Build one with a dictionary comprehension", "Print all of them"],
  explanation="A dictionary stores data as key: value pairs inside braces. Keys must be unique and immutable (strings, numbers, tuples), values can be anything. Besides the literal form, dictionaries can be built with dict(), from pairs, by zipping two lists, or with a comprehension.",
  tags=["dictionary", "create", "dict", "zip"], topics=["Operations on Dictionaries"]),

P(title="Access Dictionary Elements", category="Dictionaries", difficulty="Beginner",
  description="Reads values with square brackets and the safe get() method.",
  concepts=["key lookup", "get()", "KeyError"], filename="access_dictionary_elements.py",
  code=r'''
book = {"title": "Python Basics", "author": "R. Kumar", "price": 450}

print("Title  :", book["title"])
print("Author :", book.get("author"))
print("Year   :", book.get("year"))                 # missing key -> None
print("Year   :", book.get("year", "not available")) # default value

try:
    print(book["year"])
except KeyError as error:
    print("KeyError: key not found ->", error)
''',
  algorithm=["Create a dictionary", "Access a value with dict[key]", "Access safely with get()", "Provide a default value to get()", "Catch KeyError for a missing key"],
  explanation="dict[key] returns the value for a key but raises KeyError if the key does not exist. The get() method returns None, or a default you supply, instead of raising an error. Use get() when a key may be missing.",
  tags=["dictionary", "access", "get", "keyerror"], topics=["Operations on Dictionaries"]),

P(title="Add Dictionary Elements", category="Dictionaries", difficulty="Beginner",
  description="Adds new key-value pairs using assignment, update() and setdefault().",
  concepts=["assignment", "update()", "setdefault()"], filename="add_dictionary_elements.py",
  code=r'''
phone = {"Asha": "98450"}
print("Start        :", phone)

phone["Ravi"] = "98765"                      # new key by assignment
print("Assignment   :", phone)

phone.update({"Meena": "91234", "Kiran": "99887"})
print("update()     :", phone)

phone.setdefault("Leela", "90000")           # adds only if key is missing
phone.setdefault("Asha", "00000")            # ignored, key exists
print("setdefault() :", phone)
''',
  algorithm=["Start with one pair", "Add a pair by assigning to a new key", "Add several pairs with update()", "Use setdefault() which never overwrites", "Print the dictionary after each step"],
  explanation="Assigning to a key that does not exist adds a new pair. update() adds many pairs at once from another dictionary. setdefault(key, value) adds the pair only when the key is missing and leaves existing values untouched.",
  tags=["dictionary", "add", "update", "setdefault"], topics=["Operations on Dictionaries"]),

P(title="Update Dictionary Elements", category="Dictionaries", difficulty="Beginner",
  description="Changes existing values by assignment, update() and arithmetic on values.",
  concepts=["assignment", "update()", "+="], filename="update_dictionary_elements.py",
  code=r'''
stock = {"pen": 50, "book": 20, "bag": 5}
print("Original :", stock)

stock["pen"] = 60                 # replace a value
print("pen = 60 :", stock)

stock["book"] += 10               # use the old value
print("book += 10:", stock)

stock.update({"bag": 8, "ruler": 15})   # update old key and add new key
print("update() :", stock)

for item in stock:                # update every value
    stock[item] = stock[item] * 2
print("Doubled  :", stock)
''',
  algorithm=["Create a stock dictionary", "Replace a value by assignment", "Increase a value with +=", "Use update() for old and new keys", "Loop over the keys and double each value"],
  explanation="Dictionaries are mutable. Assigning to an existing key replaces its value, and operators like += use the current value. update() replaces the values of existing keys and adds the keys that are new. Changing values while looping over keys is safe, but adding or deleting keys during the loop is not.",
  tags=["dictionary", "update", "modify"], topics=["Operations on Dictionaries"]),

P(title="Delete Dictionary Elements", category="Dictionaries", difficulty="Beginner",
  description="Removes pairs using del, pop(), popitem() and clear().",
  concepts=["del", "pop()", "popitem()", "clear()"], filename="delete_dictionary_elements.py",
  code=r'''
d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print("Start     :", d)

del d["a"]
print("del d['a']:", d)

value = d.pop("b")
print("pop('b')  :", value, d)

print("pop('z', 'none'):", d.pop("z", "none"))   # default avoids KeyError

last = d.popitem()               # removes the last inserted pair
print("popitem() :", last, d)

d.clear()
print("clear()   :", d)

try:
    del d["x"]
except KeyError as error:
    print("KeyError:", error)
''',
  algorithm=["Create a dictionary", "Delete a key with del", "Remove and get a value with pop()", "Use pop() with a default", "Remove the last pair with popitem()", "Empty with clear() and handle KeyError"],
  explanation="del removes a key, pop(key) removes it and returns its value, and popitem() removes the most recently added pair. clear() empties the dictionary. Deleting a missing key raises KeyError, but pop(key, default) avoids this.",
  tags=["dictionary", "delete", "pop", "del"], topics=["Operations on Dictionaries"]),

P(title="Demonstrate Dictionary Methods", category="Dictionaries", difficulty="Intermediate",
  description="Shows the commonly used dictionary methods: get, keys, values, items, copy, fromkeys and more.",
  concepts=["dict methods", "copy()", "fromkeys()"], filename="dictionary_methods.py",
  code=r'''
d = {"x": 1, "y": 2}
print("d             :", d)
print("get('x')      :", d.get("x"))
print("keys()        :", list(d.keys()))
print("values()      :", list(d.values()))
print("items()       :", list(d.items()))

d.update(z=3)
print("update(z=3)   :", d)
print("setdefault    :", d.setdefault("w", 0), d)
print("pop('w')      :", d.pop("w"))
print("popitem()     :", d.popitem())

backup = d.copy()
d.clear()
print("copy / clear  :", backup, d)

print("fromkeys      :", dict.fromkeys(["a", "b", "c"], 0))
print("len / in      :", len(backup), "x" in backup)
''',
  algorithm=["Create a dictionary", "Read data with get(), keys(), values() and items()", "Add data with update() and setdefault()", "Remove data with pop() and popitem()", "Use copy(), clear() and fromkeys()"],
  explanation="Dictionaries have methods for reading (get, keys, values, items), adding (update, setdefault), removing (pop, popitem, clear) and copying (copy, fromkeys). keys(), values() and items() return live view objects, so they are wrapped in list() to print. The copy() method makes a shallow copy.",
  tags=["dictionary", "methods", "fromkeys", "copy"], topics=["Dictionary Methods"]),

P(title="Display Dictionary Keys", category="Dictionaries", difficulty="Beginner",
  description="Displays the keys of a dictionary using keys() and by iterating directly.",
  concepts=["keys()", "view object", "sorted()"], filename="display_dictionary_keys.py",
  code=r'''
capitals = {"India": "New Delhi", "Japan": "Tokyo", "France": "Paris"}

print("keys() object :", capitals.keys())
print("As a list     :", list(capitals.keys()))
print("Number of keys:", len(capitals.keys()))

print("Looping over keys:")
for country in capitals:
    print("  ", country)

print("Sorted keys   :", sorted(capitals))
''',
  algorithm=["Create a dictionary of capitals", "Print the keys() view", "Convert to a list and count", "Loop directly over the dictionary", "Print the keys in sorted order"],
  explanation="keys() returns a view of all keys that updates automatically if the dictionary changes. Looping directly over a dictionary also gives its keys. sorted() on a dictionary returns its keys as a sorted list.",
  tags=["dictionary", "keys"], topics=["Dictionary Methods"]),

P(title="Display Dictionary Values", category="Dictionaries", difficulty="Beginner",
  description="Displays dictionary values with values() and calculates with them.",
  concepts=["values()", "sum()", "max()"], filename="display_dictionary_values.py",
  code=r'''
marks = {"Asha": 82, "Ravi": 67, "Meena": 91, "Kiran": 74}

print("values() object :", marks.values())
print("As a list       :", list(marks.values()))

for score in marks.values():
    print("  score:", score)

print("Total   :", sum(marks.values()))
print("Highest :", max(marks.values()))
print("Lowest  :", min(marks.values()))
print("Average :", sum(marks.values()) / len(marks))
''',
  algorithm=["Create a dictionary of marks", "Print the values() view", "Loop through the values", "Use sum(), max(), min() on the values", "Calculate the average"],
  explanation="values() returns a view of all values without their keys. It can be looped over or passed to functions such as sum(), max() and min(). Dividing the total by len() gives the average mark.",
  tags=["dictionary", "values", "sum"], topics=["Dictionary Methods"]),

P(title="Display Dictionary Items", category="Dictionaries", difficulty="Beginner",
  description="Displays key-value pairs using items() with tuple unpacking.",
  concepts=["items()", "unpacking", "formatting"], filename="display_dictionary_items.py",
  code=r'''
prices = {"apple": 120, "mango": 200, "banana": 60}

print("items() object:", prices.items())
print("As a list     :", list(prices.items()))

print(f"{'Fruit':10}{'Price':>8}")
for fruit, price in prices.items():
    print(f"{fruit:10}{price:>8}")

# items sorted by value
for fruit, price in sorted(prices.items(), key=lambda pair: pair[1]):
    print(fruit, "->", price)
''',
  algorithm=["Create a dictionary of prices", "Print the items() view", "Loop with two variables to unpack each pair", "Print a formatted table", "Sort the items by value"],
  explanation="items() gives every key-value pair as a tuple. In a for loop the tuple is unpacked into two names, which is the usual way to process a dictionary. sorted() with a key function sorts the pairs by price instead of by name.",
  tags=["dictionary", "items", "table"], topics=["Dictionary Methods"]),

P(title="Check Dictionary Membership", category="Dictionaries", difficulty="Beginner",
  description="Checks whether a key or a value exists in a dictionary, using user input.",
  concepts=["in", "not in", "values()"], filename="dictionary_membership.py", kind="Interactive",
  code=r'''
capitals = {"India": "New Delhi", "Japan": "Tokyo", "France": "Paris"}

country = input("Enter a country: ").strip().title()
if country in capitals:
    print(f"Key found: capital of {country} is {capitals[country]}")
else:
    print(f"{country} is not a key in the dictionary.")

city = input("Enter a city: ").strip().title()
if city in capitals.values():
    print(f"{city} is a value in the dictionary.")
else:
    print(f"{city} is not a value in the dictionary.")

print("'Spain' not in capitals ->", "Spain" not in capitals)
''',
  sample_input="japan\nParis",
  algorithm=["Create a dictionary of capitals", "Read a country and test it with in", "Print its capital if found", "Read a city and test it against values()", "Show not in"],
  explanation="The in operator on a dictionary checks the keys, which is very fast. To search among values, use in with values(). The program cleans each input using strip() and title() before testing.",
  tags=["dictionary", "membership", "in"], topics=["Operations on Dictionaries"]),

P(title="Iterate Through a Dictionary", category="Dictionaries", difficulty="Beginner",
  description="Shows several ways to loop over a dictionary: keys, values, items and enumerate.",
  concepts=["for loop", "items()", "enumerate()"], filename="iterate_dictionary.py",
  code=r'''
ages = {"Asha": 21, "Ravi": 23, "Meena": 22}

print("1. Keys only:")
for name in ages:
    print("  ", name)

print("2. Values only:")
for age in ages.values():
    print("  ", age)

print("3. Keys and values:")
for name, age in ages.items():
    print(f"   {name} is {age}")

print("4. With a counter:")
for number, (name, age) in enumerate(ages.items(), start=1):
    print(f"   {number}. {name} - {age}")

print("5. Comprehension:", {name: age + 1 for name, age in ages.items()})
''',
  algorithm=["Create a dictionary", "Loop over keys", "Loop over values", "Loop over items with unpacking", "Add a counter with enumerate()", "Build a new dictionary with a comprehension"],
  explanation="A plain for loop gives the keys; values() gives the values and items() gives both together. enumerate() can number the pairs. A dictionary comprehension loops over items() to create a new dictionary with changed values.",
  tags=["dictionary", "iterate", "loop"], topics=["Operations on Dictionaries"]),

P(title="Merge Dictionaries", category="Dictionaries", difficulty="Intermediate",
  description="Merges dictionaries using update(), unpacking and the | operator.",
  concepts=["update()", "** unpacking", "| operator"], filename="merge_dictionaries.py",
  code=r'''
d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 30}

merged = {**d1, **d2}            # unpacking, later values win
print("{**d1, **d2} :", merged)

merged2 = d1 | d2                # Python 3.9+
print("d1 | d2      :", merged2)

d3 = d1.copy()
d3.update(d2)                    # changes d3 itself
print("update()     :", d3)

d1 |= {"z": 26}                  # in-place merge
print("d1 |= ...    :", d1)

# Merge and add values of common keys
total = dict(d2)
for key, value in {"b": 5, "c": 5, "d": 5}.items():
    total[key] = total.get(key, 0) + value
print("Added values :", total)
''',
  algorithm=["Create two dictionaries with a common key", "Merge with {**d1, **d2}", "Merge with the | operator", "Merge in place with update()", "Merge while adding values of common keys"],
  explanation="When dictionaries are merged, a repeated key keeps the value from the right-hand (later) dictionary. Python offers {**a, **b}, a | b (Python 3.9+), and update() which changes the dictionary in place. To combine values instead of replacing them, loop and add with get(key, 0).",
  tags=["dictionary", "merge", "update", "union"], topics=["Operations on Dictionaries"]),

P(title="Demonstrate Nested Dictionaries", category="Dictionaries", difficulty="Intermediate",
  description="Builds a dictionary of dictionaries and reads, adds and loops through inner data.",
  concepts=["nested dict", "multiple keys", "loop"], filename="nested_dictionaries.py",
  code=r'''
students = {
    101: {"name": "Asha", "age": 21, "marks": {"python": 88, "maths": 76}},
    102: {"name": "Ravi", "age": 22, "marks": {"python": 69, "maths": 81}},
}

print("Student 101      :", students[101])
print("Name of 102      :", students[102]["name"])
print("Python mark 101  :", students[101]["marks"]["python"])

students[103] = {"name": "Meena", "age": 20, "marks": {"python": 95, "maths": 90}}
students[101]["marks"]["python"] = 90          # update inner value

for roll, info in students.items():
    total = sum(info["marks"].values())
    print(f"{roll} {info['name']:6} total = {total}")

print("Safe lookup:", students.get(999, {}).get("name", "no such student"))
''',
  algorithm=["Create a dictionary whose values are dictionaries", "Access inner values with several keys", "Add a new inner dictionary", "Update an inner value", "Loop through and total the inner marks", "Use get() for a safe lookup"],
  explanation="In a nested dictionary the value of a key is another dictionary, which is how records like students are modelled. Several keys in a row, such as students[101]['marks']['python'], go level by level. Looping with items() gives each inner dictionary, and chained get() calls avoid KeyError.",
  tags=["dictionary", "nested", "records"], topics=["Operations on Dictionaries"]),

P(title="Pass a Dictionary to a Function", category="Dictionaries", difficulty="Intermediate",
  description="Passes a dictionary to functions that read it, modify it and receive it with ** unpacking.",
  concepts=["function argument", "mutability", "**kwargs"], filename="pass_dictionary_to_function.py",
  code=r'''
def show_student(info):
    """Reads a dictionary."""
    for key, value in info.items():
        print(f"  {key:8}: {value}")


def add_grade(info):
    """Modifies the caller's dictionary because dictionaries are mutable."""
    info["grade"] = "A" if info["marks"] >= 75 else "B"


def describe(**details):
    """Receives keyword arguments as a dictionary."""
    return ", ".join(f"{k}={v}" for k, v in details.items())


student = {"name": "Asha", "marks": 82}
print("Before:")
show_student(student)

add_grade(student)
print("After add_grade():")
show_student(student)

print("Unpacking with **:", describe(**student))
''',
  algorithm=["Define a function that prints a dictionary", "Define a function that changes the dictionary", "Define a function with **details", "Pass the dictionary and call the functions", "Show the change is visible to the caller"],
  explanation="A dictionary is passed to a function by object reference, so changes made inside the function are visible outside. show_student() only reads the data while add_grade() adds a new key. Using ** when calling unpacks the dictionary into keyword arguments, which describe() collects again into a dictionary.",
  tags=["dictionary", "function", "kwargs", "mutable"], topics=["Passing Dictionaries to Functions"]),

P(title="Demonstrate Ordered Dictionaries", category="Dictionaries", difficulty="Intermediate",
  description="Uses collections.OrderedDict to keep and rearrange insertion order.",
  concepts=["OrderedDict", "move_to_end()", "popitem()"], filename="ordered_dictionary.py",
  code=r'''
from collections import OrderedDict

queue = OrderedDict()
queue["first"] = 1
queue["second"] = 2
queue["third"] = 3
print("OrderedDict   :", list(queue.items()))

queue.move_to_end("first")                 # move a key to the end
print("move_to_end   :", list(queue.keys()))

queue.move_to_end("third", last=False)     # move a key to the front
print("to the front  :", list(queue.keys()))

print("popitem(last=False):", queue.popitem(last=False))
print("popitem()          :", queue.popitem())

# Equality: OrderedDict cares about order, normal dict does not
a = OrderedDict([("x", 1), ("y", 2)])
b = OrderedDict([("y", 2), ("x", 1)])
print("OrderedDict equal:", a == b)
print("dict equal       :", dict(a) == dict(b))

# Normal dict also keeps insertion order since Python 3.7
plain = {"b": 2, "a": 1}
print("Plain dict order :", list(plain))
''',
  algorithm=["Import OrderedDict from collections", "Insert keys and print their order", "Move keys to the end and to the front", "Pop from both ends with popitem()", "Compare equality with a normal dict"],
  explanation="OrderedDict remembers the order in which keys were inserted. Since Python 3.7 a normal dict does this too, but OrderedDict adds move_to_end() and popitem(last=False) and treats two dictionaries with different order as unequal. It is handy for queues and caches such as LRU caches.",
  tags=["ordereddict", "collections", "dictionary", "order"], topics=["Ordered Dictionaries"]),

P(title="Create a Student Marks Dictionary", category="Dictionaries", difficulty="Intermediate",
  description="Reads names and marks of students into a dictionary and prints a result summary.",
  concepts=["dictionary", "input", "validation"], filename="student_marks_dictionary.py", kind="Interactive",
  code=r'''
marks = {}

try:
    count = int(input("How many students? "))
except ValueError:
    print("Invalid number.")
    count = 0

for _ in range(count):
    name = input("Student name: ").strip()
    try:
        score = float(input(f"Marks of {name}: "))
        if not 0 <= score <= 100:
            raise ValueError
    except ValueError:
        print("Invalid marks, student skipped.")
        continue
    marks[name] = score

if marks:
    print("\nName        Marks  Result")
    for name, score in marks.items():
        result = "Pass" if score >= 40 else "Fail"
        print(f"{name:10} {score:6.1f}  {result}")

    topper = max(marks, key=marks.get)
    print(f"\nTopper  : {topper} ({marks[topper]})")
    print(f"Average : {sum(marks.values()) / len(marks):.2f}")
else:
    print("No data entered.")
''',
  sample_input="4\nAsha\n82\nRavi\n35\nMeena\n91\nKiran\nabc",
  algorithm=["Read the number of students", "For each student read name and marks", "Validate marks between 0 and 100", "Store name: marks in the dictionary", "Print a table with Pass/Fail", "Find the topper with max(key=) and the average"],
  explanation="The dictionary maps each student's name to the marks. Marks are validated with try/except and invalid entries are skipped. max(marks, key=marks.get) finds the name with the largest value. The table is printed with formatted strings and the average is the sum of values divided by the count.",
  tags=["dictionary", "marks", "student", "input"], topics=["Operations on Dictionaries"]),

P(title="Student Record Management Program", category="Dictionaries", difficulty="Advanced",
  description="A menu-driven mini application to add, view, search, update and delete student records stored in a dictionary.",
  concepts=["dictionary", "menu", "functions", "while loop"], filename="student_record_management.py", kind="Application",
  code=r'''
records = {}          # roll number -> {"name": ..., "marks": ...}


def add_student():
    try:
        roll = int(input("Roll number: "))
        if roll in records:
            print("Roll number already exists.")
            return
        name = input("Name: ").strip()
        marks = float(input("Marks: "))
    except ValueError:
        print("Invalid input.")
        return
    records[roll] = {"name": name, "marks": marks}
    print("Student added.")


def view_students():
    if not records:
        print("No records.")
        return
    print(f"{'Roll':6}{'Name':12}{'Marks':>7}")
    for roll, info in sorted(records.items()):
        print(f"{roll:<6}{info['name']:12}{info['marks']:>7.1f}")


def search_student():
    try:
        roll = int(input("Roll number to search: "))
    except ValueError:
        print("Invalid input.")
        return
    info = records.get(roll)
    print(f"Found: {info['name']}, marks {info['marks']}" if info else "Not found.")


def update_student():
    try:
        roll = int(input("Roll number to update: "))
        if roll not in records:
            print("Not found.")
            return
        records[roll]["marks"] = float(input("New marks: "))
    except ValueError:
        print("Invalid input.")
        return
    print("Record updated.")


def delete_student():
    try:
        roll = int(input("Roll number to delete: "))
    except ValueError:
        print("Invalid input.")
        return
    if records.pop(roll, None) is None:
        print("Not found.")
    else:
        print("Record deleted.")


actions = {"1": add_student, "2": view_students, "3": search_student,
           "4": update_student, "5": delete_student}

while True:
    print("\n--- Student Records ---")
    print("1.Add  2.View  3.Search  4.Update  5.Delete  6.Exit")
    choice = input("Choice: ").strip()
    if choice == "6":
        print("Goodbye!")
        break
    action = actions.get(choice)
    if action:
        action()
    else:
        print("Invalid choice.")
''',
  sample_input="1\n101\nAsha\n82\n1\n102\nRavi\n67\n1\n101\nX\n2\n3\n102\n4\n102\n75\n2\n5\n101\n3\n101\n9\n6",
  algorithm=["Keep records in a dictionary keyed by roll number", "Show a menu inside a while True loop", "Look up the chosen function in a dictionary of actions", "Add, view, search, update or delete a record with validation", "Exit the loop when option 6 is chosen"],
  explanation="The program is a small CRUD application. Each student is an inner dictionary stored under the roll number, which makes searching, updating and deleting quick. A dictionary maps menu choices to functions, so no long if-elif chain is needed. All numeric input is validated with try/except and the loop ends with break when the user chooses Exit.",
  tags=["dictionary", "menu", "crud", "student", "application"], topics=["Operations on Dictionaries"]),

P(title="Count Word Frequency Using Dictionaries", category="Dictionaries", difficulty="Intermediate",
  description="Counts how many times each word occurs in a sentence using a dictionary.",
  concepts=["dictionary", "get()", "split()", "sorting"], filename="word_frequency.py", kind="Interactive",
  code=r'''
import string

text = input("Enter a sentence: ")

# Clean the text: lower case and remove punctuation
cleaned = text.lower().translate(str.maketrans("", "", string.punctuation))
words = cleaned.split()

frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("\nWord counts:")
for word, count in sorted(frequency.items(), key=lambda pair: (-pair[1], pair[0])):
    print(f"  {word:10} {count} {'*' * count}")

print("Total words :", len(words))
print("Unique words:", len(frequency))
''',
  sample_input="The cat and the dog and the bird. The end!",
  algorithm=["Read a sentence", "Convert to lower case and remove punctuation", "Split into words", "For each word add 1 to its count using get(word, 0)", "Print the counts sorted by frequency", "Print total and unique words"],
  explanation="A dictionary is ideal for counting: the word is the key and its count is the value. frequency.get(word, 0) + 1 starts a new word at 1 and increases existing ones. Punctuation is removed with translate() so 'end!' and 'end' are the same word. The results are sorted by highest count first, then alphabetically.",
  tags=["dictionary", "word count", "frequency", "string"], topics=["Operations on Dictionaries"]),

P(title="Define a Function", category="Functions", difficulty="Beginner",
  description="Defines functions with def, a docstring, parameters and a return statement.",
  concepts=["def", "docstring", "parameters"], filename="define_function.py",
  code=r'''
def greet():
    """Prints a fixed greeting (no parameters, no return value)."""
    print("Hello from a function!")


def greet_person(name):
    """Prints a greeting for the given name."""
    print(f"Hello, {name}!")


def square(number):
    """Returns the square of a number."""
    return number * number


print("Functions are objects:", type(greet))
print("Docstring of square  :", square.__doc__)
print("Name of the function :", square.__name__)
greet()
greet_person("Asha")
print("square(7) =", square(7))
''',
  algorithm=["Write def, the function name, parentheses and a colon", "Indent the body of the function", "Add a docstring describing the function", "Define functions with no, one and a returned value", "Call each function to see that defining alone does nothing"],
  explanation="A function is a named block of code created with the def keyword. The names inside the parentheses are parameters, and the first string in the body is the docstring that documents it. Defining a function does not run it; the body runs only when the function is called. return sends a value back to the caller.",
  tags=["function", "def", "docstring"], topics=["Defining a Function"]),

P(title="Call a Function", category="Functions", difficulty="Beginner",
  description="Calls functions from the main program, from other functions and inside expressions.",
  concepts=["function call", "arguments", "nested calls"], filename="call_function.py",
  code=r'''
def add(a, b):
    return a + b


def show_total(x, y):
    print(f"Total of {x} and {y} is {add(x, y)}")     # function calling a function


result = add(10, 20)                    # store the returned value
print("result            :", result)
print("used in expression:", add(1, 2) * add(3, 4))
print("nested call       :", add(add(1, 2), add(3, 4)))
show_total(5, 6)

operation = add                         # a function name can be stored
print("through a variable:", operation(100, 200))

# Calling before defining fails
try:
    later(1)
except NameError as error:
    print("Error:", error)


def later(n):
    return n
''',
  algorithm=["Define add(a, b)", "Call it and store the result", "Use calls inside expressions and nested calls", "Call a function from another function", "Call through another variable name", "Show NameError when calling before definition"],
  explanation="A function is called by writing its name followed by parentheses containing the arguments. The call can be used anywhere a value is needed, even as an argument to another call. A function must be defined before the line that calls it runs, otherwise Python raises NameError. Functions are objects, so the name can be assigned to another variable.",
  tags=["function", "call", "arguments"], topics=["Calling a Function"]),

P(title="Demonstrate Function Parameters", category="Functions", difficulty="Beginner",
  description="Explains parameters versus arguments with a rectangle area function and a parameter-less function.",
  concepts=["parameters", "arguments", "TypeError"], filename="function_parameters.py",
  code=r'''
def rectangle_area(length, width):      # length and width are PARAMETERS
    return length * width


def hello():                            # no parameters
    return "hello"


print("Area:", rectangle_area(5, 3))    # 5 and 3 are ARGUMENTS
print("hello():", hello())

# Wrong number of arguments
for call in ("rectangle_area(5)", "rectangle_area(1, 2, 3)", "hello(1)"):
    try:
        eval(call)
    except TypeError as error:
        print(f"{call:25} -> TypeError: {error}")
''',
  algorithm=["Define a function with two parameters", "Call it with two arguments", "Define a function with no parameters", "Call functions with the wrong number of arguments", "Catch and print each TypeError"],
  explanation="Parameters are the names in the function definition and arguments are the actual values given in the call. The number of arguments must match the parameters unless defaults or variable-length parameters are used. A mismatch raises TypeError, which the program catches to show the message.",
  tags=["function", "parameters", "arguments"], topics=["Defining a Function"]),

P(title="Demonstrate Positional Arguments", category="Functions", difficulty="Beginner",
  description="Shows that positional arguments are matched to parameters by their order.",
  concepts=["positional arguments", "order"], filename="positional_arguments.py",
  code=r'''
def introduce(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")


introduce("Asha", 21, "Pune")          # correct order
introduce(21, "Asha", "Pune")          # wrong order -> wrong meaning

def divide(a, b):
    return a / b

print("divide(10, 2) =", divide(10, 2))
print("divide(2, 10) =", divide(2, 10))
''',
  algorithm=["Define a function with three parameters", "Call it with arguments in the correct order", "Call it again with the order mixed up", "Show that order changes the result in divide()"],
  explanation="Positional arguments are matched to parameters from left to right, so the order of values is important. Giving the values in the wrong order does not raise an error but gives wrong output, as the second introduce() call shows. divide(10, 2) and divide(2, 10) give different results for the same reason.",
  tags=["function", "positional", "arguments", "order"], topics=["Calling a Function"]),

P(title="Demonstrate Keyword Arguments", category="Functions", difficulty="Beginner",
  description="Passes arguments by parameter name so that order does not matter.",
  concepts=["keyword arguments", "name=value"], filename="keyword_arguments.py",
  code=r'''
def create_profile(name, age, city):
    return f"{name}, {age}, {city}"


print(create_profile("Asha", 21, "Pune"))                 # positional
print(create_profile(city="Pune", name="Asha", age=21))   # keywords, any order
print(create_profile("Asha", city="Delhi", age=22))       # mixed

try:
    create_profile(age=21, name="Asha", country="India")
except TypeError as error:
    print("Error:", error)

# create_profile(name="Asha", "Pune", 21)  # SyntaxError: positional argument follows keyword argument
print("A positional argument cannot follow a keyword argument (SyntaxError).")
''',
  algorithm=["Define create_profile(name, age, city)", "Call it using name=value in a different order", "Mix positional and keyword arguments", "Use a wrong keyword and catch TypeError", "Note that positional arguments cannot follow keyword ones"],
  explanation="With keyword arguments each value is given as parameter=value, so the order of arguments no longer matters and the call is easier to read. Positional arguments can be mixed with keyword ones but must come first. An unknown parameter name raises TypeError.",
  tags=["function", "keyword", "arguments"], topics=["Calling a Function"]),

P(title="Demonstrate Default Arguments", category="Functions", difficulty="Beginner",
  description="Gives parameters default values and shows the mutable-default trap.",
  concepts=["default arguments", "optional parameters", "None"], filename="default_arguments.py",
  code=r'''
def power(base, exponent=2):
    return base ** exponent


def greet(name, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"


print("power(5)    =", power(5))
print("power(2, 10) =", power(2, 10))
print(greet("Asha"))
print(greet("Ravi", "Welcome"))
print(greet("Meena", punctuation="."))


# Trap: a default list is created ONCE and shared between calls
def bad_append(item, bucket=[]):
    bucket.append(item)
    return bucket


def good_append(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


print("bad :", bad_append(1), bad_append(2))
print("good:", good_append(1), good_append(2))

# Python has no Java-style overloading; default arguments give a similar effect
''',
  algorithm=["Define power() with a default exponent", "Call it with and without the second argument", "Define greet() with several defaults", "Show the shared mutable default list problem", "Fix it using None as the default"],
  explanation="A default value is written as parameter=value; it is used when the caller leaves out that argument. Parameters with defaults must come after those without. Never use a mutable object such as a list as a default, because it is created once and shared by every call; use None and create the list inside the function. Default arguments are the Python way to get what overloading gives in other languages.",
  tags=["function", "default", "arguments", "optional"], topics=["Defining a Function"]),

P(title="Demonstrate Variable-Length Arguments", category="Functions", difficulty="Intermediate",
  description="Uses *args and **kwargs to accept any number of positional and keyword arguments.",
  concepts=["*args", "**kwargs", "unpacking"], filename="variable_length_arguments.py",
  code=r'''
def total(*numbers):
    """*numbers collects all positional arguments into a tuple."""
    print("  received", numbers)
    return sum(numbers)


def show_details(**info):
    """**info collects keyword arguments into a dictionary."""
    for key, value in info.items():
        print(f"  {key} = {value}")


def everything(first, *args, **kwargs):
    print("  first :", first)
    print("  args  :", args)
    print("  kwargs:", kwargs)


print("total() =", total())
print("total(1, 2, 3) =", total(1, 2, 3))
print("total(10, 20, 30, 40, 50) =", total(10, 20, 30, 40, 50))

show_details(name="Asha", course="MCA", year=1)
everything("A", 1, 2, x=10, y=20)

values = [4, 5, 6]
print("Unpack a list with *:", total(*values))
''',
  algorithm=["Define total(*numbers) to accept any count of values", "Call it with zero, three and five arguments", "Define show_details(**info) for keyword arguments", "Combine normal, *args and **kwargs parameters", "Unpack a list into arguments using *"],
  explanation="A parameter written with one star collects extra positional arguments into a tuple, and one with two stars collects extra keyword arguments into a dictionary. This lets a function accept any number of arguments, another substitute for overloading. A star in the call, as in total(*values), does the reverse and spreads a list into separate arguments.",
  tags=["function", "args", "kwargs", "variable length"], topics=["Defining a Function"]),

P(title="Return a Value from a Function", category="Functions", difficulty="Beginner",
  description="Returns results from functions and shows what a function without return gives back.",
  concepts=["return", "None", "early return"], filename="return_value.py",
  code=r'''
def cube(n):
    return n ** 3


def is_even(n):
    return n % 2 == 0                   # returns a bool


def grade(marks):
    if marks >= 75:
        return "A"                      # early return
    if marks >= 50:
        return "B"
    return "C"


def only_print(n):
    print("Printing", n)                # no return statement


print("cube(4)    =", cube(4))
print("is_even(7) =", is_even(7))
print("grade(82)  =", grade(82), " grade(60) =", grade(60), " grade(20) =", grade(20))

result = only_print(5)
print("A function without return gives:", result)

volume = cube(3) + cube(2)              # returned values can be reused
print("cube(3) + cube(2) =", volume)
''',
  algorithm=["Define functions that return a number, a bool and a string", "Use several return statements with conditions", "Define a function that only prints", "Capture its result and show it is None", "Use returned values in an expression"],
  explanation="return ends the function immediately and sends a value back to the place of the call, where it can be stored or used in an expression. A function can have several return statements, for example one per condition. If a function has no return statement it returns None, which is different from printing a value.",
  tags=["function", "return", "none"], topics=["Returning Results from a Function"]),

P(title="Return Multiple Values", category="Functions", difficulty="Beginner",
  description="Returns several values at once as a tuple and unpacks them.",
  concepts=["return tuple", "unpacking", "named tuple"], filename="return_multiple_values.py",
  code=r'''
from collections import namedtuple


def min_max_avg(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)


def divide(a, b):
    return a // b, a % b


Stats = namedtuple("Stats", ["low", "high", "mean"])


def stats(numbers):
    return Stats(min(numbers), max(numbers), sum(numbers) / len(numbers))


data = [12, 45, 7, 33, 21]

result = min_max_avg(data)
print("As a tuple :", result, type(result).__name__)

low, high, mean = min_max_avg(data)          # unpacking
print(f"low={low} high={high} mean={mean}")

quotient, remainder = divide(47, 5)
print(f"47 / 5 -> quotient {quotient}, remainder {remainder}")

s = stats(data)
print("Named tuple:", s, "-> highest is", s.high)
''',
  algorithm=["Return two or three values separated by commas", "Receive them as one tuple", "Unpack them into separate variables", "Return a dictionary-like namedtuple", "Access the fields by name"],
  explanation="Python functions can return several values by separating them with commas; they are really packed into one tuple. The caller either keeps the tuple or unpacks it into separate variables. A namedtuple gives each returned value a name so the result is easier to read.",
  tags=["function", "return", "multiple", "tuple"], topics=["Returning Multiple Values from a Function"]),

P(title="Demonstrate Function versus Method", category="Functions", difficulty="Intermediate",
  description="Compares a standalone function with a method that belongs to an object.",
  concepts=["function", "method", "self", "class"], filename="function_vs_method.py",
  code=r'''
# A FUNCTION: defined on its own, called by name, data passed explicitly
def double(number):
    return number * 2


# A METHOD: defined inside a class, called on an object, receives self
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
        return self.value


print("Function call  : double(5) ->", double(5))

counter = Counter()
print("Method call    : counter.increment() ->", counter.increment())
print("Method call    : counter.increment() ->", counter.increment())

# Built-in examples
text = "python"
print("Function len(text)  ->", len(text))
print("Method text.upper() ->", text.upper())

print(type(double).__name__, "|", type(counter.increment).__name__)
print("The object bound to the method:", counter.increment.__self__ is counter)
print("Same method called through the class:", Counter.increment(counter))
''',
  algorithm=["Define a normal function double()", "Define a class with a method increment(self)", "Call the function by name", "Call the method through an object", "Compare built-in len() with str.upper()", "Show that a method is bound to its object"],
  explanation="A function is an independent block of code called by its name with all the data passed as arguments. A method is a function defined inside a class and called on an object using dot notation; Python automatically passes the object as the first parameter, self. len(text) is a function while text.upper() is a method. type() reports 'function' for one and 'method' for the bound version.",
  tags=["function", "method", "class", "self"], topics=["Difference between a Function and a Method"]),

P(title="Demonstrate Local Variables", category="Functions", difficulty="Beginner",
  description="Shows that variables created inside a function exist only while it runs.",
  concepts=["local scope", "NameError", "shadowing"], filename="local_variables.py",
  code=r'''
def calculate():
    local_total = 100            # local variable
    print("Inside function  :", local_total)


def shadow():
    message = "local message"    # a different variable from the global one
    print("Inside shadow()  :", message)


message = "global message"
calculate()
shadow()
print("Outside shadow() :", message)

try:
    print(local_total)
except NameError as error:
    print("Outside function  : NameError ->", error)


def counter():
    count = 0                    # re-created on every call
    count += 1
    return count


print("counter() calls  :", counter(), counter(), counter())
''',
  algorithm=["Create a variable inside a function", "Print it inside the function", "Try to print it outside and catch NameError", "Create a local variable with the same name as a global", "Show that local variables restart on every call"],
  explanation="A variable assigned inside a function is local: it exists only during that call and cannot be used outside. A local variable with the same name as a global one hides it without changing it. Every call gets a fresh set of local variables, so counter() always returns 1.",
  tags=["function", "local", "scope", "variables"], topics=["Defining a Function"]),

P(title="Demonstrate Global Variables", category="Functions", difficulty="Intermediate",
  description="Reads and modifies global variables inside functions using the global keyword.",
  concepts=["global", "scope", "UnboundLocalError"], filename="global_variables.py",
  code=r'''
counter = 0                      # global variable
site = "MCA Lab"


def show():
    print("Reading global inside function:", site, counter)   # reading is fine


def wrong_increment():
    try:
        counter += 1             # assignment makes counter local -> error
    except UnboundLocalError as error:
        print("Error:", error)


def increment():
    global counter               # now assignment changes the global
    counter += 1


show()
wrong_increment()
for _ in range(3):
    increment()
print("After 3 increments, counter =", counter)

# Better design: pass in and return values instead of using global
def increment_value(value):
    return value + 1

counter = increment_value(counter)
print("Using return value, counter =", counter)
''',
  algorithm=["Create global variables outside any function", "Read a global inside a function", "Try to change it without global and catch the error", "Use the global keyword to change it", "Show a cleaner alternative using parameters and return"],
  explanation="Variables created outside functions are global and can be read anywhere. If a function assigns to a name, Python treats it as local unless it is declared with the global keyword. Without it the code raises UnboundLocalError. Global variables make programs harder to follow, so passing values in and returning results is usually better.",
  tags=["function", "global", "scope"], topics=["Defining a Function"]),

P(title="Demonstrate Pass by Object Reference", category="Functions", difficulty="Intermediate",
  description="Shows that Python passes references to objects, using id() to prove it.",
  concepts=["id()", "object reference", "rebinding"], filename="pass_by_object_reference.py",
  code=r'''
def show_id(value):
    print("  inside  id:", id(value))


x = 42
print("outside id:", id(x))
show_id(x)
print("Same object passed:", True)

def rebind(value):
    print("  before rebind id:", id(value))
    value = value + 1                    # creates a new object (int is immutable)
    print("  after rebind  id:", id(value), "value =", value)


def mutate(items):
    print("  list id inside  :", id(items))
    items.append(99)                     # changes the same object


n = 10
rebind(n)
print("n after rebind():", n)

numbers = [1, 2, 3]
print("list id outside :", id(numbers))
mutate(numbers)
print("numbers after mutate():", numbers)

print("Summary: the function gets a reference to the SAME object.")
print("Changing a mutable object is visible outside; rebinding the name is not.")
''',
  algorithm=["Print id() of an object outside and inside a function", "Rebind the parameter and show the caller's variable is unchanged", "Pass a list and modify it inside the function", "Show the list changed for the caller", "Summarise: object reference, not copy and not C-style pointer"],
  explanation="Python passes arguments by object reference: the parameter becomes another name for the same object the caller passed. The id() values prove it is the same object. If the function changes a mutable object such as a list, the caller sees the change. If it rebinds the name to a new object, as in value = value + 1, the caller's variable is untouched.",
  tags=["function", "pass by reference", "id", "object"], topics=["Pass by Object Reference"]),

P(title="Demonstrate Mutable Objects in Functions", category="Functions", difficulty="Intermediate",
  description="Shows how functions can change lists, dictionaries and sets, and how to avoid it with a copy.",
  concepts=["mutable", "list", "dict", "copy()"], filename="mutable_objects_in_functions.py",
  code=r'''
def add_item(items):
    items.append("new")


def update_info(info):
    info["status"] = "updated"


def add_safely(items):
    copy_of_items = items.copy()         # work on a copy
    copy_of_items.append("new")
    return copy_of_items


fruits = ["apple", "banana"]
add_item(fruits)
print("List after add_item()   :", fruits)

student = {"name": "Asha"}
update_info(student)
print("Dict after update_info():", student)

original = ["a", "b"]
new_list = add_safely(original)
print("original :", original)
print("new_list :", new_list)

# Reassigning inside the function does NOT affect the caller
def reassign(items):
    items = ["completely", "different"]

reassign(fruits)
print("After reassign()        :", fruits)
''',
  algorithm=["Pass a list to a function that appends to it", "Pass a dictionary to a function that updates it", "Show both changes are visible to the caller", "Use copy() inside a function to protect the original", "Show that reassigning the parameter does not change the caller's list"],
  explanation="Lists, dictionaries and sets are mutable, so a function that changes its parameter changes the caller's object too. To keep the original safe, the function can work on a copy and return the new object. Assigning a brand-new list to the parameter only changes the local name.",
  tags=["function", "mutable", "list", "dictionary"], topics=["Pass by Object Reference"]),

P(title="Demonstrate Immutable Objects in Functions", category="Functions", difficulty="Intermediate",
  description="Shows that numbers, strings and tuples passed to functions cannot be changed in place.",
  concepts=["immutable", "int", "str", "tuple"], filename="immutable_objects_in_functions.py",
  code=r'''
def change_number(n):
    n += 10
    print("  inside, n    =", n)


def change_text(s):
    s = s + " World"
    print("  inside, s    =", s)


def change_tuple(t):
    try:
        t[0] = 99
    except TypeError as error:
        print("  inside, error:", error)
    t = t + (4,)                         # new tuple created
    print("  inside, t    =", t)


number = 5
change_number(number)
print("number after call:", number)

text = "Hello"
change_text(text)
print("text after call  :", text)

values = (1, 2, 3)
change_tuple(values)
print("tuple after call :", values)

# To get the changed value, return it
def add_ten(n):
    return n + 10

number = add_ten(number)
print("Using return     :", number)
''',
  algorithm=["Pass an integer, string and tuple to functions", "Try to change them inside the function", "Print the values after each call to show no change", "Show the TypeError for tuple item assignment", "Return the new value and assign it to get the change"],
  explanation="Integers, strings and tuples are immutable: operations like n += 10 create a new object and rebind the local name, leaving the caller's variable unchanged. Trying to assign to a tuple item raises TypeError. If a function must give back a changed immutable value it should return it and the caller should store the result.",
  tags=["function", "immutable", "string", "tuple"], topics=["Pass by Object Reference"]),

P(title="Demonstrate Recursive Functions", category="Functions", difficulty="Intermediate",
  description="Uses recursion with a base case for countdown, sum of digits and string reversal.",
  concepts=["recursion", "base case", "recursion limit"], filename="recursive_functions.py",
  code=r'''
import sys


def countdown(n):
    if n == 0:                       # base case
        print("Liftoff!")
        return
    print(n)
    countdown(n - 1)                 # recursive call


def digit_sum(n):
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)


def reverse_text(text):
    if len(text) <= 1:
        return text
    return reverse_text(text[1:]) + text[0]


def no_base_case(n):
    return no_base_case(n + 1)       # never stops


countdown(3)
print("digit_sum(4721)       =", digit_sum(4721))
print("reverse_text('python') =", reverse_text("python"))
print("Recursion limit        :", sys.getrecursionlimit())

try:
    no_base_case(1)
except RecursionError as error:
    print("RecursionError:", str(error)[:45])
''',
  algorithm=["Write a base case that stops the recursion", "Write a recursive case that calls the function with a smaller problem", "Implement countdown, digit sum and string reversal", "Show the recursion limit", "Demonstrate RecursionError when the base case is missing"],
  explanation="A recursive function calls itself on a smaller version of the problem until it reaches a base case that can be answered directly. countdown() prints and recurses on n - 1, digit_sum() adds the last digit to the sum of the rest and reverse_text() moves the first character to the end. Without a base case Python stops with RecursionError after about 1000 calls.",
  tags=["function", "recursion", "base case"], topics=["Calling a Function"]),

P(title="Calculate Factorial Using Recursion", category="Functions", difficulty="Beginner",
  description="Finds n! with a recursive function and compares it with a loop.",
  concepts=["recursion", "factorial", "validation"], filename="factorial_recursion.py", kind="Interactive",
  code=r'''
def factorial(n):
    """Returns n! using recursion."""
    if n == 0 or n == 1:             # base case
        return 1
    return n * factorial(n - 1)      # recursive case


def factorial_loop(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


try:
    number = int(input("Enter a non-negative integer: "))
    if number < 0:
        raise ValueError("factorial is not defined for negative numbers")
except ValueError as error:
    print("Invalid input:", error)
else:
    print(f"{number}! = {factorial(number)}")
    print("Loop check :", factorial_loop(number))
    steps = " x ".join(str(i) for i in range(number, 0, -1)) or "1"
    print("Expanded   :", steps)
''',
  sample_input="6",
  algorithm=["Read an integer and validate it", "If n is 0 or 1 return 1 (base case)", "Otherwise return n * factorial(n - 1)", "Print the result", "Verify using a loop"],
  explanation="The factorial of n is n times the factorial of n - 1, and the factorial of 0 or 1 is 1, which is the base case. Each call waits for the smaller call to finish, then multiplies the results on the way back. The input is validated so negative numbers and text are rejected. A loop version is included for comparison.",
  tags=["recursion", "factorial", "function"], topics=["Returning Results from a Function"]),

P(title="Calculate Fibonacci Using Recursion", category="Functions", difficulty="Intermediate",
  description="Finds Fibonacci numbers recursively and speeds the function up using caching.",
  concepts=["recursion", "Fibonacci", "lru_cache"], filename="fibonacci_recursion.py", kind="Interactive",
  code=r'''
from functools import lru_cache


def fib(n):
    """Plain recursion: simple but slow for large n."""
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


@lru_cache(maxsize=None)
def fib_fast(n):
    """Same logic, results remembered, so it is fast."""
    if n < 2:
        return n
    return fib_fast(n - 1) + fib_fast(n - 2)


try:
    terms = int(input("How many Fibonacci terms? "))
    if terms < 1:
        raise ValueError("enter a number greater than 0")
except ValueError as error:
    print("Invalid input:", error)
else:
    print("Series :", [fib(i) for i in range(terms)])
    print("Last term, plain recursion:", fib(terms - 1))
    print("fib_fast(80)              :", fib_fast(80))
''',
  sample_input="10",
  algorithm=["Read the number of terms and validate it", "Define fib(n) with base cases fib(0)=0 and fib(1)=1", "Return fib(n-1) + fib(n-2) otherwise", "Print the series using a list comprehension", "Use lru_cache to avoid repeated calculations"],
  explanation="Each Fibonacci number is the sum of the two before it, with 0 and 1 as the base cases. The simple recursive function repeats a lot of work, so it becomes very slow for big n. The lru_cache decorator remembers earlier results so fib_fast(80) returns instantly. The list comprehension calls fib() for every position to print the series.",
  tags=["recursion", "fibonacci", "cache"], topics=["Returning Results from a Function"]),

P(title="Create a Calculator Using Functions", category="Functions", difficulty="Intermediate",
  description="A menu-driven calculator where each operation is its own function.",
  concepts=["functions", "menu", "dictionary dispatch", "ZeroDivisionError"], filename="calculator_using_functions.py", kind="Interactive",
  code=r'''
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return a / b


def power(a, b):
    return a ** b


def read_number(prompt):
    return float(input(prompt))


operations = {"1": ("Add", add, "+"), "2": ("Subtract", subtract, "-"),
              "3": ("Multiply", multiply, "*"), "4": ("Divide", divide, "/"),
              "5": ("Power", power, "**")}

while True:
    print("\n1.Add 2.Subtract 3.Multiply 4.Divide 5.Power 6.Exit")
    choice = input("Choose: ").strip()
    if choice == "6":
        print("Calculator closed.")
        break
    if choice not in operations:
        print("Invalid choice.")
        continue
    name, function, symbol = operations[choice]
    try:
        x = read_number("First number : ")
        y = read_number("Second number: ")
        print(f"{x:g} {symbol} {y:g} = {function(x, y):g}")
    except ValueError:
        print("Please enter valid numbers.")
    except ZeroDivisionError as error:
        print("Error:", error)
''',
  sample_input="1\n12\n8\n4\n10\n0\n4\n10\n4\n3\n6\n7\n5\n2\n10\n1\nabc\n9\n6",
  algorithm=["Write one function for each operation", "Store the functions in a dictionary keyed by menu choice", "Show the menu in a loop", "Read two numbers with validation", "Call the chosen function and print the result", "Handle division by zero and exit on 6"],
  explanation="Every operation is a separate small function that takes two numbers and returns the answer. A dictionary maps the menu choice to the function, so the main loop only looks up and calls it. divide() raises ZeroDivisionError for a zero divisor, and invalid numbers raise ValueError; both are handled with try/except so the calculator keeps running.",
  tags=["function", "calculator", "menu", "dispatch"], topics=["Calling a Function"]),

P(title="Function-Based Student Management Program", category="Functions", difficulty="Advanced",
  description="A menu-driven student management mini application built entirely from functions that pass data and return results.",
  concepts=["functions", "return values", "list of dicts", "menu"], filename="function_student_management.py", kind="Application",
  code=r'''
def add_student(students, roll, name, marks):
    """Adds a student; returns True if added, False if roll already exists."""
    if find_student(students, roll) is not None:
        return False
    students.append({"roll": roll, "name": name, "marks": marks})
    return True


def find_student(students, roll):
    for student in students:
        if student["roll"] == roll:
            return student
    return None


def remove_student(students, roll):
    student = find_student(students, roll)
    if student is None:
        return False
    students.remove(student)
    return True


def get_grade(marks):
    if marks >= 75:
        return "A"
    if marks >= 60:
        return "B"
    if marks >= 40:
        return "C"
    return "F"


def statistics(students):
    """Returns (average, highest, lowest) or None for an empty list."""
    if not students:
        return None
    marks = [s["marks"] for s in students]
    return sum(marks) / len(marks), max(marks), min(marks)


def display(students):
    if not students:
        print("No students.")
        return
    print(f"{'Roll':<6}{'Name':<10}{'Marks':>6}  Grade")
    for s in sorted(students, key=lambda s: s["marks"], reverse=True):
        print(f"{s['roll']:<6}{s['name']:<10}{s['marks']:>6.1f}  {get_grade(s['marks'])}")


def read_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        return None


def main():
    students = []
    while True:
        print("\n1.Add 2.Display 3.Search 4.Remove 5.Statistics 6.Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            roll = read_int("Roll: ")
            name = input("Name: ").strip()
            marks = read_int("Marks: ")
            if roll is None or marks is None or not 0 <= marks <= 100:
                print("Invalid data.")
            elif add_student(students, roll, name, marks):
                print("Added.")
            else:
                print("Roll already exists.")
        elif choice == "2":
            display(students)
        elif choice == "3":
            found = find_student(students, read_int("Roll: "))
            print(found if found else "Not found.")
        elif choice == "4":
            print("Removed." if remove_student(students, read_int("Roll: ")) else "Not found.")
        elif choice == "5":
            result = statistics(students)
            if result:
                average, highest, lowest = result       # multiple return values
                print(f"Average {average:.2f}, Highest {highest}, Lowest {lowest}")
            else:
                print("No data.")
        elif choice == "6":
            print("Bye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
''',
  sample_input="5\n1\n1\nAsha\n82\n1\n2\nRavi\n58\n1\n3\nMeena\n91\n1\n2\nKiran\n40\n2\n3\n2\n3\n9\n4\n2\n4\n7\n5\n2\n6",
  algorithm=["Store students as a list of dictionaries", "Write separate functions to add, find, remove, grade, summarise and display", "Return values (True/False, a record, a tuple) instead of printing inside logic functions", "main() shows the menu in a while loop", "Validate numeric input with read_int()", "Exit when option 6 is chosen"],
  explanation="Each task is a separate function that receives the list of students as an argument and returns a result, so the logic is easy to test and reuse. find_student() returns the record or None, add_student() returns True or False, and statistics() returns three values as a tuple. main() only handles the menu and calls these functions. The list is modified in place because it is a mutable object passed by reference.",
  tags=["function", "student", "management", "menu", "application"], topics=["Returning Multiple Values from a Function"]),
]
