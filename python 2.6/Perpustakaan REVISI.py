'''
Menggunakan Python 2.6

Jadi di program ini user akan diminta tanggal setiap menggunakan program.
Hal ini diperlukan karena program tidak dapat menyimpan data tanggal, sehingga
tanggal perlu diubah secara manual. Tanggal diatur menggunakan modul datetime
yang sudah di include pada library python 2.6

Adapun beberapa Fungsi dari programnya:
1- Masukkan Tanggal Hari ini (dd-mm-yyyy)
   berguna untuk mengubah tanggal hari
2- Menu
   - Lihat Daftar Buku
     digunakan untuk melihat isi daftar buku

   - Lihat Pinjaman Buku
     digunakan untuk melihat pinjaman buku

   - Buat Pinjaman Buku
     digunakan untuk membuat pinjaman buku

   - Kembalikan Buku
     digunakan untuk mengembalikan buku

   - Tambahkan Buku
     digunakan untuk menambahkan buku

   - Logout (Ganti Tanggal Hari Ini)
     mereference ke fungsi yang mengubah tanggal hari

3 - Notifikasi Pinjaman
    fitur dimana yang akan mengingatkan jika ada pinjaman yang melebihi 7 hari.
'''
import datetime
global hari
#Kode,[Nama Buku,Pengarang,Jumlah,Terpinjam]
buku = {
    "a1":["Almanak Dewisri                   ","Kamajaya                          ",0,1],
    "a2":["Almanak Pembangunan               ","Ismail Lutan                      ",2,0],
    "a3":["Almanak Negara RI                 ","Iwan Gayo                         ",1,0],

    "b1": ["Biografi Abu Bakar Siddiq        ", "Prof.DR. Ali Muhammad Ash-Shalabi", 3, 1],
    "b2": ["Biografi H. Agus Salim           ", "Sutrisno Kutoyo                  ", 3, 0],
    "b3": ["Biografi Moh. Hatta              ", "Anom Whani Wicaksana             ", 2, 0],

    "e1": ["Ensiklopedi Populer Remaja       ", "Yayasan Cipta Loka Caraka        ", 1, 0],
    "e2": ["Ensiklopedi Geografi             ", "Dr. Ir. Imam Santoso, M.Sc       ", 2, 0],
    "e3": ["Ensiklopedi Negara-negara Dunia  ", "Amir F. Hidayat                  ", 3, 0],

    "k1": ["Umum Bahasa Indonesia            ", "W.J.S. Poerwadarminta            ", 2, 1],
    "k2": ["Kamus Lengkap Inggris-Indonesia  ", "Prof. Drs. S. Wojowasito         ", 2, 0],
    "k3": ["Kamus Ungkapan Bahasa Indonesia  ", "J. S. Bardu                      ", 1, 0],
}
#Nama, [Punya Pinjaman?, Pinjaman, Deadline tanggal pinjam]
user = {
    "hanifan":[True,"k1",datetime.datetime(2020,01,05)],
    "alfania":[True,"b1",datetime.datetime(2020,01,8)],
    "ricardo":[False,"",datetime.datetime(2020,01,01)],
    "vincent":[False,"",datetime.datetime(2020,01,10)],
    "richard":[True,"a2",datetime.datetime(2020,01,10)],
    "ridwana":[False,"",datetime.datetime(2020,01,01)],
}
# Fitur Fitur
def menu(hari):
    print hari.strftime("\nTanggal Hari Ini: %d %b %Y")
    cek_pinjaman(hari)
    print "\t [  Menu  ]"
    print "1. Lihat Daftar Buku\n2. Lihat Pinjaman buku"
    print "3. Buat Pinjaman Buku\n4. Kembalikan Buku\n5. Tambahkan Buku\n6. Logout (Ganti Tanggal Hari Ini)"
    pilihan = raw_input("Masukkan Input anda : \n =>")
    if pilihan=="1":
        lihat_buku()
        menu(hari)
    elif pilihan=="2":
        lihat_pinjaman()
        menu(hari)
    elif pilihan=="3":
        buat_pinjaman(hari)
        menu(hari)
    elif pilihan=="4":
        kembalikan_buku(hari)
        menu(hari)
    elif pilihan=="5":
       tambahkan_buku()
       menu(hari)
    elif pilihan=="6":
        pindah_hari()
    else:
        menu(hari)
        print "Input salah"
