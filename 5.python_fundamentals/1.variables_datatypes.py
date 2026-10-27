# ============================================================
# PYTHON FUNDAMENTALS: VARIABLES AND DATA TYPES
# ============================================================
# In this file, we will learn:
# 1. Variables
# 2. Basic data types
# 3. Checking data types using type()
# 4. Taking input from the user
# 5. Type conversion
# 6. Basic arithmetic operations
# ============================================================


# ------------------------------------------------------------
# 1. VARIABLES
# ------------------------------------------------------------
# A variable is a name used to store a value.
# Think of it as a labelled box that holds some information.

name = "Darshan"
age = 19
height = 5.9

print("Name:", name)
print("Age:", age)
print("Height:", height)


# ------------------------------------------------------------
# 2. BASIC DATA TYPES
# ------------------------------------------------------------
# Python has different data types for storing different values.

# int: Whole numbers
marks = 95

# float: Numbers with decimal points
percentage = 92.5

# str: Text enclosed in quotes
college = "VJTI"

# bool: True or False values
is_student = True

print("\n--- Basic Data Types ---")
print("Marks:", marks)
print("Percentage:", percentage)
print("College:", college)
print("Is a student?", is_student)


# ------------------------------------------------------------
# 3. CHECKING DATA TYPES
# ------------------------------------------------------------
# The type() function tells us the data type of a value.

print("\n--- Checking Data Types ---")
print(type(marks))
print(type(percentage))
print(type(college))
print(type(is_student))

# Notice that Python automatically identifies the data type
# based on the value assigned to the variable.


# ------------------------------------------------------------
# 4. VARIABLES CAN STORE DIFFERENT VALUES
# ------------------------------------------------------------
# We can update a variable whenever we need to.

score = 10
print("\nOriginal score:", score)

score = 25
print("Updated score:", score)

# The variable now stores 25 instead of 10.


# ------------------------------------------------------------
# 5. TAKING INPUT FROM THE USER
# ------------------------------------------------------------
# The input() function allows the user to enter information.
# By default, input() returns the entered value as a string.

print("\n--- User Input ---")

user_name = input("Enter your name: ")
print("Hello,", user_name + "! Welcome to Python.")

# Try entering your own name when you run this program.


# ------------------------------------------------------------
# 6. TYPE CONVERSION
# ------------------------------------------------------------
# Sometimes, we need to convert a value from one data type
# to another.
#
# int()   converts a compatible value to an integer.
# float() converts a compatible value to a decimal number.
# str()   converts a value to a string.

print("\n--- Type Conversion ---")

age_text = input("Enter your age: ")

# input() gives us a string, so we convert it to an integer.
age = int(age_text)

print("Next year, you will be", age + 1, "years old.")

# Without int(), adding 1 to the input would not work as
# ordinary numerical addition because the input is a string.


# ------------------------------------------------------------
# 7. BASIC ARITHMETIC OPERATIONS
# ------------------------------------------------------------
# Python supports the usual arithmetic operators.

a = 17
b = 5

print("\n--- Arithmetic Operations ---")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# // gives the quotient without the fractional part.
print("Floor division:", a // b)

# % gives the remainder.
print("Remainder:", a % b)

# ** raises a number to a power.
print("Power:", a ** b)


# ------------------------------------------------------------
# 8. MINI EXAMPLE: CALCULATING AVERAGE MARKS
# ------------------------------------------------------------
# Let's use variables, input, type conversion and arithmetic
# together in one small example.

print("\n--- Average Marks Calculator ---")

mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))

average = (mark1 + mark2 + mark3) / 3

print("Your average marks are:", round(average, 2))


# ------------------------------------------------------------
# CHALLENGE: YOUR TURN!
# ------------------------------------------------------------
# 1. Create variables for your name, age and favourite subject.
# 2. Print all three values.
# 3. Ask the user for two numbers and print their sum.
# 4. Ask the user for the length and breadth of a rectangle.
#    Calculate and print its area.
#
# Hint:
# area = length * breadth
#
# Try solving these before looking up the answers!
# ============================================================

