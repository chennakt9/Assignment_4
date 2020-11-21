import socket
import time
import os




books = ["text1","text2","text3","text4","text5"]

conn_times = {}
dwnld_times = {}


conn_start = time.time()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 12345))    
conn_end = time.time()

print("\n ---  Connection setup time --- ")

print(f"conn time : {conn_end - conn_start}")

for book_name in books:
    


    client.send(bytes(book_name,"utf-8"))
    print(book_name)
    dwnld_start = time.time()
    filename = f"Downloads/{book_name}TCP{os.getpid()}.txt"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    file = open(filename, 'w', encoding = 'utf-8')

    while True:
        data = client.recv(2**17)
        
        # print(data)
        dcdmsg = data.decode("utf-8", "ignore")

        if dcdmsg=="end_":
            print("hi")
            break


        
        file.write(dcdmsg)
    file.close()
    

    dwnld_end = time.time()



    dwnld_times[book_name] = dwnld_end - dwnld_start

    
client.close()

print(" ---  Download time & Throughput --- ")
for book in dwnld_times:
    
    t = round(dwnld_times[book],2)
    s = os.path.getsize(f"../../Texts/{book}.txt")
    print(f"{book} => : {t} s : throughput : {(s/1024)/t} MBps")



