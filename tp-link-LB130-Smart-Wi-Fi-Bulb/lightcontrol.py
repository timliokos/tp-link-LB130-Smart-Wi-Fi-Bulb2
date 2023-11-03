import tkinter
import tkinter.messagebox
import customtkinter
import subprocess
import time
from tplight import LB130




# Appearance settings
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


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
        imagesb = tkinter.PhotoImage(file="images/d633logosm2.png")
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

        # Music Player Button
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Music Player",
                                                        command=self.open_musicplayer)
        self.sidebar_button_3.grid(row=2, column=0, padx=20, pady=(10,10))

        # Special Effects Button
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text="Special Effects",
                                                        command=self.open_specialeffects)
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
        self.appearance_mode_optionmenu.grid(row=6, column=0, padx=20, pady=(0, 20))



        # Sidebar Frame (Right)
        self.sidebar_frame2 = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame2.grid(row=0, column=4, rowspan=4, sticky="nsew")
        self.sidebar_frame2.grid_rowconfigure(4, weight=1)
      
        # Close Button
        self.main_button_1 = customtkinter.CTkButton(self.sidebar_frame2, text="Close", fg_color="transparent", hover_color="#d02626",
                                                     border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=6, column=4, padx=(20, 20), pady=(5, 20), sticky="nsew")
        self.main_button_1.configure(command=self.close_window)

        # Return Button
        self.main_button_2 = customtkinter.CTkButton(self.sidebar_frame2, text="Return", fg_color="transparent",
                                                     border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_2.grid(row=5, column=4, padx=(20, 20), pady=(20, 5), sticky="nsew")
        self.main_button_2.configure(command=self.return_home)



        # Main Frame
        self.frame = customtkinter.CTkFrame(self, width=300, corner_radius=5)
        self.frame.grid(row=0, column=1, rowspan=1, sticky="nsew")
        self.frame.grid_rowconfigure(4, weight=1)

        total_rows = self.grid_size()[1]

        middle_row = total_rows // 2

        self.frame.grid(row=1, column=1, padx=20, pady=(10,10))

        # Testing bg frame
        #self.bgframebutton = customtkinter.CTkButton(self.frame, text="", fg_color="#1a1a1a", hover_color="#1a1a1a", text_color="black", font=customtkinter.CTkFont(size=18), width=380, height=260, border_width=0, border_color="white")
        #self.bgframebutton.grid(row=3, column=1, columnspan=2, padx=(30,10), pady=(25,160), sticky='nw')
        
        # Door Button
        self.doorbutton = customtkinter.CTkButton(self.frame, text="D O O R", fg_color="black", hover_color="black", text_color="white", font=customtkinter.CTkFont(size=12), width=100, height=20, border_width=0, border_color="white")
        self.doorbutton.grid(row=3, column=1, columnspan=2, padx=(30,10), pady=(265,160), sticky='nw')
        
        # Colour Background Frame
        #self.bgframebutton = customtkinter.CTkButton(self.frame, text="", fg_color="#333333", hover_color="#333333", text_color="black", font=customtkinter.CTkFont(size=18), width=240, height=200, border_width=0, border_color="white")
        #self.bgframebutton.grid(row=3, column=2, columnspan=2, padx=(340,10), pady=(25,160), sticky='nw')

        # Colour Label
        self.doorbutton = customtkinter.CTkButton(self.frame, text="Colour", fg_color="#1a1a1a", hover_color="#1a1a1a", text_color="white", font=customtkinter.CTkFont(size=12), width=240, height=20, border_width=0, border_color="white")
        self.doorbutton.grid(row=3, column=2, columnspan=2, padx=(340,10), pady=(25,160), sticky='nw')

        # Brightness Label
        self.doorbutton = customtkinter.CTkButton(self.frame, text="Brightness", fg_color="#1a1a1a", hover_color="#1a1a1a", text_color="white", font=customtkinter.CTkFont(size=12), width=240, height=20, border_width=0, border_color="white")
        self.doorbutton.grid(row=3, column=2, columnspan=2, padx=(340,10), pady=(170,160), sticky='nw')

        #Dummy Label for col 0
        self.labeld = customtkinter.CTkLabel(self.frame, text="                           ", font=customtkinter.CTkFont(size=15))
        self.labeld.grid(row=3, column=4, padx=20, pady=(10, 10))

        


        # Page Header
        image1 = tkinter.PhotoImage(file="images/lai.png")
        new_width = 35
        new_height = 35
        resized_image1 = image1.subsample(new_width, new_height)
        self.button_3 = customtkinter.CTkButton(self.frame, image=resized_image1, text="Light Control", fg_color="#1a1a1a", hover_color="#1a1a1a", font=customtkinter.CTkFont(size=30, weight="bold"), width=650, height=50)
        self.button_3.grid(row=1, column=1, columnspan=3, padx=(25,0), pady=(10, 10), sticky='nw')
        self.button_3.icon = resized_image1

        # Light Option Menu
        self.option_menu = customtkinter.CTkOptionMenu(self.frame, values=["All Lights", "Light A1", "Light A2", "Light B1", "Light B2", "Light B3", "Light B4", "Light B5", "Light C1", "Light C2", "Light C3", "Light D1", "Light D2", "Light D3", "Light D4", "Light D5"])
        self.option_menu.grid(row=2, column=2, columnspan=2, padx=(140, 0), pady=(10, 0), sticky="nw")
        self.option_menu.configure(width=250, height=30, font=customtkinter.CTkFont(size=20), fg_color="#efefef", button_color="#1f538d", button_hover_color="#163b65", text_color="black")

        # Colour Option Menu
        
        self.option_menu2 = customtkinter.CTkOptionMenu(self.frame, values=["White", "Blue", "Red", "Yellow", "Green", "Purple", "Orange", "Pink"])
        self.option_menu2.grid(row=2, column=2, columnspan=2, padx=(140,0), pady=(50, 0), sticky="nw")
        self.option_menu2.configure(width=250, height=30, font=customtkinter.CTkFont(size=20), fg_color="#efefef", button_color="#1f538d", button_hover_color="#163b65", text_color="black")

        # Brightness Slider
        self.slider = customtkinter.CTkSlider(self.frame, from_=0, to=100, number_of_steps=100, button_color="#1f538d", button_hover_color="#07b0bf", width=190)
        self.slider.grid(row=3, column=2, columnspan=2, padx=(365,10), pady=(200, 0), sticky="nw")

        # Set Button
        self.button_3 = customtkinter.CTkButton(self.frame, text="Set", fg_color="#1f538d", hover_color="#163b65", text_color="white", font=customtkinter.CTkFont(size=18), width=150, height=40, command=self.test_set, border_width=1, border_color="white")
        self.button_3.grid(row=3, column=2, columnspan=2, padx=(385,10), pady=(240, 0), sticky="nw")

        # A1 Button
        self.a1button = customtkinter.CTkButton(self.frame, text="A1", fg_color="orange", hover_color="yellow", text_color="black", font=customtkinter.CTkFont(size=18), width=40, height=40, command=lambda: self.layoutbutton("Light A1"), border_width=1, border_color="white")
        self.a1button.grid(row=3, column=1, padx=(50,0), pady=(175,60), sticky='n')
        
        # A2 Button
        self.a2button = customtkinter.CTkButton(self.frame, text="A2", fg_color="orange", hover_color="yellow", text_color="black", font=customtkinter.CTkFont(size=18), width=40, height=40, command=lambda: self.layoutbutton("Light A2"), border_width=1, border_color="white")
        self.a2button.grid(row=3, column=1, padx=(50,0), pady=(125,60), sticky='n')
        
        # A3 Button
        self.a3button = customtkinter.CTkButton(self.frame, text="A3", fg_color="gray", hover_color="#4b4b4b", text_color="black", font=customtkinter.CTkFont(size=18), width=40, height=40, command=lambda: self.layoutbutton("Light A3"), border_width=1, border_color="white")
        self.a3button.grid(row=3, column=1, padx=(50,0), pady=(75,60), sticky='n')

        # B1 Button
        self.b1button = customtkinter.CTkButton(self.frame, text="B1", fg_color="orange", hover_color="yellow", text_color="black", font=customtkinter.CTkFont(size=18), width=40, height=40, command=lambda: self.layoutbutton("Light B1"), border_width=1, border_color="white")
        self.b1button.grid(row=3, column=2, padx=(10,10), pady=(40,160), sticky='nw')
        
        # B2 Button
        self.b2button = customtkinter.CTkButton(self.frame, text="B2", fg_color="orange", hover_color="yellow", text_color="black", font=customtkinter.CTkFont(size=18), width=40, height=40, command=lambda: self.layoutbutton("Light B2"), border_width=1, border_color="white")
        self.b2button.grid(row=3, column=2, padx=(60,10), pady=(40,160), sticky='nw')
        
        # B3 Button
        self.b3button = customtkinter.CTkButton(self.frame, text="B3", fg_color="orange", hover_color="yellow", text_color="black", font=customtkinter.CTkFont(size=18), width=40, height=40, command=lambda: self.layoutbutton("Light B3"), border_width=1, border_color="white")
        self.b3button.grid(row=3, column=2, padx=(110,10), pady=(40,160), sticky='nw')
        
        # B4 Button
        self.b4button = customtkinter.CTkButton(self.frame, text="B4", fg_color="orange", hover_color="yellow", text_color="black", font=customtkinter.CTkFont(size=18), width=40, height=40, command=lambda: self.layoutbutton("Light B4"), border_width=1, border_color="white")
        self.b4button.grid(row=3, column=2, padx=(160,10), pady=(40,160), sticky='nw')
        
        # B5 Button
        self.b5button = customtkinter.CTkButton(self.frame, text="B5", fg_color="orange", hover_color="yellow", text_color="black", font=customtkinter.CTkFont(size=18), width=40, height=40, command=lambda: self.layoutbutton("Light B5"), border_width=1, border_color="white")
        self.b5button.grid(row=3, column=2, padx=(210,10), pady=(40,160), sticky='nw')

        # C1 Button
        self.c1button = customtkinter.CTkButton(self.frame, text="C1", fg_color="orange", hover_color="yellow", text_color="black", font=customtkinter.CTkFont(size=18), width=40, height=40, command=lambda: self.layoutbutton("Light C1"), border_width=1, border_color="white")
        self.c1button.grid(row=3, column=2, padx=(260,60), pady=(75,0), sticky='nw')
        
        # C2 Button
        self.c2button = customtkinter.CTkButton(self.frame, text="C2", fg_color="orange", hover_color="yellow", text_color="black", font=customtkinter.CTkFont(size=18), width=40, height=40, command=lambda: self.layoutbutton("Light C2"), border_width=1, border_color="white")
        self.c2button.grid(row=3, column=2, padx=(260,60), pady=(125,0), sticky='nw')

        # C3 Button
        self.c3button = customtkinter.CTkButton(self.frame, text="C3", fg_color="orange", hover_color="yellow", text_color="black", font=customtkinter.CTkFont(size=18), width=40, height=40, command=lambda: self.layoutbutton("Light C3"), border_width=1, border_color="white")
        self.c3button.grid(row=3, column=2, padx=(260,60), pady=(175,0), sticky='nw')

        # D1 Button
        self.d1button = customtkinter.CTkButton(self.frame, text="D1", fg_color="orange", hover_color="yellow", text_color="black", font=customtkinter.CTkFont(size=18), width=40, height=40, command=lambda: self.layoutbutton("Light D1"), border_width=1, border_color="white")
        self.d1button.grid(row=3, column=2, padx=(210,10), pady=(210,50), sticky='nw')
        
        # D2 Button
        self.d2button = customtkinter.CTkButton(self.frame, text="D2", fg_color="orange", hover_color="yellow", text_color="black", font=customtkinter.CTkFont(size=18), width=40, height=40, command=lambda: self.layoutbutton("Light D2"), border_width=1, border_color="white")
        self.d2button.grid(row=3, column=2, padx=(160,10), pady=(210,50), sticky='nw')
        
        # D3 Button
        self.d3button = customtkinter.CTkButton(self.frame, text="D3", fg_color="orange", hover_color="yellow", text_color="black", font=customtkinter.CTkFont(size=18), width=40, height=40, command=lambda: self.layoutbutton("Light D3"), border_width=1, border_color="white")
        self.d3button.grid(row=3, column=2, padx=(110,10), pady=(210,50), sticky='nw')
        
        # D4 Button
        self.d4button = customtkinter.CTkButton(self.frame, text="D4", fg_color="orange", hover_color="yellow", text_color="black", font=customtkinter.CTkFont(size=18), width=40, height=40, command=lambda: self.layoutbutton("Light D4"), border_width=1, border_color="white")
        self.d4button.grid(row=3, column=2, padx=(60,10), pady=(210,50), sticky='nw')
        
        # D5 Button
        self.d5button = customtkinter.CTkButton(self.frame, text="D5", fg_color="orange", hover_color="yellow", text_color="black", font=customtkinter.CTkFont(size=18), width=40, height=40, command=lambda: self.layoutbutton("Light D5"), border_width=1, border_color="white")
        self.d5button.grid(row=3, column=2, padx=(10,10), pady=(210,50), sticky='nw')
        
        # All Lights Button
        self.albutton = customtkinter.CTkButton(self.frame, text="All Lights", fg_color="orange", hover_color="yellow", text_color="black", font=customtkinter.CTkFont(size=18), width=170, height=40, command=lambda: self.layoutbutton("All Lights"), border_width=1, border_color="white")
        self.albutton.grid(row=3, column=2, padx=(46,10), pady=(125,0), sticky='nw')
        
        # White Button
        self.whitebutton = customtkinter.CTkButton(self.frame, text="", fg_color="white", hover_color="#cbcbcb", text_color="black", font=customtkinter.CTkFont(size=18), width=40, height=40, command=lambda: self.colourbutton("White"), border_width=0, border_color="white", corner_radius=20)
        self.whitebutton.grid(row=3, column=2, columnspan=2, padx=(365,10), pady=(55,160), sticky='nw')
        
        # Blue Button
        self.bluebutton = customtkinter.CTkButton(self.frame, text="", fg_color="#0362e4", hover_color="#014cb2", text_color="black", font=customtkinter.CTkFont(size=18), width=40, height=40, command=lambda: self.colourbutton("Blue"), border_width=0, border_color="white", corner_radius=20)
        self.bluebutton.grid(row=3, column=2, columnspan=2, padx=(415,10), pady=(55,160), sticky='nw')
        
        # Red Button
        self.redbutton = customtkinter.CTkButton(self.frame, text="", fg_color="red", hover_color="#ad0909", text_color="black", font=customtkinter.CTkFont(size=18), width=40, height=40, command=lambda: self.colourbutton("Red"), border_width=0, border_color="white", corner_radius=20)
        self.redbutton.grid(row=3, column=2, columnspan=2, padx=(465,10), pady=(55,160), sticky='nw')
        
        # Yellow Button
        self.yellowbutton = customtkinter.CTkButton(self.frame, text="", fg_color="yellow", hover_color="#b3ad0b", text_color="black", font=customtkinter.CTkFont(size=18), width=40, height=40, command=lambda: self.colourbutton("Yellow"), border_width=0, border_color="white", corner_radius=20)
        self.yellowbutton.grid(row=3, column=2, columnspan=2, padx=(515,10), pady=(55,160), sticky='nw')
        
        # Green Button
        self.yellowbutton = customtkinter.CTkButton(self.frame, text="", fg_color="#05a803", hover_color="#047d03", text_color="black", font=customtkinter.CTkFont(size=18), width=40, height=40, command=lambda: self.colourbutton("Green"), border_width=0, border_color="white", corner_radius=20)
        self.yellowbutton.grid(row=3, column=2, columnspan=2, padx=(365,10), pady=(105,160), sticky='nw')
        
        # Purple Button
        self.yellowbutton = customtkinter.CTkButton(self.frame, text="", fg_color="#6b069f", hover_color="#510579", text_color="black", font=customtkinter.CTkFont(size=18), width=40, height=40, command=lambda: self.colourbutton("Purple"), border_width=0, border_color="white", corner_radius=20)
        self.yellowbutton.grid(row=3, column=2, columnspan=2, padx=(415,10), pady=(105,160), sticky='nw')
        
        # Orange Button
        self.yellowbutton = customtkinter.CTkButton(self.frame, text="", fg_color="orange", hover_color="#a87703", text_color="black", font=customtkinter.CTkFont(size=18), width=40, height=40, command=lambda: self.colourbutton("Orange"), border_width=0, border_color="white", corner_radius=20)
        self.yellowbutton.grid(row=3, column=2, columnspan=2, padx=(465,10), pady=(105,160), sticky='nw')
        
        # Pink Button
        self.yellowbutton = customtkinter.CTkButton(self.frame, text="", fg_color="#ff03d9", hover_color="#a607ac", text_color="black", font=customtkinter.CTkFont(size=18), width=40, height=40, command=lambda: self.colourbutton("Pink"), border_width=0, border_color="white", corner_radius=20)
        self.yellowbutton.grid(row=3, column=2, columnspan=2, padx=(515,10), pady=(105,160), sticky='nw')

        # Default Values
        self.appearance_mode_optionmenu.set("Dark")
        


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

    # Open Home Page
    def return_home(self):
        subprocess.Popen(["python", "homepage.py"])
        self.destroy()

    # Open Music Player Page
    def open_musicplayer(self):
        subprocess.Popen(["python", "musicplayer.py"])
        self.destroy()

    # Open Special Effects Page
    def open_specialeffects(self):
        subprocess.Popen(["python", "specialeffects.py"])
        self.destroy()

    # Open Add More Lights Page
    def open_addmorelights(self):
        subprocess.Popen(["python", "addmorelights.py"])
        self.destroy()
        
    # Layout Option Button
    def layoutbutton(self, option):
        
        self.option_menu.set(option)
        
    # Colour Option Button
    def colourbutton(self, option):
        
        self.option_menu2.set(option)
        

    # Test to see if set button works
    def test_set(self):
        
        selection = "individual"
        
        match self.option_menu._current_value:
            
            case "Light A1":
                individualip = "192.168.1.100"

            case "Light A2":
                individualip = "192.168.1.101"
                
            case "Light B1":
                individualip = "192.168.1.102"

            case "Light B2":
                individualip = "192.168.1.103"
                
            case "Light B3":
                individualip = "192.168.1.104"

            case "Light B4":
                individualip = "192.168.1.105"
                
            case "Light B5":
                individualip = "192.168.1.106"

            case "Light C1":
                individualip = "192.168.1.107"
                
            case "Light C2":
                individualip = "192.168.1.108"

            case "Light C3":
                individualip = "192.168.1.109"
                
            case "Light D1":
                individualip = "192.168.1.110"

            case "Light D2":
                individualip = "192.168.1.111"
                
            case "Light D3":
                individualip = "192.168.1.112"

            case "Light D4":
                individualip = "192.168.1.113"
                
            case "Light D5":
                individualip = "192.168.1.114"
                
            case _:
                selection = "all"
                
        match self.option_menu2._current_value:
            
            case "White":
                selectedhue = 240
                selsat = 0
                

            case "Blue":
                selectedhue = 240
                selsat = 90

            case "Red":
                selectedhue = 0
                selsat = 90
                
            case "Yellow":
                selectedhue = 60
                selsat = 90
                
            case "Green":
                selectedhue = 120
                selsat = 90
                
            case "Purple":
                selectedhue = 276
                selsat = 90
                
            case "Orange":
                selectedhue = 30
                selsat = 90
                
            case "Pink":
                selectedhue = 350
                selsat = 90
                
            case _:
                print("The language doesn't matter, what matters is solving problems.")
                
       
        if selection == "individual":
        
        
            print(individualip)
            print(selectedhue)
            print(self.slider.get())

            light = LB130(individualip)
            #light.transition_period = 0
            time.sleep(0)
            light.saturation = selsat
            time.sleep(0)
            light.hue = selectedhue
            time.sleep(0)
            
            light.brightness = int(self.slider.get())

        else:
            
            bulb_ips = [ '192.168.1.100', '192.168.1.101', '192.168.1.102', '192.168.1.103', '192.168.1.104', '192.168.1.105',#
             '192.168.1.106', '192.168.1.107', '192.168.1.108', '192.168.1.109', '192.168.1.110', '192.168.1.111',
             '192.168.1.112', '192.168.1.113', '192.168.1.114', ]
            
            for bulb_ip in bulb_ips:
                try:
                    
                    light = LB130(bulb_ip)
            
                    #light.transition_period = 0
                    time.sleep(0)

                    light.saturation = selsat
                    time.sleep(0)
                    light.hue = selectedhue
                    light.brightness = int(self.slider.get())
                    time.sleep(0)

                    print(bulb_ip)
                    print(selectedhue)
                    print(self.slider.get())
                        
            
                except Exception as e:
                    print(f"Error controlling bulb at {bulb_ips}: {str(e)}")
            


        

if __name__ == "__main__":
    app = App()
    app.mainloop()
    
