# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 22:06:31 2015

@author: RedSpiderMkV
"""

import subprocess

class NetworkFailTester:
    '''Network fail tester class - test network connectivity.'''
    def __init__(self, hostIp):
        '''Initiliase object with hostIp to test connectivity with.'''
        self.hostIp = hostIp
        
    def TestNetwork(self):
        '''Ping ip address and return if it was successful.'''
        response = subprocess.call("ping -n 1 -w 2 " + self.hostIp,\
            stdout=subprocess.PIPE)
        return response
