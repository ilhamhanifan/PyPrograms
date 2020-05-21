# MENUGGUNAKAN PYTHON 3.7

jawab = ""          # Variabel untuk memilih di menu
jalan  = True       # Variabel yang untuk mengakhiri program

def penjumlahan():  # Fungsi Penjumlahan - mereturn hasilnya
    angka1 = int(input("Masukan Angka Pertama : "))
    angka2 = int(input("Masukan Angka Kedua : "))
    return angka1+angka2
def pengurangan():  # Fungsi Pengurangan - mereturn hasilnya
    angka1 = int(input("Masukan Angka Pertama : "))
    angka2 = int(input("Masukan Angka Kedua : "))
    return angka1-angka2

while jalan is True:            # LOOP utama program
    print("====PROGRAM PENJUMLAHAN DAN PENGURANGAN====")    # MENU PROGRAM
    print("\t1. Penjumlahan\n\t2. Pengurangan\n\t3. Keluar\n")
    jawab = input("Masukkan Pilihan Anda: ")

    if jawab == "1":    # Mengecek jika user memilih penjumlahan
        print("Hasilnya adalah = " + str(penjumlahan()) + "\n")
    elif jawab == "2":  # Mengecek jika user memilih penngurangan
        print("Hasilnya adalah = " + str(pengurangan()) + "\n")
    elif jawab == "3":  # Mengecek jika user memilih untuk mengakhiri program
        jalan = False
        print("Program Selesai")
    else:
        print("Input anda salah!")

