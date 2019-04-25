
### TCP:面向连接的协议

TCP把连接作为最基本的对象，每一条TCP连接都有两个端点，这种断点我们叫作套接字（socket），它的定义为端口号拼接到IP地址即构成了套接字，例如，若IP地址为192.3.4.16 而端口号为80，那么得到的套接字为192.3.4.16:80。
> 三次握手  
> 1.最开始的时候客户端和服务器都是处于CLOSED状态。主动打开连接的为客户端，被动打开连接的是服务器。  
> TCP服务器进程先创建传输控制块TCB，时刻准备接受客户进程的连接请求，此时服务器就进入了LISTEN（监听）状态；  
> 2.TCP客户进程也是先创建传输控制块TCB，然后向服务器发出连接请求报文，这是报文首部中的同部位SYN=1，同时选择一个初始序列号 seq=x ，此时，TCP客户端进程进入了 SYN-SENT（同步已发送状态）状态。TCP规定，SYN报文段（SYN=1的报文段）不能携带数据，但需要消耗掉一个序号。  
> 3.TCP服务器收到请求报文后，如果同意连接，则发出确认报文。确认报文中应该 ACK=1，SYN=1，确认号是ack=x+1，同时也要为自己初始化一个序列号 seq=y，此时，TCP服务器进程进入了SYN-RCVD（同步收到）状态。这个报文也不能携带数据，但是同样要消耗一个序号。  
> 4.TCP客户进程收到确认后，还要向服务器给出确认。确认报文的ACK=1，ack=y+1，自己的序列号seq=x+1，此时，TCP连接建立，客户端进入ESTABLISHED（已建立连接）状态。TCP规定，ACK报文段可以携带数据，但是如果不携带数据则不消耗序号。  
> 5.当服务器收到客户端的确认后也进入ESTABLISHED状态，此后双方就可以开始通信了。  


### 架构
C/S 
B/S 轻量 不需要更新

### socket编程

ipv6和ipv4

### 案例：聊天机器人
> 分析：需要一个服务器文件和客户机文件。服务器文件用来模拟服务器，实例化socket对象，并且接收客户机发送过来的内容。还可以连接图灵机器人api接口，从而达到聊天目的。客户机文件主要进行连接服务器，发送数据，接收服务器返回的数据。

- serve.py

```python
import socket
import requests,json
# 实例化socket对象
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# # 参数一
# socket.AF_INET ipv4
# socket.AF_INET ipv6
# # 参数二
# socke.SOCK_STREAM TCP协议 （面向连接）特点：效率要求不高，但是安全可靠性高  打电话，收发文件
# socket.SOCK_DGRAM UDP协议 （面向无连接） 特点：效率要求高，内容要求不高  直播，语音

ip_port = ("127.0.0.1",9000) # 元组 127.0.0.1代表本地 5000以下的接口已经被占据
sk.bind(ip_port)  # 绑定端口号与ip地址 不绑定是随机的，创建客户端会找不到服务器
print("开始监听")
sk.listen(5)     # 监听5个请求，类似进程池
print("accept")
conn,addr = sk.accept()  # 响应请求队列 返回元组 （con,addr）(连接，地址)
print("接收内容。。。")

# 服务器接收客户机发送的数据后返回一个数据
def getInfo(text):
    url = "http://openapi.tuling123.com/openapi/api/v2"
    data = {
        "reqType":0,
        "perception": {
            "inputText": {
                "text": "%s"%text
            }
        },
        # 只需要修改这里的值 在自己的图灵机器人找
        "userInfo": {
            "apiKey": "bcfc041d96c44144a4f0fd77ed46b6e2",
            "userId": "79296a03be075466"
        }
    }
    data = json.dumps(data)
    res = requests.post(url=url,data=data,headers={
        'content-type':'application/json'
    })
    res = json.loads(res.text)
    res2 = res['results'][0]['values']['text']
    return res2


while True:
    data = conn.recv(1024).decode()
    text = getInfo(data)
    print(data)
    conn.send(text.encode())
```
- client.py
```python
import socket

sk = socket.socket()

ip_port = ("127.0.0.1",9000)

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
```