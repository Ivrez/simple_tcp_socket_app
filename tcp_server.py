from socket import *
server_port = 12000
server_sock = socket(AF_INET, SOCK_STREAM)

server_sock.bind(('', server_port))
server_sock.listen(1)

print('server socket initialized: \n {} \n'.format(server_sock))
print('the server is ready to recieve')

while True:
    conn_sock, addr = server_sock.accept()
    msg = conn_sock.recv(1024).decode()

    mod_msg = msg[::-1]
    conn_sock.send(mod_msg.encode())

    print("log \n msg: {} \n mod_msg: {} \n addr: {} \n sock: {} \n\n".format(msg, mod_msg, addr, conn_sock))
    conn_sock.close()
