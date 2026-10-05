# This file demonstrates functions, parameters, docstrings, and return values.

def greet(name, greeting="Hello"):
    """Return a greeting message."""
    return f"{greeting}, {name}!"


# Call the function with one positional argument.
print(greet("Maria"))

# Call the function with two positional arguments.
print(greet("Maria", "Welcome"))

# Call the function using keyword arguments.
print(greet(name="Maria", greeting="Hi"))


def check_status(status_code):
    """Return success or failure based on the HTTP status code."""
    if status_code == 200:
        return "Success"
    else:
        return "Failure"


# Store and print the value returned by the function.
result = check_status(200)
print("Status result:", result)

result = check_status(404)
print("Status result:", result)