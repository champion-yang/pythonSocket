import socket

# 实例化socket对象
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# # 参数一
# socket.AF_INET ipv4
# socket.AF_INET ipv6
# # 参数二
# socke.SOCK_STREAM TCP协议 （面向连接）特点：效率要求不高，但是安全可靠性高  打电话，收发文件
# socket.SOCK_DGRAM UDP协议 （面向无连接） 特点：效率要求高，内容要求不高  直播，语音

ip_port = ("127.0.0.1",9000) # 元组 127.0.0.1代表本地 5000以下的电脑自己定义的
sk.bind(ip_port)  # 绑定端口号与ip地址 不绑定是随机的，创建客户端会找不到服务器
print("开始监听")
sk.listen(5)     # 监听5个请求，类似进程池
print("accept")
conn,addr = sk.accept()  # 响应请求队列 返回元组 （con,addr）(连接，地址)
print("接收内容。。。")
data = conn.recv(1024).decode() # 接收内容并解码
print(data)
sk.close()