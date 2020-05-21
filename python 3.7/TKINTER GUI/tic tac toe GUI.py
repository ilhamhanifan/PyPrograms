import tkinter as tk
from functools import partial
window = tk.Tk()
window.title('TIC TAC TOE 2 PLAYERS')
window.resizable(0,0)
#window.geometry('1070x395')
# P1 X   P2 O
p1Score = 0
p2Score = 0
movecount = 0

# ngambil nilai lbl_turn. Nentuin tile X atau O, sesuai gilirannya
def getTile():
    turn = lbl_turn['text']
    if turn=='Player 1 (X)':
        tile = 'X'
    else:
        tile = 'O'
    return tile

# ganti turn dengan ngambil nilai lbl_turn, diubah jadi turn player berikutnya
def changeTurn():
    newTurn = lbl_turn['text']
    if newTurn=='Player 1 (X)':
        newTurn = 'Player 2 (O)'
        lbl_turn['text'] = newTurn
    elif newTurn=='Player 2 (O)':
        newTurn = 'Player 1 (X)'
        lbl_turn['text'] = newTurn
    return newTurn

# mengganti tile dengan X atau O, relatif terhadap button mana yang ditekan
def changeTile(btn,tile):
    if btn==1:
        btn_box1['text'] = tile
    elif btn==2:
        btn_box2['text'] = tile
    elif btn==3:
        btn_box3['text'] = tile

    elif btn==4:
        btn_box4['text'] = tile
    elif btn==5:
        btn_box5['text'] = tile
    elif btn==6:
        btn_box6['text'] = tile

    elif btn==7:
        btn_box7['text'] = tile
    elif btn==8:
        btn_box8['text'] = tile
    elif btn==9:
        btn_box9['text'] = tile

# mengecek jika suatu tile sudah terisi atau belum. True jika terisi
def isFilled(btn):
    tiles = ['X','O']
    if btn==1 and btn_box1['text'] in tiles:
        return True
    elif btn==2 and btn_box2['text'] in tiles:
        return True
    elif btn==3 and btn_box3['text'] in tiles:
        return True

    elif btn==4 and btn_box4['text'] in tiles:
        return True
    elif btn==5 and btn_box5['text'] in tiles:
        return True
    elif btn==6 and btn_box6['text'] in tiles:
        return True

    elif btn==7 and btn_box7['text'] in tiles:
        return True
    elif btn==8 and btn_box8['text'] in tiles:
        return True
    elif btn==9 and btn_box9['text'] in tiles:
        return True
    else:
        return False

# memeriksa jika suatu player menang. akan mencetak PLAYER WINS
def checkWin(win,tile):
    global p1Score
    global p2Score

    print(tile)
    if win is True:
        print("winnerfound")
        if tile == 'X':
            p1Score+=1
            lbl_p1Score['text']='Skor P1 : '+str(p1Score)
            lbl_winner['text'] = '|  P1 WINS!'
        elif tile == 'O':
            p2Score+=1
            lbl_p2Score['text']='Skor P2 : '+str(p2Score)
            lbl_winner['text'] = '|  P2 WINS!'
        disableButtons()    # Mematikan buttons ketika player menang
    elif win is False and movecount == 9:
        lbl_winner['text'] = '|  DRAW!'

# memeriksa board permainan. jika ada 3 tile yang berderet, return TRUE
def isPlayerWin(tiles): # 0 and 1
    print('isplayerwin' + tiles)
    return  (
             (btn_box1['text'] == tiles and btn_box2['text'] == tiles and btn_box3['text'] == tiles) or
             (btn_box4['text'] == tiles and btn_box5['text'] == tiles and btn_box6['text'] == tiles) or
             (btn_box7['text'] == tiles and btn_box8['text'] == tiles and btn_box9['text'] == tiles) or

             (btn_box7['text'] == tiles and btn_box4['text'] == tiles and btn_box1['text'] == tiles) or
             (btn_box8['text'] == tiles and btn_box5['text'] == tiles and btn_box2['text'] == tiles) or
             (btn_box9['text'] == tiles and btn_box6['text'] == tiles and btn_box3['text'] == tiles) or

             (btn_box7['text'] == tiles and btn_box5['text'] == tiles and btn_box3['text'] == tiles) or
             (btn_box9['text'] == tiles and btn_box5['text'] == tiles and btn_box1['text'] == tiles)
             )

