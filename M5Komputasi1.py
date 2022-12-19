# Program Pengurutan
# Spesifikasi: Program untuk mengurutkan data array
# Versi      : 1.1
# Last Edited: 2020-09-20
# Programmer : Sabda Wahidatulhusna


#kamus
#a Array
print("==============Program untuk mengurutkan data array==============")
print(" masukan 10 bilangan")
#algoritme
#a =[19 21 22 23 76 87 56 78 12 25]
a = [ ]
for i in range(1,11):
    a.append(int(input("masukan bilangan = ")))#masukan data sesuai array yang di berikan
a.sort()# Data disusun dari yang terkecil ke yang terbesar
a.reverse()# kemudian data  di balik ke yang Terbesar ke Terkecil
print("Terbesar ke yang tekecil", a)
