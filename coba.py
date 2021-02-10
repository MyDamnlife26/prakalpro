# a = 0.5
# al = int(input("Masukkan nilai alas: "))
# ti = int(input("Masukkan nilai tinggi: "))
# luas = a * al * ti
# print(luas)

# a = 10
# b = 12
# c = 14

# if a > b and a > c:
#     print("a")
# elif b > a and b > c:
#     print('b')
# elif c > a and c > b:
#     print('c')

# namaDepan = "Joko"
# namaBelakang = "Widodo"
# nama = namaDepan + " " + namaBelakang
# umur = 22
# hobi = "Berenang"
# print("Biodata\n", nama, "\n", umur, "\n", hobi)

# Nama = input("Nama Anda : ")
# Alamat = input("Alamat Tinggal Anda : " )
# Umur = input("Umur Anda : ")
# TL = input("Tempat Lahir Anda : ")
# Tgl = input("Tanggal Lahir Anda : ")
# IPK = input("IPK Anda : ")
# print("====================================")
# print("DATA AKADEMIK")
# print("Nama Anda : ", Nama)
# print("Alamat Tinggal Anda : ", Alamat)
# print("Umur Anda : ", Umur)
# print("Tempat Lahir Anda : ", TL)
# print("Tanggal Lahir Anda : ", Tgl)
# print("IPK Anda :", IPK)

# x1 = eval(input("X1 = "))
# x2 = eval(input("X2 = "))
# x3 = eval(input("X3 = "))
# x4 = eval(input("X4 = "))
# jumlah = x1+x2+x3+x4
# kali = x1*x2*x3*x4
# print('Hasil Penjumlah semua bilangan = ', jumlah)
# print('Hasil Perkalian semua bilangan = ', kali)
# jumlah = jumlah + 0.5
# print('Jika ditambah 0.5 hasilnya = ',jumlah)
# kali = kali * 0.5
# print('Jika dikali 0.5 hasilnya = ',kali)

# total_hrg_brg = 0.0
# kd_brg = input("Kode barang = ")
# nama_brg = input("Nama barang = ")
# harga_satuan = eval(input("Harga satuan barang = Rp. "))
# jum_brg = eval(input("Jumlah barang yang dibeli = "))
# harga_beli = harga_satuan * jum_brg
# total_hrg_brg = harga_beli + total_hrg_brg
# print("Total harga yang dibayar Rp", total_hrg_brg)

# x=30
# print(x)
# type float(x)

# y = 4*int(x)
# print(y)
# print("Tipe data X dikonversi ke int agar dapat dihitung Y=4*x")

# z = y+float(x)
# print("z", z)
# print("Tipe data X dikonversi menjadi float untuk dijumlahkan dengan tipe data Y, hasilnya yang ditampung bertipe float juga")

# P = True
# L = False
# P!=L
# print("Tanda != artinya tidak sama dengan")
# P==L
# print("Tanda == artinya sama dengan")

# a = int(input())
# b = int(input())
# c = int(input())
# hasil = a+b+c//3
# print('rata-rata: ', hasil)

# masukkan = input('masukkan angka : ')
# angka = masukkan.split(',')
# n = [int(x) for x in angka]
# jumlah = 0
# for angka in n:
#     jumlah += angka
# rata2 = jumlah / len(n)
# print(rata2)

# a = int(input())
# rumus = 2*(a)**3 + 2*(a)+15//(a)
# print("Hasil: ", rumus)

a = int(input('Gaji yang diinginkan: Rp '))
b = int(input('Jumlah jam kerja: '))
c = a*b
d = c - (c*0.14)
akse = (d*0.10)
altul = (d*0.01)
e = d - (akse + altul)
alms = (e * (25/100))
# yatim =  
# duafa = 

print(f"Pendapatan kotor: Rp. ", int(c))
print(f"Pendapatan bersih: Rp. ", int(d))
print(f"Uang untuk aksesoris & pakaian: Rp. ", int(akse))
print(f"Uang untuk alat tulis: Rp. ", int(altul))
print(f"Uang untuk sedekah: Rp. ", int(alms))