import socket
import os
import psutil

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((socket.gethostname(), 12345))



buffer_size = 32


p = psutil.Process(os.getpid())

con = p.connections()[0]

print(f"\n\nServer address : {con.laddr} \n\n")


while True:

    book_name, client_address = server.recvfrom(1024)
    book_name = book_name.decode('utf-8')

    print(f"Client address : {client_address}")



    file = open(f'../../Texts/{book_name}.txt', 'r', encoding="utf-8")

    while True:

        data = file.read(buffer_size)

        # print(data)

        if not data:
            server.sendto( bytes("__stop","utf-8") , client_address)
            file.close()
            break
        
        server.sendto( bytes(data,"utf-8") , client_address)



