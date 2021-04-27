'''
Azriel Setyo Nugroho H. (71200576)
Topik : Dictionary
Referensi : UG
Pak Sebas adalah pekerja dari bagian tata usaha sekolah hunter.
Dia merasa bingung harus bagaimana supaya dapat mendata data pengecekan kesehatan di sekolahnya.
Bantulah Pak Sebas membuat sebuah sistem untuk mendata murid yang ada di sekolahnya.

input:
1. Pilihan pengguna dalam mengakses sistem (input data, lihat data, hapus data, dan keluar dari sistem)
2. Nama siswa sebagai key
3. Kelas, berat, dan tinggi siswa sebagai value

proses:
1. Buat perulangan untuk sistem
2. Buat percabangan untuk pilihan user
3. Buat inputan untuk memasukkan data
4. Buat perulangan untuk melihat data
5. Buat perulangan dan percabangan untuk menghapus data
6. Buat pilihan untuk keluar dari sistem

output:
------------------------- Data Siswa -------------------------
1.      Nama: Andi      Kelas: 2        Berat: 80       Tinggi: 190
2.      Nama: Lala      Kelas: 2        Berat: 68       Tinggi: 178
3.      Nama: Jai       Kelas: 3        Berat: 80       Tinggi: 189
4.      Nama: Rindu     Kelas: 3        Berat: 67       Tinggi: 169

'''
masukData = dict()
while True:
    print("""------------------------------------
1. Input Data
2. Lihat Data
3. Hapus Data
4. Keluar""")
    inp = int(input("Masukkan pilihan: "))
    try:
        if inp == 1:
            jml = int(input("Masukkan jumlah data yang akan dimasukkan: "))
            for i in range(jml):
                nama = input("Masukkan nama siswa/siswi: ")
                nama = nama.title()
                kelas = input("Masukkan kelas siswa/siswi: ")
                berat = input("Masukkan berat siswa/siswi: ")
                tinggi = input("Masukkan tinggi siswa/siswi: ")
                masukData[nama] = kelas, berat, tinggi
                print("-"*50)
        elif inp == 2:
            c = 1
            print("------------------------- Data Siswa -------------------------")
            for i in masukData:
                a = masukData[i]
                print(
                    f"{c}.\tNama: {i}\t Kelas: {a[0]}\t Berat: {a[1]}\t Tinggi: {a[2]}")
                c += 1
        elif inp == 3:
            nama = input("Masukkan data yang ingin dihapus: ")
            nama = nama.title()
            for i in range(len(masukData)):
                a = list(masukData.keys())
                b = a[i]
                if nama == b:
                    del masukData[nama]
                    print("Data berhasil dihapus.")
                else:
                    print("Data tidak berada dalam tabel.")
        elif inp == 4:
            print("Selamat tinggal...")
            break
        else:
            print("Input non-valid")
    except:
        print()
