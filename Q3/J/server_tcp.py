import socket
import time
import threading
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


HOST = sys.argv[1]
server.bind((HOST, 12345))



server.listen(1)


BUFFER_SIZE = 32


print("Listening for connections ...")


def client_handler(clientsocket):
    file = open(f'../../Texts/{book_name}.txt', 'r', encoding="utf-8")
    
    while True:


        data = file.read(BUFFER_SIZE)
        

        if not data:
            file.close()
            break
        
        clientsocket.send( bytes(data,"utf-8"))
        

    clientsocket.close()




clientsocket, address = server.accept()

print(f"Connection from {address} has been established.")

book_name = clientsocket.recv(128).decode('utf-8')

print("book name : ",book_name)

# t1 = threading.Thread(target=client_handler,
#     args=(clientsocket,)
# )

# t1.start()

client_handler(clientsocket)

    



