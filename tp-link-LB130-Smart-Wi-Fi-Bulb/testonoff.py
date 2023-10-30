#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Demo for the TP-Link A19-LB130 RBGW WiFi bulb
'''

import time
from tplight import LB130

def main():
    '''
    Main program function
    '''
    # Define the IP addresses of the lights
    ip_addresses = [
        "192.168.1.106", "192.168.1.107", "192.168.1.108", "192.168.1.109",
        "192.168.1.110", "192.168.1.111", "192.168.1.112", "192.168.1.113",
        "192.168.1.114", "192.168.1.100", "192.168.1.101", "192.168.1.102",
        "192.168.1.103", "192.168.1.104", "192.168.1.105"
    ]
    
    # Create a list of light instances
    lights = [LB130(ip) for ip in ip_addresses]
    
    # Set common properties for all lights
    for light in lights:
        
        light.off()
        
    time.sleep(0)
    
    
    
    
if __name__ == "__main__":
    main()