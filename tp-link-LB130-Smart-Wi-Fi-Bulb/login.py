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
def login(event=None):
     
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
frame.pack(pady=20, padx=360, fill="both", expand=True)

# Logo Icon
image1 = tk.PhotoImage(file="images/D633LOGO3.png")
new_width = 8
new_height = 8
resized_image1 = image1.subsample(new_width, new_height)
button_1 = customtkinter.CTkButton(master=frame, image=resized_image1, text="", fg_color="#212121", hover_color="#212121", font=customtkinter.CTkFont(size=18), width=50, height=40)
button_1.pack(pady=0, padx=10)
button_1.icon = resized_image1

# Page Heading
label = customtkinter.CTkLabel(master=frame, text="Login", font=customtkinter.CTkFont(size=30, weight="bold"))
label.pack(pady=(0,20), padx=10)

# Username Entry
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username", width=250, height=40)
entry1.pack(pady=12, padx=10)

# Password Entry
entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*", width=250, height=40)
entry2.pack(pady=12, padx=10)

# Login Button
button = customtkinter.CTkButton(master=frame, text="Login", command=login, fg_color="#1f538d", hover_color="#163b65", text_color="white", font=customtkinter.CTkFont(size=18), width=150, height=40, border_width=1, border_color="white")
button.pack(pady=12, padx=10)

# Binding 'Enter' Key as Login
root.bind('<Return>', login)

# Start Main Event Loop
root.mainloop()