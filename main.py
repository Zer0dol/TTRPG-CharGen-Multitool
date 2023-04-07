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
        for F in (MainPage, Shadowrun5E, DnD5E, Cyberpunk_2020, World_Of_Darkness):
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
        global window_height
        window_height = GetSystemMetrics(1) #Workaround until I figure out how to change button size dynamically
        LogoHeight = window_height // 4
        LogoWidth = LogoHeight * 2

        tkinter.Grid.rowconfigure(self, 0, weight=1)
        tkinter.Grid.rowconfigure(self, 1, weight=1)
        tkinter.Grid.rowconfigure(self, 2, weight = 1)
        tkinter.Grid.columnconfigure(self, 0, weight=1)
        tkinter.Grid.columnconfigure(self, 1, weight=1)

        label = tkinter.Label(self, text="Tabletop RPG Character Generation Multitool", font=("Arial", 32), fg="White", bg="#1e1e20", pady=30)
        label.grid(row=0, column=0, columnspan=2, sticky="n")

        Shadowrun_5E_Orig_Image = Image.open("img/Shadowrun_5E_Logo.png")
        Shadowrun_5E_Image = ImageTk.PhotoImage(Shadowrun_5E_Orig_Image.resize((LogoWidth, LogoHeight), Image.LANCZOS))
        Shadowrun_5E_Button = tkinter.Button(self, bg="#1e1e20", activebackground="#1e1e20", bd=0, image=Shadowrun_5E_Image, command= lambda: controller.show_frame("Shadowrun5E"))
        Shadowrun_5E_Button.grid(row=1, column=0, sticky="n")

        DnD_5E_Orig_Image = Image.open("img/DnD_5E_Logo.png")
        DnD_5E_Image =  ImageTk.PhotoImage(DnD_5E_Orig_Image.resize((LogoWidth, LogoHeight), Image.LANCZOS))
        DnD_5E_Button = tkinter.Button(self, bg="#1e1e20", activebackground="#1e1e20", bd=0, image=DnD_5E_Image, command= lambda: controller.show_frame("DnD5E"))
        DnD_5E_Button.grid(row=1, column=1, sticky="n")

        Cyberpunk_2020_Orig_Image = Image.open("img/Cyberpunk_2020_Logo.png")
        Cyberpunk_2020_Image = ImageTk.PhotoImage(Cyberpunk_2020_Orig_Image.resize((LogoWidth, LogoHeight), Image.LANCZOS))
        Cyberpunk_2020_Button = tkinter.Button(self, bg="#1e1e20", activebackground="#1e1e20", bd=0, image=Cyberpunk_2020_Image, command = lambda: controller.show_frame("Cyberpunk_2020"))
        Cyberpunk_2020_Button.grid(row=2, column=0, sticky="n")

        World_Of_Darkness_Orig_Image = Image.open("img/World_Of_Darkness_Logo.png")
        World_Of_Darkness_Image = ImageTk.PhotoImage(World_Of_Darkness_Orig_Image.resize((LogoWidth, LogoHeight), Image.LANCZOS))
        World_Of_Darkness_Button = tkinter.Button(self, bg="#1e1e20", activebackground="#1e1e20", bd=0, image=World_Of_Darkness_Image, command = lambda: controller.show_frame("World_Of_Darkness"))
        World_Of_Darkness_Button.grid(row=2, column=1, sticky="n") 

class Shadowrun5E(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent, bg="#1e1e20")
        self.controller = controller
        global Shadowrun_5E_Orig_Logo, Shadowrun_5E_Logo
        global window_height

        window_height = GetSystemMetrics(1) #Workaround until I figure out how to change button size dynamically
        LogoHeight = window_height // 8
        LogoWidth = LogoHeight * 2

        #tkinter.Grid.rowconfigure(self, 0, weight=1)
        tkinter.Grid.rowconfigure(self, 1, weight=1)
        tkinter.Grid.rowconfigure(self, 2, weight = 1)
        tkinter.Grid.columnconfigure(self, 0, weight=1)
        tkinter.Grid.columnconfigure(self, 1, weight=1)
        
        Shadowrun_5E_Orig_Logo = Image.open("img/Shadowrun_5E_Logo.png")
        Shadowrun_5E_Logo = ImageTk.PhotoImage(Shadowrun_5E_Orig_Logo.resize((LogoWidth, LogoHeight), Image.LANCZOS))
        label = tkinter.Label(self, image=Shadowrun_5E_Logo, font=("Arial", 32), fg="White", bg="#1e1e20", pady=30)
        label.grid(row=0, column=0, sticky="wn", padx=20, pady=20)

        Back_Button = tkinter.Button(self, bg="#1e1e20", activebackground="#1e1e20", bd=1, font=("Arial", 14), fg="White", text="Назад", command=lambda:controller.show_frame("MainPage"))
        Back_Button.grid(row=1, column=0, sticky="nw", padx=110, pady=0)

