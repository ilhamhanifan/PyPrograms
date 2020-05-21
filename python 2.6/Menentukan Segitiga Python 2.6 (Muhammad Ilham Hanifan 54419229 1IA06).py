# Menggunakan Python 2.6
# PROGRAM JENIS SEGITIGA

# SUDUT < 90 : LANCIP
# SUDUT = 90 : SIKU SIKU
# SUDUT > 90 : TUMPUL

sudut = int(raw_input("Masukkan Sudut : "))

if sudut > 90:
    print 'Segitiga Tumpul'
elif sudut == 90:
    print 'Segitiga Siku Siku'
else:
    print 'Segitiga Lancip'