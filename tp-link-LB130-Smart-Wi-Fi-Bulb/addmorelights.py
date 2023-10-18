import tkinter
import tkinter.messagebox
import customtkinter
import subprocess

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
        self.sidebar_frame.grid_rowconfigure(5, weight=1)

        # Logo Label
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="D633 LMMS",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

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

        # Special Effects Button
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Special Effects",
                                                        command=self.open_specialeffects)
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

        # Page Heading
        self.label = customtkinter.CTkLabel(self.frame, text="Add More Lights",
                                                 font=customtkinter.CTkFont(size=30, weight="bold"))
        self.label.grid(row=0, column=1, padx=(40,20), pady=(60, 30))

        # Dummy Label for col 0
        self.labeld = customtkinter.CTkLabel(self.frame, text="                           ", font=customtkinter.CTkFont(size=15))
        self.labeld.grid(row=1, column=0, padx=20, pady=(10, 10), sticky="nw")

        # Light Name
        entry1 = customtkinter.CTkEntry(self.frame, placeholder_text="Enter Light Name", width=250, height=40)
        entry1.grid(row=1, column=1, pady=12, padx=(30,10))

        # IP Address
        entry2 = customtkinter.CTkEntry(self.frame, placeholder_text="Enter Light IP Address", width=250, height=40)
        entry2.grid(row=2, column=1, pady=12, padx=(30,10))

        # Add Light Button
        button = customtkinter.CTkButton(self.frame, text="Add Light", fg_color="#44dd45", hover_color="#02c910", text_color="black", font=customtkinter.CTkFont(size=18), width=150, height=40, border_width=3, border_color="white")
        button.grid(row=3, column=1, pady=(12,100), padx=(50,200))

        # View All Lights Button
        button = customtkinter.CTkButton(self.frame, text="View All Lights", command=self.open_lightslist, fg_color="#44dd45", hover_color="#02c910", text_color="black", font=customtkinter.CTkFont(size=18), width=150, height=40, border_width=3, border_color="white")
        button.grid(row=3, column=1, pady=(12,100), padx=(200,10))


        # Default Values
        self.appearance_mode_optionmenu.set("Dark")



    # Functions

    # Open Home Page
    def return_home(self):
        subprocess.Popen(["python", "homepage.py"])
        self.destroy()
    
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

    # Open Lights List Page
    def open_lightslist(self):
        subprocess.Popen(["python", "lightslist.py"])
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

if __name__ == "__main__":
    app = App()
    app.mainloop()
