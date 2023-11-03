import tkinter
import tkinter.messagebox
import customtkinter
import subprocess
from databaseinfo import *

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

        self.frame.grid(row=1, column=1, padx=20, pady=(10,10))

        # Page Heading
        image1 = tkinter.PhotoImage(file="images/ali.png")
        new_width = 35
        new_height = 35
        resized_image1 = image1.subsample(new_width, new_height)
        self.button_3 = customtkinter.CTkButton(self.frame, image=resized_image1, text="Add More Lights", fg_color="#1a1a1a", hover_color="#1a1a1a", font=customtkinter.CTkFont(size=30, weight="bold"), width=650, height=50)
        self.button_3.grid(row=1, column=1, columnspan=3, padx=(25,0), pady=(10, 10), sticky='nw')
        self.button_3.icon = resized_image1

         # Light Name Entry
        self.entry1 = customtkinter.CTkEntry(self.frame, placeholder_text="Enter Light Name", width=250, height=40)
        self.entry1.grid(row=1, column=1, pady=(140,10), padx=(230,10), sticky='nw')

        # IP Address Entry
        self.entry2 = customtkinter.CTkEntry(self.frame, placeholder_text="Enter Light IP Address", width=250, height=40)
        self.entry2.grid(row=1, column=1, pady=(190,10), padx=(230,10), sticky='nw')

        # Add Light Button
        button = customtkinter.CTkButton(self.frame, text="Add Light", command=self.addlight, fg_color="#1f538d", hover_color="#163b65", text_color="white", font=customtkinter.CTkFont(size=18), width=150, height=40, border_width=1, border_color="white")
        button.grid(row=1, column=1, pady=(270,200), padx=(195,200), sticky='nw')

        # View All Lights Button
        button = customtkinter.CTkButton(self.frame, text="View All Lights", command=self.open_lightslist, fg_color="#1f538d", hover_color="#163b65", text_color="white", font=customtkinter.CTkFont(size=18), width=150, height=40, border_width=1, border_color="white")
        button.grid(row=1, column=1, pady=(270,200), padx=(355,10), sticky='nw')


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
        
    # Add Light Command
    def addlight(self):
        light_name = self.entry1.get()
        ip_address = self.entry2.get()    
        
        if not light_name or not ip_address:
            # One or both fields are empty, display an error message
            error_text = "Error: Both fields must be filled!"
            self.error_label = customtkinter.CTkButton(self.frame, text=error_text, font=customtkinter.CTkFont(size=16), fg_color="#1a1a1a", hover_color="#1a1a1a", text_color=("red"))
            self.error_label.grid(row=1, column=1, pady=(330, 200), padx=(245, 10), sticky='nw')
        
            # Schedule the error message to disappear after 5 seconds
            self.after(5000, self.hide_error)
        else:
            
            # Append inputs into respective lists
            light_names.append(self.entry1.get())
            ip_addresses.append(self.entry2.get())
        
            # Write new data back to database
            with open("database.txt", "a") as f:
                f.write(f"{self.entry1.get()},{self.entry2.get()}\n")
            
            confirmation_text = f"Light {self.entry1.get()} has been added!"
            self.confirmation = customtkinter.CTkButton(self.frame, text=confirmation_text, font=customtkinter.CTkFont(size=16), fg_color="#1a1a1a", hover_color="#1a1a1a", text_color=("green"))
            self.confirmation.grid(row=1, column=1, pady=(330, 200), padx=(245, 10), sticky='nw')
        
            self.after(5000, self.hide_confirmation)
       
    # Hide Confirmation
    def hide_confirmation(self):
        self.confirmation.grid_forget()
        
    # Hide Error
    def hide_error(self):
        self.error_label.grid_forget()

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
    light_names, ip_addresses = get_light_information()
    print("Light Names:", light_names)
    print("IP Addresses:", ip_addresses)
    print("Number of Lines in the Array:", len(light_names))
    app = App()
    app.mainloop()
    
