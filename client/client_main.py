# 简单实现一个客户端向服务端发送一句字符串将字符串全部转大写的功能

import grpc
from example import data_pb2, data_pb2_grpc

_HOST = 'localhost'
_PORT = '8080'


def run():
    conn = grpc.insecure_channel(target=(_HOST + ':' + _PORT))  # 创建一个连接对象
    print(conn)
    client = data_pb2_grpc.FormatDataStub(channel=conn)   # 客户端使用Stub类发送请求,参数为频道,为了绑定链接
    print(client)
    response = client.DoFormat(data_pb2.actionrequest(text='hello, python!'))   # 返回的结果就是proto中定义的类
    print("received: " + response.text)


if __name__ == '__main__':
    run()
