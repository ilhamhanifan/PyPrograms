# Menggunakan python 2.6
# Program Bangun Datar
'''

LK Segitiga
LK Lingkaran
LK PP
'''
is_running = True
while is_running:
    print "PROGRAM LK BANGUN DATAR"
    answer = raw_input("1. Segitiga (Luas)\n"
                       "2. Lingkaran (Luas&Keliling)\n"
                       "3. Persegi Panjang (Luas&Keliling)\n"
                       "4. Exit\n=>")
    if answer == '1':
        try:
            a = int(raw_input("Masukan Besar Alas      :\n=>"))
            b = int(raw_input("Masukan Besar Tinggi    :\n=>"))
            luas = a * b * 0.5
            print 'Luas Segitiga : ',luas
        except ValueError:
            print "Angka Tidak Boleh String\n"

    elif answer == '2':
        try:
            pi = 3.14
            a = int(raw_input("Masukan Besar Jari-Jari :\n=>"))
            luas = pi*a*a
            keliling = 2*pi*a
            print 'Luas Lingkaran : ',luas
            print 'Keliling Lingkaran : ',keliling
        except ValueError:
            print "Angka Tidak Boleh String\n"
    elif answer == '3':
        try:
            a = int(raw_input("Masukan Besar Panjang  :\n=>"))
            b = int(raw_input("Masukan Besar Lebar    :\n=>"))
            luas = a*b
            keliling = (2*a)+(2*b)
            print 'Luas Persegi Panjang : ',luas
            print 'Keliling Persegi Panjang : ',keliling
        except ValueError:
            print "Angka Tidak Boleh String\n"
    elif answer == '4':
        is_running = False
        print "\n\n....PROGRAM SELESAI"
    else:
        print "Invalid Input"
