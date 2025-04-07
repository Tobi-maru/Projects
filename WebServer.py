# A simple webserver build in pyhton using inbuilt sockect module 

import socket

def handle_request(request):
    """Handles the HTTP request."""
    headers = request.split('\n')
    filename = headers[0].split()[1]
    if filename == '/':
        filename = '/index.html'

    try:
        filepath = '/home/tobi/website' + filename
        fin = open(filepath, 'rb')
        content = fin.read()
        fin.close()

        # Determine the content type
        if filename.endswith('.html'):
            content_type = 'text/html'
        elif filename.endswith('.jpg') or filename.endswith('.jpeg'):
            content_type = 'image/jpeg'
        elif filename.endswith('.png'):
            content_type = 'image/png'
        elif filename.endswith('.gif'):
            content_type = 'image/gif'
        else:
            content_type = 'application/octet-stream'

        response = f'HTTP/1.0 200 OK\r\nContent-Type: {content_type}\r\n\r\n'.encode() + content
    except FileNotFoundError:
        response = 'HTTP/1.0 404 NOT FOUND\r\n\r\nFile Not Found'.encode()

    return response

# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8080

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    print(request)

    # Return an HTTP response
    response = handle_request(request)
    client_connection.sendall(response)

    # Close connection
    client_connection.close()

# Close socket
server_socket.close()   