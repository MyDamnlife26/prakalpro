'''
Azriel Setyo Nugroho H. (71200576)
Topik: Files
Referensi: Modul topik bahasan
Dari sebuah file text, anda harus mengambil 2 value, value pertama sebagai soal, dan value kedua sebagai jawaban.
Lalu, buatlah sebuah program kuis sederhana dari data tersebut.

Input:
1. Nama file
2. Jawaban dari user

Proses:
1. Membuat perulangan untuk mengubah isi text menjadi list
2. Membuat perulangan berdasarkan list untuk menampilkan soal
3. Menerima input jawaban dari user
4. Mengeluarkan timbal balik berupa komentar apakah jawaban salah atau benar

Output:
************************************************************************************************************************
1. 'Future Nostalgia' yang berisi single 'Don't Start Now' merupakan album studio kedua dari penyanyi Inggris mana?
        Masukkan jawaban: dua lipa
        Jawaban benar!
************************************************************************************************************************
2. Apa nama band dengan anggota berikut: John Deacon, Brian May, Freddie Mercury, Roger Taylor?
        Masukkan jawaban: Queen
        Jawaban benar!
************************************************************************************************************************
3. Penyanyi manakah yang dikenal antara lain sebagai 'The King of Pop' dan 'The Gloved One'?
        Masukkan jawaban: Michael Jacks
        Jawaban salah!
************************************************************************************************************************
4. Dimanakah Taj Mahal dapat ditemukan?
        Masukkan jawaban: India
        Jawaban benar!
************************************************************************************************************************
5. Dimanakah Colloseum dapat ditemukan?
        Masukkan jawaban: Italia
        Jawaban benar!
************************************************************************************************************************
6. Ada pepatah "lebih baik terlambat daripada ....."
        Masukkan jawaban: tidak sama sekali
        Jawaban benar!
************************************************************************************************************************
Sudah selesai, terimakasih
'''

filename = input("Masukkan nama file: ")
handle1 = open(filename, "r")
a = []
b = []
c = 0

for i in handle1:
        i = i.split(",,")
        for j in i:
                if c % 2 == 0:
                        j = j.strip()
                        a.append(j)
                        c += 1
                elif c % 2 == 1:
                        j = j.strip()
                        j = j.lower()
                        b.append(j)
                        c += 1

handle2 = open("hasil.txt", "w")

c = 1
for i in a:
        print("*"*120)
        try:
                print(f"{c} {a[c]}")
                inp = input("\tMasukkan jawaban Anda: ")
                inp = inp.lower()
                if inp == b[c]:
                        print("\tJawaban benar")
                        handle2.write(f"{c}. Jawaban benar\n")
                        c += 1
                elif inp != b[c]:
                        print("\tJawaban salah")
                        handle2.write(f"{c}. Jawaban salah\n")
                        c += 1
        except:
                print("Sudah selesai, Terimakasih")

handle2.close()
handle1.close()
