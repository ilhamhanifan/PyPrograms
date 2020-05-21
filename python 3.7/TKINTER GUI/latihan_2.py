import tkinter as tk
window  = tk.Tk()

label   = tk.Label(text='Name')
entry   = tk.Entry()
name    = entry.get()
text_box= tk.Text()

label.pack()
entry.pack()
text_box.pack()

entry.insert(0,'Han')
entry.delete(0,tk.END)
window.mainloop()