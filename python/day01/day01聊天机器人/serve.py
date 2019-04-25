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
