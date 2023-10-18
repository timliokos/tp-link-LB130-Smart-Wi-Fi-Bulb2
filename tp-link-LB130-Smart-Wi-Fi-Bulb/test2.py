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
        light.transition_period = 0
        light.brightness = 50
        light.saturation = 90
    
    time.sleep(1)
    
    # Cycle through the colors
    for i in range(2):
        for light in lights:
            light.hue = 180 if i % 2 == 0 else 60
        time.sleep(0.5)
    
    # Set the color to warm white and brightness to 0 for the first light
    lights[0].temperature = 6000
    lights[0].hue = 240
    # lights[0].brightness = 0
    
if __name__ == "__main__":
    main()