#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Demo for the TP-Link A19-LB130 RBGW WiFi bulb
'''

import time
from tplight import LB130

light_names = []  # Initialize an empty list to store light names
ip_addresses = []  # Initialize an empty list to store IP addresses

def get_light_information():


    
    # Open the file in read mode
    with open("database.txt", "r") as f:
        # Read each line from the file
        for line in f:
            # Split the line into light name and IP address using comma as the separator
            light_name, ip_address = line.strip().split(',')

            # Append the light name and IP address to their respective lists
            light_names.append(light_name)
            ip_addresses.append(ip_address)

    # Return the lists containing light information
    return light_names, ip_addresses

        
    # Open the file in write mode to overwrite the content
    #with open("demofile.txt", "w") as f:
        # Write the content back to the file
        #for i in range(len(light_names)):
            #f.write(f"{light_names[i]},{ip_addresses[i]}\n")
        
    #print("File overwritten successfully.")
    
    
    
if __name__ == "__main__":
    light_names, ip_addresses = get_light_information()
    print("Light Names:", light_names)
    print("IP Addresses:", ip_addresses)
    print("Number of Lines in the Array:", len(light_names))