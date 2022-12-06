import socket 
from common import ip, port

server = socket.socket()                                # instantiating a server socket
print("Server created!")

server.bind((ip, port))                                 # binding a server with ip address and the port
server.listen(1)                                        # listening for client requests
print("Waiting for a client")

while True:
    client, clientSocket = server.accept()              # accepting a client request

    with client:
        print("\n\nConnected with ", clientSocket, "\n")
        while True:
            message = client.recv(1024).decode()        # getting the message from the client
            print(message)
            if message == "exit()":
                client.send("Bye!!!".encode())
                client.close()
                break
            client.send(message.encode())               # transferring the message back to that client

# server.close()
