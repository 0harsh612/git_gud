# ============================================================
# PYTHON FUNDAMENTALS: STRINGS
# ============================================================
# In this file, we will learn:
# 1. Creating strings
# 2. Accessing individual characters
# 3. String indexing
# 4. String slicing
# 5. Common string methods
# 6. Searching inside strings
# 7. String formatting
# 8. A small practical example
# ============================================================


# ------------------------------------------------------------
# 1. CREATING STRINGS
# ------------------------------------------------------------
# A string is a sequence of characters.
# We can create strings using single or double quotes.

name = "Darshan"
college = 'VJTI'

print("Name:", name)
print("College:", college)

# Triple quotes can be used for multi-line strings.
message = """Welcome to Python!
Let's learn strings together."""

print("\n", message)


# ------------------------------------------------------------
# 2. STRING LENGTH
# ------------------------------------------------------------
# The len() function returns the number of characters
# in a string, including spaces and punctuation.

text = "Hello World"

print("\n--- String Length ---")
print("Text:", text)
print("Length:", len(text))

# Try changing the text and checking its length.


# ------------------------------------------------------------
# 3. STRING INDEXING
# ------------------------------------------------------------
# Every character in a string has an index.
#
# Positive indexing starts from 0 on the left.
# Negative indexing starts from -1 on the right.

word = "PYTHON"

print("\n--- String Indexing ---")
print("Original word:", word)

print("First character:", word[0])
print("Second character:", word[1])
print("Last character:", word[-1])
print("Second-last character:", word[-2])

# Remember: indexing starts at 0, not 1!


# ------------------------------------------------------------
# 4. STRING SLICING
# ------------------------------------------------------------
# Slicing lets us extract a part of a string.
#
# Syntax: string[start:stop:step]
#
# The start index is included, but the stop index is excluded.

word = "PYTHON"

print("\n--- String Slicing ---")
print("Original word:", word)

print("First three characters:", word[0:3])
print("Characters from index 2:", word[2:])
print("First four characters:", word[:4])
print("Complete word:", word[:])

# A step of 2 selects every second character.
print("Every second character:", word[::2])

# A step of -1 reverses the string.
print("Reversed word:", word[::-1])


# ------------------------------------------------------------
# 5. COMMON STRING METHODS
# ------------------------------------------------------------
# String methods help us perform common operations on text.
# They return results without changing the original string.

sentence = "  python is fun to learn  "

print("\n--- String Methods ---")
print("Original:", repr(sentence))

# Convert all letters to uppercase.
print("Uppercase:", sentence.upper())

# Convert all letters to lowercase.
print("Lowercase:", sentence.lower())

# Capitalize the first character of the string.
print("Capitalized:", sentence.strip().capitalize())

# Remove spaces from the beginning and end.
print("Without extra spaces:", sentence.strip())

# Replace one part of a string with another.
print("Replace Python:", sentence.replace("python", "coding"))

# Count how many times a character appears.
print("Number of 'n' characters:", sentence.count("n"))

# Check whether a string starts or ends with certain text.
print("Starts with spaces?", sentence.startswith(" "))
print("Ends with 'learn'?", sentence.strip().endswith("learn"))

# The original string remains unchanged.
print("Original after methods:", repr(sentence))


# ------------------------------------------------------------
# 6. CHECKING AND SEARCHING STRINGS
# ------------------------------------------------------------
# We can check whether a smaller string exists inside another.

sentence = "Python is beginner friendly"

print("\n--- Searching Strings ---")

print("Contains 'Python'?", "Python" in sentence)
print("Contains 'Java'?", "Java" in sentence)

# find() returns the index of the first occurrence.
# If the text is not found, it returns -1.
print("Position of 'beginner':", sentence.find("beginner"))
print("Position of 'Java':", sentence.find("Java"))


# ------------------------------------------------------------
# 7. SPLITTING AND JOINING STRINGS
# ------------------------------------------------------------
# split() breaks a string into a list of smaller strings.
# By default, it splits wherever whitespace occurs.

subjects = "Python C++ Mathematics Operating Systems"

print("\n--- Splitting and Joining ---")

subject_list = subjects.split()

print("Original string:", subjects)
print("List of subjects:", subject_list)
print("First subject:", subject_list[0])

# join() combines multiple strings using a separator.
joined_subjects = " | ".join(subject_list)

print("Joined subjects:", joined_subjects)


# ------------------------------------------------------------
# 8. STRING FORMATTING
# ------------------------------------------------------------
# f-strings let us insert variable values directly into text.
# Put the letter f before the opening quotation mark.

name = "Aarav"
age = 18
marks = 91.567

print("\n--- String Formatting ---")

print(f"My name is {name}.")
print(f"I am {age} years old.")
print(f"My marks are {marks:.2f}.")

# :.2f displays a floating-point number to 2 decimal places.
# For example, 91.567 becomes 91.57.


# ------------------------------------------------------------
# 9. STRINGS ARE IMMUTABLE
# ------------------------------------------------------------
# Strings are immutable, which means we cannot directly
# change an individual character inside an existing string.

word = "CAT"

print("\n--- String Immutability ---")
print("Original word:", word)

# The following operation would cause a TypeError:
# word[0] = "B"

# Instead, create a new string using concatenation.
new_word = "B" + word[1:]

print("New word:", new_word)
print("Original word is still:", word)


# ------------------------------------------------------------
# 10. MINI EXAMPLE: USERNAME GENERATOR
# ------------------------------------------------------------
# Let's combine string methods, indexing and slicing
# to create a simple username from a user's name.

print("\n--- Username Generator ---")

full_name = input("Enter your full name: ")

# Remove extra spaces and convert the name to lowercase.
clean_name = full_name.strip().lower()

# Replace spaces with underscores.
username = clean_name.replace(" ", "_")

print("Your username could be:", username)

# Example:
# Input:  Aarav Sharma
# Output: aarav_sharma


# ------------------------------------------------------------
# CHALLENGE: YOUR TURN!
# ------------------------------------------------------------
# 1. Take a word as input and print its length.
# 2. Print its first and last characters.
# 3. Print the word in uppercase and lowercase.
# 4. Reverse the word using slicing.
# 5. Ask for a sentence and count how many times 'a' appears.
#
# Hint:
# word[::-1] reverses a string.
# word.count("a") counts occurrences of the letter 'a'.
#
# Try solving these before looking up the answers!
# ============================================================
