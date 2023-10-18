import customtkinter
import subprocess
import tkinter as tk

# Appearance Settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Configure Window
root = customtkinter.CTk()

# Window Size
root.geometry("1100x480")



# Login Method
def login():
     
    username = entry1.get()
    password = entry2.get()

    if username == "admin" and password == "password":
        # Open Home Page
        subprocess.Popen(["python", "homepage.py"])
        # Close Current Window
        root.destroy()
    else:
        print("Invalid username or password")



# Login Frame
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=60, padx=360, fill="both", expand=True)

# Page Heading
label = customtkinter.CTkLabel(master=frame, text="D633 LMMS Login", font=customtkinter.CTkFont(size=30, weight="bold"))
label.pack(pady=(50,20), padx=10)

# Username Entry
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username", width=250, height=40)
entry1.pack(pady=12, padx=10)

# Password Entry
entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*", width=250, height=40)
entry2.pack(pady=12, padx=10)

# Login Button
button = customtkinter.CTkButton(master=frame, text="Login", command=login, fg_color="#44dd45", hover_color="#02c910", text_color="black", font=customtkinter.CTkFont(size=18), width=150, height=40, border_width=3, border_color="white")
button.pack(pady=12, padx=10)

# Start Main Event Loop
root.mainloop()