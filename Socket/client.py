import socket
from common import ip, port

client = socket.socket()                        # instantiating a client socket
print("Client created!")

client.connect((ip, port))                      # connecting to a server with ip address and the port
print("Connected to a server\n")

while True:
    message = input("Write your message:\t")    # taking the message as input
    client.send(message.encode())               # sending the message to the server
    reply = client.recv(1024).decode()          # getting the message from server
    print(f"Server: ", reply, "\n")
    
    if message == "exit()":
        break

client.close()
