import socket

def start_client(host='127.0.0.1', port=65432):
    """
        This function creates a socket and connects it to the specified server and port.
        It then prompts the user to enter messages to send to the server.
        If the user types 'quit', the client sends this message to the server and exits.
    """

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print('Now connected to the server.')
        while True:
            message = input("Please enter your message (type 'quit' to exit): ")
            s.sendall(message.encode())
            if message.lower() == 'quit':
                break
            data = s.recv(1024)
            print(f'Server reply: {data.decode()}')

if __name__ == "__main__":
    start_client()
