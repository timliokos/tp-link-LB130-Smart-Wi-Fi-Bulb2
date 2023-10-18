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

    # create an instance of the light with its IP address 
    
    light7 = LB130("192.168.1.112")
    light8 = LB130("192.168.1.113")
    
    light10 = LB130("192.168.1.100")
    light11 = LB130("192.168.1.101")
    light12 = LB130("192.168.1.102")
    
    
    # fetch the details for the light
    

    # set the transition period for any changes to 1 seconds
    
    light7.transition_period = 0
    light8.transition_period = 0
    
    light10.transition_period = 0
    light11.transition_period = 0
    light12.transition_period = 0
    
    

    # set the brightness to 50%
    
    light7.brightness = 50
    light8.brightness = 50
    
    light10.brightness = 50
    light11.brightness = 50
    light12.brightness = 50
    
    time.sleep(1)

    # set the saturation to 100%
    
    light7.saturation = 90
    light8.saturation = 90
    
    light10.saturation = 90
    light11.saturation = 90
    light12.saturation = 90
    
    time.sleep(1)
    

    # cycle through the colours
    
    light7.hue = 0
    light8.hue = 240
    
    light10.hue = 240
    light11.hue = 0
    light12.hue = 240
    
    
    time.sleep(0.5)

    
    light7.hue = 240
    light8.hue = 0
    
    light10.hue = 0
    light11.hue = 240
    light12.hue = 0
    

    time.sleep(0.5)

    
    light7.hue = 0
    light8.hue = 240
    
    light10.hue = 240
    light11.hue = 0
    light12.hue = 240
    
    
    time.sleep(0.5)

    
    light7.hue = 240
    light8.hue = 0
    
    light10.hue = 0
    light11.hue = 240
    light12.hue = 0
    

    time.sleep(0.5)
    
    
    light7.hue = 0
    light8.hue = 240
    
    light10.hue = 240
    light11.hue = 0
    light12.hue = 240
    
    
    time.sleep(0.5)

    
    light7.hue = 240
    light8.hue = 0
    
    light10.hue = 0
    light11.hue = 240
    light12.hue = 0
    

    time.sleep(0.5)

    
    light7.hue = 0
    light8.hue = 240
    
    light10.hue = 240
    light11.hue = 0
    light12.hue = 240
    
    
    time.sleep(0.5)

    
    light7.hue = 240
    light8.hue = 0
    
    light10.hue = 0
    light11.hue = 240
    light12.hue = 0
    

    time.sleep(0.5)

   
    light7.hue = 0
    light8.hue = 240
    
    light10.hue = 240
    light11.hue = 0
    light12.hue = 240
  

    time.sleep(0.5)
    

   

    # set the colour to warm white and the brightness to 0
    light7.temperature = 6000
    #light2.temperature = 6000

    light7.hue = 240
    #light.brightness = 0
    #light2.brightness = 0
    


   
  
    

if __name__ == "__main__":
    main()
