import time
from tplight import LB130
import threading
import librosa
import random
import pygame

def getbpm(selected_song):

    # get tempo of song
    y, sr = librosa.load(selected_song)
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    
    # convert tempo to seconds
    bps = 60 / tempo
    
    return bps

def runTempo(bps): 
    bulb_ips = ['192.168.1.100', '192.168.1.101', '192.168.1.102', '192.168.1.103', '192.168.1.104', '192.168.1.105',#
             '192.168.1.106', '192.168.1.107', '192.168.1.108', '192.168.1.109', '192.168.1.110', '192.168.1.111',
             '192.168.1.112', '192.168.1.113', '192.168.1.114']
    
    threads = []

    for bulb_ip in bulb_ips:
        thread = threading.Thread(target=tempo_effects, args=(bulb_ip, bps))
        threads.append(thread)
        
    for thread in threads:
        thread.start()
        
    for thread in threads:
        thread.join()    
        

def tempo_effects(bulb_ips, bps):
      
    light = LB130(bulb_ips)
  
    # while a song is playing 
    while pygame.mixer.music.get_busy():
        # Create a variable to change hue to a random integer 0-360
        random_hue = random.randint(0, 360)
        # Set the hue of the light.
        light.hue = random_hue
        time.sleep(bps)
        light.hue = random_hue
        time.sleep(bps)
    
def runChristmas(bulb_ips): 
    threads = []

    for bulb_ip in bulb_ips:
        thread = threading.Thread(target=effectChristmas, args=(bulb_ip,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
        

def effectChristmas(bulb_ips):
    for bulb_ip in bulb_ips:
        try:
            light = LB130(bulb_ips)
            light.transition_period = 0

            light.hue = 0
            time.sleep(0)
            light.brightness = 10
            time.sleep(0)
            light.saturation = 90
            time.sleep(0.75)
            light.hue = 120
            time.sleep(0.75)
            light.hue = 0
            time.sleep(0.75)
                  

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
    runChristmas(bulb_ips)
    