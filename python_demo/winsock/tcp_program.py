import socket

print('''---------------------TCP编程---------------------
''')
# Socket是网络编程的一个抽象概念。通常我们用一个Socket表示“打开了一个网络链接”，
# 而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可。

# *********** 客户端 ***********
# 1.导入socket库:
#
# 2.创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3.建立连接:
s.connect(('www.sina.com.cn', 80))
# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
print("data=", data)
header, html = data.split(b'\r\n\r\n', 1)
print("\nheader", header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)
# 接收数据时，调用recv(max)方法，一次最多接收指定的字节数，
# 因此，在一个while循环中反复接收，直到recv()返回空数据，表示接收完毕，退出循环。
#
# 当我们接收完数据后，调用close()方法关闭Socket，这样，一次完整的网络通信就结束了：
# 关闭连接:
s.close()

# 小结
# 用TCP协议进行Socket编程在Python中十分简单，对于客户端，要主动连接服务器的IP和指定端口，
# 对于服务器，要首先监听指定端口，然后，对每一个新的连接，创建一个线程或进程来处理。
# 通常，服务器程序会无限运行下去。
#
# 同一个端口，被一个Socket绑定了以后，就不能被别的Socket绑定了。