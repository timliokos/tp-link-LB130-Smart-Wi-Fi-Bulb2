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

        # Christmas Icon
        image1 = tkinter.PhotoImage(file="christmasiconwhite.png")
        new_width = 15
        new_height = 15
        resized_image1 = image1.subsample(new_width, new_height)
        self.button_3 = customtkinter.CTkButton(self.frame, image=resized_image1, text="", fg_color="#212121", hover_color="#212121", font=customtkinter.CTkFont(size=18), width=50, height=40)
        self.button_3.grid(row=0, column=1, padx=(200,20), pady=(0,0))
        self.button_3.icon = resized_image1

        # Page Heading
        self.label = customtkinter.CTkLabel(self.frame, text="Special Effects",
                                                 font=customtkinter.CTkFont(size=30, weight="bold"))
        self.label.grid(row=0, column=1, padx=(200,20), pady=(100, 0))

        # Effect Menu
        # Effect 1
        self.button_1 = customtkinter.CTkButton(self.frame, text="Christmas Lights", font=customtkinter.CTkFont(size=20),
                                                        command=self.start_flashing_gr, width=300, height=50, fg_color="#44dd45", hover_color="#02c910", text_color="black", border_width=3, border_color="red")
        self.button_1.grid(row=1, column=1, padx=(200,20), pady=(20,15))
        
        # Effect 2
        self.button_2 = customtkinter.CTkButton(self.frame, text="Police Lights", font=customtkinter.CTkFont(size=20),
                                                        command=self.start_flashing_br, width=300, height=50, fg_color="blue", hover_color="#0e93e8", text_color="black", border_width=3, border_color="red")
        self.button_2.grid(row=2, column=1, padx=(200,20), pady=(10,10))

        # Effect 3
        self.button_3 = customtkinter.CTkButton(self.frame, text="Hazard Lights", font=customtkinter.CTkFont(size=20),
                                                        command=self.start_flashing_hl, width=300, height=50, fg_color="orange", hover_color="yellow", text_color="black", border_width=3, border_color="white")
        self.button_3.grid(row=3, column=1, padx=(200,20), pady=(10,20))

        # Effect 4
        self.button_4 = customtkinter.CTkButton(self.frame, text="Merry Go Round", font=customtkinter.CTkFont(size=20),
                                                        command=self.start_flashing_pw, width=300, height=50, fg_color="purple", hover_color="#f902e5", text_color="black", border_width=3, border_color="white")
        self.button_4.grid(row=4, column=1, padx=(200,20), pady=(0,20))


        # Testing SE Light
        self.circle1 = customtkinter.CTkButton(self.frame, text="", width=30, height=30, fg_color="white", hover_color="white", border_width=1, border_color="black", corner_radius=20)
        self.circle1.grid(row=0, column=1, padx=(0,20), pady=0)

        self.circle2 = customtkinter.CTkButton(self.frame, text="", width=30, height=30, fg_color="white", hover_color="white", border_width=1, border_color="black", corner_radius=20)
        self.circle2.grid(row=0, column=1, padx=(400,20), pady=0)



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

    # Play Christmas Light Example
    def flash_gr(self, circle1_state, circle2_state):
        if not circle1_state and not circle2_state:
            return
        
        new_circle1_state = not circle1_state
        new_circle2_state = not circle2_state

        if circle1_state:
            self.circle1.configure(fg_color="red")
            self.circle2.configure(fg_color="green")
        else:
            self.circle1.configure(fg_color="green")
            self.circle2.configure(fg_color="red")

        self.after_id = self.after(500, self.flash_gr, new_circle1_state, new_circle2_state)

    def start_flashing_gr(self):
        if self.after_id is not None:
            self.after_cancel(self.after_id)  # Stop the current flashing if any
        self.after_id = self.after(500, self.flash_gr, True, False)

    # Play Police Light Example
    def flash_br(self, circle1_state, circle2_state):
         
        if not circle1_state and not circle2_state:
            return  # Stop flashing when both states are False

        new_circle1_state = not circle1_state
        new_circle2_state = not circle2_state

        if circle1_state:
            self.circle1.configure(fg_color="red")
            self.circle2.configure(fg_color="blue")
        else:
            self.circle1.configure(fg_color="blue")
            self.circle2.configure(fg_color="red")

        self.after_id = self.after(500, self.flash_br, new_circle1_state, new_circle2_state)

    def start_flashing_br(self):
        if self.after_id is not None:
            self.after_cancel(self.after_id)  # Stop the current flashing if any
        self.after_id = self.after(500, self.flash_br, True, False)

    # Play Hazard Light Example
    def flash_hl(self, circle1_state, circle2_state):
         
        if not circle1_state and not circle2_state:
            return  # Stop flashing when both states are False

        new_circle1_state = not circle1_state
        new_circle2_state = not circle2_state

        if circle1_state:
            self.circle1.configure(fg_color="orange")
            self.circle2.configure(fg_color="orange")
        else:
            self.circle1.configure(fg_color="black")
            self.circle2.configure(fg_color="black")

        self.after_id = self.after(500, self.flash_hl, new_circle1_state, new_circle2_state)

    def start_flashing_hl(self):
        if self.after_id is not None:
            self.after_cancel(self.after_id)  # Stop the current flashing if any
        self.after_id = self.after(500, self.flash_hl, True, False)

    # Play Merry Go Round Example
    def flash_pw(self, circle1_state, circle2_state):
         
        if not circle1_state and not circle2_state:
            return  # Stop flashing when both states are False

        new_circle1_state = not circle1_state
        new_circle2_state = not circle2_state

        if circle1_state:
            self.circle1.configure(fg_color="purple")
            self.circle2.configure(fg_color="white")
        else:
            self.circle1.configure(fg_color="white")
            self.circle2.configure(fg_color="purple")

        self.after_id = self.after(500, self.flash_pw, new_circle1_state, new_circle2_state)

    def start_flashing_pw(self):
        if self.after_id is not None:
            self.after_cancel(self.after_id)  # Stop the current flashing if any
        self.after_id = self.after(500, self.flash_pw, True, False)

    

if __name__ == "__main__":
    app = App()
    app.mainloop()
