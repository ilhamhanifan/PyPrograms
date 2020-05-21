#menggunakan Python 2.6
#dibuat oleh: Muhammad Ilham Hanifan 1IA06 54419229
#Array Di Dalam List
#{ nama barang:[jumlah,harga,total] }
nama_barang = {

}
def pembukaan():
    bulan = raw_input("Masukkan Bulan Penjualan :")
    try:
        jumlah_data = int(raw_input("Masukkan jumlah data : "))
        ambil_input(bulan,jumlah_data)
    except ValueError:
        print "Jumlah Data Harus Berisi Angka"
        pembukaan()

# dibuat oleh: Muhammad Ilham Hanifan 1IA06 54419229
def ambil_input(bulan,jumlah_data):
    for x in range(jumlah_data):
        try:
            input_nama = raw_input("Nama Barang ke-{0} : ".format(x+1))
            input_jumlah = int(raw_input("Jumlah : "))
            input_harga = int(raw_input("Harga Rp. : "))
            input_total = input_jumlah * input_harga

            # Menambahkan Angka Ke Digit Terakhir jika ada data sama
            if input_nama in nama_barang:
                count = 1
                loop = True
                input_nama += str(count)
                while loop == True:
                    input_nama = input_nama[:-1]
                    input_nama+=str(count)
                    count += 1
                    if input_nama not in nama_barang:
                        input_nama = input_nama
                        nama_barang[input_nama] = [input_jumlah,input_harga,input_total]
                        loop = False
                    else:
                        continue
                #cetak_output(bulan,nama_barang)
            else:
                input_nama = input_nama
                nama_barang[input_nama] = [input_jumlah, input_harga, input_total]
                #cetak_output(bulan, nama_barang)

        except(ValueError):
            print "Input Salah"
    cetak_output(bulan,nama_barang,jumlah_data)

# dibuat oleh: Muhammad Ilham Hanifan 1IA06 54419229
def cetak_output(bulan,nama_barang,jumlah_data):
    print "\n\nLAPORAN PENJUALAN PT. Gunadarma"
    print "BULAN : {0}".format(bulan)
    print "====================================================="
    print "NO  NAMA BARANG \t\t\tJUMLAH \tHARGA   TOTAL"
    print "====================================================="

    count = 0
    for nama in nama_barang:
        count += 1
        print str(count).ljust(2),"\t",nama.ljust(20),"\t",str(nama_barang[nama][0]).ljust(5),"\t",str(nama_barang[nama][1]).ljust(6),"\t",str(nama_barang[nama][2]).ljust(6)

    #total penjualan
    total_penjualan = 0
    for x in nama_barang:
        total_penjualan += nama_barang[x][2]

    print "TOTAL BARANG : {0}".format(jumlah_data)
    print "TOTAL PENJUALAN : {0}".format(total_penjualan)

pembukaan()
