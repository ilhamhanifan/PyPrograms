# Menggunakan Python 2.6
# Program memutar balik String
nama = raw_input("Masukan Nama Anda : \n=>")
print nama
for huruf in range(len(nama)-1,-1,-1):
    print nama[huruf],
