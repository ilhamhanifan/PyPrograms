# Menggunakan Python 3.7
# caesar cipher onlen neh https://www.dcode.fr/caesar-cipher
alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
hasil_kata = ''
enc_atau_dec = int(input("1. Encoder 2. Decoder (1/2) :"))
kata = (input("Masukan String : ")).upper()
key = int(input('Masukan Kunci : '))

# CAESAR ENCODER
for x in kata:
    if x not in alfabet:
        hasil_kata += x
        continue

    if  enc_atau_dec == 1:    # Menentukan decoding atau encoding
        num = alfabet.find(x) + key
    elif enc_atau_dec == 2:
        num = alfabet.find(x) - key

    if num >= 26: # Membatasi jika nilainya lebih dari 26, akan kembali ke 0
        num -= 26
    hasil_kata += alfabet[num]

print(hasil_kata)