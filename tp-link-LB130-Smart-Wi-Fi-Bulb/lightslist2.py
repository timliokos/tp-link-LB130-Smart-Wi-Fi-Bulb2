import customtkinter
from CTkTable import *

root = customtkinter.CTk()

value = [["Light Name","Light IP Address"],
         ["Light A1","192.168.1.100"],
         ["Light A2","192.168.1.101"],
         ["Light B1","192.168.1.102"],
         ["Light B2","192.168.1.103"],
         ["Light B3","192.168.1.104"],
         ["Light B4","192.168.1.105"],
         ["Light B5","192.168.1.106"],
         ["Light C1","192.168.1.107"],
         ["Light C2","192.168.1.108"],
         ["Light C3","192.168.1.109"],
         ["Light D1","192.168.1.110"],
         ["Light D2","192.168.1.111"],
         ["Light D3","192.168.1.112"],
         ["Light D4","192.168.1.113"],
         ["Light D5","192.168.1.114"]]

table = CTkTable(master=root, row=16, column=2, values=value)
table.pack(expand=True, fill="both", padx=20, pady=20)

root.mainloop()