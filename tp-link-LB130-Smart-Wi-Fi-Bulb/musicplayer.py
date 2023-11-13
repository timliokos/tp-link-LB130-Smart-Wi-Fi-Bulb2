import tkinter
import tkinter.messagebox
import customtkinter
import subprocess
import time
import math
import pygame
import threading
from PIL import Image, ImageTk
from effectscode import *


# Appearance Settings
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

bulb_ips = [ '192.168.1.100', '192.168.1.101', '192.168.1.102', '192.168.1.103', '192.168.1.104', '192.168.1.105',#
                '192.168.1.106', '192.168.1.107', '192.168.1.108', '192.168.1.109', '192.168.1.110', '192.168.1.111',
                '192.168.1.112', '192.168.1.113', '192.168.1.114', ]
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configure Window
        self.title("D633 Lights/Music Management System")

        # Window Size
        self.geometry(f"{1100}x{480}")

        # Configure Grid Layout
        self.grid_columnconfigure((0, 2, 3), weight=0)
        self.grid_columnconfigure((1), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)


        # Sidebar Frame (Left)
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)

        # Logo Label
        imagesb = tkinter.PhotoImage(file="tp-link-LB130-Smart-Wi-Fi-Bulb/images/d633logosm2.png")
        new_width = 10
        new_height = 10
        resized_imagesb = imagesb.subsample(new_width, new_height)
        self.sidebar_button_sb = customtkinter.CTkButton(self.sidebar_frame, image=resized_imagesb, text="", fg_color="#212121", hover_color="#212121", width=50, height=40)
        self.sidebar_button_sb.grid(row=0, column=0, padx=0, pady=(20,20))
        self.sidebar_button_sb.icon = resized_imagesb

        # Home Button
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Home",
                                                        command=self.return_home)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        # Light Control Button
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Light Control",
                                                        command=self.open_lightcontrol)
        self.sidebar_button_3.grid(row=2, column=0, padx=20, pady=(10,10))

        # Special Effects Button
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text="Special Effects",
                                                        command=self.open_specialeffects)
        self.sidebar_button_4.grid(row=3, column=0, padx=20, pady=(10,10))

        #Add More Lights Button
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Add More Lights",
                                                        command=self.open_addmorelights)
        self.sidebar_button_2.grid(row=4, column=0, padx=20, pady=(10,135))

        # Appearance Mode (Light/Dark)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionmenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                      values=["Light", "Dark", "System"],
                                                                      command=self.change_appearance_mode_event)
        self.appearance_mode_optionmenu.grid(row=6, column=0, padx=20, pady=(0, 20))

        # Sidebar Frame (Right)
        self.sidebar_frame2 = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame2.grid(row=0, column=2, rowspan=4, sticky="nsew")
        self.sidebar_frame2.grid_rowconfigure(4, weight=1)
      
        # Close Button
        self.main_button_1 = customtkinter.CTkButton(self.sidebar_frame2, text="Close", fg_color="transparent", hover_color="#d02626",
                                                     border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=6, column=2, padx=(20, 20), pady=(5, 20), sticky="nsew")
        self.main_button_1.configure(command=self.close_window)


        # Main Frame
        self.frame = customtkinter.CTkFrame(self, width=300, corner_radius=5)
        self.frame.grid(row=0, column=1, rowspan=1, sticky="nsew")
        self.frame.grid_rowconfigure(4, weight=1)

        total_rows = self.grid_size()[1]

        middle_row = total_rows // 2

        self.frame.grid(row=1, column=1, padx=20, pady=(10,10))


        # Page Header
        image1 = tkinter.PhotoImage(file="tp-link-LB130-Smart-Wi-Fi-Bulb/images/mai.png")
        new_width = 35
        new_height = 35
        resized_image1 = image1.subsample(new_width, new_height)
        self.button_3 = customtkinter.CTkButton(self.frame, image=resized_image1, text="Music Player", fg_color="#1a1a1a", hover_color="#1a1a1a", font=customtkinter.CTkFont(size=30, weight="bold"), width=650, height=50)
        self.button_3.grid(row=1, column=1, columnspan=3, padx=(25,0), pady=(10, 10), sticky='nw')
        self.button_3.icon = resized_image1

        # Dummy label for col 0
        #self.labeld = customtkinter.CTkLabel(self.frame, text="                           ", font=customtkinter.CTkFont(size=15))
        #self.labeld.grid(row=1, column=0, padx=20, pady=(10, 10), sticky="nw")

        # Song Label
        self.doorbutton = customtkinter.CTkButton(self.frame, text="Song", fg_color="#1a1a1a", hover_color="#1a1a1a", text_color="white", font=customtkinter.CTkFont(size=12), width=240, height=20, border_width=0, border_color="white")
        self.doorbutton.grid(row=1, column=1, padx=(230,10), pady=(75,0), sticky='nw')

        # Song Menu
        self.option_menu = customtkinter.CTkOptionMenu(self.frame, values=["RFM - Trap Future Bass", "Red Skies - Laugh Now", "TFP - Happy Day"])
        self.option_menu.grid(row=1, column=1, padx=(230,10), pady=(105, 10), stick='nw')
        self.option_menu.configure(width=240, height=30, font=customtkinter.CTkFont(size=18), fg_color="#efefef", button_color="#1f538d", button_hover_color="#163b65", text_color="black")
        
        # Light Show Switch
        #self.switch_1 = customtkinter.CTkSwitch(self.frame, text="Light Show", font=customtkinter.CTkFont(size=20),
                                   #onvalue="on", offvalue="off", switch_width=65, switch_height=30, progress_color="#44dd45")
        #self.switch_1.grid(row=1, column=1,padx=(35,20), pady=(190, 70), sticky='nw')

        self.albumbutton = customtkinter.CTkButton(self.frame, text = "", fg_color="#1a1a1a", hover_color="#1a1a1a", width=185, height=185)
        self.albumbutton.grid(row=1, column=1, padx=(260,10), pady=(155,0), sticky='nw')
        
        #Progress Bar
        self.progressbar = customtkinter.CTkProgressBar(self.frame, determinate_speed=0.008, width=300)
        self.progressbar.grid(row=1, column=1, padx=(200,10), pady=(350, 10), stick='nw')

        self.progressbar.set(0)

        # Play Button
        image1 = tkinter.PhotoImage(file="tp-link-LB130-Smart-Wi-Fi-Bulb/images/newplay.png")
        new_width = 35
        new_height = 35
        resized_image1 = image1.subsample(new_width, new_height)
        self.button_3 = customtkinter.CTkButton(self.frame, image=resized_image1, text="", fg_color="#212121", hover_color="#1f538d", font=customtkinter.CTkFont(size=18), width=50, height=40, command=self.play_song)
        self.button_3.grid(row=1, column=1, padx=(20,20), pady=(380,60))
        self.button_3.icon = resized_image1

        # Pause Button
        image2 = tkinter.PhotoImage(file="tp-link-LB130-Smart-Wi-Fi-Bulb/images/newpause.png")
        new_width = 35
        new_height = 35
        resized_image2 = image2.subsample(new_width, new_height)
        self.button_4 = customtkinter.CTkButton(self.frame, image=resized_image2, text="", fg_color="#212121", hover_color="#1f538d", font=customtkinter.CTkFont(size=18), width=50, height=40, command=self.pause_song)
        self.button_4.grid(row=1, column=1, padx=(160,20), pady=(380,60))
        self.button_4.icon = resized_image2
        
        # Stop Button
        image2 = tkinter.PhotoImage(file="tp-link-LB130-Smart-Wi-Fi-Bulb/images/newstop.png")
        new_width = 35
        new_height = 35
        resized_image2 = image2.subsample(new_width, new_height)
        self.button_4 = customtkinter.CTkButton(self.frame, image=resized_image2, text="", fg_color="#212121", hover_color="#1f538d", font=customtkinter.CTkFont(size=18), width=50, height=40, command=self.stop_song)
        self.button_4.grid(row=1, column=1, padx=(300,20), pady=(380,60))
        self.button_4.icon = resized_image2

        # Default Values
        self.appearance_mode_optionmenu.set("Dark")
        self.option_menu.set("Choose a song...")
        self.music_thread = None

    # Functions

    # Change Appearance Mode
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # Change Scaling Event
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    # Close Window
    def close_window(self):
        self.destroy()

    def switch_event(self):
        print("switch toggled, current value:", switch_var.get())

    # Play Song
    def play_song(self):
        if self.music_thread and self.music_thread.is_alive():
            # Music is already playing
            return

        # Get the selected song from the option menu
        selected_song = self.option_menu.get()

        if selected_song == "Choose a song...":
            # No song is selected, do nothing
            return

        # Create a new thread to handle music playback
        self.music_thread = threading.Thread(target=self._play_music, args=(selected_song,))
        self.music_thread.start()
        
        self.progressbar.set(0)
        self.progressbar.start()
        
        
        #runPolice(bulb_ips)  
    
    # Play Selected Song From Song Map
    def _play_music(self, selected_song):   
        song_map = {
            "RFM - Trap Future Bass": "tp-link-LB130-Smart-Wi-Fi-Bulb/music/trap-future-bass.mp3",
            "Red Skies - Laugh Now": "tp-link-LB130-Smart-Wi-Fi-Bulb/music/laugh-now.mp3",
            "TFP - Happy Day": "tp-link-LB130-Smart-Wi-Fi-Bulb/music/happy-day.mp3",
            }
        if selected_song in song_map:
            pygame.mixer.init()
            pygame.mixer.music.load(song_map[selected_song])
            pygame.mixer.music.play()
            self.get_album_cover(selected_song, self.option_menu)
            
            # get tempo of song
            bps = getbpm(song_map[selected_song])
            print("Tempo= ", bps)
            
            runTempo(bps)
            
        else:
            return
        
    # Pause Song
    def pause_song(self):
        self.elapsed_time = 0
        self.playing = False
        
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.progressbar.stop()
            
    # Stop Song
    def stop_song(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.progressbar.stop()

    # Open Home Page
    def return_home(self):
        subprocess.Popen(["python", "tp-link-LB130-Smart-Wi-Fi-Bulb/homepage.py"])
        self.destroy()

    # Open Light Control Page
    def open_lightcontrol(self):
        subprocess.Popen(["python", "tp-link-LB130-Smart-Wi-Fi-Bulb/lightcontrol.py"])
        self.destroy()

    # Open Special Effects Page
    def open_specialeffects(self):
        subprocess.Popen(["python", "tp-link-LB130-Smart-Wi-Fi-Bulb/specialeffects.py"])
        self.destroy()

    # Open Add More Lights Page
    def open_addmorelights(self):
        subprocess.Popen(["python", "tp-link-LB130-Smart-Wi-Fi-Bulb/addmorelights.py"])
        self.destroy()
        
    def get_album_cover(self, song_name, option_menu):
        list_of_covers = ['tp-link-LB130-Smart-Wi-Fi-Bulb/images/trapfuturebass.jpg','tp-link-LB130-Smart-Wi-Fi-Bulb/images/laughnow.jpg','tp-link-LB130-Smart-Wi-Fi-Bulb/images/happyday.jpg']
        n=0
    
        #test switch case
        selected_song = option_menu.get()
        if selected_song == "RFM - Trap Future Bass":
            n = 0
        elif selected_song == "Red Skies - Laugh Now":
            n = 1
        elif selected_song == "TFP - Happy Day":
            n = 2
            

        image1 = Image.open(list_of_covers[n])
        image2=image1.resize((250, 250))
        load = ImageTk.PhotoImage(image2)
    
        label1 = tkinter.Label(self.frame, image=load)
        label1.image = load
        label1.grid(row=1, column=1, padx=(220,10), pady=(26, 10))

        stripped_string = song_name[6::] #This is to exlude the other characters
                                                    # 6       :      -4
                                        # Example: 'music/ | City | .wav'
                                        # This works because the music will always be between those 2 values
    
        song_name_label = tkinter.Label(text = song_name, bg='#222222', fg='white')
        song_name_label.grid(row=1, column=1, padx=(433,10), pady=(260, 10), sticky='nw')



    def progress(self):
        list_of_songs = ['tp-link-LB130-Smart-Wi-Fi-Bulb/music/trap-future-bass.mp3', 
                         'tp-link-LB130-Smart-Wi-Fi-Bulb/music/laugh-now.mp3', 
                         'tp-link-LB130-Smart-Wi-Fi-Bulb/music/happy-day.mp3',]
            
        a = pygame.mixer.Sound(f'{list_of_songs[n]}')
        song_len = a.get_length() * 3
        for i in range(0, math.ceil(song_len)):
            time.sleep(.4)
            self.progressbar.set(pygame.mixer.music.get_pos() / 1000000)

    def threading(progress):
        t1 = threading.Thread(target=progress)
        t1.start()
            



if __name__ == "__main__":
    app = App()
    app.mainloop()
