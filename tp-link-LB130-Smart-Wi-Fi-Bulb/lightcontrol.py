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
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="D633 LMMS",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

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
        self.frame.grid(row=0, column=1, rowspan=1, sticky="nsew")
        self.frame.grid_rowconfigure(4, weight=1)

        total_rows = self.grid_size()[1]

        middle_row = total_rows // 2

        self.frame.grid(row=1, column=1, padx=20, pady=(20,10))

        # Light Icon
        image1 = tkinter.PhotoImage(file="lighticonwhite.png")
        new_width = 15
        new_height = 15
        resized_image1 = image1.subsample(new_width, new_height)
        self.button_3 = customtkinter.CTkButton(self.frame, image=resized_image1, text="", fg_color="#212121", hover_color="#212121", font=customtkinter.CTkFont(size=18), width=50, height=40)
        self.button_3.grid(row=0, column=1, padx=(90,20), pady=(10,0))
        self.button_3.icon = resized_image1

        # Page Heading
        self.label = customtkinter.CTkLabel(self.frame, text="         Light Control", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.label.grid(row=1, column=1, padx=20, pady=(0, 10))

        # Dummy Label for col 0
        self.labeld = customtkinter.CTkLabel(self.frame, text="                           ", font=customtkinter.CTkFont(size=15))
        self.labeld.grid(row=1, column=0, padx=20, pady=(10, 10), sticky="nw")

        # Light Option Menu
        self.label1 = customtkinter.CTkLabel(self.frame, text="Light:", font=customtkinter.CTkFont(size=15))
        self.label1.grid(row=2, column=1, padx=20, pady=(20, 20), sticky="nw")

        self.option_menu = customtkinter.CTkOptionMenu(self.frame, values=["All Lights", "Light A1", "Light A2", "Light A3", "Light B1", "Light B2", "Light B3", "Light B4", "Light B5", "Light C1", "Light C2", "Light C3", "Light D1", "Light D2", "Light D3", "Light D4", "Light D5"])
        self.option_menu.grid(row=2, column=1, padx=(85,10), pady=(10, 10))
        self.option_menu.configure(width=250, height=30, font=customtkinter.CTkFont(size=20), fg_color="white", button_color="#4d4d4d", button_hover_color="#44dd45", text_color="black")
        
        # Colour Option Menu
        self.label2 = customtkinter.CTkLabel(self.frame, text="Colour:", font=customtkinter.CTkFont(size=15))
        self.label2.grid(row=3, column=1, padx=(10,20), pady=(20, 40), sticky="nw")

        self.option_menu2 = customtkinter.CTkOptionMenu(self.frame, values=["White", "Blue", "Light Blue", "Red", "Yellow", "Green", "Light Green", "Purple", "Orange", "Pink"])
        self.option_menu2.grid(row=3, column=1, padx=(85,10), pady=(10, 30))
        self.option_menu2.configure(width=250, height=30, font=customtkinter.CTkFont(size=20), fg_color="white", button_color="#4d4d4d", button_hover_color="#44dd45", text_color="black")

        # Brightness Slider
        self.label3 = customtkinter.CTkLabel(self.frame, text="Brightness:", font=customtkinter.CTkFont(size=15))
        self.label3.grid(row=5, column=1, padx=(10,20), pady=(10, 0), sticky="nw")

        self.slider = customtkinter.CTkSlider(self.frame, from_=1, to=100, number_of_steps=100, button_color="#44dd45", button_hover_color="green")
        self.slider.grid(row=5, column=1, padx=(85, 10), pady=(15, 30), sticky="n")

        # Set Button
        self.button_3 = customtkinter.CTkButton(self.frame, text="Set", fg_color="#44dd45", hover_color="#02c910", text_color="black", font=customtkinter.CTkFont(size=18), width=150, height=40, command=self.test_set, border_width=3, border_color="white")
        self.button_3.grid(row=7, column=1, padx=(85,20), pady=(10,60))



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

    # Test to see if set button works
    def test_set(self):
        light = LB130("192.168.1.101")
        light.transition_period = 0

        # set the brightness to 50%
        light.brightness = 50
        time.sleep(1)

        # set the saturation to 100%
        light.saturation = 90
        time.sleep(1)

        # cycle through the colours
        light.hue = 0
        time.sleep(1)
        light.hue = 60
        time.sleep(1)
        light.hue = 120
        time.sleep(1)
        light.hue = 180
        time.sleep(1)
        light.hue = 240
        time.sleep(1)
        light.hue = 300
        time.sleep(1)

        # set the colour to warm white and the brightness to 0
        light.temperature = 6000
        #light.hue = 240
        light.brightness = 100

if __name__ == "__main__":
    app = App()
    app.mainloop()
