"""
Azriel Setyo Nugroho H. (71200576)
Topik : Tuple
Referensi : UG
hitung perkalian dari perubahan data berikut (data di ubah menjadi angka berdasarkan ASCII code) lalu dibagi dengan jumlah karakter tanpa spasi:
kalimat = ("Saya", "Suka", "Makan", "Bayam")

input:
tuple yang sudah disediakan

proses:
mengubah tuple menjadi angka
menghitung hasil perkalian
menghitung jumlah karakter tanpa spasi
memperlihatkan hasil perkalian, pembagian, dan jumlah karakter 

output:
Saya = 398
Suka = 404
Makan = 488
Bayam = 490
Jumlah karakter yang ada adalah 18
Hasil perkalian dari perubahan Saya, Suka, Makan, Bayam adalah 38448583040
Hasil dari hasil perkalian dibagi jumlah karakter dalam list adalah 2136032391,11

"""
# kalimat = ("Saya", "Suka", "Makan", "Bayam")
kalimat = ("Azriel", "Suka", "Menonton", "Youtube")
#mengubah jadi list
lst = []
for i in kalimat:
    lst.append(i)

#menghitung jumlah karakter
tam = 0
for i in lst:
    a = len(i)
    tam += a

#menghitung perubahan dari string ke angka berdasarkan kode ASCII
dsc = {}
for j in lst:
    dsc[j] = sum(ord(i) for i in j)

#menghitung hasil perkalian antar kata
val = list(dsc.values())
hasil = 1
for i in val:
    hasil = hasil * i

#menghitung pembagian dari hasil perkalian dan dibagi dengan jumlah karakter
hasilAkhir = hasil / tam

#menampilkan output yang diharapkan
key = list(dsc.keys())
for i in range(len(key)):
    print(f"{key[i]} = {dsc[key[i]]}")
print(f"""Jumlah karakter yang ada adalah {tam}
Hasil perkalian dari perubahan Saya, Suka, Makan, Bayam adalah {hasil}
Hasil dari hasil perkalian dibagi jumlah karakter dalam list adalah %.2f"""%hasilAkhir)