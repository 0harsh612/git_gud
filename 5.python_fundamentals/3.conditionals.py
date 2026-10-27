# ============================================================
# PYTHON FUNDAMENTALS: CONDITIONAL STATEMENTS
# ============================================================
# In this file, we will learn:
# 1. Comparison operators
# 2. The if statement
# 3. The if-else statement
# 4. The if-elif-else statement
# 5. Logical operators
# 6. Nested if statements
# 7. Membership operators
# 8. A practical example
# ============================================================


# ------------------------------------------------------------
# 1. COMPARISON OPERATORS
# ------------------------------------------------------------
# Comparison operators compare two values.
# The result is always either True or False.

a = 10
b = 20

print("--- Comparison Operators ---")

print("a == b:", a == b)   # Equal to
print("a != b:", a != b)   # Not equal to
print("a > b:", a > b)     # Greater than
print("a < b:", a < b)     # Less than
print("a >= b:", a >= b)   # Greater than or equal to
print("a <= b:", a <= b)   # Less than or equal to


# ------------------------------------------------------------
# 2. THE if STATEMENT
# ------------------------------------------------------------
# An if statement executes a block of code only when
# its condition is True.
#
# IMPORTANT: Python uses indentation to define code blocks.

print("\n--- The if Statement ---")

age = 19

if age >= 18:
    print("You are eligible to vote.")

# Since age is 19, the condition is True and the message prints.


# ------------------------------------------------------------
# 3. THE if-else STATEMENT
# ------------------------------------------------------------
# Use else when you want to execute one block if the condition
# is True and another block if it is False.

print("\n--- The if-else Statement ---")

number = 7

if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")

# The % operator gives the remainder.
# An even number has a remainder of 0 when divided by 2.


# ------------------------------------------------------------
# 4. THE if-elif-else STATEMENT
# ------------------------------------------------------------
# Use elif when you need to check multiple conditions.
# Python checks the conditions from top to bottom.
# The first matching block is executed.

print("\n--- The if-elif-else Statement ---")

marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F")

# Since marks are 85, the grade is B.
# Notice that we check the highest range first.


# ------------------------------------------------------------
# 5. LOGICAL OPERATORS
# ------------------------------------------------------------
# Logical operators combine or reverse conditions.
#
# and: True only when both conditions are True.
# or:  True when at least one condition is True.
# not: Reverses True and False.

print("\n--- Logical Operators ---")

age = 19
has_id = True

# Both conditions must be True.
if age >= 18 and has_id:
    print("Entry allowed.")

# At least one condition must be True.
is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("You can relax today!")

# not reverses a Boolean value.
is_raining = False

if not is_raining:
    print("It is not raining. You can go outside.")


# ------------------------------------------------------------
# 6. NESTED if STATEMENTS
# ------------------------------------------------------------
# A nested if is an if statement inside another if statement.
# It is useful when one decision depends on another.

print("\n--- Nested if Statements ---")

age = 20
has_ticket = True

if age >= 18:
    print("Age requirement satisfied.")

    if has_ticket:
        print("You can enter the event.")
    else:
        print("You need a ticket to enter.")

else:
    print("You do not meet the age requirement.")


# ------------------------------------------------------------
# 7. MEMBERSHIP OPERATORS
# ------------------------------------------------------------
# The 'in' operator checks whether a value exists in a sequence.
# The 'not in' operator checks whether it does not exist.

print("\n--- Membership Operators ---")

available_subjects = ["Python", "C++", "Mathematics", "OS"]

print("Python available?", "Python" in available_subjects)
print("Java available?", "Java" in available_subjects)

if "C++" in available_subjects:
    print("C++ is included in the list.")

if "Java" not in available_subjects:
    print("Java is not included in the list.")


# ------------------------------------------------------------
# 8. TAKING INPUT AND MAKING DECISIONS
# ------------------------------------------------------------
# Let's allow the user to enter their marks and calculate
# their grade using conditional statements.

print("\n--- Grade Calculator ---")

marks = float(input("Enter your marks out of 100: "))

# Validate the input range before assigning a grade.
if marks < 0 or marks > 100:
    print("Invalid marks! Enter a value between 0 and 100.")

elif marks >= 90:
    print("Grade: A")

elif marks >= 75:
    print("Grade: B")

elif marks >= 60:
    print("Grade: C")

elif marks >= 40:
    print("Grade: D")

else:
    print("Grade: F")

# Try entering different marks to see how the output changes.


# ------------------------------------------------------------
# 9. MINI EXAMPLE: SIMPLE LOGIN CHECK
# ------------------------------------------------------------
# This example demonstrates how conditions can be used
# to make decisions based on user input.
#
# NOTE: This is only a basic demonstration.
# Real applications need proper authentication and security.

print("\n--- Simple Login Check ---")

correct_username = "student"
correct_password = "python123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful! Welcome.")
else:
    print("Incorrect username or password.")


# ------------------------------------------------------------
# CHALLENGE: YOUR TURN!
# ------------------------------------------------------------
# 1. Ask the user for a number and check whether it is positive,
#    negative, or zero.
#
# 2. Ask the user for their age.
#    Print whether they are a child, teenager, or adult.
#
# 3. Ask for three numbers and print the largest one.
#
# 4. Create a simple calculator that accepts two numbers
#    and an operator (+, -, *, /), then prints the result.
#
# HINT:
# Use if, elif and else to handle different cases.
# For division, check that the second number is not zero.
# ============================================================
