import time
from tplight import LB130
import threading

bulb_ips = [ '192.168.1.100', '192.168.1.101', '192.168.1.102', '192.168.1.103', '192.168.1.104', '192.168.1.105',#
             '192.168.1.106', '192.168.1.107', '192.168.1.108', '192.168.1.109', '192.168.1.110', '192.168.1.111',
             '192.168.1.112', '192.168.1.113', '192.168.1.114', ]
colors = [0,1]
current_color = 0
flashing = False

def sfcl():
    global flashing
    if not flashing:
        flashing = True
        flashing_thread = threading.Thread(target=runChristmas)
        flashing_thread.start()
        

def runChristmas(): 
    global flashing, current_color
    while flashing:
        threads = []

        for idx, bulb_ip in enumerate(bulb_ips):
            thread = threading.Thread(target=effectChristmas, args=(bulb_ip, idx))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
            
        current_color = 1 - current_color
        time.sleep(0.5)
        

def effectChristmas(bulb_ip, idx):
    
        try:
            light = LB130(bulb_ips)
            light.transition_period = 0

            if idx % 2 == current_color:
                light.hue = 0
            else:
                light.hue = 120

            light.brightness = 10
            light.saturation = 90
            
        except Exception as e:
            print(f"Error controlling bulb at {bulb_ips}: {str(e)}")
            

def runPolice(bulb_ips): 
    threads = []

    for bulb_ip in bulb_ips:
        thread = threading.Thread(target=effectPolice, args=(bulb_ip,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

 
def effectPolice(bulb_ips):
    for bulb_ip in bulb_ips:
        try:
            light = LB130(bulb_ips)
            #light.transition_period = 0

            light.hue = 0
            time.sleep(0)
            light.brightness = 10
            time.sleep(0)
            light.saturation = 90
            time.sleep(0.3)
            light.hue = 240
            time.sleep(0.3)
            light.hue = 0
            time.sleep(0.3)
            light.hue = 240
            time.sleep(0.3)
            light.hue = 0
            time.sleep(0.3)
            light.hue = 240
            time.sleep(0.3)
            light.hue = 0
            time.sleep(0.3)
            light.hue = 240
            time.sleep(0.3)
            light.hue = 0
            time.sleep(0.3)
            light.hue = 240
            time.sleep(0.3)
            light.hue = 0
            time.sleep(0.3)
            light.hue = 240
            time.sleep(0.3)
            light.hue = 0
            time.sleep(0.3)
            
        except Exception as e:
            print(f"Error controlling bulb at {bulb_ips}: {str(e)}")        


def runHazards(bulb_ips): 
    threads = []

    for bulb_ip in bulb_ips:
        thread = threading.Thread(target=effectHazards, args=(bulb_ip,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

 
def effectHazards(bulb_ips):
    for bulb_ip in bulb_ips:
        try:
            light = LB130(bulb_ips)
            #light.transition_period = 0

            light.hsb = (0,0,0)
            time.sleep(0.9)
            light.hsb = (30,90,75)
            time.sleep(0.9)
            light.hsb = (0,0,0)
            time.sleep(0.9)
            light.hsb = (30,90,75)
            time.sleep(0.9)
            light.hsb = (0,0,0)
            time.sleep(0.9)
            light.hsb = (30,90,75)
            time.sleep(0.9)
            light.hsb = (0,0,0)
            time.sleep(0.9)
            light.hsb = (30,90,75)
            time.sleep(0.9)
            light.hsb = (0,0,0)
            time.sleep(0.9)
            light.hsb = (30,90,75)
            time.sleep(0.9)
            light.hsb = (0,0,0)
            time.sleep(0.9)
            light.hsb = (30,90,75)
            time.sleep(0.9)
            light.hsb = (0,0,0)
            time.sleep(0.9)
            light.hsb = (30,90,75)
            time.sleep(0.9)
            light.hsb = (0,0,0)
            time.sleep(0.9)
            
        except Exception as e:
            print(f"Error controlling bulb at {bulb_ips}: {str(e)}") 


def runMerrygo(bulb_ips): 

    
    threads = []

    for bulb_ip in bulb_ips:
        thread = threading.Thread(target=effectMerrygo, args=(bulb_ip,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

 
def effectMerrygo(bulb_ips):
    bulb_ips = [ '192.168.1.100', '192.168.1.101', '192.168.1.102', '192.168.1.103', '192.168.1.104', '192.168.1.105',#
             '192.168.1.106', '192.168.1.107', '192.168.1.108', '192.168.1.109', '192.168.1.110', '192.168.1.111',
             '192.168.1.112', '192.168.1.113', '192.168.1.114', ]
    n = 0
    for bulb_ip in bulb_ips:
        try:    
            light = LB130(bulb_ips[n])  # Pass the individual IP address to the constructor
            light.hsb = (300, 50, 50)
            time.sleep(0.2)
            light.hsb = (0, 0, 0)
            time.sleep(0)
            n += 1
        except Exception as e:
            print(f"Error controlling bulb at {bulb_ip}: {str(e)}")
        

if __name__ == "__main__":
    
    bulb_ips = [ '192.168.1.100', '192.168.1.101', '192.168.1.102', '192.168.1.103', '192.168.1.104', '192.168.1.105',#
             '192.168.1.106', '192.168.1.107', '192.168.1.108', '192.168.1.109', '192.168.1.110', '192.168.1.111',
             '192.168.1.112', '192.168.1.113', '192.168.1.114', ]
    sfcl()
    