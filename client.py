#!/usr/bin/env python3
import sys
import socket
from Crypto.Cipher import AES

host_server = 'localhost'
host_port = '1776'
aes_key = '8ZT%a*SJxTD*f6#8C6BfpHmf#DcE5^qH'
aes_iv = 'sPqapxT*4vZXjZ$w'


def do_encrypt(message):
    obj = AES.new(aes_key, AES.MODE_CBC, aes_iv)
    ciphertext = obj.encrypt(message)
    return(ciphertext)

def send_message(clientsocket, message):
    conn_status = do_encrypt(conn_status)
    clientsocket.send(message)

def connect_to_server(server, port):
    global clientsocket
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((server, int(port)))
    conn_status = 'conn established'
    send_message(clientsocket, conn_status)
    return(clientsocket)

def check_os():
    if sys.platform == "linux" or sys.platform == "linux2":
        current_os = 'linux'
    elif sys.platform == "darwin":
        current_os = 'macOS'
    elif sys.platform == "win32":
        current_os = 'windows'
    else:
        current_os = 'other'
    return(current_os)


def main(server, port):
    clientsocket = connect_to_server(server, port)
    operating_system = check_os()


if __name__ == '__main__':
    main(host_server, host_port)
