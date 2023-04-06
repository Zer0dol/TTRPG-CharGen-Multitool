import tkinter
from PIL import Image, ImageTk
from win32api import GetSystemMetrics

window_width, window_height = GetSystemMetrics(0), GetSystemMetrics(1)

window = tkinter.Tk()
window.geometry("1280x720")
window.minsize(1280, 720)
window.title("TTRPG CharGen Multitool")
window.config(background = "#1e1e20")

tkinter.Grid.rowconfigure(window, 0, weight=1)
tkinter.Grid.rowconfigure(window, 1, weight=1)
tkinter.Grid.rowconfigure(window, 2, weight = 1)
tkinter.Grid.columnconfigure(window, 0, weight=1)
tkinter.Grid.columnconfigure(window, 1, weight=1)

label = tkinter.Label(window,text="Tabletop RPG Character Generation Multitool", font=("Arial", 32), fg="White", bg="#1e1e20", pady=50)
label.grid(row=0, column=0, columnspan=2, sticky="n")

LogoHeight = window_height // 4 #Theese are placeholders. This will be like that until I figure out how to make button images update dynamically with window resolution
LogoWidth = LogoHeight * 2

Shadowrun_5E_Orig_Image = Image.open("img/Shadowrun_5E_Logo.png")
Shadowrun_5E_Image = ImageTk.PhotoImage(Shadowrun_5E_Orig_Image.resize((LogoWidth, LogoHeight), Image.ANTIALIAS))
Shadowrun_5E_Button = tkinter.Button(window, bg="#1e1e20", activebackground="#1e1e20", bd=0, image=Shadowrun_5E_Image)
Shadowrun_5E_Button.grid(row=1, column=0, sticky="n")

DnD_5E_Orig_Image = Image.open("img/DnD_5E_Logo.png")
DnD_5E_Image =  ImageTk.PhotoImage(DnD_5E_Orig_Image.resize((LogoWidth, LogoHeight), Image.ANTIALIAS))
DnD_5E_Button = tkinter.Button(window, bg="#1e1e20", activebackground="#1e1e20", bd=0, image=DnD_5E_Image)
DnD_5E_Button.grid(row=1, column=1, sticky="n")

Cyberpunk_2020_Orig_Image = Image.open("img/Cyberpunk_2020_Logo.png")
Cyberpunk_2020_Image = ImageTk.PhotoImage(Cyberpunk_2020_Orig_Image.resize((LogoWidth, LogoHeight), Image.ANTIALIAS))
Cyberpunk_2020_Button = tkinter.Button(window, bg="#1e1e20", activebackground="#1e1e20", bd=0, image=Cyberpunk_2020_Image)
Cyberpunk_2020_Button.grid(row=2, column=0, sticky="n")

World_Of_Darkness_Orig_Image = Image.open("img/World_Of_Darkness_Logo.png")
World_Of_Darkness_Image = ImageTk.PhotoImage(World_Of_Darkness_Orig_Image.resize((LogoWidth, LogoHeight), Image.ANTIALIAS))
World_Of_Darkness_Button = tkinter.Button(window, bg="#1e1e20", activebackground="#1e1e20", bd=0, image=World_Of_Darkness_Image)
World_Of_Darkness_Button.grid(row=2, column=1, sticky="n")

window.mainloop()
