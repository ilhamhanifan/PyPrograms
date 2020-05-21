# Menggunakan Python 2.6
# Program Bilangan kecil dan besar
angka1 = int(raw_input('Masukan Angka pertama : '))
angka2 = int(raw_input('Masukan Angka kedua : '))

if angka1 > angka2:
    print 'Angka Pertama adalah Bilangan Besar\nAngka Kedua adalah Bilangan Kecil'
elif angka1 == angka2:
    print 'Angka Pertama sama besar dengan Angka Kedua'
else:
    print 'Angka Kedua adalah Bilangan Besar\nAngka Pertama adalah Bilangan Kecil'