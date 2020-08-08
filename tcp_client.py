from socket import *

server_name = '127.0.0.1'
server_port = 12000

while True:
    client_sock = socket(AF_INET, SOCK_STREAM)
    client_sock.connect((server_name, server_port))

    msg = input('input: ')

    client_sock.send(msg.encode())
    mod_msg = client_sock.recv(1024)

    print('msg from server: \n {}\n'.format(mod_msg.decode()))
    client_sock.close()
