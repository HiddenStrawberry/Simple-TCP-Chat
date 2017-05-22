# encoding=utf8
from socket import *
import threading
import time
import multiprocessing


def client(ip, port):
    while True:
        try:
            HOST = ip
            PORT = port
            ADDR = (HOST, PORT)
            tcpCliSock = socket(AF_INET, SOCK_STREAM)
            tcpCliSock.connect(ADDR)
            sendmsg(tcpCliSock)
            tcpCliSock.close()
        except:
            tcpCliSock.close()
            time.sleep(5)


def sendmsg(tcpCliSock):
    status = 1
    while True and status == 1:
        data = raw_input('> ')
        if not data:
            break
        tcpCliSock.send(data)
        if data == 'close':
            status = 0
            break


def server(port):
    while True:
        try:
            HOST = ''
            PORT = port
            BUFSIZ = 1024
            ADDRT = (HOST, PORT)
            tcpSerSock = socket(AF_INET, SOCK_STREAM)
            tcpSerSock.bind(ADDRT)
            tcpSerSock.listen(5)
            while True:
                print 'Waiting for connection'
                tcpClient, addrt = tcpSerSock.accept()
                print '...Connected from:', addrt
                while True:
                    try:
                        data_send = tcpClient.recv(BUFSIZ)
                        if not data_send:
                            break
                        if data_send:
                            print data_send
                        if data_send == 'close':
                            tcpClient.close()
                    except:
                        tcpClient.close()
            tcpSerSock.close()
        except:
            tcpSerSock.close()
            time.sleep(5)


def start_server(port):
    multiprocessing.Process(target=server, args=(port,)).start()


def start_client(ip, port):
    threading.Thread(target=client, args=(ip, port,)).start()


if __name__ == '__main__':
    start_server(8081)
    start_client('192.168.2.1', 1234)
