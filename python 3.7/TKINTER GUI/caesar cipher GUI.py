# Menggunakan Python 3.7
import tkinter as tk
window = tk.Tk()
window.title("Sandi Caesar - GUI")

def proses_encode():
    alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    hasil_kata=''
    kata = ent_txtInput.get()
    key  = int(ent_key.get())

    for x in kata:
        if x not in alfabet:
            hasil_kata += x
            continue

        num = alfabet.find(x) + key
        print(num)
        if num >= 26:  # Membatasi jika nilainya lebih dari 26, akan kembali ke 0
            num -= 26
        hasil_kata += alfabet[num]
    lbl_txtOutput['text'] = f'{hasil_kata}'

def proses_decode():
    alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    hasil_kata = ''
    kata = ent_txtInput.get()
    key  = ent_key.get()

    for x in kata:
        if x not in alfabet:
            hasil_kata += x
            continue
        num = alfabet.find(x) - key
        if num >= 26:  # Membatasi jika nilainya lebih dari 26, akan kembali ke 0
            num -= 26
        hasil_kata += alfabet[num]
    lbl_txtOutput['text'] = f'{hasil_kata}'

def getText():
    ham = ent_key.get()
    lbl_txtOutput['text'] = f'{ham}'

ent_txtInput = tk.Entry()
ent_txtInput.grid(row=0,column=1)

ent_key = tk.Entry()
ent_key.grid(row=2,column=0)

lbl_txtOutput = tk.Label()
lbl_txtOutput.grid(row=1,column=1)

btn_encode = tk.Button(text='encode',command=proses_encode)#proses_encode)
btn_encode.grid(row=0,column=0)

btn_decode = tk.Button(text='decode',command=proses_decode)
btn_decode.grid(row=1,column=0)

window.mainloop()