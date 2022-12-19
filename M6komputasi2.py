# Program Fmengubah bilang desimal ke bilangan biner
# Spesifikasi: Program mengubah bilang desimal ke bilangan biner
# Versi      : 1.4
# Last Edited: 2020-09-27
# Programmer : Sabda Wahidatulhusna

import numpy as np #mengimport numpy sebgai np
import math#mengimport math

#KAMUS
# NAMA STR
# nim int
# n int
# desimal ARRAY
# A array

print("-" * 100)
nama = str(input("Masukan nama: "))#menginput nama
nim = int(input("Masukan NIM: "))#menginput nim
print("-" * 100)

n = int(input("Masukan 2 angka nim terakhir anda:"))#menginput n
desimal = np.array([0, 1, 2, 3, 15, 16, 32, 64, 128, n])
print(desimal)
print("Matriks biner dari Array diatas yaitu: ")

def deskeBin(desimal):#argumen bagian untuk biner
    a = np.array([])# variabel a untuk array kosong
    while (desimal != 0):# akan di while apa bila desimal bukan sama dengan no
        hasil = desimal % 2
        desimal = math.floor(desimal / 2)
        a = np.append(a, hasil)
    return a #didapat a bilang biner dari array desimal dalam bentuk array list terbalik dan digit nya belum rata

jumlahDigit = len(deskeBin(max(desimal)))# jumlah digit diambil yang baling besar dari biner array a
hasilakhir=np.array([])# dibuat variabel hasil akhir agar menambah digit dan membalikan angka biner dan mengubah dari data list ke data array
for i in desimal:#i dalam desimal
    hasil = deskeBin(i).astype('int32')#variabel hasil dmengubah pernyattaan deskebin diulang untuk i dalam int

    ix = len(hasil) - 1#variable ix untuk merubah hasil posisi nya terbalik

    for j in range(len(hasil)):#kemudian di loop dalam range panjang hasil
        if j != ix:# jika j bukan sama dengan ix
            hasildibalik = hasil[j]#maka hasil di balik merupakan hasil j
            hasil[j] = hasil[ix]# dimana hasilj sama dengan hasil ix
            hasil[ix] = hasildibalik #maka hasilil di balik


    while len(hasil) != jumlahDigit :#kemudian hasil bukan sama dengan jumlah digit
        hasil = np.insert(hasil,0,0)#jika kondisi true digit akan di tamabah sampai max

    hasilakhir = np.append(hasilakhir,hasil)# hasil akhir merupakaarray hasil akhir dan hasil
print(hasilakhir.reshape((len(desimal),jumlahDigit)))# menampilkan hasil akhir
Biner = hasilakhir.reshape((len(desimal),jumlahDigit))

print(100*"-")
print("a. tunjukkan bariske 7 dari matrix :",Biner[6])
print("b. Tunjukkan elemen ke [x1,x2] dari matrix dimana x1 adalah angka keduaterakhir nim dan x2 adalah angka terakhir")
print("nim (e.g. nim 31 x1 =3 x2=1).Jika angka nimmelebihi size matrix, tuliskan elemen paling akhir dari matrix.")
print("nim 30 x1= 3 dan x2=0")
print(Biner[2,-1])