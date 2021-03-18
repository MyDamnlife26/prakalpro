'''
Azriel Setyo Nugroho H. (71200576)
Topik : Struktur Kontrol Kompleks
Referensi : UG6

Buat sebuah pola dengan menggunakan bahasa python
Pola tersebut berbentuk jajar genjang, dengan bagian tengah sesuai dari input yang dimasukkan
Tersusun atas angka sejumlah baris n

Input: 
Input titik tengah pola

Proses: 
1. Perulangan spasinya
2. Perulangan angkanya

Output: 
n = 5
    1
   22
  333
 4444
55555
4444
333
22
1
'''

n = int(input('Masukkan angka: '))
for i in range (0, n+1):
    for j in range (0, n-i):
        print(end = ' ')
    for j in range (0, i):
        print (i, end = '')
    print()

for i in range (n-1, 0, -1):
    for j in range(0, i):
        print(i, end = '')
    print()