def pindah_hari():
    hari = raw_input("Masukkan tanggal hari ini (dd-mm-yy). cth: 01-01-2020 \n =>")
    hari = hari.split('-')
    try:
        hari = datetime.datetime(int(hari[2]), int(hari[1]), int(hari[0]))
        menu(hari)
    except (IndexError,ValueError):
        print "Input Anda Salah,Silahkan Coba Lagi "
def lihat_buku():
    print "\nDAFTAR BUKU"
    print "KODE \tJudul Buku\t\t\t\t\t\t\tPengarang\t\t\t\t\t\t\tBuku Tersedia\tBuku Dipinjam"
    print "-------------------------------------------------------------------------------------------------------------"
    for x in buku:
        print x +"\t"+ buku[x][0] +"\t"+ buku[x][1] +"\t\t  "+ str(buku[x][2]).ljust(2) +"\t\t\t\t  "+ str(buku[x][3])
    return
def lihat_pinjaman():
    print "PINJAMAN AKTIF"
    print "Nama\t\tPinjaman\tKode Buku"
    print "---------------------------------"
    for x in user:
        print "{0} \t{1} \t\t{2}".format(x,user[x][0],user[x][1])
    return
def buat_pinjaman(hari):
    try:
        new_user = raw_input("Masukkan Nama Peminjam : \n=>")
        # cek pinjaman aktif user
        if user[new_user][0] == True:
            print "User Sudah Memiliki Pinjaman Buku"
            return
    except KeyError:
        print "User tidak ditemukan"
        return
    lihat_buku()
    new_buku  = raw_input("Masukkan Kode Buku yang mau dipinjam : \n=>")
    #cek stok buku, lalu update stok
    if buku[new_buku][2]>0:
        #update data user
        user[new_user][0] = True
        user[new_user][1] = new_buku
        user[new_user][2] = hari.replace(hari.year,hari.month,hari.day+7)
        #update stok buku
        buku[new_buku][2] -= 1
        buku[new_buku][3] += 1
        print "Buku {0} terpinjam oleh {1}".format(new_buku,new_user)
    else:
        print "Tidak Ada Buku Yang Tersedia Untuk Dipinjam"
        return
def cek_pinjaman(hari):
    print "Notifikasi : "
    for x in user:
        selisih = hari - user[x][2]
        if selisih.days > 7 and user[x][0]==True:
            print x + " dengan buku : " + str(buku[user[x][1]][0]).rstrip() + " terlambat " + str(selisih.days) + " hari"
    return
def kembalikan_buku(hari):
    print "KEMBALIKAN BUKU"
    lihat_pinjaman()
    pilihan = raw_input("Masukkan Nama: ")
    try:
        up1 = user[pilihan][1]
    except KeyError:
        print "Invalid Input"
        menu(hari)
    if user[pilihan][0]==True and pilihan in user:
        #update user
        user[pilihan][0]=False
        user[pilihan][1]=""
        user[pilihan][2]=datetime.datetime(2020,01,01)
        #update stok buku
        buku[up1][2] += 1
        buku[up1][3] += -1
        print "Buku Berhasil Dikembalikan"
    else:
        print "Invalid Input"
        menu(hari)
def tambahkan_buku():
    print"TAMBAHKAN BUKU"
    lihat_buku()
    kode_bk = raw_input("Masukan Kode Buku Baru : \n=>")
    for x in buku:
        if x == kode_bk:
            print "Kode buku sudah ada!"
            menu(hari)
    judul_bk = (raw_input("Masukan Judul Buku : \n=>")).ljust(33)
    pengarang_bk = (raw_input("Masukan Pengarang Buku : \n=>")).ljust(34)
    stok_bk = raw_input("Masukan Jumlah stok buku").ljust(2)
    buku[kode_bk] = [judul_bk,pengarang_bk,stok_bk,0]
while True:
# Main Program Loop
    pindah_hari()