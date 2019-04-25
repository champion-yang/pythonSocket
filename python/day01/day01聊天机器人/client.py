import socket

sk = socket.socket()

ip_port = ("192.168.32.101",8000)

try:
    # 建立连接
    sk.connect(ip_port)
except:
    print("服务器未开启")

while True:
    data = input(">").encode()
    sk.send(data)
    # 接收服务器返回的数据
    res = sk.recv(1024).decode()
    print("服务器:%s" % res)
