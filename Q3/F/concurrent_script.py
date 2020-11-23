import multiprocessing
import subprocess

def worker(file):
    subprocess.Popen(["python", file])


if __name__ == '__main__':
    files = ["1_client_tcp.py","2_client_tcp.py","3_client_tcp.py","4_client_tcp.py","5_client_tcp.py"]
    for file in files:
        p = multiprocessing.Process(target=worker(file))
        p.start()