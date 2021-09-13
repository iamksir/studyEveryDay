from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread

def main():

    class FileTransferHandler(Thread):

        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):
            my_dict = {}
            my_dict['filename'] = '1c099a8b6900b2c.png'
            my_dict['filedata'] = data
            json_str = dumps(my_dict)
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()


    server = socket()
    server.bind(('127.0.0.1', 5566))
    server.listen(512)
    print('服务器启动开始监听...')
    with open('../file/1c099a8b6900b2c.png', 'rb') as f:
        # 将二进制数据处理成base64再解码成字符串
        data = b64encode(f.read()).decode('utf-8')
    while True:
        # accept方法返回一个元组其中的第一个元素是客户端对象
        client, addr = server.accept()
        print(str(addr)+ '连接到了服务器')
        # 启动一个线程处理客户端的请求
        FileTransferHandler(client).start()

if __name__ == "__main__":
    main()