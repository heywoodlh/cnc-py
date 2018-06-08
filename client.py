#!/usr/bin/env python3
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

def connect_to_server(server, port):
    global clientsocket
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((server, int(port)))
    conn_status = 'conn established'
    conn_status = do_encrypt(conn_status)
    return(conn_status)

def send_message(clientsocket, message):
    clientsocket.send(message)


def main(server, port):
    connection_status = connect_to_server(server, port)
    send_message(clientsocket, connection_status)


if __name__ == '__main__':
    main(host_server, host_port)
