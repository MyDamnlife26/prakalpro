'''
Azriel Setyo Nugroho H. (71200576)
Topik : Regex
Referensi : UG

Diberikan beberapa kode voucher top-up untuk game online. Cek lah ke valid-an dari kode tersebut dengan menggunakan regex, apabila diberikan syarat-syarat berikut untuk dinyatakan valid:
1. Tidak terdapat spasi dalam kode.
2. Terdapat minimal 1 deret angka sejumlah 5 digit.
3. Terdapat huruf besar dan huruf kecil.
4. Diawali selain huruf a, c, t, v, x, dan y, mau itu huruf besar ataupun huruf kecil.
5. Sepanjang 16 digit.
6. Terdapat sebuah karakter spesial.

input:
kode voucher top-up

proses:
1. Kode dimasukkan untuk proses pencarian
2. Pemrosesan kode dengan menggunakan pattern yang dibuat
3. Memberikan feedback berupa "Valid" atau "Invalid"

output:
Valid atau Invalid

Test case: 
Ab435i-6SDj23473
Bb435i6SDj234737
Bb435i-6SDj23473 (BERHASIL)
Bb435i-6SDj234yu
Bb435i-6S Dj2347
BB435I-SDJ234R73
Zb435i-6SDj23473

'''
import re
def valcode(kode):
    if len(kode) == 16 and not(re.search("\s", kode)):
        if not re.search("\d{5}",kode):
            print("Invalid")
        elif not re.search("[A-Za-z]", kode):
            print("Invalid")
        elif not re.search("^[^actvxyzACTVYZ]", kode):
            print("Invalid")
        elif not re.search("\W", kode):
            print("Invalid")
        else:
            print("Valid")
    else:
        print("Invalid")

kode = input("Masukkan kode voucher: ")
valcode(kode)