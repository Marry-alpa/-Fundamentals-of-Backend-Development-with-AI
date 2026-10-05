# This file demonstrates basic string operations.

name = "Maria"
course = "Python Fundamentals"

# Create a sentence using string concatenation.
sentence_plus = "My name is " + name + " and I am studying " + course + "."
print(sentence_plus)

# Create the same sentence using an f-string.
sentence_f = f"My name is {name} and I am studying {course}."
print(sentence_f)

# Convert the f-string result to uppercase.
print(sentence_f.upper())

# Create a two-line string using a carriage return and line feed.
two_lines = "First line\r\nSecond line"
print(two_lines)