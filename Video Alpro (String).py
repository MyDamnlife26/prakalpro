'''
Azriel Setyo Nugroho H. (71200576)
Topik : String
Referensi : UG

Dito berteman dengan Dadi. Dito mengirimkan pesan dalam bentuk yang tidak karuan kepada Dadi. 
Bentuk pesannya seperti ini:
KsdAaK234AsfdK M342EfsdNgdfG234O234NertTR3456gdfgAK RasfU34M2345AfhgH K324ewE324C435dfgrIL D345tdI D324reEdfgSA. f352AYsdfAHfssfd NsffsdA543I543dfgK UfsdNTewtU34K MsdfEgdfLfsdIfHdgfAT Grget345EdsggNdfgTdfgE534frdNdgfG RdfhdfdUgdf3235MdfgAerw53H KgO2436NdgdfTRgdfgAKdfdfgAN Y3tr52AdrtNtg54G Bgd43Ofs3t4Chyt34342O534gdfR. AKfr243U Mfd2345E52gf34LIfd523Hf5234Ad2345T Kdd3456Ed5324Jad5A6gDytI678ArtyN I1c23T24g3vU Dcv234v6bE2cv3N34545G4b23AN Mc1324Ac123Tc123A43K4v23Uv423v2. KdfgdAfsdgM345Usfd KE34tr5NdhfgA P345gdRfAfgNetrdK, HegrgAdfgHdergAre34HgergA.

Dito memberikan clue bahwa huruf besar adalah pesannya. Bantulah Dadi untuk mengetahui pesan itu!

Input: 
Pesan Dito

Proses: 
1. Membuat input untuk pesan Dito.
2. Membuat perulangan dan percabangan, untuk mencacah pesan Dito dan mengetahui isi pesannya.

Output: Pesan Dito dalam bentuk yang baku dan mudah dibaca.

'''
b = ''
a = input('Masukkan pesan: ')
for i in a:
    if i.isupper():
        b += i
    elif i == ' ':
        b += i
    elif i == '.': 
        b += i

b = b.lower()
b = b.split('.')

for i in b:
    i = i.strip()
    i = i.capitalize()
    print(i, end = '. ')