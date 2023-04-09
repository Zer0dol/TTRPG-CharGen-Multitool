import tkinter
from tkinter import ttk
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

        self.Shadowrun_5E_Orig_Image = Image.open("img/Shadowrun_5E_Logo.png")
        self.Shadowrun_5E_Image = ImageTk.PhotoImage(self.Shadowrun_5E_Orig_Image.resize((LogoWidth, LogoHeight), Image.LANCZOS))
        Shadowrun_5E_Button = tkinter.Button(self, bg="#1e1e20", activebackground="#1e1e20", bd=0, image=self.Shadowrun_5E_Image, command= lambda: controller.show_frame("Shadowrun5E"))
        Shadowrun_5E_Button.grid(row=1, column=0, sticky="n")

        self.DnD_5E_Orig_Image = Image.open("img/DnD_5E_Logo.png")
        self.DnD_5E_Image =  ImageTk.PhotoImage(self.DnD_5E_Orig_Image.resize((LogoWidth, LogoHeight), Image.LANCZOS))
        DnD_5E_Button = tkinter.Button(self, bg="#1e1e20", activebackground="#1e1e20", bd=0, image=self.DnD_5E_Image, command= lambda: controller.show_frame("DnD5E"))
        DnD_5E_Button.grid(row=1, column=1, sticky="n")

        self.Cyberpunk_2020_Orig_Image = Image.open("img/Cyberpunk_2020_Logo.png")
        self.Cyberpunk_2020_Image = ImageTk.PhotoImage(self.Cyberpunk_2020_Orig_Image.resize((LogoWidth, LogoHeight), Image.LANCZOS))
        Cyberpunk_2020_Button = tkinter.Button(self, bg="#1e1e20", activebackground="#1e1e20", bd=0, image=self.Cyberpunk_2020_Image, command = lambda: controller.show_frame("Cyberpunk_2020"))
        Cyberpunk_2020_Button.grid(row=2, column=0, sticky="n")

        self.World_Of_Darkness_Orig_Image = Image.open("img/World_Of_Darkness_Logo.png")
        self.World_Of_Darkness_Image = ImageTk.PhotoImage(self.World_Of_Darkness_Orig_Image.resize((LogoWidth, LogoHeight), Image.LANCZOS))
        World_Of_Darkness_Button = tkinter.Button(self, bg="#1e1e20", activebackground="#1e1e20", bd=0, image=self.World_Of_Darkness_Image, command = lambda: controller.show_frame("World_Of_Darkness"))
        World_Of_Darkness_Button.grid(row=2, column=1, sticky="n") 

class Shadowrun5E(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent, bg="#1e1e20")
        self.controller = controller
        global window_height

        window_height = GetSystemMetrics(1) #Workaround until I figure out how to change button size dynamically
        LogoHeight = window_height // 8
        LogoWidth = LogoHeight * 2

        #tkinter.Grid.rowconfigure(self, 0, weight=1)
        tkinter.Grid.rowconfigure(self, 1, weight=1)
        tkinter.Grid.rowconfigure(self, 2, weight = 1)
        #tkinter.Grid.columnconfigure(self, 0, weight=1)
        tkinter.Grid.columnconfigure(self, 1, weight=1)
        
        self.Shadowrun_5E_Orig_Logo = Image.open("img/Shadowrun_5E_Logo.png")
        self.Shadowrun_5E_Logo = ImageTk.PhotoImage(self.Shadowrun_5E_Orig_Logo.resize((LogoWidth, LogoHeight), Image.LANCZOS))
        label = tkinter.Label(self, image=self.Shadowrun_5E_Logo, bg="#1e1e20", pady=30)
        label.grid(row=0, column=0, sticky="wn", padx=20, pady=20)

        Back_Button = tkinter.Button(self, bg="#272727", activebackground="#313131", bd=0, font=("Arial", 14), width=25, height=2, fg="White", activeforeground="White", text="Назад", command=lambda:controller.show_frame("MainPage"))
        Back_Button.grid(row=1, column=0, sticky="nw", padx=10, pady=0)

        style = ttk.Style()
        style.theme_create( "TTRPGChargen", parent="alt", settings={
            "TNotebook":{
                "configure": {"tabmargins":[10, 10, 20, 10], "background": "#1e1e20"}},
            "TNotebook.Tab": {
                "configure": {"padding": [30, 15], "background":"#1e1e20", "font":("Arial", 13), "foreground": "white", "borderwidth":[0]},
                "map": {"background": [("selected", "#313131"), ("!active", "#1e1e20"), ("active", "#272727")],
                        "expand": [("selected", [1, 1, 1, 0])]}
            }
        })
        style.theme_use("TTRPGChargen")
        style.layout("TNotebook", [])
        style.configure("TNotebook", tabmargins=0)

        Shadowrun_Notebook = ttk.Notebook(self, style="TNotebook")
        Shadowrun_Notebook_Priorities = tkinter.Frame(Shadowrun_Notebook, background="#1e1e20")
        Shadowrun_Notebook_Attributes = tkinter.Frame(Shadowrun_Notebook, background="#1e1e20")
        Shadowrun_Notebook_MagicResonance = tkinter.Frame(Shadowrun_Notebook, background="#1e1e20")
        Shadowrun_Notebook_Traits = tkinter.Frame(Shadowrun_Notebook, background="#1e1e20")
        Shadowrun_Notebook_Knowledge = tkinter.Frame(Shadowrun_Notebook, background="#1e1e20")
        Shadowrun_Notebook_Skills = tkinter.Frame(Shadowrun_Notebook, background="#1e1e20")
        Shadowrun_Notebook_Resourses = tkinter.Frame(Shadowrun_Notebook, background="#1e1e20")
        Shadowrun_Notebook.add(Shadowrun_Notebook_Priorities, text="Приоритеты")
        Shadowrun_Notebook.add(Shadowrun_Notebook_Attributes, text = "Атрибуты")
        Shadowrun_Notebook.add(Shadowrun_Notebook_MagicResonance, text="Магия")
        Shadowrun_Notebook.add(Shadowrun_Notebook_Traits, text="Качества")
        Shadowrun_Notebook.add(Shadowrun_Notebook_Knowledge, text="Знания")
        Shadowrun_Notebook.add(Shadowrun_Notebook_Skills, text="Умения")
        Shadowrun_Notebook.add(Shadowrun_Notebook_Resourses, text="Снаряжение")
        Shadowrun_Notebook.grid(row=0, rowspan=3, column=1, sticky="nwse", pady=20, padx=(0, 20))

