'''
Topik : Modular Programming

Andi membuat sebuah toko kelontong. Disana dia menerapkan protokol kesehatan 
tapi bingung karena pelanggan harus berinteraksi langsung dengan pembeli.
Karena anda adalah teman yang biasa Andi andalkan, 
buatkan sebuah sistem untuk membantu Andi mencatat semua barang yang dibeli pelanggan.

Input:
1. Input pilihan berdasarkan pilihan yang ada tambah data, hapus data, melihat data dalam list, atau keluar 
2. Input nama barang yang akan dibeli
3. Input nama barang yang akan hapus dari daftar belanjaan

Proses:
1. Membuat list untuk menampung daftar belanjaan
2. Membuat fungsi menambahkan barang ke dalam list
3. Membuat fungsi menghapus barang dari list
4. Membuat fungsi untuk melihat apa saja yang berapa dalam list
5. Membuat fungsi exit
6. Membuat fungsi invalid
7. Membuat fungsi belanja

Output: fungsi yang dibuat dapat berjalan dengan baik
'''

daftarBelanja = []

def tambah():
    barang1 = (input('Masukkan barang yang ingin Anda beli: '))
    daftarBelanja.append(barang1)
    print(f'{barang1} telah berhasil ditambahkan ke dalam list.')

def hapus():
    barang2 = (input('Masukkan barang yang ingin dihapus: '))
    if barang2 in (daftarBelanja):
        daftarBelanja.remove(barang2)
        print(f'{barang2} telah berhasil dihapus ke dalam list.')
    else:
        print(f'{barang2} tidak ditemukan di dalam list.')

def daftar():
    a = len(daftarBelanja)
    for b in range (a):
        print(daftarBelanja[b])

def exit():
    print('Silahkan membayar ke kasir... \n Terima kasih atas pembelian Anda.')

def invalid():
    print('Invalid, input yang Anda lakukan salah, silahkan di ulangi.')

def belanja():
    while True:
        print('Silahkan pilih: \n 1. Menambahkan barang yang akan di beli \n 2. Menghapus barang dari daftar belanja \n 3. Menampilkan daftar belanja \n 4. Exit')
        a = int(input('Masukkan pilihan anda: '))
        if a == 1:
            tambah()
        elif a == 2:
            hapus()
        elif a == 3:
            print('Daftar Belanja Anda: ')
            daftar()
        elif a == 4:
            exit()
            break
        else:
            invalid()
            break

belanja()