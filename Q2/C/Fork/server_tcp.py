import socket
import time
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 12345))

server.listen(1)


BUFFER_SIZE = 32


print("Listening for connections ...")


clientsocket, address = server.accept()

print(f"Connection from {address} has been established.")


def client_handler(clientsocket):
    file = open(f'../Texts/{book_name}.txt', 'r', encoding="utf-8")

    while True:

        data = file.read(BUFFER_SIZE)
        
        if not data:
            clientsocket.send( bytes("end_","utf-8"))

            file.close()
            break
        clientsocket.send( bytes(data,"utf-8"))

while True:

    book_name = clientsocket.recv(128).decode('utf-8')

    if not book_name:
        break

    print("book name : ",book_name)

    child_pid = os.fork()

    if child_pid==0: #child process
        client_handler(clientsocket)
        break


clientsocket.close()
    

        
        

    