# Mematikan akses buttons
def disableButtons():
    btn_box1['state'] = 'disabled'
    btn_box2['state'] = 'disabled'
    btn_box3['state'] = 'disabled'
    btn_box4['state'] = 'disabled'
    btn_box5['state'] = 'disabled'
    btn_box6['state'] = 'disabled'
    btn_box7['state'] = 'disabled'
    btn_box8['state'] = 'disabled'
    btn_box9['state'] = 'disabled'

# fungsi utama yang aktif ketika button ditekan
def btn_press(btn):
    global movecount
    movecount +=1
    print('move'+str(movecount))
    tile = getTile()
    condition = isFilled(btn)
    if not condition:
        changeTile(btn,tile)
        changeTurn()
    winner = isPlayerWin(tile)
    checkWin(winner,tile)

# reset papan
def resetBoard():
    global movecount
    resetButtons()
    movecount = 0
    if lbl_turn['text'] == 'Player 2 (O)':
        lbl_turn['text'] = 'Player 1 (X)'


# reset tombol ke keadaan semula
def resetButtons():
    btn_box1['text'] = ''; btn_box1['state'] = 'normal'
    btn_box2['text'] = ''; btn_box2['state'] = 'normal'
    btn_box3['text'] = ''; btn_box3['state'] = 'normal'
    btn_box4['text'] = ''; btn_box4['state'] = 'normal'
    btn_box5['text'] = ''; btn_box5['state'] = 'normal'
    btn_box6['text'] = ''; btn_box6['state'] = 'normal'
    btn_box7['text'] = ''; btn_box7['state'] = 'normal'
    btn_box8['text'] = ''; btn_box8['state'] = 'normal'
    btn_box9['text'] = ''; btn_box9['state'] = 'normal'

# DECLARATIONS

lbl_title = tk.Label(text='TIC TAC TOE',font=("Lato", 30))
frm_box = tk.Frame(padx=30,pady=10) #FRAME 1

btn_box1 = tk.Button(master=frm_box,width=5,height=5,font=("Lato", 10,'bold'),command=partial(btn_press,1))
btn_box2 = tk.Button(master=frm_box,width=5,height=5,font=("Lato", 10,'bold'),command=partial(btn_press,2))
btn_box3 = tk.Button(master=frm_box,width=5,height=5,font=("Lato", 10,'bold'),command=partial(btn_press,3))

btn_box4 = tk.Button(master=frm_box,width=5,height=5,font=("Lato", 10,'bold'),command=partial(btn_press,4))
btn_box5 = tk.Button(master=frm_box,width=5,height=5,font=("Lato", 10,'bold'),command=partial(btn_press,5))
btn_box6 = tk.Button(master=frm_box,width=5,height=5,font=("Lato", 10,'bold'),command=partial(btn_press,6))

btn_box7 = tk.Button(master=frm_box,width=5,height=5,font=("Lato", 10,'bold'),command=partial(btn_press,7))
btn_box8 = tk.Button(master=frm_box,width=5,height=5,font=("Lato", 10,'bold'),command=partial(btn_press,8))
btn_box9 = tk.Button(master=frm_box,width=5,height=5,font=("Lato", 10,'bold'),command=partial(btn_press,9))

frm_desc = tk.Frame() #FRAME 2

lbl_turn = tk.Label(master=frm_desc,text='Player 1 (X)',font=("Lato", 15))
lbl_winner = tk.Label(master=frm_desc,text='| ========',font=("Lato", 15))
lbl_p1Score = tk.Label(master=frm_desc,text='Skor P1 : 0',font=("Lato", 15),bg='#f04d67')
lbl_p2Score = tk.Label(master=frm_desc,text='Skor P2 : 0',font=("Lato", 15),bg='#7a78ff')
btn_reset = tk.Button(text='RESET',font=("Lato",15),command=partial(resetBoard)) #FRAME 3


# PACK-IN                       URUTAN: lbl_title, frm_box, frm_desc, btn_reset
lbl_title.grid(row=0,column=0)
frm_box.grid(row=1,column=0)

btn_box1.grid(row=2,column=0)
btn_box2.grid(row=2,column=1)
btn_box3.grid(row=2,column=2)

btn_box4.grid(row=1,column=0)
btn_box5.grid(row=1,column=1)
btn_box6.grid(row=1,column=2)

btn_box7.grid(row=0,column=0)
btn_box8.grid(row=0,column=1)
btn_box9.grid(row=0,column=2)

frm_desc.grid(row=2,column=0)

lbl_turn.grid(row=0,column=0)
lbl_winner.grid(row=0,column=1)
lbl_p1Score.grid(row=1,column=0)
lbl_p2Score.grid(row=1,column=1)

btn_reset.grid(row=3)

window.mainloop()