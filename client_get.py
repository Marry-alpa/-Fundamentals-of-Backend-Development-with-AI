import socket

# Server address and HTTP port.
HOST = "httpbingo.org"
PORT = 80

# Create a raw TCP socket and connect to the server.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    # Build a simple HTTP GET request.
    request = (
        "GET /get HTTP/1.1\r\n"
        f"Host: {HOST}\r\n"
        "Connection: close\r\n"
        "User-Agent: MyPythonSocketClient/1.0\r\n"
        "\r\n"
    )

    # Send the request to the server.
    sock.sendall(request.encode("ascii"))

    # Read the response until the server closes the connection.
    response = b""

    while True:
        chunk = sock.recv(4096)

        if not chunk:
            break

        response += chunk

# Decode and print the complete HTTP response.
print(response.decode("utf-8", errors="replace"))