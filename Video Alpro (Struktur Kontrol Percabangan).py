'''
Azriel Setyo Nugroho H. (71200576)
Topik: Struktur Kontrol Percabangan
Referensi : UG3

Indra baru saja membangun sebuah usaha rumah makan. Makanan yang di jual adalah sushi dan sashimi. Sushi memiliki 2 tipe yaitu plate dan roll dengan harga 
masing-masing Rp. 35.000,00 dan Rp. 70.000,00. Juga sashimi memiliki 2 tipe yaitu sake dan akami dengan harga masing-masing Rp. 60.000,00 dan Rp 70.000,00. 
Bantulah Indra untuk mencatat dan menghitung total harga yang harus dibayar oleh pelanggan bila:
1. Jika membeli sushi roll lebih dari 2 porsi akan diberi potongan 5%
2. Jika membeli sashimi akami lebih dari 3 porsi akan diberi potongan 15%

Input: 
    Sushi:
        Plate: 35.000
        Roll: 70.000
    Sashimi: 
        Sake: 60.000
        Akami: 70.000

Proses: 
1. Menginput semua harga yang ada.
2. Mulai dengan percabangan pertama, pembeli memilih antara sushi dan sashimi.
3. Percabangan kedua, pembeli memilih jenis/tipe dari makanan yang dipilih.
4. Pembeli menginputkan berapa banyak makanan yang akan di beli.

Output: Harga total yang harus dibayarkan oleh pelanggan di restoran Indra.
'''
plate = 35000  
roll = 70000
sake = 60000
akami = 70000

print('Pilihan Menu: \n', '1. Sushi \n', '2. Sashimi\n')
a = int(input('Masukkan pilihan Anda: '))
if a == 1:
    print('Pilihan tipe sushi: \n', '1. Plate \n', '2. Roll \n')
    b = int(input("Masukkan pilihan Anda: "))
    if b == 1:
        c = int(input('Jumlah porsi yang Anda inginkan: '))
        hargaplate = c*plate
        print(f'Harga total adalah Rp. {hargaplate}')
    else:
        c = int(input('Jumlah porsi yang Anda inginkan: '))
        if c > 2:
            d = c*roll
            hargaroll = d - (d*0.05)
            print(f'Harga total adalah Rp. {hargaroll}')
        else:
            hargaroll = c*roll
            print(f'Harga total adalah Rp. {hargaroll}')
elif a == 2:
    print('Pilihan tipe sushi: \n', '1. Sake \n', '2. Akami \n')
    b = int(input("Masukkan pilihan Anda: "))
    if b == 1:
        c = int(input('Jumlah porsi yang Anda inginkan: '))
        hargasake = c*sake
        print(f'Harga total adalah Rp. {hargasake}')
    else:
        c = int(input('Jumlah porsi yang Anda inginkan: '))
        if c > 3:
            d = c*akami
            hargaakami = d - (d*0.15)
            print(f'Harga total adalah Rp. {hargaakami}')
        else:
            hargaakami = c*akami
            print(f'Harga total adalah Rp. {hargaakami}')
else:
    print('Angka yang Anda masukkan tidak ada.')