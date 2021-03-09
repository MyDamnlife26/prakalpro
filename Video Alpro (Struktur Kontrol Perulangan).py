'''
Azriel Setyo Nugroho Hasudungan
71200576
Topik: Struktur Kontrol Perulangan

Bambang membangun usaha boutique baju. Namun dia kesusahan untuk memasukkan data barang agar lebih mudah dalam melihat dan mengatur harga jual dari produk.
Oleh karena itu bantulah Bambang untuk membuat sebuah program yang dapat mempermudahnya memasukkan data barang dan kodenya sesuai dengan urutan data dimasukkan. 

Input:
a. input angka (tambah atau hapus barang atau keluar)
b. input nama dan kode barang

Proses: 
a. Masukkan pilihan antara menambah atau menghapus barang atau keluar
b. Menambahkan nama produk dan kodenya
c. Keluar 

Output: 
Daftar barang dan kodenya

'''

produk = []
kode = []

while True:
    print('''----------------------------------------------------------------
Silahkan pilih:
1. Tambah Produk
2. Hapus produk
3. Keluar''')
    a = int(input('Masukkan pilihan: '))
    if a == 1:
        b = str(input('Masukkan nama produk: '))
        produk.append(b)
        c = str(input('Masukkan kode produk: '))
        kode.append(c)
    elif a == 2:
        b = str(input('Masukkan nama produk: '))
        if b in produk:
            produk.remove(b)
        else:
            print('Produk tidak terdapat dalam daftar.')
        c = str(input('Masukkan kode produk: '))
        if c in kode:
            kode.remove(c)
        else:
            print('Kode tidak terdapat dalam daftar.')
    elif a == 3:
        print('Inilah daftar produk dan kode yang telah dimasukkan: ')
        for index,produk in zip(kode,produk):
            print(f'{index} - {produk}')
        break
    else:
        print('Tidak terdapat dalam daftar.')