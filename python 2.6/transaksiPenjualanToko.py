# Menggunakan Python 2.6
# Program Transaksi Penjualan toko (apotek)

# Dekrasi Daftar Harga Barang dan Keranjang belanja
keranjang_belanja = {}
barang_harga = {
    "obat batuk abc":10000,
    "masker sensiku":4000,
    "hand sanitizer":25000,
    "obat demam fgh":16000,
    "vaksin corona":3000
}

barang_stok = {
    "obat batuk abc": 10,
    "masker sensiku": 12,
    "hand sanitizer": 3,
    "obat demam fgh": 7,
    "vaksin corona" :4
}

def transaksi():
    global keranjang_belanja

    belanja = True
    keranjang_belanja = {}

    while belanja:
        print "===============  KASIR APOTEK  ================="
        print "\tNama Barang\t\t\tHarga Barang\t\tStok"
        for y in barang_harga:
            print "\t",y,"\t\t",barang_harga[str(y)],"\t\t\t\t",barang_stok[str(y)]

        print "\nKeranjang Belanja Anda : ",keranjang_belanja
        item = raw_input("\nKetik 'Selesai' Untuk Keluar\nKetikan nama item yang anda mau: ").lower()
        if item == "selesai":
            belanja = False
        elif item in barang_harga:
            print "\nAnda memilih barang : ",item
            print "\tSaat ini terdapat Stok sejumlah : ",barang_stok[item]
            jumlah = int(raw_input("\tBerapa jumlah barang yang anda mau? : "))

            if jumlah <= barang_stok[item]:
                keranjang_belanja[item] = jumlah
                barang_stok[item] -= jumlah
                print "\nkeranjang diisi dengan :",item, " ", jumlah," Pcs"
            else:
                print "\tStok tidak Cukup"
        else:
            print "Barang tidak ada"


def proses_transaksi():
    global keranjang_belanja
    total_transaksi = 0
    print "\n== == == == == == == = STRUK BELANJA = == == == == == == == ==\n"
    print "Nama Barang\t\tJumlah barang\tHarga Barang\tHarga Total"
    for item in keranjang_belanja:
        jumlah_item = keranjang_belanja[item]
        harga_item  = barang_harga[item]
        harga_total = harga_item * jumlah_item
        total_transaksi += harga_total
        print item,"\t",jumlah_item,"\t\t\t\tRP ",harga_item,"\t\tRP ",harga_total
    print "\nTotal Transaksi anda adalah : RP ", total_transaksi
    print "\n== == == == == == == == == == == == == == == == == == == == =="

transaksi()
proses_transaksi()

