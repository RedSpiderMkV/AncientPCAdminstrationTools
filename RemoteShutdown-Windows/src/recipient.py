# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 21:04:48 2015

@author: redspidermkv
"""

import time
import socket
import constants
import subprocess
   
class ShutdownListener:
    hostAddress = ''
    port = 0

    socketConnection = None    
    
    def __init__(self, address, port):
        self.port = port
        self.hostAddress = socket.gethostname()
        
        self.socketConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def BeginListener(self):
        self.socketConnection.bind((self.hostAddress, self.port))
        self.socketConnection.listen(5)

        print('Listener started...')
        
        while True:
            conn, addr = self.socketConnection.accept()

            command = conn.recv(1024)
            if command == constants.COMMAND:
                # run shutdown command
                subprocess.call(['shutdown', '/s', '/t', '0'])
            
            conn.send('Command receieved...')
            conn.close()

def main():
    time.sleep(120) # at some point, use a proper ping system to check when
                    # network ready instead of a dumb timer...
    shutDownListener = ShutdownListener('0.0.0.0', 1885)
    shutDownListener.BeginListener()
        
if __name__ == "__main__":
    main()
