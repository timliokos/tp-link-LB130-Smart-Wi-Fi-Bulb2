import time
from tplight import LB130
import threading


def controlBulbs_parallel(bulb_ips): 
    threads = []

    for bulb_ip in bulb_ips:
        thread = threading.Thread(target=controlBulbs, args=(bulb_ip,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
        
def controlBulbs(bulb_ip):
     
    try:
        light = LB130(bulb_ip)
            
        light.transition_period = 0
        light.brightness = 50
        time.sleep(0)
        light.saturation = 90
        time.sleep(0)
        light.hue = 240
        time.sleep(1)
        light.transition_period = 0
        light.brightness = 50
        time.sleep(0)
        light.saturation = 90
        time.sleep(0)
        light.hue = 0
        time.sleep(1)
            
            
    except Exception as e:
        print(f"Error controlling bulb at {bulb_ips}: {str(e)}")

    
if __name__ == "__main__":
    
    bulb_ips = [ '192.168.1.100', '192.168.1.101', '192.168.1.102', '192.168.1.103', '192.168.1.104', '192.168.1.105',#
             '192.168.1.106', '192.168.1.107', '192.168.1.108', '192.168.1.109', '192.168.1.110', '192.168.1.111',
             '192.168.1.112', '192.168.1.113', '192.168.1.114', ]
    
    while True:
        controlBulbs_parallel(bulb_ips)
        time.sleep(60)
    