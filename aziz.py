#!/usr/bin/env python3
#  Aziz.py
#  tkinter gui for xbacklight command.
#  "Aziz Light!" 

import os
import subprocess
from math import ceil
from tkinter import *

scriptname = "Aziz 1.0"
        
def get_backlight():
    level = subprocess.check_output(['xbacklight', '-get'])
    level = level.decode('utf-8')
    level = ceil(float(level))
    return(level)

def set_backlight(level):
    command = "xbacklight -set " + str(level)
    os.system(command)

def reset_backlight():
    previous_value = current_bl
    scale.set(previous_value)
    set_backlight(previous_value)


current_bl = get_backlight()

window = Tk()
window.title("{}".format(scriptname))

top_frame = Frame(window)
middle_frame = Frame(window)
bottom_frame = Frame(window)

label = Label(top_frame, bd=4, anchor=CENTER, #relief="groove",
              text="Set backlight level:", font="Verdana")
label.grid(row=0, column=0)

scale = Scale(middle_frame, from_=0, to=100,
              command=set_backlight, orient=HORIZONTAL, width=12,
              font="Verdana", relief="sunken",
              length=220, sliderlength=50, troughcolor="#c3c3c3")
scale.set(current_bl)
scale.grid(row=1, column=0, padx=4, pady=4, columnspan=2)

quit_button = Button(bottom_frame, text="OK", command=window.destroy)
quit_button.grid(row=1, column=1)

reset_button = Button(bottom_frame, text="Cancel", command=reset_backlight)
reset_button.grid(row=1, column=2)

top_frame.pack(padx=4, pady=4, ipadx=4, ipady=4)
middle_frame.pack(padx=4, pady=4, ipadx=4, ipady=4)
bottom_frame.pack(padx=4, pady=4, ipadx=4, ipady=4)

window.mainloop()
