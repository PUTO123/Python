import socket

client_socket = socket.socket(socket.AF_INET)


server.adress = (("127.0.0.1, 1337"))
client_socket.connect(server_adress)
client_socket.send("Hi") 
