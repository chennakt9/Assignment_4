import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



server.bind((socket.gethostname(), 12345))



server.listen(1)


BUFFER_SIZE = 32


print("Listening for connections ...")


clientsocket, address = server.accept()

print(f"Connection from {address} has been established.")


while True:

    book_name = clientsocket.recv(128).decode('utf-8')

    if not book_name:
        break

    print("book name : ",book_name)

    file = open(f'../../Texts/{book_name}.txt', 'r', encoding="utf-8")

    while True:


        data = file.read(BUFFER_SIZE)
        

        if not data:
            clientsocket.send( bytes("end_","utf-8"))
            print("kk")
            file.close()
            break
        clientsocket.send( bytes(data,"utf-8"))


clientsocket.close()
    

        
        

    



