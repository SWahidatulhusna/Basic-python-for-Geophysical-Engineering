# Program menghitung suatu suku bunga
# Spesifikasi: Program menghitung suatu suku bunga dengan bunga nya sesuai NIM
# Versi      : 1.3
# Last Edited: 2020-09-18
# Programmer : Sabda Wahidatulhusna

#kamus
#a STR
#b INT
#bunga float
#modal float
#i INT

#Algoritma
print(" Program Interaktif")
print("-"*100)
a = str(input("Masukan Nama:"))#menginput nama
b = int(input("Masukan NIM:"))#menginput NIM
modal= float(input("Masukan Modal:"))#menginput modal
bunga = b/100000000# bunga merupakan 0.XX dimana XX adalah NIM ex:0.1231903
print("Bunga:", bunga)
i = int(input("Bulan:"))#menginput bulan
z = 0
x = 1
print("Hallo", a, "NIM kamu adalah",b)

while ( i!=0  ):#dibuat pernyataan while i bukan sama dengan 0
    saldoAkhir = (modal * bunga) * z+ modal# memproses saldo sesuia keinginana bulan
    print("Saldo bulan ke",x,"adalah:",saldoAkhir)
    i -= 1# karena while i bukan sama dengan 0 maka saat memasukan bulan kondisinya true dan di buat i-= agar berhenti sesuai jumlah bulan yang dinginkan
    z +=1 #variabel z untuk menampilkan jumlah bulan dan memproses penghitungan uang sesuai bulan yang diinginkan
    x+= 1
print("-"*100)