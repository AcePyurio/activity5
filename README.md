### Activity 5
The main goal of this project is to demonstrate the concept of concurrency through socket programming. This is demonstrated in the server by handling multiple connections simultaneously.

### Server.py
This project implements a Python TCP server that listens for incoming connections from clients. It uses threading to handle multiple clients, allowing to communicate with other client connection without blocking other connections. The server binds to a user-specified address and port. This server has the clientHandle() function that is use by thread as an argument. Inside that function, every connection message received from the client is send back to the client. The function can detect the message “quit” which closes the connection, but the server is still running and able to accept new connection. The server uses a global counter to generate unique connection IDs for each client connection.

### Client.py
The client side connect to the server by TCP. It specify the host and port. The client prompts the user to enter their message once the user enter the message will be send to the server. The client then received a reply from the server which will be printed in the console. If the user send the message “quit” to the server connection will be close. 

### How to run the Server and Client
1. Make sure that Python is installed on your system.
2. Clone this repository to your local machine.
3. Open a terminal and navigate to the directory containing the cloned repository.
4. Start the server by running python server.py.
5. Start the client by running python client.py. Run multiple client by opening new terminal. 
6. Follow the prompts to interact with the server and send messages.
