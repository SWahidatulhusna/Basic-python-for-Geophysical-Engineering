# Program Fibonacci
# Spesifikasi: Program Angka fibonnaci berdasarkan bessar arrray
# Versi      : 1.4
# Last Edited: 2020-09-27
# Programmer : Sabda Wahidatulhusna

#KAMUS
#NAMA str
#NIM int
#fibonacci Array
#N int

#Algoritma
print("Program Interaktif")
print("-"*100)
nama= str(input("Masukan nama: "))#menginput  nama
nim= int(input("Masukan NIM: "))#menginput masukan nim
print("-"*100)
print("Hallo saya", nama ,",nim saya adalah:" , nim)
import numpy as np#mengimport numpy sebagi np array

fibonacciSeries = np.array ([0,1]).astype('int64')
print("N adalah penjumlahan 2 angka terakhir nim anda ditambahkan 1")
N = int(input("masukan N:")) #menginput n dimana suatu matrix n x 4 dimana nilai n adalah penjumlahan dari 2 angka terakhir nimanda ditambahkan 1.
if N>2: # jika N lebih dari 2
	for i in range(2,N*4):#untuk i dalam range 2 dana matrik nx4
		nextElement = fibonacciSeries[i-1] + fibonacciSeries[i-2]# i akan di loop sesuai range
		fibonacciSeries = np.append(fibonacciSeries,nextElement)# fibonacci akan bebentuk array

hasil = fibonacciSeries.reshape([N,4])#hasil fibonacci akan di ubah bentuk nya menjadi Nx 4
print(hasil)