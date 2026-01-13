import tkinter as tk  # Add at top of file
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import random
from PIL import Image, ImageTk

class SimpleApp:
    def __init__(self, width, height, master):
        self.master = master
        
        self.width = width     
        self.height = height   
        
        # Might adjust this line to work better with console API
        self.update_interval = 100  # milliseconds

        style = ttk.Style()
        # Configure a red (danger) button style with larger font/padding
        style.configure("danger.TButton", font=("Arial", 46), padding=16)
        style.configure("Dialog.TButton", font=("Arial", 18), padding=12)
        
        self.canvas = ttk.Canvas(master, width=self.width, height=self.height, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        
        ## power button in top left to quit the app
        self.button = ttk.Button(
            master,
            text="⏻",
            bootstyle="danger",
            command=self.quit_app,
            
        )
        
        self.button.configure(style="danger.TButton")
        
        self.button.place(x=20, y=20, width=120, height=120)
        
    
        
    def quit_app(self):
        sure_window = ttk.Toplevel(self.master)
        sure_window.title("Confirm Exit")
        sure_window.geometry("800x300")
        sure_window.resizable(False, False)
        sure_window.grab_set()  # Make this window modal
        label = ttk.Label(sure_window, text="Power Off?", font=("Arial", 24))
        label.pack(pady=20)
        yes_button = ttk.Button(sure_window, width=16, text="Shut Down", bootstyle="danger", style="Dialog.TButton", command=self.master.destroy)
        yes_button.pack(side="left", padx=30, pady=16)
        no_button = ttk.Button(sure_window, width=16, text="Cancel", bootstyle="secondary", style="Dialog.TButton", command=sure_window.destroy)
        no_button.pack(side="right", padx=30, pady=16)
            
        
if __name__ == "__main__":
    # Using a slightly darker theme to make neon colors pop
    app = ttk.Window(themename="darkly", scaling=1.5) 
    width = app.winfo_screenwidth()
    height = app.winfo_screenheight()
    print(f"Screen size: {width}x{height}")
    SimpleApp(width, height, app)
    app.attributes("-fullscreen", True)  # Launch in fullscreen
    app.resizable(False, False)
    app.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable window closing
    app.mainloop()