import topics from '../../content/syllabus_topics.json';
export const COURSE = { semester: 'MCA 1 SEMESTER', code: 'MCA 102 A', name: 'Programming in Python' };
export const UNITS = [
  { n: 1, title: 'Introduction to Python', short: 'Introduction', folder: 'Unit_1_Introduction_to_Python',
    desc: 'Python fundamentals, how Python runs (PVM), memory management, garbage collection, and setting up Python and pandas on Windows.',
    syllabus: [{ text: 'Introduction to Python, Python Fundamentals, Components of a Python Program, Features of Python, Python Virtual Machine (PVM), Memory Management in Python, Garbage Collection in Python, Installing Python for Windows, Verifying the Path to Python, Installing pandas, Verifying Installed Packages.' }] },
  { n: 2, title: 'Data Types and Operators', short: 'Data Types', folder: 'Unit_2_Data_Types_and_Operators',
    desc: 'Data types, sequences, sets, literals, constants, strings, identifiers and the complete family of Python operators.',
    syllabus: [{ head: 'Data types and Operators.', text: 'Comments in Python, Data types in Python, Sequences in Python, Sets, Literals, Constants, Strings and Characters, User-defined Data types, Identifiers and Reserved words.' },
      { head: 'Operators:', text: 'Arithmetic Operators, Assignment Operators, Unary Minus Operator, Relational Operators, Logical Operators, Boolean Operators, Bitwise Operators, Membership Operators, Identity Operators.' }] },
  { n: 3, title: 'Control Statements and Arrays', short: 'Control & Arrays', folder: 'Unit_3_Control_Statements_and_Arrays',
    desc: 'Input/output, command-line arguments, decision making, loops and arrays using the array module and NumPy.',
    syllabus: [{ head: 'Control Statements and Arrays.', text: 'Input Statements, Output statements, Command Line Arguments.' },
      { head: 'Control Statements:', text: 'if Statement, if … else Statement, if … elif … else Statement, The while Loop, The for Loop, Infinite Loops, Nested Loops, The else Suite, The break Statement, The continue Statement, The pass Statement, The return Statement.' },
      { head: 'Arrays:', text: 'Advantages of Arrays, Creating an Array, Types of Arrays, Mathematical Operations on Arrays, Dimensions of Arrays, Attributes of an Array.' }] },
  { n: 4, title: 'Lists, Tuples, Dictionaries and Functions', short: 'Collections & Functions', folder: 'Unit_4_Lists_Tuples_Dictionaries_Functions',
    desc: 'Lists, tuples, dictionaries and functions: creating, processing, sorting, nesting, passing objects and returning results.',
    syllabus: [{ head: 'Components and Functions.' , text: '' },
      { head: 'List:', text: 'Creating Lists, Updating the Elements of a List, Concatenation of Two Lists, Repetition of Lists, Membership in Lists, Methods to Process Lists, Sorting, Nested Lists.' },
      { head: 'Tuples:', text: 'Creating Tuples, Accessing the Tuple Elements, Operations on Tuples, Functions to Process Tuples, Nested Tuples.' },
      { head: 'Dictionaries:', text: 'Operations on Dictionaries, Dictionary Methods, Passing Dictionaries to Functions, Ordered Dictionaries.' },
      { head: 'Functions:', text: 'Defining a Function, Difference between a Function and a Method, Calling a Function, Returning Results from a Function, Returning Multiple Values from a Function, Pass by Object Reference.' }] },
  { n: 5, title: 'OOPS and Data Structures', short: 'OOP & Data Structures', folder: 'Unit_5_OOPS_Data_Structures_Database',
    desc: 'Object oriented programming, abstract classes, exceptions, linked lists, stacks, queues, deques, date/time and SQLite database connectivity.',
    syllabus: [{ head: 'OOPS and Data Structures.', text: 'Object Oriented Programming System (OOPS), Classes and Objects, Encapsulation, Abstraction, Inheritance, Polymorphism.' },
      { text: 'Abstract Classes and Interfaces, Exceptions.' },
      { head: 'Data structures:', text: 'Linked list, stacks, Queues, Dequeues.' },
      { text: 'Date and Time, Python’s Database Connectivity.' }] },
];
export const UNIT_TOPICS = topics; // syllabus topic names per unit (used for coverage display)
export const unitOf = (n) => UNITS[n - 1];
export const UNIT_LABEL = (n) => `Unit ${n}: ${UNITS[n - 1].title}`;
export const syllabusText = () => {
  let s = `${COURSE.semester}\n${COURSE.code}: ${COURSE.name}\n\n`;
  UNITS.forEach((u) => { s += `UNIT ${u.n}\n\n`; u.syllabus.forEach((b) => { if (b.head) s += b.head + '\n'; if (b.text) s += b.text + '\n'; s += '\n'; }); });
  return s;
};
