#!/usr/bin/env python3
import socket

host_server = 'localhost'
host_port = '1776'

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((host_server, int(host_port)))
conn_status = 'connection established'
clientsocket.send(conn_status.encode('utf-8'))