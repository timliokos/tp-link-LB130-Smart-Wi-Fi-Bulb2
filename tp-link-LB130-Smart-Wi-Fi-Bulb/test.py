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
    light = LB130("192.168.1.100")
    light2 = LB130("192.168.1.101")
    light3 = LB130("192.168.1.102")
    light4 = LB130("192.168.1.103")
    light5 = LB130("192.168.1.104")
    light6 = LB130("192.168.1.105")
    light7 = LB130("192.168.1.106")
    light8 = LB130("192.168.1.107")
    light9 = LB130("192.168.1.108")
    light10 = LB130("192.168.1.109")
    light11 = LB130("192.168.1.110")
    light12 = LB130("192.168.1.111")
    light13 = LB130("192.168.1.112")
    light14 = LB130("192.168.1.113")
    light15 = LB130("192.168.1.114")
    
    # fetch the details for the light
    

    # set the transition period for any changes to 1 seconds
    light.transition_period = 0
    light2.transition_period = 0
    light3.transition_period = 0
    light4.transition_period = 0
    light5.transition_period = 0
    light6.transition_period = 0
    light7.transition_period = 0
    light8.transition_period = 0
    light9.transition_period = 0
    light10.transition_period = 0
    light11.transition_period = 0
    light12.transition_period = 0
    light13.transition_period = 0
    light14.transition_period = 0
    light15.transition_period = 0
    

    # set the brightness to 50%
    light.brightness = 50
    light2.brightness = 50
    light3.brightness = 50
    light4.brightness = 50
    light5.brightness = 50
    light6.brightness = 50
    light7.brightness = 50
    light8.brightness = 50
    light9.brightness = 50
    light10.brightness = 50
    light11.brightness = 50
    light12.brightness = 50
    light13.brightness = 50
    light14.brightness = 50
    light15.brightness = 50
    time.sleep(1)

    # set the saturation to 100%
    light.saturation = 90
    light2.saturation = 90
    light3.saturation = 90
    light4.saturation = 90
    light5.saturation = 90
    light6.saturation = 90
    light7.saturation = 90
    light8.saturation = 90
    light9.saturation = 90
    light10.saturation = 90
    light11.saturation = 90
    light12.saturation = 90
    light13.saturation = 90
    light14.saturation = 90
    light15.saturation = 90
    time.sleep(1)
    

    # cycle through the colours
    light.hue = 0
    light2.hue = 240
    light3.hue = 0
    light4.hue = 240
    light5.hue = 0
    light6.hue = 240
    light7.hue = 0
    light8.hue = 240
    light9.hue = 0
    light10.hue = 240
    light11.hue = 0
    light12.hue = 240
    light13.hue = 0
    light14.hue = 240
    light15.hue = 0
    
    time.sleep(0.5)

    light.hue = 240
    light2.hue = 0
    light3.hue = 240
    light4.hue = 0
    light5.hue = 240
    light6.hue = 0
    light7.hue = 240
    light8.hue = 0
    light9.hue = 240
    light10.hue = 0
    light11.hue = 240
    light12.hue = 0
    light13.hue = 240
    light14.hue = 0
    light15.hue = 240

    time.sleep(0.5)

    light.hue = 0
    light2.hue = 240
    light3.hue = 0
    light4.hue = 240
    light5.hue = 0
    light6.hue = 240
    light7.hue = 0
    light8.hue = 240
    light9.hue = 0
    light10.hue = 240
    light11.hue = 0
    light12.hue = 240
    light13.hue = 0
    light14.hue = 240
    light15.hue = 0
    
    time.sleep(0.5)

    light.hue = 240
    light2.hue = 0
    light3.hue = 240
    light4.hue = 0
    light5.hue = 240
    light6.hue = 0
    light7.hue = 240
    light8.hue = 0
    light9.hue = 240
    light10.hue = 0
    light11.hue = 240
    light12.hue = 0
    light13.hue = 240
    light14.hue = 0
    light15.hue = 240

    time.sleep(0.5)
    
    light.hue = 0
    light2.hue = 240
    light3.hue = 0
    light4.hue = 240
    light5.hue = 0
    light6.hue = 240
    light7.hue = 0
    light8.hue = 240
    light9.hue = 0
    light10.hue = 240
    light11.hue = 0
    light12.hue = 240
    light13.hue = 0
    light14.hue = 240
    light15.hue = 0
    
    time.sleep(0.5)

    light.hue = 240
    light2.hue = 0
    light3.hue = 240
    light4.hue = 0
    light5.hue = 240
    light6.hue = 0
    light7.hue = 240
    light8.hue = 0
    light9.hue = 240
    light10.hue = 0
    light11.hue = 240
    light12.hue = 0
    light13.hue = 240
    light14.hue = 0
    light15.hue = 240

    time.sleep(0.5)

    light.hue = 0
    light2.hue = 240
    light3.hue = 0
    light4.hue = 240
    light5.hue = 0
    light6.hue = 240
    light7.hue = 0
    light8.hue = 240
    light9.hue = 0
    light10.hue = 240
    light11.hue = 0
    light12.hue = 240
    light13.hue = 0
    light14.hue = 240
    light15.hue = 0
    
    time.sleep(0.5)

    light.hue = 240
    light2.hue = 0
    light3.hue = 240
    light4.hue = 0
    light5.hue = 240
    light6.hue = 0
    light7.hue = 240
    light8.hue = 0
    light9.hue = 240
    light10.hue = 0
    light11.hue = 240
    light12.hue = 0
    light13.hue = 240
    light14.hue = 0
    light15.hue = 240

    time.sleep(0.5)

    light.hue = 0
    light2.hue = 240
    light3.hue = 0
    light4.hue = 240
    light5.hue = 0
    light6.hue = 240
    light7.hue = 0
    light8.hue = 240
    light9.hue = 0
    light10.hue = 240
    light11.hue = 0
    light12.hue = 240
    light13.hue = 0
    light14.hue = 240
    light15.hue = 0
    
    time.sleep(0.5)

    light.hue = 240
    light2.hue = 0
    light3.hue = 240
    light4.hue = 0
    light5.hue = 240
    light6.hue = 0
    light7.hue = 240
    light8.hue = 0
    light9.hue = 240
    light10.hue = 0
    light11.hue = 240
    light12.hue = 0
    light13.hue = 240
    light14.hue = 0
    light15.hue = 240

    time.sleep(0.5)

    light.hue = 0 
    light2.hue = 240
    light3.hue = 0
    light4.hue = 240
    light5.hue = 0
    light6.hue = 240
    light7.hue = 0
    light8.hue = 240
    light9.hue = 0
    light10.hue = 240
    light11.hue = 0
    light12.hue = 240
    light13.hue = 0
    light14.hue = 240
    light15.hue = 0
    
    time.sleep(0.5)

    light.hue = 240
    light2.hue = 0
    light3.hue = 240
    light4.hue = 0
    light5.hue = 240
    light6.hue = 0
    light7.hue = 240
    light8.hue = 0
    light9.hue = 240
    light10.hue = 0
    light11.hue = 240
    light12.hue = 0
    light13.hue = 240
    light14.hue = 0
    light15.hue = 240

    time.sleep(0.5)
   

    # set the colour to warm white and the brightness to 0
    light.temperature = 6000
    #light2.temperature = 6000

    light.hue = 240
    #light.brightness = 0
    #light2.brightness = 0
    


   
  
    

if __name__ == "__main__":
    main()
