# Menggunakan Python 2.6
# Menentukan Barisa Bilangan Ganjil Genap
gage = raw_input("1.Ganjil\n2.Genap\n=>")
batas = int(raw_input("Masukkan batas : \n=>"))
if gage =='1':
    for x in range(1,batas,2):
        print x
elif gage =='2':
    for x in range(2,batas,2):
        print x
else:
    print"Invalid Input"