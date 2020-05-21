a = 1
b = 1
c = 0
batas = int(input("masukan batas"))

for i in range(0,batas):
    a = b
    b = c
    c = a+b
    print(c)

