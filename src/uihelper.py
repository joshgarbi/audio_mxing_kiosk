import ttkbootstrap as ttk
import tkinter as tk
from audiometer import GradientAudioMeter
from ttkbootstrap.constants import *

def drawfader(self, master):
    self.canvas = ttk.Canvas(master, width=self.width, height=self.height, highlightthickness=0)
    self.canvas.pack(fill="both", expand=True)
        
    self.faderBank = ttk.Frame(master, style="secondary.TFrame")
    self.faderBank.place(x=170, y=0, width=self.width - 170, height=self.height)
    self.fader1group = ttk.Frame(self.faderBank, style="tertiary.TFrame")
    self.fader1group.place(x=50, y=50, width=200, height=self.height - 200)
    
    self.fader1_container = ttk.Frame(self.fader1group, style="TFrame", borderwidth=0)
    self.fader1_container.pack(side=LEFT, padx=10)
    self.fader1_label = ttk.Label(self.fader1_container, text="Fader 1", font=("Helvetica", 24), background="", borderwidth=0)    
    self.fader1_label.pack()
        
    self.fader1slider = tk.Scale(self.fader1_container, from_=100, to=0, orient=VERTICAL, length=800, 
        command=self.change_fader1_value,
        bg='#2d7dd2', activebackground='#4a9eff',
        troughcolor='#1e1e1e', highlightthickness=0,
        sliderlength=160, sliderrelief='solid', width=100, bd=0)
        
        
    self.fader1slider.set(0.5)
    self.fader1slider.pack(pady=20)
        
    self.level1 = GradientAudioMeter(self.fader1group, width=50, height=800)
    self.level1.pack(side="right", pady=15)
    
    
    
    
    # def settings_menu():
        

def ip_settings(self, masterC):
    ip_frame = ttk.Frame(masterC)
    ip_frame.place(x=10, y=10, width=400, height=200)
    ipSettings = ttk.Entry(
        ip_frame,
        textvariable=self.ip,
        validate='focusout',          
    )
    ipSettings.configure(font=36)
    ipSettings.place(x=5, y=5, width=200, height=50)
    
    portSettings = ttk.Entry(
        ip_frame,
        textvariable=self.port,
        validate='focusout'
    )
    portSettings.configure(font=36)
    portSettings.place(x=210, y = 5, width=100, height=50)

