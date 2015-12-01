# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 22:33:23 2015

@author: RedSpiderMkV
"""

import os
import time
from NetworkFailTester import NetworkFailTester

def main():
    '''Test connectivity to router.
    This doesn't handle the case of a real fault with the network.
    In such case, it would restart every 5 mins... handle this somehow at
    some point.'''

    hostIp = '192.168.0.1'
    
    # 300 seconds, test every 5 mins
    timeout = 5*60
    
    failTester = NetworkFailTester(hostIp)
    
    while(True):
        time.sleep(timeout)
        responseCode = failTester.TestNetwork()
    
        if responseCode != 0:
            os.system("shutdown -r -t 0 -f")

if __name__ == "__main__":
    main()