class DnD5E(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent, bg="#1e1e20")
        self.controller = controller
        global DnD_5E_Orig_Logo, DnD_5E_Logo
        global window_height

        window_height = GetSystemMetrics(1) #Workaround until I figure out how to change button size dynamically
        LogoHeight = window_height // 8
        LogoWidth = LogoHeight * 2

        #tkinter.Grid.rowconfigure(self, 0, weight=1)
        tkinter.Grid.rowconfigure(self, 1, weight=1)
        tkinter.Grid.rowconfigure(self, 2, weight = 1)
        tkinter.Grid.columnconfigure(self, 0, weight=1)
        tkinter.Grid.columnconfigure(self, 1, weight=1)
        
        DnD_5E_Orig_Logo = Image.open("img/DnD_5E_Logo.png")
        DnD_5E_Logo = ImageTk.PhotoImage(DnD_5E_Orig_Logo.resize((LogoWidth, LogoHeight), Image.LANCZOS))
        label = tkinter.Label(self, image=DnD_5E_Logo, font=("Arial", 32), fg="White", bg="#1e1e20", pady=30)
        label.grid(row=0, column=0, sticky="wn", padx=20, pady=20)

        Back_Button = tkinter.Button(self, bg="#1e1e20", activebackground="#1e1e20", bd=1, font=("Arial", 14), fg="White", text="Назад", command=lambda:controller.show_frame("MainPage"))
        Back_Button.grid(row=1, column=0, sticky="nw", padx=110, pady=0)

class Cyberpunk_2020(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent, bg="#1e1e20")
        self.controller = controller
        global Cyberpunk_2020_Orig_Logo, Cyberpunk_2020_Logo
        global window_height

        window_height = GetSystemMetrics(1) #Workaround until I figure out how to change button size dynamically
        LogoHeight = window_height // 8
        LogoWidth = LogoHeight * 2

        #tkinter.Grid.rowconfigure(self, 0, weight=1)
        tkinter.Grid.rowconfigure(self, 1, weight=1)
        tkinter.Grid.rowconfigure(self, 2, weight = 1)
        tkinter.Grid.columnconfigure(self, 0, weight=1)
        tkinter.Grid.columnconfigure(self, 1, weight=1)
        
        Cyberpunk_2020_Orig_Logo = Image.open("img/Cyberpunk_2020_Logo.png")
        Cyberpunk_2020_Logo = ImageTk.PhotoImage(Cyberpunk_2020_Orig_Logo.resize((LogoWidth, LogoHeight), Image.LANCZOS))
        label = tkinter.Label(self, image=Cyberpunk_2020_Logo, font=("Arial", 32), fg="White", bg="#1e1e20", pady=30)
        label.grid(row=0, column=0, sticky="wn", padx=20, pady=20)

        Back_Button = tkinter.Button(self, bg="#1e1e20", activebackground="#1e1e20", bd=1, font=("Arial", 14), fg="White", text="Назад", command=lambda:controller.show_frame("MainPage"))
        Back_Button.grid(row=1, column=0, sticky="nw", padx=110, pady=0)

class World_Of_Darkness(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent, bg="#1e1e20")
        self.controller = controller
        global World_Of_Darkness_Orig_Logo, World_Of_Darkness_Logo
        global window_height

        window_height = GetSystemMetrics(1) #Workaround until I figure out how to change button size dynamically
        LogoHeight = window_height // 8
        LogoWidth = LogoHeight * 2

        #tkinter.Grid.rowconfigure(self, 0, weight=1)
        tkinter.Grid.rowconfigure(self, 1, weight=1)
        tkinter.Grid.rowconfigure(self, 2, weight = 1)
        tkinter.Grid.columnconfigure(self, 0, weight=1)
        tkinter.Grid.columnconfigure(self, 1, weight=1)
        
        World_Of_Darkness_Orig_Logo = Image.open("img/World_Of_Darkness_Logo.png")
        World_Of_Darkness_Logo = ImageTk.PhotoImage(World_Of_Darkness_Orig_Logo.resize((LogoWidth, LogoHeight), Image.LANCZOS))
        label = tkinter.Label(self, image=World_Of_Darkness_Logo, font=("Arial", 32), fg="White", bg="#1e1e20", pady=30)
        label.grid(row=0, column=0, sticky="wn", padx=20, pady=20)

        Back_Button = tkinter.Button(self, bg="#1e1e20", activebackground="#1e1e20", bd=1, font=("Arial", 14), fg="White", text="Назад", command=lambda:controller.show_frame("MainPage"))
        Back_Button.grid(row=1, column=0, sticky="nw", padx=110, pady=0)

if __name__ == "__main__":
    app = TTRPGCharGen()
    app.title("TTRPG CharGen Multitool")
    app.geometry("1280x720")
    app.minsize(1280, 720)
    app.config(background = "#1e1e20")
    app.mainloop()
