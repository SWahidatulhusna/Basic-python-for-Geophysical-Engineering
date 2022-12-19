# Program    : Menampilkan Persamaan Diferensial Biasa 1
# Spesifikasi: Persamaan Diferensial Biasa 1 dengan Metode Euler,Runge Kutta, dan Heun
# Versi      : 1.0
# Last Edited: 2020-11-12
# Programmer : Sabda Wahidatulhusna

#kamus
# dx list
# bawah int
# atas int
# N list
# X list
# Y list
# yEuleur list
# yHeun list
# yRungeKutta list

#Algoritma
import numpy as np#import library numpy
import matplotlib.pyplot as plt#import library matplotlib

def fungsi(x,y):#defnisikan soal
    output = -2 * np.power(x,3) + 12 * np.power(x,2) - 20 * x + 8.5
    return output
def yAnalitik(x):#definsikan hasil analitik soal
    yanal= -0.5*np.power(x,4)+ 4*np.power(x,3)-10*np.power(x,2)+8.5*x+1
    return yanal
dx = [0.5,0.1,0.01,0.05]#lebar grid
bawah = 0#mulai dari 0
atas = 4#hingga 4
#list kosong untuk memudahkan plot
N=[]
X=[]
Y=[]
yEuleur=[]
yHeun=[]
yRungeKutta=[]

for i in range (len(dx)):#menghitung n
    n= (int)((atas-bawah) / dx[i]) + 1
    N.append(n)# memasukan hasil n ke list array
for j in range (len(N)):#menghitung x
    x = np.linspace(0,4,num=N[j])
    X.append(x)# memasukan hasil x ke list array
for k in range (len(N)):#menghitung y analitik
    y= yAnalitik(X[k])
    Y.append(y)#memasukan y ke list array
for k in range (len(N)):
    Xarray = X[k]
    Yarray = Y[k]
    ye = np.zeros(N[k])
    ye[0] = 1
    # -------------------------------------------
    # Euler
    for i in range (N[k]-1):#menghitung dengan metode euler
        ye[i+1] = ye[i] + dx[k] * fungsi(Xarray[i], ye[i])
    yEuleur.append(ye)#memasukan hasil metode Euler ke list array
    #-------------------------------------------
    #Heun
    yh = np.zeros(N[k])
    yh[0] = 1
    for i in range(N[k]-1):#menghitung dengan metode heun
        k1 = fungsi(Xarray[i], yh[i])
        k2 = fungsi(Xarray[i]+dx[k], yh[i]+dx[k] * k1)
        yh[i+1] = yh[i] + dx[k] * (k1 + k2) / 2
    yHeun.append(yh)#memasukan hasil metode heun ke list array
    # -------------------------------------------
    #Runge Kutta
    yrk = np.zeros(N[k])
    yrk[0] = 1
    for i in range (N[k]-1):#menghitung dengan metode runge kutta
        k1 = fungsi(Xarray[i], yrk[i])
        k2 = fungsi(Xarray[i] + 0.5 * dx[k], Yarray[i] + 0.5 * dx[k] * k1)
        k3 = fungsi(Xarray[i] + 0.5 * dx[k], Yarray[i] + 0.5 * dx[k] * k2)
        k4 = fungsi(Xarray[i] + dx[k], Yarray[i] + dx[k] * k3)
        yrk[i+1] = yrk[i] + ((k1 + 2 * k2 + 2 * k3 + k4) * dx[k])/6
    yRungeKutta.append(yrk)#memasukan hasil metode Runge kutta ke list array
    # -----------------------------------------------
    #Menampilkan plot dari dari masing-masing plot berdasar lebar grid
    plt.subplot(2, 2, k+1)# sub plot 4x4
    plt.plot(X[k], Y[k], "k", label="analitik")#plot untuk metode analitik
    plt.plot(X[k], yEuleur[k], "r", label="Euler")#plot untuk metode Euler
    plt.plot(X[k], yRungeKutta[k], "g--", label="Runge Kutta")#plot untuk metode Runge kutta
    plt.plot(X[k], yHeun[k], "b", label="Heun")#plot untuk metode heun
    plt.xlabel("Nilai-x")#memberi judul pada sumbu x
    plt.ylabel("Nilai-y")#memberi  judul pada sumbu y
    plt.title('Lebar Grid {}'.format(dx[k]))#memberi judul pada plot
    plt.grid()#memberi garis-garis
    plt.legend(loc='lower right')#menempatkan legenda di kiri bawah
plt.tight_layout()#memberi jarak antar plot lain agar mudah terlihat
plt.show()#menampilkan plot