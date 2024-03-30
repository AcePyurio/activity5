import socket
import threading

# Global counter for generating unique connection IDs
connection_counter = 0
connection_lock = threading.Lock()

def clientHandler(conn, addr):
    """
    Handles communication with a client connection.
    This function continuously receives messages from a client connection,
    prints them to the console, and echoes them back to the client.
    If the message received is "quit", the connection with the client is closed.
    """
    global connection_counter
    with connection_lock:
        connection_counter += 1
        connection_id = connection_counter
    
    print(f'Connected to the Client {connection_id} from {addr}')
    
    while True:
        data = conn.recv(1024)
        if not data:
            break
        message = data.decode()
        print(f'Client connection {connection_id} : {message}')
        if message.lower() == 'quit':
            break
        conn.sendall(data)
    
    print(f'Client-{connection_id} is closed.')
    conn.close()



def start_server(host='127.0.0.1', port=65432):
    """
    Starts a TCP server that listens for incoming connections and handles them concurrently.
    It then listens for incoming connections and spawns a new thread to handle each connection.
    The clientHandler function is used to handle communication with each client connection.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        print(f'Server started, listening on {host}:{port}')
        s.listen()
        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=clientHandler, args=(conn, addr))
            thread.start()

if __name__ == "__main__":
    start_server()
