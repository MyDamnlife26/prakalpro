'''
Azriel Setyo Nugroho H. (71200576)
Topik : Set
Referensi : UG
Rumongso adalah seorang guru sekolah dasar di SD Suka Maju Mundur
Dia ingin mendata semua siswa yang ada di kelasnya
Buatkan lah program untuk mendata siswa di SD tempat mengajar Pak Rumongso

input:
1. Pilihan pengguna dalam mengakses sistem (input data, hapus data, lihat data, atau keluar dari sistem)
2. Nama siswa yang ingin diinput
3. Nama siswa yang ingin dihapus
4. Inputan data kelas mana yang akan dihapus  

proses:
1. Perulangan & percabangan untuk sistem awal
2. Perulangan & percabangan untuk menentukan data kelas mana yang ingin dihapus
3. Perulangan untuk menampilkan data kelas

output:
Silahkan pilih hal yang Anda inginkan:
1. Menambahkan data siswa
2. Menghapus data siswa
3. Menampilkan data siswa
4. Keluar
Masukkan pilihan:


Berapa jumlah siswa kelas A yang ingin dimasukkan?
Masukkan angka: 3
Silahkan masukkan nama siswa: ju
Silahkan masukkan nama siswa: ki
Silahkan masukkan nama siswa: nan


Siswa kelas mana yang ingin Anda hapus (A/B)?
Masukkan pilihan Anda: b

Berapa jumlah siswa yang ingin Anda hapus?
Masukkan angka: 1
Masukkan nama siswa: ka


-------------------------------- KELAS A --------------------------------
1. Di
2. Ju
3. Ki
4. Nan

-------------------------------- KELAS B --------------------------------
1. An
2. Cur
3. Da
4. Han
5. Ji

Jumlah siswa saat ini adalah 9
'''

kelasA = set()
kelasB = set()
while True:
    print("""\nSilahkan pilih hal yang Anda inginkan: 
1. Menambahkan data Siswa
2. Menghapus data Siswa
3. Menampilkan data Siswa
4. Keluar""")
    inp = int(input("Masukkan pilihan: "))
    try:
        if inp == 1:
            a = int(input("\nBerapakah jumlah siswa kelas A yang ingin dimasukkan? \nMasukkan angka: "))
            for i in range(a):
                b = input("Silahkan masukkan nama siswa: ")
                b = b.title()
                kelasA.add(b)
            a = int(input("\nBerapakah jumlah siswa kelas B yang ingin dimasukkan? \nMasukkan angka: "))
            for i in range(a):
                b = input("Silahkan masukkan nama siswa: ")
                b = b.title()
                kelasB.add(b)
        if inp == 2:
            a = input("\nSiswa kelas mana yang akan dihapus (A/B)? \nMasukkan pilihan Anda: ")
            a = a.lower()
            if a == "a":
                b = int(input("\nBerapakah jumlah siswa yang ingin Anda hapus? \nMasukkan angka: "))
                for i in range(b):
                    c = input("Masukkan nama siswa: ")
                    c = c.title()
                    kelasA.discard(c)
            if a == "b":
                b = int(input("\nBerapakah jumlah siswa yang ingin Anda hapus? \nMasukkan angka: "))
                for i in range(b):
                    c = input("Masukkan nama siswa: ")
                    c = c.title()
                    kelasB.discard(c)
        if inp == 3:
            print("\n-------------------------------- KELAS A --------------------------------")
            a = sorted(kelasA)
            c = 1
            for i in range(len(a)):
                print(f"{c}. {a[i]}")
                c += 1
            print("\n-------------------------------- KELAS B --------------------------------")
            b = sorted(kelasB)
            c = 1
            for i in range(len(b)):
                print(f"{c}. {b[i]}")
                c += 1
        if inp == 4:
            gabungan = kelasA.union(kelasB)
            print(f"\nJumlah total siswa saat ini adalah {len(gabungan)}")
            print("Selamat tinggal...")
            break
    except: 
        print("Pilihan nonvalid")