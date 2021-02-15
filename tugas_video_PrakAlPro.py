'''
Bila sebuah katrol yang terbuat dari benda pejal dengan percepatan linear sebesar 25.5 m/s^2, 
percepatan sudut sebesar 250.5 rad/s^2, dan momen gaya sebesar 6 Nm. Berapakah besar massa 
katrol (dalam satuan kg dan 1 angka di belakang koma?
(Sumber Referensi = https://gurumuda.net/pembahasan-soal-un-fisika-sma-tahun-2015.htm)

I = (2/5)*m*r^2
τ = I*α
a = r*α

I = Momen inersia katrol
m = Massa kartol
r = Jari-jari katrol
τ = Momen gaya
α = Percepatan sudut
a = Percepatan linear

Ditanya = Massa katrol (kg)?

Input = a = 25.5; τ = 6 ; α = 250.5

Proses = 
1. Mencari momen inersia katrol
2. Mencari jari-jari katrol
3. Mencari massa katrol 

Output = massa katrol (kg)

'''
a = float(input('Masukkan besar percepatan linear katrol = '))
b = float(input('Masukkan besar percepatan sudut = '))
c = float(input('Masukkan momen gaya katrol = '))

I = c / b
r = a / b
m = I / ((2/5)*(r**2))

print(f'Massa katrol adalah %.1f' %(m), 'kg')