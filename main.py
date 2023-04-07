import tkinter
from PIL import Image, ImageTk
from win32api import GetSystemMetrics

class TTRPGCharGen(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        container = tkinter.Frame(self)
        container.pack(fill="both", expand=True, anchor="center", side="left")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainPage, Shadowrun5E):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class MainPage(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent, bg="#1e1e20")
        self.controller = controller

        global Shadowrun_5E_Orig_Image, Shadowrun_5E_Image, DnD_5E_Orig_Image, DnD_5E_Image, Cyberpunk_2020_Orig_Image, Cyberpunk_2020_Image, World_Of_Darkness_Orig_Image, World_Of_Darkness_Image
        
        window_height = GetSystemMetrics(1) #Workaround until I figure out how to change button size dynamically
        LogoHeight = window_height // 4
        LogoWidth = LogoHeight * 2

        tkinter.Grid.rowconfigure(self, 0, weight=1)
        tkinter.Grid.rowconfigure(self, 1, weight=1)
        tkinter.Grid.rowconfigure(self, 2, weight = 1)
        tkinter.Grid.columnconfigure(self, 0, weight=1)
        tkinter.Grid.columnconfigure(self, 1, weight=1)

        label = tkinter.Label(self, text="Tabletop RPG Character Generation Multitool", font=("Arial", 32), fg="White", bg="#1e1e20", pady=50)
        label.grid(row=0, column=0, columnspan=2, sticky="n")

        Shadowrun_5E_Orig_Image = Image.open("img/Shadowrun_5E_Logo.png")
        Shadowrun_5E_Image = ImageTk.PhotoImage(Shadowrun_5E_Orig_Image.resize((LogoWidth, LogoHeight), Image.ANTIALIAS))
        Shadowrun_5E_Button = tkinter.Button(self, bg="#1e1e20", activebackground="#1e1e20", bd=0, image=Shadowrun_5E_Image, command= lambda: controller.show_frame("Shadowrun5E"))
        Shadowrun_5E_Button.grid(row=1, column=0, sticky="n")

        DnD_5E_Orig_Image = Image.open("img/DnD_5E_Logo.png")
        DnD_5E_Image =  ImageTk.PhotoImage(DnD_5E_Orig_Image.resize((LogoWidth, LogoHeight), Image.ANTIALIAS))
        DnD_5E_Button = tkinter.Button(self, bg="#1e1e20", activebackground="#1e1e20", bd=0, image=DnD_5E_Image)
        DnD_5E_Button.grid(row=1, column=1, sticky="n")

        Cyberpunk_2020_Orig_Image = Image.open("img/Cyberpunk_2020_Logo.png")
        Cyberpunk_2020_Image = ImageTk.PhotoImage(Cyberpunk_2020_Orig_Image.resize((LogoWidth, LogoHeight), Image.ANTIALIAS))
        Cyberpunk_2020_Button = tkinter.Button(self, bg="#1e1e20", activebackground="#1e1e20", bd=0, image=Cyberpunk_2020_Image)
        Cyberpunk_2020_Button.grid(row=2, column=0, sticky="n")

        World_Of_Darkness_Orig_Image = Image.open("img/World_Of_Darkness_Logo.png")
        World_Of_Darkness_Image = ImageTk.PhotoImage(World_Of_Darkness_Orig_Image.resize((LogoWidth, LogoHeight), Image.ANTIALIAS))
        World_Of_Darkness_Button = tkinter.Button(self, bg="#1e1e20", activebackground="#1e1e20", bd=0, image=World_Of_Darkness_Image)
        World_Of_Darkness_Button.grid(row=2, column=1, sticky="n") 

class Shadowrun5E(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent, bg="#1e1e20")
        self.controller = controller

        tkinter.Grid.rowconfigure(self, 0, weight=1)
        tkinter.Grid.rowconfigure(self, 1, weight=1)
        tkinter.Grid.rowconfigure(self, 2, weight = 1)
        tkinter.Grid.columnconfigure(self, 0, weight=1)
        tkinter.Grid.columnconfigure(self, 1, weight=1)
        
        label = tkinter.Label(self, text="Shadowrun", font=("Arial", 32), fg="White", bg="#1e1e20", pady=50)
        label.grid(row=0, column=0, columnspan=2, sticky="n")

if __name__ == "__main__":
    app = TTRPGCharGen()
    app.title("TTRPG CharGen Multitool")
    app.geometry("1280x720")
    app.minsize(1280, 720)
    app.config(background = "#1e1e20")
    app.mainloop()
