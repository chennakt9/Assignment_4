import socket
import time
import os


start_time = time.time()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 12345))



file  = open('Downloads/test.txt', 'w')

while True:
    data = client.recv(2**17)
    if len(data) <= 0:
        break

    # print(data)
    dcdmsg = data.decode("utf-8", "ignore")

    print(len(dcdmsg))
    
    file.write(dcdmsg)

client.close()

end_time = time.time()

time_diff = end_time - start_time

print(f"time diff in seconds : {round(time_diff,2)} s")



