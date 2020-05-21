# Menggunakan Python 2.6
# Menggunakan Python 2.6
def faktorial(nilai):
    if nilai <= 1:
        return 1
    else:
        return nilai* faktorial(nilai-1)

#for i in range(6):
#    print "%2d ! = %d" %(i,faktorial(i))

for nilai in range(6):
    print "%2d ! = %d" %(nilai, faktorial(nilai))