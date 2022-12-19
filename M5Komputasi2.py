# Program Angka Biner
# Spesifikasi: Program membuat angka biner dari angka nim
# Versi      : 1.2
# Last Edited: 2020-09-18
# Programmer : Sabda Wahidatulhusna
import math #menmasukan math ke program
i=0 #menginstruksikan bahwa fata di mulai dari nol
print("Program Interaktif")
print("-"*100)
#kamus
#a STR
#b INT

a = str(input('Masukan nama:'))#menginputa nama
b = int(input("Masukan NIM:"))# menginput nim
print("*ANGKA = 2 NOMOR AKHIR NIM + 69 ")
c = int(input("Masukan Angka:"))# menginput nim# disoal di beritahu angka merupakan XX+69 dimana XX adlah NIM
print("Masukan angka:",c )
print("-"*100)
print("Hallo", a , "NIM kamu adalah:", b)
print ("angka" , c,"dalam biner adalah:")

while (c != 0):# fungsi while perulangan yang teergantung input, disini menginput angka, dimana angka tidak sama dengan no
    hasil= c % 2#dicari modulus dari angka tersebut
    c = math.floor(c/2)# data angka yang dibagi 2 akan di nulat kan kebawah oleh fungsi math.floor
    print (' digit ke', i,":", hasil)
    i += 1
print("-"*100)