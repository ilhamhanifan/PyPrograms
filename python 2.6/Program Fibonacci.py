# Menggunakan python 2.6
# Program Fibonacci

a = 0
b = 1
c = 0
batas = int(raw_input("Input batasan :\n=>"))
for x in range(batas):
    print a,' '
    c = a + b
    a = b
    b = c