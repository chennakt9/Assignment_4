import socket
import time
import os


start_time = time.time()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 12345))


books = ["test1","text2","text3","text4","text5"]

for book_name in books:
    
    client.send(bytes(book_name,"utf-8"))

    file = open(f"{book_name}TCP{os.getpid()}.txt", 'w', encoding = 'utf-8')

    while True:
        data = client.recv(2**17)
        if len(data) <= 0:
            break

        # print(data)
        dcdmsg = data.decode("utf-8", "ignore")


        
        file.write(dcdmsg)

    client.close()

    end_time = time.time()

    time_diff = end_time - start_time

    print(f"{book_name} => time diff in seconds : {round(time_diff,2)} s")



