from socket import *

server_name = 'localhost'
server_port = 8560
client_socket = socket(AF_INET, SOCK_DGRAM)
message = input("Enter the message: ")
client_socket.sendto(message.encode(), (server_name, server_port))
modified_message, server_address = client_socket.recvfrom(2048)
print(modified_message.decode())
client_socket.close()