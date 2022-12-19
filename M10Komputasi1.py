# Program Regresi Linear
# Spesifikasi: Program Regresi Linear & Nilai Erms
# Versi      : 1.0
# Last Edited: 2020-10-24
# Programmer : Sabda Wahidatulhusna

import numpy as np
import matplotlib.pyplot as plt
#KAMUS
#x array
#y array
#n int
#x_total int
#y_total int
#x_sq_total int
#xy_total int
#sumtot int
#x_plot array
#y_plot array
#N int

#Algoritma
def f(a,b,x):
    return a + b * x

x = np.array([1.0,1.5,2.0,2.5,3.0])
y = np.array([2.0,3.2,4.1,4.9,5.9])
n = x.size

x_total = 0
y_total = 0
x_sq_total = 0
xy_total = 0
#mencari regresi untuk a dan b
for i in range (n):
    x_total = x_total + x[i]
    y_total = y_total + y[i]
    x_sq_total = x_sq_total + x[i] * x[i]
    xy_total = xy_total + x[i] * y[i]
b = (n * xy_total -x_total * y_total) / (n * x_sq_total -(x_total) * x_total)
a = y_total/n -b * x_total/n
print("a = ", a)
print("b = ", b)
print("𝑓(𝑥)=",a,"+",b,"𝑥")#hasil persamaan regresi

sumtot=0
# mencari Erms
for i in range (n):
    fxkurangY = (abs(f(a,b,x[i]) - y[i]))**2
    sumtot+= fxkurangY
E=(1/n*(sumtot))**1/2
print("Nilai Erms adalah",E)#Hasil Erms
#mencari nilai perkiraan
x_soal = [1.2, 2.7, 3.5, 4.0]
xsoal= len(x_soal)
for i in range (xsoal):
    y_jawab = f(a,b,x_soal[i])
    print(i+1,".Nilai perkiraan y untuk x = ", x_soal[i], " adalah : ", y_jawab)
    #hasil mencari nilai perkiraan setiap x

#Membuat plot untuk regresi
N = 100
x_plot = [0 for i in range(N)]
y_plot = [0 for i in range(N)]
for i in range (N):
    x_plot[i] += (5 / 100.0) * i
    y_plot[i] += f(a,b,x_plot[i])
fig, ax = plt.subplots()
ax.plot(x, y, 'ro', label='data')
for j in range (xsoal):
    y_jawab = f(a,b,x_soal[j])
    ax.plot(x_soal[j], y_jawab, 'bs')
ax.plot(x_soal[0],f(a,b,x_soal[0]),'bs',label='titik yang diestimasi')
ax.plot(x_plot, y_plot, 'g', label='garis regresi')
legend = ax.legend()
plt.xlabel("x")
plt.ylabel("f(x) = y")
plt.grid(True, which='both')
plt.show()#hasil plot

