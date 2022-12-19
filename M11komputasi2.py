# Program Interpolasi Newton
# Spesifikasi: Program Interpolasi Newton
# Versi      : 1.0
# Last Edited: 2020-10-24
# Programmer : Sabda Wahidatulhusna

#kamus


#Algoritma
import numpy as np
import matplotlib.pyplot as plt
x= np.arange(0.0,11.0,1)
y= np.sin(x) + np.cos(x)

N=len(x)
n_polinoms = 1
n_polinom = n_polinoms + 1
ST = [[0 for j in range(n_polinom)]for i in range(N)]
for i in range (N):
    ST[i][0]=y[i]
for j in range (1,n_polinom):
    for i in range(N-j):
        ST[i][j] = (ST[i+1][j-1] -ST[i][j-1])/(x[i+j]-x[i])

N = 100
x_min = 0
x_max = 11.0
y_min = -5
y_max = 5
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
print(jumlah)



fig, ax = plt.subplots()
ax.plot(x,y, 'ro', label='Data')
ax.plot(x_plot, y_plot, "g", label='Garis Interpolasi Derajat{}'.format(n_polinoms))
legend = ax.legend()
plt.xlabel("x")
plt.grid()
plt.axhline(y=0, color='#000000')
plt.ylabel("f(x) = y")
plt.axis([x_min,x_max,y_min,y_max])
plt.show()