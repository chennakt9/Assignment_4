import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# server.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY, True)  #For Disabling Nagle's Algorithm


server.bind((socket.gethostname(), 12345))



server.listen(1)


BUFFER_SIZE = 1024


print("Listening for connections ...")

# FC text2TCP8224.txt ../Texts/text2.txt

while True:

    clientsocket, address = server.accept()

    print(f"Connection from {address} has been established.")

    
    book_name = clientsocket.recv(128).decode('utf-8')

    print("book name : ",book_name)


    file = open(f'Texts/{book_name}.txt', 'r', encoding="utf-8")
    
    


    while True:

        # time.sleep(1/(10**9))

        data = file.read(BUFFER_SIZE)

        # print(data)
        

        if not data:
            file.close()
            break
        
        clientsocket.send( bytes(data,"utf-8"))
        

    clientsocket.close()