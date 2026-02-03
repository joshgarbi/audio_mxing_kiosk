import ttkbootstrap as ttk
import tkinter as tk
from audiometer import GradientAudioMeter
from ttkbootstrap.constants import *
from fader import FaderManager

def drawfaderbank(self, master):
    self.canvas = ttk.Canvas(master, width=self.width, height=self.height, highlightthickness=0)
    self.canvas.pack(fill="both", expand=True)
        
    self.faderBank = ttk.Frame(master, style="secondary.TFrame")
    self.faderBank.place(x=170, y=0, width=self.width - 170, height=self.height)
    
    # self.fader1 = Fader(self.faderBank, x=20, y=20, label="Fader 1")
    self.faders = FaderManager(self.faderBank)
    self.faders.createFaders()
    self.faders.updateAll()


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

