'''
Azriel Setyo Nugroho H. (71200576)
Topik : List
Referensi : UG
Bambang membuka sebuah rumah makan, dia ingin membuat menu yang berbeda setiap harinya.
Buatlah sebuah program sederhana untuk membuat menu rumah makan milik bambang. 

input:
1. Nama dan harga menu di rumah makan
2. Pilihan menu dalam program (menambahkan isi daftar menu, menghapus isi daftar menu, menampilkan isi menu, dan keluar dari program)

proses:
1. Membuat percabangan untuk pilihan pengguna
2. Membuat perulangan untuk menambahkan ini menu
3. Membuat percabangan untuk menghapus poin khusus dari menu atau secara keseluruhan
4. membuat perulangan untuk menampilkan isi menu

output:
========== Menu Rumah Makan Bambang ==========
1. Ayam           Rp. 10.000,00
2. Telur          Rp. 10.000,00
3. Rendang        Rp. 15.000,00
4. Sayur          Rp. 8.000,00

'''

nama = []
harga = []

while True:
    print("""--------------------------------- SELAMAT DATANG ---------------------------------
SILAHKAN PILIH MENU DI BAWAH:
1. Tambah menu
2. Hapus menu
3. Lihat menu
4. Keluar""")
    masuk = int(input("Masukkan pilihan: "))
    if masuk == 1:
        masuk1 = int(input("Jumlah menu yang akan dimasukkan: "))
        for i in range(masuk1):
            name = input("Masukkan nama menu: ")
            nama.append(name.title())
            price = input("Masukkan harga menu: ")
            harga.append(price)
            print("*"*50)
    elif masuk == 2:
        print("""Pilihan: 
1. Hapus poin Khusus
2. Hapus keseluruhan""")
        masuk1 = int(input("Masukkan pilihan: "))
        if masuk1 == 1:
            masuk2 = input("Masukkan nama menu: ")
            masuk2 = masuk2.title()
            if masuk2 in nama:
                indexMenu = nama.index(masuk2)
                nama.remove(masuk2)
                harga.remove(harga[indexMenu])
                print(f"{masuk2} berhasil dihapus dari menu.")
            else:
                print("Input tidak ditemukan dalam menu.")
        if masuk1 == 2:
            nama.clear()
            harga.clear()
    elif masuk == 3:
        c = 1
        print("========== Menu Rumah Makan Bambang ==========")
        for i in range(len(nama)):
            print(f"{c}.", nama[i], "    ", "\t", f"Rp. {harga[i]},00")
            c += 1
    elif masuk == 4:
        print("--------------------------------- SELAMAT TINGGAL ---------------------------------")
        break
    else:
        print("Input error.")