""""
HASIL OUTPUT:

/home/ilham/PycharmProjects/python 2.6/venv/bin/python" "/home/ilham/PycharmProjects/python 2.6/Tugas/transaksiPenjualanToko.py"
===============  KASIR APOTEK  =================
	Nama Barang			Harga Barang		Stok
	hand sanitizer 		25000 				3
	masker sensiku 		4000 				12
	obat batuk abc 		10000 				10
	obat demam fgh 		16000 				7
	vaksin corona 		3000 				4

Keranjang Belanja Anda :  {}

Ketik 'Selesai' Untuk Keluar
Ketikan nama item yang anda mau: masker sensiku

Anda memilih barang :  masker sensiku
	Saat ini terdapat Stok sejumlah :  12
	Berapa jumlah barang yang anda mau? : 5

keranjang diisi dengan : masker sensiku   5  Pcs
===============  KASIR APOTEK  =================
	Nama Barang			Harga Barang		Stok
	hand sanitizer 		25000 				3
	masker sensiku 		4000 				7
	obat batuk abc 		10000 				10
	obat demam fgh 		16000 				7
	vaksin corona 		3000 				4

Keranjang Belanja Anda :  {'masker sensiku': 5}

Ketik 'Selesai' Untuk Keluar
Ketikan nama item yang anda mau: hand sanitizer

Anda memilih barang :  hand sanitizer
	Saat ini terdapat Stok sejumlah :  3
	Berapa jumlah barang yang anda mau? : 2

keranjang diisi dengan : hand sanitizer   2  Pcs
===============  KASIR APOTEK  =================
	Nama Barang			Harga Barang		Stok
	hand sanitizer 		25000 				1
	masker sensiku 		4000 				7
	obat batuk abc 		10000 				10
	obat demam fgh 		16000 				7
	vaksin corona 		3000 				4

Keranjang Belanja Anda :  {'hand sanitizer': 2, 'masker sensiku': 5}

Ketik 'Selesai' Untuk Keluar
Ketikan nama item yang anda mau: obat batuk abc

Anda memilih barang :  obat batuk abc
	Saat ini terdapat Stok sejumlah :  10
	Berapa jumlah barang yang anda mau? : 5

keranjang diisi dengan : obat batuk abc   5  Pcs
===============  KASIR APOTEK  =================
	Nama Barang			Harga Barang		Stok
	hand sanitizer 		25000 				1
	masker sensiku 		4000 				7
	obat batuk abc 		10000 				5
	obat demam fgh 		16000 				7
	vaksin corona 		3000 				4

Keranjang Belanja Anda :  {'hand sanitizer': 2, 'masker sensiku': 5, 'obat batuk abc': 5}

Ketik 'Selesai' Untuk Keluar
Ketikan nama item yang anda mau: vaksin corona

Anda memilih barang :  vaksin corona
	Saat ini terdapat Stok sejumlah :  4
	Berapa jumlah barang yang anda mau? : 4

keranjang diisi dengan : vaksin corona   4  Pcs
===============  KASIR APOTEK  =================
	Nama Barang			Harga Barang		Stok
	hand sanitizer 		25000 				1
	masker sensiku 		4000 				7
	obat batuk abc 		10000 				5
	obat demam fgh 		16000 				7
	vaksin corona 		3000 				0

Keranjang Belanja Anda :  {'hand sanitizer': 2, 'masker sensiku': 5, 'obat batuk abc': 5, 'vaksin corona': 4}

Ketik 'Selesai' Untuk Keluar
Ketikan nama item yang anda mau: obat demam fgh

Anda memilih barang :  obat demam fgh
	Saat ini terdapat Stok sejumlah :  7
	Berapa jumlah barang yang anda mau? : 2

keranjang diisi dengan : obat demam fgh   2  Pcs
===============  KASIR APOTEK  =================
	Nama Barang			Harga Barang		Stok
	hand sanitizer 		25000 				1
	masker sensiku 		4000 				7
	obat batuk abc 		10000 				5
	obat demam fgh 		16000 				5
	vaksin corona 		3000 				0

Keranjang Belanja Anda :  {'hand sanitizer': 2, 'masker sensiku': 5, 'obat batuk abc': 5, 'obat demam fgh': 2, 'vaksin corona': 4}

Ketik 'Selesai' Untuk Keluar
Ketikan nama item yang anda mau: nasi goreng
Barang tidak ada
===============  KASIR APOTEK  =================
	Nama Barang			Harga Barang		Stok
	hand sanitizer 		25000 				1
	masker sensiku 		4000 				7
	obat batuk abc 		10000 				5
	obat demam fgh 		16000 				5
	vaksin corona 		3000 				0

Keranjang Belanja Anda :  {'hand sanitizer': 2, 'masker sensiku': 5, 'obat batuk abc': 5, 'obat demam fgh': 2, 'vaksin corona': 4}

Ketik 'Selesai' Untuk Keluar
Ketikan nama item yang anda mau: selesai

== == == == == == == = STRUK BELANJA = == == == == == == == ==

Nama Barang		Jumlah barang	Harga Barang	Harga Total
hand sanitizer 	2 				RP  25000 		RP  50000
masker sensiku 	5 				RP  4000 		RP  20000
obat batuk abc 	5 				RP  10000 		RP  50000
obat demam fgh 	2 				RP  16000 		RP  32000
vaksin corona 	4 				RP  3000 		RP  12000

Total Transaksi anda adalah : RP  164000

== == == == == == == == == == == == == == == == == == == == ==

Process finished with exit code 0
"""