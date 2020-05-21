import tkinter as tk

window = tk.Tk()
window.geometry('500x200')
frame1 = tk.Frame(master = window, height=100,bg='red')
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window,height=50,bg='yellow')
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=window,height=25,bg='blue')
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.mainloop()
