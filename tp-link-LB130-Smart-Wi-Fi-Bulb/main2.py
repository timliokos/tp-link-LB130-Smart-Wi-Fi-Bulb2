import time
from tplight import LB130
import threading
import colorsys

def smoothColorTransition(start_color, end_color, steps):
    start_hue, start_saturation, start_value = colorsys.rgb_to_hsv(*start_color)
    end_hue, end_saturation, end_value = colorsys.rgb_to_hsv(*end_color)
    
    hue_step = (end_hue - start_hue) / steps
    saturation_step = (end_saturation - start_saturation) / steps
    value_step = (end_value - start_value) / steps
    
    for i in range(steps):
        hue = start_hue + i * hue_step
        saturation = start_saturation + i * saturation_step
        value = start_value + i * value_step
        yield colorsys.hsv_to_rgb(hue, saturation, value)

def controlBulbs_parallel(bulb_ips): 
    threads = []

    for bulb_ip in bulb_ips:
        thread = threading.Thread(target=controlBulbs, args=(bulb_ips,))  # Pass the entire list as a single argument
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
        
def controlBulbs(bulb_ips):
    while True:
        try:
            for color in smoothColorTransition((0, 0, 1), (1, 0, 0), 36):
                for bulb_ip in bulb_ips:
                    try:
                        light = LB130(bulb_ip)
                        light.transition_period = 1

                        hue, saturation, brightness = colorsys.rgb_to_hsv(*color)

                        light.hue = int(hue * 360)
                        light.saturation = int(saturation * 100)
                        light.brightness = int(brightness * 100)

                        time.sleep(1)
                    except Exception as e:
                        print(f"Error controlling bulb at {bulb_ip}: {str(e)}")
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    
    bulb_ips = ['192.168.1.100', '192.168.1.101', '192.168.1.102', '192.168.1.103', '192.168.1.104', '192.168.1.105',
                '192.168.1.106', '192.168.1.107', '192.168.1.108', '192.168.1.109', '192.168.1.110', '192.168.1.111',
                '192.168.1.112', '192.168.1.113', '192.168.1.114']
    controlBulbs_parallel(bulb_ips)


    