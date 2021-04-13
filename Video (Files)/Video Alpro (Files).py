'''
Azriel Setyo Nugroho H. (71200576)
Topik: Files
Referensi : 
Dari sebuah file text, anda harus mengambil nilai 


Input: 

Proses: 

Output: 
'''
# a = open("mbox.txt", "r")
# b = []
# for i in a:
#     b.append(i)
# c = open("hasil.txt", "w")
# for i in b:
#     c.write(i)

filename = input("nama file: ")
handle1 = open(filename, "r")
c = 0
a = []
b = []

# for line in handle:
#     if line.startswith("Subject:"):
#         c += 1
#         line = line.strip().title()
#         print(line)
# print("Jumlah: ",c)



# for i in handle:
#     i = i.split()
#     for j in i:
#         print(j[-3:])
#         if j[-4:] == ".edu" or ".org":
#             a.append(j)
#             c += 1
#         elif j[-3:] == ".za" or ".uk":
#             a.append(j)
#             c += 1



# while True:
#     print("""Selamat datang di Kuis Dadakan
# Silahkan pilih mode soal:
# 1. Easy
# 2. Medium
# 3. Hard""")
#     masuk1 = int(input("Silahkan masukan pilihan: "))



for i in handle1:
    i = i.split("||")
    for j in i:
        if c % 2 == 0:
            j = j.strip()
            a.append(j)
            c += 1
        elif c % 2 == 1:
            j = j.strip()
            b.append(j)
            c += 1
# print(a)
# print(b)

handle2 = open("hasil.txt", "w")

c = 1
for i in a:
    try:
        print(f"{c}. {a[c]}")
        inp = input("\tMasukkan jawaban: ")
        if inp == b[c]:
            print("Jawaban benar!")
            handle2.write(f"{c}. Jawaban benar\n")
            c += 1
        elif inp != b[c]:
            print("Jawaban salah!")
            handle2.write(f"{c}. Jawaban salah\n")
            c += 1
    except:
        print("Sudah selesai, terimakasih")

handle1.close()
handle2.close()