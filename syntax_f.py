# This file demonstrates if/elif/else branching.

status_code = 200

# Select a message based on the HTTP status code.
if status_code == 200:
    print("Success")
elif status_code == 404:
    print("Not Found")
elif status_code >= 500:
    print("Server Error")
else:
    print("Other status code")