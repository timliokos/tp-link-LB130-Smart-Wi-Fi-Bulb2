import tkinter
import tkinter.messagebox
import customtkinter
import subprocess
import time
from tplight import LB130

# Appearance Settings
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
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure((1), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)



        # Sidebar Frame (Left)
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # Logo Label
        imagesb = tkinter.PhotoImage(file="images/d633logosm2.png")
        new_width = 10
        new_height = 10
        resized_imagesb = imagesb.subsample(new_width, new_height)
        self.sidebar_button_sb = customtkinter.CTkButton(self.sidebar_frame, image=resized_imagesb, text="", fg_color="#212121", hover_color="#212121", width=50, height=40)
        self.sidebar_button_sb.grid(row=0, column=0, padx=0, pady=(20,20))
        self.sidebar_button_sb.icon = resized_imagesb

        # All Lights ON Button
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.alllightson, text="All Lights ON")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        # All Lights OFF Button
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.alllightsoff, text="All Lights OFF")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

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
        self.main_button_1 = customtkinter.CTkButton(self.sidebar_frame2, text="Close", fg_color="transparent",
                                                     border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=6, column=2, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.main_button_1.configure(command=self.close_window)



        # Main Frame
        self.frame = customtkinter.CTkFrame(self, width=300, corner_radius=5)
        self.frame.grid(row=0, column=1, rowspan=2, sticky="nsew")
        self.frame.grid_rowconfigure(4, weight=1)

        total_rows = self.grid_size()[1]

        middle_row = total_rows // 2

        self.frame.grid(row=1, column=1, padx=20, pady=(10,10))

        # Logo Icon
        image1 = tkinter.PhotoImage(file="images/D633LOGO3.png")
        new_width = 5
        new_height = 5
        resized_image1 = image1.subsample(new_width, new_height)
        self.button_1 = customtkinter.CTkButton(self.frame, image=resized_image1, text="", fg_color="#212121", hover_color="#212121", font=customtkinter.CTkFont(size=18), width=50, height=40)
        self.button_1.grid(row=0, column=2, columnspan=2, padx=0, pady=(0,0))
        self.button_1.icon = resized_image1

        # Main Menu
        # Light Control Button
        image2 = tkinter.PhotoImage(file="images/lai.png")
        new_width = 12
        new_height = 12
        resized_image2 = image2.subsample(new_width, new_height)
        self.button_2 = customtkinter.CTkButton(self.frame, image=resized_image2, text="", command=self.open_lightcontrol, width=100, height=100, corner_radius=0, fg_color="#212121", hover_color="#212121")
        self.button_2.grid(row=1, column=1, padx=(50,20), pady=0)
        
        self.label = customtkinter.CTkLabel(self.frame, text="Light Control", font=customtkinter.CTkFont(size=14, weight="bold"))
        self.label.grid(row=2, column=1, padx=(25,0), pady=(0,50))
        
        # Music Player Button
        image3 = tkinter.PhotoImage(file="images/mai.png")
        new_width = 12
        new_height = 12
        resized_image3 = image3.subsample(new_width, new_height)
        self.button_3 = customtkinter.CTkButton(self.frame, image=resized_image3, text="", command=self.open_musicplayer, width=100, height=100, corner_radius=0, fg_color="#212121", hover_color="#212121")
        self.button_3.grid(row=1, column=2, padx=20, pady=0)
        
        self.label3 = customtkinter.CTkLabel(self.frame, text="Music Player", font=customtkinter.CTkFont(size=14, weight="bold"))
        self.label3.grid(row=2, column=2, padx=0, pady=(0,50))

        # Special Effects Button
        image4 = tkinter.PhotoImage(file="images/sei.png")
        new_width = 12
        new_height = 12
        resized_image4 = image4.subsample(new_width, new_height)
        self.button_4 = customtkinter.CTkButton(self.frame, image=resized_image4, text="", command=self.open_specialeffects, width=100, height=100, fg_color="#212121", hover_color="#212121")
        self.button_4.grid(row=1, column=3, padx=20, pady=0)
        
        self.label4 = customtkinter.CTkLabel(self.frame, text="Special Effects", font=customtkinter.CTkFont(size=14, weight="bold"))
        self.label4.grid(row=2, column=3, padx=0, pady=(0,50))

        # Add More Lights Button
        image5 = tkinter.PhotoImage(file="images/ali.png")
        new_width = 12
        new_height = 12
        resized_image5 = image5.subsample(new_width, new_height)
        self.button_5 = customtkinter.CTkButton(self.frame, image=resized_image5, text="", command=self.open_addmorelights, width=100, height=100, corner_radius=0, fg_color="#212121", hover_color="#212121")
        self.button_5.grid(row=1, column=4, padx=(20,50), pady=0)

        self.label5 = customtkinter.CTkLabel(self.frame, text="Add More Lights", font=customtkinter.CTkFont(size=14, weight="bold"))
        self.label5.grid(row=2, column=4, padx=(0,30), pady=(0,50))



        # Default Values
        self.appearance_mode_optionmenu.set("Dark")



    # Functions

    # Open Light Control Page
    def open_lightcontrol(self):
        subprocess.Popen(["python", "lightcontrol.py"])
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
        
    # All Lights On
    def alllightson(self):
        ip_addresses = [
        "192.168.1.106", "192.168.1.107", "192.168.1.108", "192.168.1.109",
        "192.168.1.110", "192.168.1.111", "192.168.1.112", "192.168.1.113",
        "192.168.1.114", "192.168.1.100", "192.168.1.101", "192.168.1.102",
        "192.168.1.103", "192.168.1.104", "192.168.1.105"
        ]
        # Create a list of light instances
        lights = [LB130(ip) for ip in ip_addresses]
        # Set common properties for all lights
        for light in lights:
            light.on()
            
    # All Lights Off
    def alllightsoff(self):
        ip_addresses = [
        "192.168.1.106", "192.168.1.107", "192.168.1.108", "192.168.1.109",
        "192.168.1.110", "192.168.1.111", "192.168.1.112", "192.168.1.113",
        "192.168.1.114", "192.168.1.100", "192.168.1.101", "192.168.1.102",
        "192.168.1.103", "192.168.1.104", "192.168.1.105"
        ]
        # Create a list of light instances
        lights = [LB130(ip) for ip in ip_addresses]
        # Set common properties for all lights
        for light in lights:
            light.off()


if __name__ == "__main__":
    app = App()
    app.mainloop()
    