import tkinter as tk
from functools import partial
window = tk.Tk()
window.title('SANDI CAESAR - GUI')
window.resizable(0,0)
window.geometry('1070x395')
#window.grid_propagate(False)

def proses(ed):
    alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    hasil_kata = ''
    kata = txt_input.get(1.0,tk.END).upper()
    kunci = int(ent_inputKey.get())
    #print(kata)
    for x in kata:              # Mengecek tiap huruf dalam kata
        if x not in alfabet:    # Jika huruf bukan alfabet huruf akan ditambahkan ke hasil_kata dan perulangan dilanjutkan
            hasil_kata += x
            continue

        if(ed==1):
            num = alfabet.find(x) + kunci   # Proses encode (index + kunci)
        else:
            num = alfabet.find(x) - kunci   # Proses decode (index - kunci)

        if num >= 26:                       # Jika kunci melebihi dari 26 maka akan kembali lagi ke 0
            num -=26

        hasil_kata += alfabet[num]          # Menambahkan hasil_kata dengan alfabet yg cocok dengan index

    txt_output.delete(1.0,tk.END)
    txt_output.insert(tk.END,hasil_kata)

    #lbl_output['text']= f'{hasil_kata}'     # Menampilkan hasil_kata ke dalam lbl_output
#LAYOUT
frm_buttons = tk.Frame(window)
frm_texts   = tk.Frame(window)

window.columnconfigure([0],weight=1)
frm_texts.rowconfigure([1],weight=1)

#DECLARATIONS
txt_input = tk.Text(master=frm_texts,width='35',height='10',font=("Lato", 20))  #frm texts
txt_input.insert(1.0,'ABCDE\nFGHIJ\nKLMNO\nPQRST\nUVWXYZ')
txt_output = tk.Text(master=frm_texts,width='35',height='10',font=("Lato", 20))
txt_output.insert(1.0,'BCDEF\nGHIJK\nLMNOP\nQRSTU\nVWXYZA')

ent_inputKey = tk.Entry(master=frm_buttons,text='1')  #frm_buttons
ent_inputKey.insert(1,'1')
btn_encode   = tk.Button(master=frm_buttons,text='ENCODE',command=partial(proses,1))
btn_decode   = tk.Button(master=frm_buttons,text='DECODE',command=partial(proses,2))
lbl_key      = tk.Label(master=frm_buttons,text='Masukkan Kunci')



#PACK-IN
lbl_key.grid(row=0,column=0)
ent_inputKey.grid(row=0,column=1)
btn_encode.grid(row=1,column=0)
btn_decode.grid(row=1,column=1)

txt_input.grid(row=0,column=0)
txt_output.grid(row=0,column=1)

frm_buttons.grid(row=0,column=0)
frm_texts.grid(row=1,column=0)

window.mainloop()
