import tkinter as tk

def convert():
    lbl_f['text'] = f"{(int(ent_box.get()) -32) * 5/9}*C"

window = tk.Tk()
window.title("Fahrenheit To Celcius")

frm_layout = tk.Frame;

ent_box = tk.Entry(width='30')
ent_box.grid(row=0,column=0,pady=10,padx=(10,0))

lbl_f = tk.Label(text='0')
lbl_f.grid(row=0,column=1)

btn_convert = tk.Button(text='->',command=convert)
btn_convert.grid(row=0,column=2,padx=10,pady=10)

lbl_temprature  = tk.Label(text='0*C')
lbl_temprature.grid(row=0,column=3,padx=10,pady=10)

window.mainloop()