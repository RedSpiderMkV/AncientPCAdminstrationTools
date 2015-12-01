#!/usr/bin/python

# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 21:29:45 2015

@author: redspidermkv
"""

import socket
import constants

class CommandTransmitter:
    sock = None
    host = ''
    port = 0
    
    def __init__(self, hostAddress, port):
        self.sock = socket.socket()
        self.host = hostAddress
        self.port = port
    
    def TransmitShutdown(self):
        self.sock.connect((self.host, self.port))
        self.sock.send(constants.COMMAND)
        
        print(self.sock.recv(1024))
        self.sock.close()

def main():
    #commandTransmitter = CommandTransmitter(socket.gethostname(), 1885)
    commandTransmitter = CommandTransmitter('192.168.0.15', 1885)
    commandTransmitter.TransmitShutdown()
    
if __name__ == "__main__":
    main()