import socket
import time
import os




book_name = "text3"

conn_start = time.time()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 12345))
conn_end = time.time()

conn_time = conn_end - conn_start

client.send(bytes(book_name,"utf-8"))

dwnld_start = time.time()
filename = f"Downloads/{book_name}TCP{os.getpid()}.txt"
os.makedirs(os.path.dirname(filename), exist_ok=True)
file = open(filename, 'w', encoding = 'utf-8')

while True:
    data = client.recv(2**17)
    if len(data) <= 0:
        break

    dcdmsg = data.decode("utf-8", "ignore")


    
    file.write(dcdmsg)
    
file.close()
dwnld_end = time.time()


client.close()


dwnld_time = round(dwnld_end - dwnld_start,2)

print("\n ---  Download time setup times --- ")
s = os.path.getsize(f"../../../Texts/{book_name}.txt")
print(f"{book_name} => : {dwnld_time} s : throughput : {(s/(2**20))/dwnld_time} MBps")




print("\n ---  Connection setup time --- ")

print(f"{book_name} => : {conn_time} s")

    
