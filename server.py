import socket

server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address=('localhost',65432)

server_socket.bind(server_address)

server_socket.listen(1)
print("waiting for the connection..........")

connection, client_address=server_socket.accept()


try:
    print("connection eastablished wiht",client_address)
    
    #now we will receive data from the client

    while True:
        data=connection.recv(1024)
        if data:
            print('Received:', data.decode())
            #send data back to client
            connection.sendall(data)
        else:
            break

finally:
    #time to clean up the connection
    connection.close()

