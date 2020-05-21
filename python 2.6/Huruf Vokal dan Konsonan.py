# Menggunakan Python 2.6
# Menentukan Huruf Vokal dan Konsonan
vokal = ['a','b','c','d','e']
input = raw_input("Masukkan huruf :\n=>")
if input in vokal:
    print "Huruf Vokal"
else:
    print "Huruf Konsonan"