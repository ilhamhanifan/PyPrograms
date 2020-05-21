import tkinter as tk
window = tk.Tk()
window.title("Latihan Tkinter Form ")

#FORM FRAME
labels = [
    'first name:','last name:','Address Line 1:','Address Line 2:',
    'City:','State/Province:','Postal Code:','Country'
]

frm_form = tk.Frame()
frm_form.pack()

for i in range(len(labels)):
    lbl = tk.Label(master=frm_form,text=labels[i])
    ent = tk.Entry(master=frm_form,width=20)
    lbl.grid(row=i,column=0,sticky='e')
    ent.grid(row=i,column=1)

# BUTTON FRAME
frm_button = tk.Frame()
frm_button.pack(fill=tk.X)

btn_clear = tk.Button(master=frm_button,text = 'Clear')
btn_clear.pack(side=tk.RIGHT)

btn_submit = tk.Button(master=frm_button,text='Submit')
btn_submit.pack(side=tk.RIGHT)

window.mainloop()