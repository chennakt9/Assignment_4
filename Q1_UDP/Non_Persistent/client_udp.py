import socket
import os
import time

books = ["text1", "text2", "text3" , "text4", "text5"]


conn_times = {}
dwnld_times = {}

for book_name in books:


    conn_start = time.time()
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect((socket.gethostname(), 12345))
    conn_end = time.time()

    conn_times[book_name] = conn_end - conn_start

    client.sendto(bytes(book_name,"utf-8"), (socket.gethostname(), 12345))


    dwnld_start = time.time()

    filename = f"Downloads/{book_name}UDP{os.getpid()}.txt"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    file = open(filename, 'w', encoding = 'utf-8')


    while True:
        data,server_address = client.recvfrom(2**18)

        dcd_dada = data.decode("utf-8","ignore")

        if dcd_dada=="__stop":
            break
        else:
            file.write(dcd_dada)


    file.close()
    dwnld_end = time.time()

    client.close()

    dwnld_times[book_name] = dwnld_end - dwnld_start




print(" ---  Download time & Throughput --- ")
for book in dwnld_times:
    
    t = round(dwnld_times[book],2)
    s = os.path.getsize(f"../../Texts/{book}.txt")
    print(f"{book} => : {t} s : throughput : {(s/(2**20))/t} MBps")


print("\n ---  Connection setup times --- ")

for book in conn_times:
    print(f"{book} => : {conn_times[book]} s")