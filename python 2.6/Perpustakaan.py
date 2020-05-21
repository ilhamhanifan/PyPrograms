#Nama Buku,[Pengarang,Jumlah,Terpinjam]
buku = {
    "a1":["Almanak Dewisri                   ","Kamajaya                          ",1,0],
    "a2":["Almanak Pembangunan               ","Ismail Lutan                      ",2,0],
    "a3":["Almanak Negara RI                 ","Iwan Gayo                         ",1,1],

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

#ID anggota, Nama, Punya Pinjaman?, Pinjaman
user = {
    "id1":["hanifan",True,"K1"],
    "id2":["alfan  ",True,"B1"],
    "id3":["ricardo",False,""],
    "id4":["vincent",False,""],
    "id5":["emir   ",True,"A3"],
    "id6":["wieby  ",False,""],
}
def menu():
    print "Selamat Datang di Program Perpustakaan"
    print "1. Lihat Koleksi Buku\t2. Lihat Peminjaman\n3. Pinjam Buku\t\t\t4. Kembalikan Buku"
    answer = raw_input("Input: ")
    if answer == "1": lihat_bk()
    elif answer == "2": lihat_pm()
    elif answer == "3": pinjam_bk()

def lihat_bk():
    print "DAFTAR BUKU"
    print "KODE \tJudul Buku\t\t\t\t\t\t\tPengarang\t\t\t\t\t\t\tBuku Tersedia\tBuku Dipinjam"
    print "-------------------------------------------------------------------------------------------------------------"
    for x in buku:
        print x +"\t"+ buku[x][0] +"\t"+ buku[x][1] +"\t\t  "+ str(buku[x][2]) +"\t\t\t\t  "+ str(buku[x][3])

def lihat_pm():
    print "PINJAMAN AKTIF"
    print "ID\t\tNama\tKode Buku\tJudul Buku"
    print "-----------------------------------------------------"
    for x in user:
        if user[x][1] == True:
            print x +"\t"+ user[x][0] +"\t"+ user[x][2] +"\t\t"+ buku[str(user[x][2])][0]

def pinjam_bk():
    id = raw_input("Ketik (buat user) untuk buat akun baru\nMasukkan ID anggota perpusatakaan : ")
    bk = ""

    if id == "buat akun":
        buat_user()

    if id not in user:
        print "User not found"
        id = raw_input("Apakah anda mau membuat akun baru? (Y/N) : ")
        if id.lower() == 'y':buat_user()
        elif id.lower() == 'n':menu()

    lihat_bk()
    bk = raw_input("Masukkan KODE buku yang ingin dipinjam: ")
    for x in buku:
        if bk == x:
            print "Nama Peminjam        : ", id ," / ",user[id][0]
            print "Buku yang dipinjam   : ", bk ," / ",buku[bk][0]

            break
    print "Buku tidak ditemukan"


def buat_user():
    #Generate ID baru5
    print "Ketentuan nama: Max 7 digit"
    id  = "1"

    nama = raw_input("Masukkan Nama anda: ").lower()
    print nama
    if len(nama) > 7:
        print "Nama terlalu panjang, Max 7 digit"
        menu()
    for x in user:
        if user[x][0] == nama:
            print "Nama sudah ada, Masukan nama lain"
            menu()

    for x in user:
        if x.replace('id','') > id:
            id = x.replace('id','')
    id = "id" + str(int(id)+1)  #id baru
    user[id]=nama
    print "User added"
    print user
    menu()
pinjam_bk()
#def kembali_bk()

