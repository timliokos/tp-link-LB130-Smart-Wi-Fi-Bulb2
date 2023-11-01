import time
from tplight import LB130
import threading

# Light Bulbs '192.168.1.100', '192.168.1.101', '192.168.1.102', '192.168.1.103', '192.168.1.104', '192.168.1.105',#
#             '192.168.1.106', '192.168.1.107', '192.168.1.108', '192.168.1.109', '192.168.1.110', '192.168.1.111',
#             '192.168.1.112', '192.168.1.113', '192.168.1.114',

def controlBulbs_parallel(bulb_ips): 
    threads = []

    for bulb_ip in bulb_ips:
        thread = threading.Thread(target=controlBulbs, args=(bulb_ip,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
        
def controlBulbs(bulb_ips):
     for bulb_ip in bulb_ips:
        try:
            light = LB130(bulb_ips)
            
            light.transition_period = 0

            #set brightness
            light.brightness = 20
            time.sleep(0)
            
            #setsaturation
            light.saturation = 90
            time.sleep(0)

            for hue in range(0, 360, 1, ):  # Cycle through hues in increments of 10
                light.hue = hue
                time.sleep(0.01)
            
        except Exception as e:
            print(f"Error controlling bulb at {bulb_ips}: {str(e)}")

    
if __name__ == "__main__":
    
    bulb_ips = [ '192.168.1.100', '192.168.1.101', '192.168.1.102', '192.168.1.103', '192.168.1.104', '192.168.1.105',#
             '192.168.1.106', '192.168.1.107', '192.168.1.108', '192.168.1.109', '192.168.1.110', '192.168.1.111',
             '192.168.1.112', '192.168.1.113', '192.168.1.114', ]
    controlBulbs_parallel(bulb_ips)
    