# Program Interpolasi Newton
# Spesifikasi: Program Interpolasi Newton
# Versi      : 1.0
# Last Edited: 2020-10-24
# Programmer : Sabda Wahidatulhusna

#kamus

print(" Nama       : Sabda Wahidatulhusna")
print(" NIM        : 12319030 ")
print(" Fungsi     : f(x) = sin(x) + cos(x)")
#Algoritma
import numpy as np
import matplotlib.pyplot as plt
x= np.arange(0.0,11.0,1)
y= np.sin(x) + np.cos(x)
N = len(x)
n_polinoms = int(input("Masukan Derajat Polinom:"))
n_polinom = n_polinoms + 1
ST = [[0 for j in range(n_polinom)]for i in range(N)]
print(ST)
for i in range (N):
    ST[i][0]=y[i]
for j in range (1,n_polinom):
    for i in range(N-j):
        ST[i][j] = (ST[i+1][j-1] -ST[i][j-1])/(x[i+j]-x[i])

x_soal = int(input("Nilai x yang akan di taksir:"))
jumlah = ST[0][0]
for i in range(1,n_polinom):
    suku=ST[0][i]
    for j in range(i):
        suku = suku*(x_soal-x[j])
    jumlah=jumlah+suku
y_jawab = jumlah
print("Hasil taksiran dari x adalah :",y_jawab)

N = 100
x_min = 0
x_max = 11.0
y_min = -10
y_max = 10
x_plot = [0 for i in range(N)]
y_plot = [0 for i in range(N)]

for k in range(N):
    x_plot[k] = ((x_max-x_min) / N) * k + x_min
    jumlah = ST[0][0]
    for i in range(1, n_polinom):
        suku = ST[0][i]
        for j in range(i):
            suku = suku * (x_plot[k] - x[j])
        jumlah = jumlah + suku
    y_plot[k] = jumlah

fig, ax = plt.subplots()
ax.plot(x,y, 'ro', label='data')
ax.plot(x_soal, y_jawab, 'bs', label='titik yang diestimasi')
ax.plot(x_plot, y_plot, "g", label='garis interpolasiderajat4')
legend = ax.legend()
plt.grid()
plt.axhline(y=0, color='#000000')
plt.xlabel("x")
plt.ylabel("f(x) = y")
plt.axis([x_min,x_max,y_min,y_max])
plt.show()
