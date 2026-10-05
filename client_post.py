import socket
import json
from datetime import date

# Server address and HTTP port.
HOST = "httpbingo.org"
PORT = 80

# Data that will be sent as JSON in the POST request.
data = {
    "name": "Марія",
    "date": str(date.today())
}

# Convert the Python dictionary to UTF-8 encoded JSON bytes.
body = json.dumps(data, ensure_ascii=False).encode("utf-8")

# Content-Length must count bytes, not characters.
# This is important because UTF-8 characters can use more than one byte.
content_length = len(body)

# Build the HTTP POST request.
request = (
    "POST /post HTTP/1.1\r\n"
    f"Host: {HOST}\r\n"
    "User-Agent: MyPythonSocketClient/1.0\r\n"
    "Content-Type: application/json\r\n"
    f"Content-Length: {content_length}\r\n"
    "\r\n"
).encode("ascii") + body

# Connect to the server and send the request.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall(request)

    # First read the response headers.
    response = b""

    while b"\r\n\r\n" not in response:
        chunk = sock.recv(4096)

        if not chunk:
            break

        response += chunk

    headers_end = response.find(b"\r\n\r\n")

    if headers_end != -1:
        header_part = response[:headers_end].decode("iso-8859-1")
        body_part = response[headers_end + 4:]

        # Find Content-Length to know how many response bytes to read.
        response_content_length = None

        for line in header_part.split("\r\n"):
            if line.lower().startswith("content-length:"):
                response_content_length = int(line.split(":", 1)[1].strip())
                break

        # Read the complete response body.
        while (
            response_content_length is not None
            and len(body_part) < response_content_length
        ):
            chunk = sock.recv(4096)

            if not chunk:
                break

            body_part += chunk

        response = response[:headers_end + 4] + body_part

# Decode and print the complete HTTP response.
print(response.decode("utf-8", errors="replace"))