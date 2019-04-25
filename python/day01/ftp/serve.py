import socket,threading
import os

# ftp 文件传输协议 可以进行文件操作

ip_port = ("127.0.0.1",8000)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

def main(conn,addr):
    while True:
        commend = conn.recv(1024).decode()
        # list = os.chdir(r"C:\Users\Champion\AppData")

        print(commend)
while True:
    conn,addr = sk.accept()
    t = threading.Thread(target=main,args=(conn,addr))
    t.start()