class DnD5E(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent, bg="#1e1e20")
        self.controller = controller
        global window_height

        window_height = GetSystemMetrics(1) #Workaround until I figure out how to change button size dynamically
        LogoHeight = window_height // 8
        LogoWidth = LogoHeight * 2

        #tkinter.Grid.rowconfigure(self, 0, weight=1)
        tkinter.Grid.rowconfigure(self, 1, weight=1)
        tkinter.Grid.rowconfigure(self, 2, weight = 1)
        tkinter.Grid.columnconfigure(self, 0, weight=1)
        tkinter.Grid.columnconfigure(self, 1, weight=1)
        
        self.DnD_5E_Orig_Logo = Image.open("img/DnD_5E_Logo.png")
        self.DnD_5E_Logo = ImageTk.PhotoImage(self.DnD_5E_Orig_Logo.resize((LogoWidth, LogoHeight), Image.LANCZOS))
        label = tkinter.Label(self, image=self.DnD_5E_Logo, font=("Arial", 32), fg="White", bg="#1e1e20", pady=30)
        label.grid(row=0, column=0, sticky="wn", padx=20, pady=20)

        Back_Button = tkinter.Button(self, bg="#313131", activebackground="#272727", bd=0, font=("Arial", 14), width=25, height=2, fg="White", activeforeground="White", text="Назад", command=lambda:controller.show_frame("MainPage"))
        Back_Button.grid(row=1, column=0, sticky="nw", padx=10, pady=0)

class Cyberpunk_2020(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent, bg="#1e1e20")
        self.controller = controller
        global window_height

        window_height = GetSystemMetrics(1) #Workaround until I figure out how to change button size dynamically
        LogoHeight = window_height // 8
        LogoWidth = LogoHeight * 2

        #tkinter.Grid.rowconfigure(self, 0, weight=1)
        tkinter.Grid.rowconfigure(self, 1, weight=1)
        tkinter.Grid.rowconfigure(self, 2, weight = 1)
        tkinter.Grid.columnconfigure(self, 0, weight=1)
        tkinter.Grid.columnconfigure(self, 1, weight=1)
        
        self.Cyberpunk_2020_Orig_Logo = Image.open("img/Cyberpunk_2020_Logo.png")
        self.Cyberpunk_2020_Logo = ImageTk.PhotoImage(self.Cyberpunk_2020_Orig_Logo.resize((LogoWidth, LogoHeight), Image.LANCZOS))
        label = tkinter.Label(self, image=self.Cyberpunk_2020_Logo, font=("Arial", 32), fg="White", bg="#1e1e20", pady=30)
        label.grid(row=0, column=0, sticky="wn", padx=20, pady=20)

        Back_Button = tkinter.Button(self, bg="#313131", activebackground="#272727", bd=0, font=("Arial", 14), width=25, height=2, fg="White", text="Назад", activeforeground="White", command=lambda:controller.show_frame("MainPage"))
        Back_Button.grid(row=1, column=0, sticky="nw", padx=10, pady=0)

class World_Of_Darkness(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent, bg="#1e1e20")
        self.controller = controller
        global window_height

        window_height = GetSystemMetrics(1) #Workaround until I figure out how to change button size dynamically
        LogoHeight = window_height // 8
        LogoWidth = LogoHeight * 2

        #tkinter.Grid.rowconfigure(self, 0, weight=1)
        tkinter.Grid.rowconfigure(self, 1, weight=1)
        tkinter.Grid.rowconfigure(self, 2, weight = 1)
        tkinter.Grid.columnconfigure(self, 0, weight=1)
        tkinter.Grid.columnconfigure(self, 1, weight=1)
        
        self.World_Of_Darkness_Orig_Logo = Image.open("img/World_Of_Darkness_Logo.png")
        self.World_Of_Darkness_Logo = ImageTk.PhotoImage(self.World_Of_Darkness_Orig_Logo.resize((LogoWidth, LogoHeight), Image.LANCZOS))
        label = tkinter.Label(self, image=self.World_Of_Darkness_Logo, font=("Arial", 32), fg="White", bg="#1e1e20", pady=30)
        label.grid(row=0, column=0, sticky="wn", padx=20, pady=20)

        Back_Button = tkinter.Button(self, bg="#313131", activebackground="#272727", bd=0, font=("Arial", 14), width=25, height=2, fg="White", text="Назад", activeforeground="White", command=lambda:controller.show_frame("MainPage"))
        Back_Button.grid(row=1, column=0, sticky="nw", padx=10, pady=0)

if __name__ == "__main__":
    app = TTRPGCharGen()
    app.title("TTRPG CharGen Multitool")
    app.geometry("1280x720")
    app.minsize(1280, 720)
    app.config(background = "#1e1e20")
    app.mainloop()
