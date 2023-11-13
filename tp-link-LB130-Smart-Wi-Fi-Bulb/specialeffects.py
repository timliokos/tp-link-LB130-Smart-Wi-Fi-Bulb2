import tkinter
import tkinter.messagebox
import customtkinter
import subprocess
import threading
import time
from tplight import LB130
from effectscode import *

# Appearance Settings
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        
        self.running_effect = None  # Initialize the running_effect to None
        self.stop_event = threading.Event()  # Initialize the stop event

        global value
        value = 1
       

        super().__init__()

        self.after_id = None

        # Configure Window
        self.title("D633 Lights/Music Management System")

        # Window Size
        self.geometry(f"{1100}x{480}")

        # Configure Grid Layout
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure((1), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)



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

        # Music Player Button
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text="Music Player",
                                                        command=self.open_musicplayer)
        self.sidebar_button_4.grid(row=3, column=0, padx=20, pady=(10,10))

        # Add More Lights Button
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Add More Lights",
                                                        command=self.open_addmorelights)
        self.sidebar_button_2.grid(row=4, column=0, padx=20, pady=(10,135))

        # Appearance Mode (Light/Dark)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionmenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                      values=["Light", "Dark", "System"],
                                                                      command=self.change_appearance_mode_event)
        self.appearance_mode_optionmenu.grid(row=6, column=0, padx=20, pady=(10, 10))



        # Sidebar Frame (Right)
        self.sidebar_frame2 = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame2.grid(row=0, column=2, rowspan=4, sticky="nsew")
        self.sidebar_frame2.grid_rowconfigure(4, weight=1)

        # Close Button
        self.main_button_1 = customtkinter.CTkButton(self.sidebar_frame2, text="Close", fg_color="transparent", hover_color="#d02626",
                                                     border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=6, column=2, padx=(20, 20), pady=(5, 20), sticky="nsew")
        self.main_button_1.configure(command=self.close_window)

        # Return Button
        self.main_button_2 = customtkinter.CTkButton(self.sidebar_frame2, text="Return", fg_color="transparent",
                                                     border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_2.grid(row=5, column=2, padx=(20, 20), pady=(20, 5), sticky="nsew")
        self.main_button_2.configure(command=self.return_home)



        # Main Frame
        self.frame = customtkinter.CTkFrame(self, width=300, corner_radius=5)
        self.frame.grid(row=0, column=1, rowspan=2, sticky="nsew")
        self.frame.grid_rowconfigure(4, weight=1)

        total_rows = self.grid_size()[1]

        middle_row = total_rows // 2

        self.frame.grid(row=1, column=1, padx=20, pady=(10,10))

        # Page Header
        image1 = tkinter.PhotoImage(file="tp-link-LB130-Smart-Wi-Fi-Bulb/images/sei.png")
        new_width = 35
        new_height = 35
        resized_image1 = image1.subsample(new_width, new_height)
        self.button_3 = customtkinter.CTkButton(self.frame, image=resized_image1, text="Special Effects", fg_color="#1a1a1a", hover_color="#1a1a1a", font=customtkinter.CTkFont(size=30, weight="bold"), width=650, height=50)
        self.button_3.grid(row=1, column=1, columnspan=3, padx=(25,0), pady=(10, 10), sticky='nw')
        self.button_3.icon = resized_image1

        # Effect Menu
        # Christmas Lights Effect
        imagecl = tkinter.PhotoImage(file="tp-link-LB130-Smart-Wi-Fi-Bulb/images/CHRLIG3.png")
        new_width = 4
        new_height = 4
        resized_imagecl = imagecl.subsample(new_width, new_height)
        self.button_1 = customtkinter.CTkButton(self.frame, image=resized_imagecl, text="",
                                                        command=self.christmaslights, width=100, height=77, fg_color="#1a1a1a", hover_color="white", text_color="black")
        self.button_1.grid(row=2, column=1, padx=(177,20), pady=(10,15), sticky='nw')
        
        
        # Police Lights Effect
        imagecl = tkinter.PhotoImage(file="tp-link-LB130-Smart-Wi-Fi-Bulb/images/POLLIG3.png")
        new_width = 4
        new_height = 4
        resized_imagepl = imagecl.subsample(new_width, new_height)
        self.button_2 = customtkinter.CTkButton(self.frame, image=resized_imagepl, text="",
                                                        command=self.policelights, width=100, height=77, fg_color="#1a1a1a", hover_color="white", text_color="black")
        self.button_2.grid(row=2, column=1, padx=(177,20), pady=(105,10), sticky='nw')

        # Hazard Lights Effect
        imagecl = tkinter.PhotoImage(file="tp-link-LB130-Smart-Wi-Fi-Bulb/images/HAZLIG3.png")
        new_width = 4
        new_height = 4
        resized_imagepl = imagecl.subsample(new_width, new_height)
        self.button_2 = customtkinter.CTkButton(self.frame, image=resized_imagepl, text="",
                                                        command=self.hazardlights, width=100, height=77, fg_color="#1a1a1a", hover_color="white", text_color="black")
        self.button_2.grid(row=2, column=1, padx=(177,20), pady=(200,10), sticky='nw')

        # Merry Go Round Effect
        imagecl = tkinter.PhotoImage(file="tp-link-LB130-Smart-Wi-Fi-Bulb/images/MGRLIG3.png")
        new_width = 4
        new_height = 4
        resized_imagepl = imagecl.subsample(new_width, new_height)
        self.button_2 = customtkinter.CTkButton(self.frame, image=resized_imagepl, text="",
                                                        command=self.merrygoround, width=100, height=77, fg_color="#1a1a1a", hover_color="white", text_color="black")
        self.button_2.grid(row=2, column=1, padx=(177,20), pady=(295,100), sticky='nw')

        # Set Button
        self.button_3 = customtkinter.CTkButton(self.frame, text="Set", fg_color="#1f538d", hover_color="#163b65", text_color="white", font=customtkinter.CTkFont(size=18), width=150, height=40, command=self.stopeffect, border_width=1, border_color="white")
        self.button_3.grid(row=2, column=1, padx=(385,10), pady=(290, 0), sticky="nw")

        # Default Values
        self.appearance_mode_optionmenu.set("Dark")



    # Functions

    # Open Home Page
    def return_home(self):
        subprocess.Popen(["python", "tp-link-LB130-Smart-Wi-Fi-Bulb/homepage.py"])
        self.destroy()

    # Open Light Control Page
    def open_lightcontrol(self):
        subprocess.Popen(["python", "tp-link-LB130-Smart-Wi-Fi-Bulb/lightcontrol.py"])
        self.destroy()

    # Open Music Player Page
    def open_musicplayer(self):
        subprocess.Popen(["python", "tp-link-LB130-Smart-Wi-Fi-Bulb/musicplayer.py"])
        self.destroy()

    # Open Add More Lights Page
    def open_addmorelights(self):
        subprocess.Popen(["python", "addmorelights.py"])
        self.destroy()

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



    def christmaslights(self):
        bulb_ips = [ '192.168.1.100', '192.168.1.101', '192.168.1.102', '192.168.1.103', '192.168.1.104', '192.168.1.105',#
                '192.168.1.106', '192.168.1.107', '192.168.1.108', '192.168.1.109', '192.168.1.110', '192.168.1.111',
                '192.168.1.112', '192.168.1.113', '192.168.1.114', ]
        if not self.running_effect:
            self.stop_event.clear()  # Reset the stop event before starting a new effect
            self.running_effect = threading.Thread(target=runChristmas, args=(bulb_ips,))
            self.running_effect.start()
             
        
    def policelights(bulb_ips):
        bulb_ips = [ '192.168.1.100', '192.168.1.101', '192.168.1.102', '192.168.1.103', '192.168.1.104', '192.168.1.105',#
                '192.168.1.106', '192.168.1.107', '192.168.1.108', '192.168.1.109', '192.168.1.110', '192.168.1.111',
                '192.168.1.112', '192.168.1.113', '192.168.1.114', ]
        runPolice(bulb_ips)
        

    def hazardlights(bulb_ips):
        bulb_ips = [ '192.168.1.100', '192.168.1.101', '192.168.1.102', '192.168.1.103', '192.168.1.104', '192.168.1.105',#
                '192.168.1.106', '192.168.1.107', '192.168.1.108', '192.168.1.109', '192.168.1.110', '192.168.1.111',
                '192.168.1.112', '192.168.1.113', '192.168.1.114', ]
        runHazards(bulb_ips)
        
    def merrygoround(bulb_ips):
        bulb_ips = [ '192.168.1.100', '192.168.1.101', '192.168.1.102', '192.168.1.103', '192.168.1.104', '192.168.1.105',#
                '192.168.1.106', '192.168.1.107', '192.168.1.108', '192.168.1.109', '192.168.1.110', '192.168.1.111',
                '192.168.1.112', '192.168.1.113', '192.168.1.114', ]
        runMerrygo(bulb_ips)


    
    def stopeffect(self):
        global value
        value -= 1
        if value == 0:
            print("button pressed")
            value = 1
        else:
            pass 


if __name__ == "__main__":
    
    app = App()
    app.mainloop()
    