# This file demonstrates lists, dictionaries, and tuples.

# Create a list of HTTP headers and add another header.
headers = ["Host", "User-Agent", "Accept"]
headers.append("Content-Type")

print("First header:", headers[0])
print("Number of headers:", len(headers))

# Create a dictionary of request headers.
request_headers = {
    "Host": "httpbingo.org",
    "User-Agent": "MyPythonClient/1.0"
}

# Add more headers to the dictionary.
request_headers["Accept"] = "*/*"
request_headers["Connection"] = "close"

# Iterate through all dictionary items.
for key, value in request_headers.items():
    print(key, "=", value)

# Use get() to safely access a missing key with a default value.
print("Missing header:", request_headers.get("Authorization", "Not found"))

# Store a host and port in a tuple and unpack its values.
host_port = ("httpbingo.org", 80)
host, port = host_port

print("Host:", host)
print("Port:", port)