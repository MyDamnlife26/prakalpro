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
handle = open(filename, "r")
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
#     i = i.split(" ")
#     for j in i:
#         print(j[-3:])
#         if j[-3:] == "edu" or "org":
#             a.append(j)
#             c += 1
#         elif j[-2:] == "za" or "uk":
#             a.append(j)
#             c += 1

for i in handle:
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
print(a)
print(b)

c = 0
for i in a:
    print(a[c])
    inp = input("Masukkan jawaban: ")
    if inp == b[c]:
        print("Jawaban benar!")
        c += 1
    elif inp != b[c]:
        print("Jawaban salah!")
        c += 1