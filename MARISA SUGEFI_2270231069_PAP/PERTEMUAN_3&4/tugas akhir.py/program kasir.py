print("           Risa Store           ")
print("          Toko Sembako          ")
print("     JL. Jatiwaringin No. XX    ")
print("     Pondok Gede. Kota Bekasi   ")
print("================================")

nama = input ("Nama Pelanggan : ")
tanggal = input ("Tanggal Pembelian :")
print("==============================")
print("  ======Menu======  ")
print("1. minyak 1kg            Rp.19.000")
print("2. terigu 1kg             Rp.9.000")
print("3. telor 1kg             Rp.18.000")   
print("4. gula 1kg              Rp.14.000")
print("5. beras 1liter          Rp.10.000")
print("6. indomie                Rp.3.500")  
print("  ======Menu======  ")
h=[]
a=1

menu_pesanan = int (input("Masukan Menu Pesanan(Nomor Menu) : "))
if menu_pesanan == 1:
    harga = 19000
elif menu_pesanan == 2:
    harga = 9000
elif menu_pesanan == 3:
    harga = 18000
elif menu_pesanan == 4:
    harga = 14000
elif menu_pesanan == 5:
    harga = 10000
elif menu_pesanan == 6:
    harga = 3500 
else:
    while True :
        print("====Menu Tidak Tersedia Silahkan Pilih Menu Lainnya====")
        if menu_pesanan == 1 or menu_pesanan == 2 or menu_pesanan == 3 or menu_pesanan == 4:
           if menu_pesanan == 1:
             harga = 19000
        elif menu_pesanan == 2:
             harga = 9000
        elif menu_pesanan == 3:
             harga = 18000
        elif menu_pesanan == 4:
             harga = 14000
        elif menu_pesanan == 5:
             harga = 10000
        elif menu_pesanan == 6:
             harga = 3500 
             break 
         
jumlah_pembelian = int (input("Masukan Jumlah Pembelian: "))
for i in range(jumlah_pembelian):
    h.append(harga)

while True:
    jawab = input("Apakah ada yang ingin ditambah/dikurangi ?tambah/kurang/tidak   :")
    if jawab == 'tambah':
        tambah = int(input("Masukan Menu Pesanan (Nomor Menu): "))
        if menu_pesanan == 1:
          harga = 19000
        elif tambah == 2:
             harga = 9000
        elif tambah == 3:
             harga = 18000
        elif tambah == 4:
             harga = 14000
        elif tambah == 5:
             harga = 10000
        elif tambah == 6:
             harga = 3500 
        jumlah_tambahan = int(input("Masukan jumlah Pembelian : "))
        for i in range(jumlah_tambahan):
            h.append(harga)
        c = jumlah_tambahan + jumlah_pembelian
        print("Total Pesanan: ",c)
        bayar = sum(h)
        print("Total Pembayaran : Rp.{}".format(bayar))
        break
    elif jawab == 'kurang':
        kurang = int(input("berapa Jumlah yang dikurangkan ? :"))
        for i in range(kurang):
            if kurang <= 1:
                a -= kurang
                del h[a]
                bayar = sum(h)
                break
            else:
                kurang -= a
                del h[kurang]
                if kurang < 0:
                    break
        c = jumlah_pembelian - kurang
        print("Total Pemesanan: ",c)
        bayar = sum(h)
        print("Total Pembayaran : Rp. {}".format(bayar))
        break
    else:
        bayar = sum(h)
        c = jumlah_pembelian
        print(" Total Pemesanan : ",c)
        print("Total Pembayaran : Rp. ".format(bayar))
        break