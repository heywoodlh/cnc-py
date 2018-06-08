#!/usr/bin/env python3
import socket
from Crypto.Cipher import AES

host_port = '1776'
aes_key = '8ZT%a*SJxTD*f6#8C6BfpHmf#DcE5^qH'
aes_iv = 'sPqapxT*4vZXjZ$w'

def server(port):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('', int(host_port)))
    serversocket.listen(5) # become a server socket, maximum 5 connections
    return serversocket

def do_decrypt(key, iv, ciphertext):
    obj2 = AES.new(aes_key, AES.MODE_CBC, aes_iv)
    message = obj2.decrypt(ciphertext)
    return message

def receive(key, iv, serversocket):
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    if len(buf) > 0:
        message = do_decrypt(key, iv, buf)
        message = message.decode('utf-8')
        print(message)


def main(port, key, iv):
    serversocket = server(port)
    while True:
        receive(key, iv, serversocket)

if __name__ == '__main__':
    main(host_port, aes_key, aes_iv)
