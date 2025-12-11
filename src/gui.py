import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import random
import test

# A simple GUI application with audio faders
class SimpleApp:
    def __init__(self, master):
        self.master = master
        master.title("Audio Fader Control")
    
        style = ttk.Style()
        style.configure("Gradient.Vertical.TProgressbar", troughcolor="black", bordercolor="black", background="green")

        # Create a canvas for the gradient background
        self.canvas = ttk.Canvas(master, width=1240, height=720, highlightthickness=0)
        self.canvas.bind("<Configure>", self.on_resize)
        self.canvas.pack(fill="both", expand=True)
        self.draw_gradient()

        # Frame to hold the content
        self.content_frame = ttk.Frame(master, style="TFrame")
        self.content_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.label = ttk.Label(self.content_frame, font=("Helvetica", 16), background="", borderwidth=0)
        self.label.pack(pady=10)

        # Frame to hold the faders
        self.fader_frame = ttk.Frame(self.content_frame, style="TFrame", borderwidth=0)
        self.fader_frame.pack(pady=20)

        # Fader group 1
        self.fader_group1_label = ttk.Frame(self.fader_frame, style="TFrame", borderwidth=0)
        self.fader_group1_label.pack(side=LEFT, padx=20)


        # Fader 1
        self.fader1_container = ttk.Frame(self.fader_group1_label, style="TFrame", borderwidth=0)
        self.fader1_container.pack(side=LEFT, padx=10)
        self.fader1_label = ttk.Label(self.fader1_container, text="Fader 1", font=("Helvetica", 12), background="", borderwidth=0)
        self.fader1_label.pack()
        self.fader1 = ttk.Scale(self.fader1_container, from_=100, to=0, orient=VERTICAL, length=200, command=self.update_fader1_value, style="TScale")
        self.fader1.pack()
        self.fader1_value = ttk.Label(self.fader1_container, text="0", font=("Helvetica", 10), background="", borderwidth=0)
        self.fader1_value.pack()

        #Level indicator 1 (should turn green/yellow/red based on level)
        self.level1_label = ttk.Label(self.fader_group1_label, font=("Helvetica", 12), background="", borderwidth=0)
        self.level1_label.pack(pady=(10,0))
        self.level1 = test.GradientAudioMeter(self.fader_group1_label, width=25, height=200)
    
        self.level1.pack(side=RIGHT, pady=5)
        # level should bounce around fader value
        self.update_level1()
        
        # Fader group 2
        self.fader_group2_label = ttk.Frame(self.fader_frame, style="TFrame", borderwidth=0)
        self.fader_group2_label.pack(side=LEFT, padx=20)

        # Fader 2
        self.fader2_container = ttk.Frame(self.fader_group2_label, style="TFrame", borderwidth=0)
        self.fader2_container.pack(side=LEFT, padx=10)
        self.fader2_label = ttk.Label(self.fader2_container, text="Fader 2", font=("Helvetica", 12), background="", borderwidth=0)
        self.fader2_label.pack()
        self.fader2 = ttk.Scale(self.fader2_container, from_=100, to=0, orient=VERTICAL, length=200, command=self.update_fader2_value, style="TScale")
        self.fader2.pack()
        self.fader2_value = ttk.Label(self.fader2_container, text="0", font=("Helvetica", 10), background="", borderwidth=0)
        self.fader2_value.pack()

        # Level indicator 2 (should turn green/yellow/red based on level)
        self.level2_label = ttk.Label(self.fader_group2_label, font=("Helvetica", 12), background="", borderwidth=0)
        self.level2_label.pack(pady=(10,0))
        self.level2 = ttk.Progressbar(self.fader_group2_label, orient=VERTICAL, length=200, mode='determinate', maximum=100, style="success.Vertical.TProgressbar")
        self.level2.pack(side=RIGHT, pady=5)
        # level should bounce around fader value
        self.update_level2()
    
        # Fader group 3 
        self.fader_group3_label = ttk.Frame(self.fader_frame, style="TFrame", borderwidth=0)
        self.fader_group3_label.pack(side=LEFT, padx=20)

        # Fader 3
        self.fader3_container = ttk.Frame(self.fader_group3_label, style="TFrame", borderwidth=0)
        self.fader3_container.pack(side=LEFT, padx=10)
        self.fader3_label = ttk.Label(self.fader3_container, text="Fader 3", font=("Helvetica", 12), background="", borderwidth=0)
        self.fader3_label.pack()
        self.fader3 = ttk.Scale(self.fader3_container, from_=100, to=0, orient=VERTICAL, length=200, command=self.update_fader3_value, style="TScale")
        self.fader3.pack()
        self.fader3_value = ttk.Label(self.fader3_container, text="0", font=("Helvetica", 10), background="", borderwidth=0)
        self.fader3_value.pack()

        # Level indicator 3
        self.level3_label = ttk.Label(self.fader_group3_label, font=("Helvetica", 12), background="", borderwidth=0)
        self.level3_label.pack(pady=(10,0))
        self.level3 = ttk.Progressbar(self.fader_group3_label, orient=VERTICAL, length=200, mode='determinate', maximum=100, style="success.Vertical.TProgressbar")
        self.level3.pack(side=RIGHT, pady=5)
        self.update_level3()

    def draw_gradient(self, size=(1240, 720)):
        # Draw a vertical gradient from blue to white
        width, height = size
        for i in range(height):
            r = int(90 * (i / height))
            g = int(100 * (i / height))
            b = int(130 * (i / height))
            color = f"#{r:02x}{g:02x}{b:02x}"
            self.canvas.create_line(0, i, width, i, fill=color)
    
    def on_resize(self, event):
        self.canvas.delete("all")
        self.draw_gradient((event.width, event.height))

    def update_fader1_value(self, value):
        self.fader1_value.config(text=f"{int(float(value))}")

    def update_fader2_value(self, value):
        self.fader2_value.config(text=f"{int(float(value))}")

    def update_fader3_value(self, value):
        self.fader3_value.config(text=f"{int(float(value))}")

    def update_level1(self):
        fader_value = self.fader1.get()
        # Simulate level bouncing around fader value
        level_value = max(0, min(100, int(fader_value + random.randint(-10, 10))))
        self.level1['value'] = level_value
        self.master.after(100, self.update_level1)
       
    def update_level2(self):
        fader_value = self.fader2.get()
        # Simulate level bouncing around fader value
        level_value = max(0, min(100, int(fader_value + random.randint(-10, 10))))
        self.level2['value'] = level_value
        self.master.after(100, self.update_level2)

    def update_level3(self):
        fader_value = self.fader3.get()
        # Simulate level bouncing around fader value
        level_value = max(0, min(100, int(fader_value + random.randint(-10, 10))))
        self.level3['value'] = level_value
        self.master.after(100, self.update_level3)

if __name__ == "__main__":
    app = ttk.Window(themename="darkly", scaling=1.5)  # Modern theme with larger scaling
    SimpleApp(app)
    app.mainloop()