import socket

client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address=('localhost',65432)
client_socket.connect(server_address)

try:
    #send data to the server
    message="Hello, server!"
    print('sending:',message)
    client_socket.sendall(message.encode())

    #receive response from the server
    data=client_socket.recv(1024)
    print("Received:",data.decode())

finally:
    #close the connection
    client_socket.close
