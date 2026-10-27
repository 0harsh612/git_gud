# ============================================================
# PYTHON FUNDAMENTALS: LOOPS
# ============================================================
# In this file, we will learn:
# 1. Why loops are useful
# 2. The for loop
# 3. The range() function
# 4. The while loop
# 5. break and continue
# 6. Nested loops
# 7. Looping through strings and lists
# 8. A practical example
# ============================================================


# ------------------------------------------------------------
# 1. WHY DO WE NEED LOOPS?
# ------------------------------------------------------------
# Imagine printing "Hello" 5 times.
# We could write print("Hello") five times, but that is repetitive.
# A loop allows us to repeat a block of code automatically.

print("--- Without a Loop ---")

print("Hello")
print("Hello")
print("Hello")

print("\n--- With a Loop ---")

for i in range(3):
    print("Hello")

# Both approaches print Hello three times.
# The loop is shorter and easier to modify.


# ------------------------------------------------------------
# 2. THE for LOOP
# ------------------------------------------------------------
# A for loop repeats a block of code for each item
# in a sequence or other iterable object.

print("\n--- The for Loop ---")

for number in [1, 2, 3, 4, 5]:
    print("Number:", number)

# The variable 'number' takes each value from the list
# one at a time.


# ------------------------------------------------------------
# 3. THE range() FUNCTION
# ------------------------------------------------------------
# range() generates a sequence of integers.
#
# range(stop)             starts at 0 and stops before stop.
# range(start, stop)      starts at start and stops before stop.
# range(start, stop, step) changes the value by step each time.

print("\n--- Using range() ---")

# Prints 0, 1, 2, 3, 4.
for i in range(5):
    print(i)

# Prints 2, 3, 4, 5.
print("\nStarting from 2:")
for i in range(2, 6):
    print(i)

# Prints 2, 4, 6, 8, 10.
print("\nEven numbers:")
for i in range(2, 11, 2):
    print(i)

# Counts backwards from 5 to 1.
print("\nCountdown:")
for i in range(5, 0, -1):
    print(i)

print("Go!")


# ------------------------------------------------------------
# 4. CALCULATING A SUM USING A LOOP
# ------------------------------------------------------------
# Loops can help us perform calculations on a sequence
# of numbers.

print("\n--- Sum of First 5 Natural Numbers ---")

total = 0

for number in range(1, 6):
    total = total + number

print("Total:", total)

# The loop calculates:
# 0 + 1 + 2 + 3 + 4 + 5 = 15


# ------------------------------------------------------------
# 5. THE while LOOP
# ------------------------------------------------------------
# A while loop repeats as long as its condition is True.
# Remember to update the variable used in the condition,
# otherwise the loop might never stop.

print("\n--- The while Loop ---")

count = 1

while count <= 5:
    print("Count:", count)
    count += 1

# count += 1 is shorthand for count = count + 1.


# ------------------------------------------------------------
# 6. break STATEMENT
# ------------------------------------------------------------
# break immediately terminates the nearest enclosing loop.

print("\n--- Using break ---")

for number in range(1, 11):

    if number == 5:
        print("Found 5! Stopping the loop.")
        break

    print(number)

# The loop stops when number becomes 5.
# Therefore, 5 is not printed by the print(number) statement.


# ------------------------------------------------------------
# 7. continue STATEMENT
# ------------------------------------------------------------
# continue skips the remaining statements in the current
# iteration and moves to the next iteration.

print("\n--- Using continue ---")

for number in range(1, 6):

    if number == 3:
        continue

    print(number)

# The number 3 is skipped, but the loop continues afterward.


# ------------------------------------------------------------
# 8. NESTED LOOPS
# ------------------------------------------------------------
# A nested loop is a loop inside another loop.
# The inner loop completes its iterations for each iteration
# of the outer loop.

print("\n--- Nested Loops ---")

for row in range(1, 4):

    for column in range(1, 4):
        print("(", row, ",", column, ")", end=" ")

    print()

# The outer loop controls the rows.
# The inner loop controls the columns.
# The final print() moves the output to a new line.


# ------------------------------------------------------------
# 9. PRINTING A SIMPLE PATTERN
# ------------------------------------------------------------
# Nested loops are useful for printing patterns.

print("\n--- Star Pattern ---")

for row in range(1, 5):
    for column in range(row):
        print("*", end=" ")

    print()

# Expected output:
# *
# * *
# * * *
# * * * *


# ------------------------------------------------------------
# 10. LOOPING THROUGH STRINGS AND LISTS
# ------------------------------------------------------------
# A for loop can process each character in a string
# or each item in a list.

print("\n--- Looping Through a String ---")

word = "PYTHON"

for character in word:
    print(character)

print("\n--- Looping Through a List ---")

subjects = ["Python", "C++", "Mathematics", "OS"]

for subject in subjects:
    print("Subject:", subject)


# ------------------------------------------------------------
# 11. MINI EXAMPLE: GUESS THE NUMBER
# ------------------------------------------------------------
# Let's create a simple number-guessing game.
# The player gets three attempts to guess the secret number.

print("\n--- Guess the Number ---")

secret_number = 7
attempts = 3

for attempt in range(1, attempts + 1):

    guess = int(input("Guess the number (1 to 10): "))

    if guess == secret_number:
        print("Correct! You guessed the number.")
        break

    elif guess < secret_number:
        print("Too low! Try a bigger number.")

    else:
        print("Too high! Try a smaller number.")

else:
    # This else belongs to the for loop.
    # It runs only when the loop finishes without a break.
    print("Game over! The number was", secret_number)


# ------------------------------------------------------------
# CHALLENGE: YOUR TURN!
# ------------------------------------------------------------
# 1. Print the numbers from 1 to 20.
#
# 2. Print all even numbers between 1 and 50.
#
# 3. Calculate the factorial of a positive integer.
#    Example: 5! = 5 * 4 * 3 * 2 * 1 = 120
#
# 4. Print this pattern:
#
#    *
#    * *
#    * * *
#    * * * *
#    * * * * *
#
# 5. Create a program that keeps asking the user for numbers
#    until they enter 0. Then print the sum of all the numbers
#    entered, excluding the final 0.
#
# HINT:
# Use a while loop for Question 5.
# ============================================================
