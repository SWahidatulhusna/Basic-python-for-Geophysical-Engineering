# Program hitung integral
# Spesifikasi: Program hitung integral menggunakan metode trapezoidal
# Versi      : 1.0
# Last Edited: 2020-10-17
# Programmer : Sabda Wahidatulhusna

print(" Nama       : Sabda Wahidatulhusna")
print(" NIM        : 12319030 ")
print(" Fungsi     : f(x) = 3𝑥^2+2)")
print(" Batas Bawah: 0")
print(" batas Atas : 5")
#kamus
#a INT
#b INT
#N List

#Algoritma
def f(x):  #fungsiyang ingin diintegralkan
    return 3*x**2 + 2

def trapZ(a,b,N):
    h=(b-a)/N#lebar grid
    jum=0.5*f(a)
    for i in range(1,N):
        xi=a+h*i
        jum= jum+f(xi)
    jum= jum+0.5*f(b)
    hasil= jum*h
    return hasil

a=0#batas bawah
b=5#batas atas
N=[1, 5, 10, 50, 100,1000]#jumlah grid
print("jumlah Grid       ||       Hasil   ")
for i in N:
    x=trapZ(a,b,i)
    print(i,'                   ',x)

import matplotlib.pyplot as plt
import numpy as np

def tabel(g):#menampil jumlah grid pada plot
    X=np.linspace(a,b,N[g]+1)#Grid yang akan di tampilkan
    Xd=np.linspace(a,b,N[g])#Xd Array untuk membuat ploting dengan F(Xd)
    for i in range (N[g]):
        xs=[X[i],X[i],X[i+1],X[i+1]]#garis sejajar sumbu x
        ys=[0,f(X[i]),f(X[i+1]),0]#garis sejajar sumbu y
        plt.fill(xs,ys,'b',edgecolor='b',alpha=0.2)#Jumlah grid di tampilkan pada ploting
    return Xd
ax1 = plt.subplot(2, 3, 1)
plt.plot(tabel(0),f(tabel(0)))#Menampilkan Plot pada jumlah Grid=1
plt.xticks([0,1,2,3,4,5])
plt.title('Trapezoid Rule, N = {}'.format(N[0]))
ax2 = plt.subplot(2, 3, 2)
plt.plot(tabel(1),f(tabel(1)))#Menampilkan Plot pada jumlah Grid=5
plt.xticks([0,1,2,3,4,5])
plt.title('Trapezoid Rule, N = {}'.format(N[1]))
ax3 = plt.subplot(2, 3, 3)
plt.plot(tabel(2),f(tabel(2)))#Menampilkan Plot pada jumlah Grid=10
plt.xticks([0,1,2,3,4,5])
plt.title('Trapezoid Rule, N = {}'.format(N[2]))
ax4 = plt.subplot(2, 3, 4)
plt.plot(tabel(3),f(tabel(3)))#Menampilkan Plot pada jumlah Grid=50
plt.xticks([0,1,2,3,4,5])
plt.title('Trapezoid Rule, N = {}'.format(N[3]))
ax5 = plt.subplot(2, 3, 5)
plt.plot(tabel(4),f(tabel(4)))#Menampilkan Plot pada jumlah Grid=100
plt.xticks([0,1,2,3,4,5])
plt.title('Trapezoid Rule, N = {}'.format(N[4]))
ax6 = plt.subplot(2, 3, 6)
plt.plot(tabel(5),f(tabel(5)))#Menampilkan Plot pada jumlah Grid=100
plt.xticks([0,1,2,3,4,5])
plt.title('Trapezoid Rule, N = {}'.format(N[5]))

plt.show()


