import socket
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s'-'%(levelname)s'-'%(message)s')

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=('localhost',65432)

try:
    server_socket.bind(server_address)
    logging.info(f"server started on {server_address}")
except socket.error as e:
    logging.error(f"Bind failed:{e}")
    exit()

server_socket.listen(1)
logging.info("waiting for the connection..")

connection, client_address=server_socket.accept()
logging.info(f"connection established with {client_address}")

try:
    while True:
        data=connection.recv(1024)
        if data:
            logging.info(f"received:{data.decode()}")
                    # Send data back to the client
            connection.sendall(data)

        else:
            logging.info("no data hase received so we are closing the connection")
            break

finally:
     # Clean up the connection
     logging.info("cleaning up the connection")
     connection.close()


