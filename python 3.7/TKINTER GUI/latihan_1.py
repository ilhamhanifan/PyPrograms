'''

Pengenalan Widget Label,Button,dan Entry

'''

import tkinter as tk
window = tk.Tk()

#Label Widget
greeting = tk.Label(
    text        ="Python Rocks!",
    width       =10,
    height      =10,
    foreground  ='white',
    background  ='black',
)
greeting.pack()

# Button Widget
button = tk.Button(
    text    = 'Click me',
    width   =25,
    height  =5,
    bg      ='blue',
    fg      ='yellow',
)
button.pack()

#Entry Widget
entry = tk.Entry(
    fg = 'yellow',
    bg = 'blue',
    width = 50
)
entry.pack()


window.mainloop()