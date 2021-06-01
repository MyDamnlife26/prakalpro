'''
Azriel Setyo Nugroho H. (71200576)
Topik : Rekursif
Referensi : UG

Carilah hasil dari perkalian bilangan prima sesuai dengan jumlah yang ditentukan dengan menggunakan fungsi rekursif.

Output: 
print(kaliPrima(3)) = (2*3)*5) = (6*5) = 30
print(kaliPrima(5)) = (((2*3)*5)*7)*9) = 2310
'''


def kaliPrima(a, lst=[], b=2):
    while len(lst) != a:
        if b not in lst:
            if b == 2 or b == 3 or b == 5 or b == 7 or b == 11 or b == 13 or b == 17 or b == 23 or b == 29 or b == 31 or b == 37 or b == 41 or b == 43 or b == 47 or b == 53 or b == 59 or b == 61 or b == 67 or b == 71 or b == 73 or b == 79 or b == 83 or b == 89 or b == 97:
                lst.append(b)
                b += 1
            else:
                kaliPrima(a, lst, b+1)
        else:
            kaliPrima(a, lst, b+1)
    hasil = 1
    for i in lst:
        hasil = hasil * i
    return(hasil)


print(kaliPrima(6))
print(kaliPrima(7))
