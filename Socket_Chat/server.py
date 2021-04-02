import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((socket.gethostname(), 1337))

server_socket.listen(7)
