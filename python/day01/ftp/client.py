import socket

ip_port = ("127.0.0.1",8000)
sk = socket.socket()

try:
    sk.connect(ip_port)
except:
    print("连接异常")

while True:
    commend = input(">")

    sk.send(commend.encode())