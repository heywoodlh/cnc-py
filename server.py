#!/usr/bin/env python3
import socket

host_port = '1776'

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('', int(host_port)))
serversocket.listen(5) # become a server socket, maximum 5 connections

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    if len(buf) > 0:
        buf = buf.decode('utf-8')
        print(buf)
