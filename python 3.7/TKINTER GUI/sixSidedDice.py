import random
import tkinter as tk

def getnumber():
    lbl_number['text'] = f"{random.randint(1,6)}"

window = tk.Tk()

btn_roll = tk.Button(text='Roll', width = 20,height=5,command=getnumber)
btn_roll.pack()

lbl_number = tk.Label(text='1')
lbl_number.pack()



window.mainloop()