import socket

# Server address and HTTP port.
HOST = "httpbingo.org"
PORT = 80

# Request path used to test the HTTP status code.
PATH = "/status/404"

# Create a TCP connection to the server.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    # Build and send an HTTP GET request.
    request = (
        f"GET {PATH} HTTP/1.1\r\n"
        f"Host: {HOST}\r\n"
        "Connection: close\r\n"
        "User-Agent: MyPythonSocketClient/1.0\r\n"
        "\r\n"
    )

    sock.sendall(request.encode("ascii"))

    # Read the response until the server closes the connection.
    response = b""

    while True:
        chunk = sock.recv(4096)

        if not chunk:
            break

        response += chunk

# Decode only the beginning of the response to get the status line.
response_text = response.decode("utf-8", errors="replace")
status_line = response_text.split("\r\n", 1)[0]

print(status_line)

# Extract the numeric HTTP status code.
parts = status_line.split(" ", 2)
status_code = int(parts[1])

# Print a message depending on the status code.
if status_code == 200:
    print("OK")
elif status_code == 404:
    print("Not Found")
elif status_code >= 500:
    print("Server error")
else:
    print("Other status code")