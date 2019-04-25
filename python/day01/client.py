import socket

sk = socket.socket()

ip_port = ("127.0.0.1",9000)

try:
    # 建立连接
    sk.connect(ip_port)
except:
    print("服务器未开启")

sk.send("hello socket".encode())
sk.close()