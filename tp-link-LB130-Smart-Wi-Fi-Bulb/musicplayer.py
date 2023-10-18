import tkinter
import tkinter.messagebox
import customtkinter
import subprocess
import time
from tplight import LB130
import pygame
import threading

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

        # Music Icon
        image1 = tkinter.PhotoImage(file="musiciconwhite.png")
        new_width = 15
        new_height = 15
        resized_image1 = image1.subsample(new_width, new_height)
        self.button_3 = customtkinter.CTkButton(self.frame, image=resized_image1, text="", fg_color="#212121", hover_color="#212121", font=customtkinter.CTkFont(size=18), width=50, height=40)
        self.button_3.grid(row=0, column=1, padx=(85,20), pady=(10,0))
        self.button_3.icon = resized_image1

        # Page Heading
        self.label = customtkinter.CTkLabel(self.frame, text="        Music Player", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.label.grid(row=1, column=1, padx=20, pady=(0, 40))

        # Dummy label for col 0
        self.labeld = customtkinter.CTkLabel(self.frame, text="                           ", font=customtkinter.CTkFont(size=15))
        self.labeld.grid(row=1, column=0, padx=20, pady=(10, 10), sticky="nw")

        # Song Menu
        self.label1 = customtkinter.CTkLabel(self.frame, text="Song:", font=customtkinter.CTkFont(size=15))
        self.label1.grid(row=2, column=1, padx=(20,20), pady=(20, 20), sticky="nw")
        
        self.option_menu = customtkinter.CTkOptionMenu(self.frame, values=["TFP - Happy Day", "Red Skies - Laugh Now"])
        self.option_menu.grid(row=2, column=1, padx=(80,10), pady=(10, 10))
        self.option_menu.configure(width=250, height=30, font=customtkinter.CTkFont(size=20), fg_color="white", button_color="#4d4d4d", button_hover_color="#44dd45", text_color="black")
        
        # Light Show Switch
        self.switch_1 = customtkinter.CTkSwitch(self.frame, text="Light Show", font=customtkinter.CTkFont(size=20),
                                   onvalue="on", offvalue="off", switch_width=65, switch_height=30, progress_color="#44dd45")
        self.switch_1.grid(row=3, column=1,padx=(80,20), pady=(10, 70))

        # Play Song Button
        image1 = tkinter.PhotoImage(file="play.png")
        new_width = 15
        new_height = 15
        resized_image1 = image1.subsample(new_width, new_height)
        self.button_3 = customtkinter.CTkButton(self.frame, image=resized_image1, text="", fg_color="white", hover_color="#44dd45", font=customtkinter.CTkFont(size=18), width=50, height=40, command=self.play_song)
        self.button_3.grid(row=6, column=1, padx=(0,20), pady=(10,100))
        self.button_3.icon = resized_image1

        # Pause Song Button
        image2 = tkinter.PhotoImage(file="pause.png")
        new_width = 15
        new_height = 15
        resized_image2 = image2.subsample(new_width, new_height)
        self.button_4 = customtkinter.CTkButton(self.frame, image=resized_image2, text="", fg_color="white", hover_color="#44dd45", font=customtkinter.CTkFont(size=18), width=50, height=40, command=self.pause_song)
        self.button_4.grid(row=6, column=1, padx=(160,20), pady=(10,100))
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

    # Play Selected Song From Song Map
    def _play_music(self, selected_song):
        song_map = {
            "TFP - Happy Day": "happy-day.mp3",
            "Red Skies - Laugh Now": "laugh-now.mp3",
            }
        if selected_song in song_map:
            pygame.mixer.init()
            pygame.mixer.music.load(song_map[selected_song])
            pygame.mixer.music.play()
        else:
            return

    # Pause Song
    def pause_song(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()

    # Open Home Page
    def return_home(self):
        subprocess.Popen(["python", "homepage.py"])
        self.destroy()

    # Open Light Control Page
    def open_lightcontrol(self):
        subprocess.Popen(["python", "lightcontrol.py"])
        self.destroy()

    # Open Special Effects Page
    def open_specialeffects(self):
        subprocess.Popen(["python", "specialeffects.py"])
        self.destroy()

    # Open Add More Lights Page
    def open_addmorelights(self):
        subprocess.Popen(["python", "addmorelights.py"])
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
