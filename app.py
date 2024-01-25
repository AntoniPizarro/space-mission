# Aplicación principal (cliente)

from tkinter import *
from tkinter import messagebox, simpledialog
from tkinter.ttk import *
from datetime import datetime

from start_config import *
from test import build_title_bar

root = Tk()

TITLE = app_cfg["tkinter"]["title"]
WIDTH = root.winfo_screenwidth() - 200
HEIGHT = root.winfo_screenheight() - 200

# Márgenes generales para los componentes
MARGIN_INT_X = 8
MARGIN_INT_Y = 4

def center_root(root):
    '''
    Centra y expande la ventana
    '''
    root.update_idletasks()

    width_monitor = root.winfo_screenwidth()
    height_monitor = root.winfo_screenheight()

    position_x = (width_monitor - WIDTH) // 2
    position_y = (height_monitor - HEIGHT) // 2

    root.geometry(f"{WIDTH}x{HEIGHT}+{position_x}+{position_y}")
    root.state("zoomed")

def init_config():
    root.title(f"{TITLE}")
    root.iconbitmap('assets/rocket-logo.ico')
    root.wm_iconbitmap(PhotoImage(file='assets/rocket-logo.ico'))
    root.configure(background="#3D3D3D")
    center_root(root)
    
    # Barra de título personalizada
    #title_bar = build_title_bar(root, TITLE) # La devolvemos por si luego es necesario hacer algo mas

# Configuraciones
init_config()

print("OK!")
root.mainloop()