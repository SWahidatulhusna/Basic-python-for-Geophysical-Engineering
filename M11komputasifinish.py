# Program Interpolasi Polinom
# Spesifikasi: Program Interpolasi Polinom Newton
# Versi      : 1.0
# Last Edited: 2020-11-07
# Programmer : Sabda Wahidatulhusna


print(" Nama       : Sabda Wahidatulhusna")#menampilkan nama
print(" NIM        : 12319030 ")#menampilkan nim
print(" Fungsi     : f(x) = sin(x) + cos(x)")#menampilkan fungsi
#kamus
#f(x) Argumen
#x List
#y List
#n Int
#n_polinom List
# x_plots list kosong
# y_plots list kosong
# y_jawabs list kosong
# N int
# x_min int
# x_max  int
# y_min  int
# y_max  int
# x_plot  list nol
# y_plot list nol

#Algoritma
#import perpus yg di butuhkan
import numpy as np
import matplotlib.pyplot as plt
#membuat argumen f(x)
def f(x):
    return np.sin(x) + np.cos(x)
x= [float(j) for j in range(0,11)]#mengisi x (list) dengan looping j dari 0 sampai 10 dengan tipe float
y = [f(i) for i in x]#mengisi y(list) dengan looping dari x ke fung f(x)
n = 10
n_polinom = [1,2,3,4]#jumlah derajat polinom
x_plots = []#list kossong
y_plots = []#list kososng
y_jawabx = []#list kososng

for jj in n_polinom:
    n_derajat = jj
    n_derajat = n_derajat + 1
    ST = [[0 for j in range(n_derajat)]for i in range(n)]#membuat array 0 dengan shape(derajat polinom, jumlah data x)
    # print (ST)
    for i in range(n):
        ST[i][0] = y[i]
    # print(ST)
    for j in range(1,n_derajat):
        for i in range(n-j):
            ST[i][j] = (ST[i+1][j-1] -ST[i][j-1])/(x[i+j]-x[i])# menghitung array dengan rumus interpolasi
    x_soal = 3.0# taksiran x yang di cari
    jumlah = ST[0][0]
    for i in range(1, n_derajat):#menghitung hasil y yang di taksir x=3
        suku = ST[0][i]
        for j in range(i):
            suku = suku * (x_soal - x[j])
        jumlah = jumlah + suku
    y_jawab = jumlah
    # MEMBENTUK KURVA INTERPOLASI BERDASAR DERAJAT N
    N= 100
    x_min = 0
    x_max = 10.0
    y_min = -2.0
    y_max = 2.0
    x_plot = [0 for i in range(N)]# membuat arrray 0 dengan jumlah looping dari range (N)
    y_plot = [0 for i in range(N)]# membuat arrray 0 dengan jumlah looping dari range (N)
    for ii in range(N):
        x_plot[ii] = ((x_max - x_min) / N) * ii + x_min
        jumlah = ST[0][0]
        for i in range(1, n_derajat):
            suku = ST[0][i]
            for j in range(i): #menghitung kurva interpolasi berdasarkan n derajat
                suku = suku * (x_plot[ii] - x[j])
            jumlah = jumlah + suku
        y_plot[ii] = jumlah
    # hasil semua looping di masukan ke list kosong pada awal
    x_plots.append(x_plot)
    y_plots.append(y_plot)
    y_jawabx.append(y_jawab)
print("nilai taksiran fungsi di x=3.0 dengan polinom derajat tiga adalah ",y_jawabx[2])#untuk menjawab soal nomor 1
fig, ax = plt.subplots(2,2) #membuat 4 plot
y_jawabx = np.array(y_jawabx).reshape(2,2)# list y_jawabx di ubah menjadi array 2x2
derajat = 0#variable untuk iterasi
colors = [['purple','grey'],['green','brown']]
#plot grafik interpolasi dengan looping
for row in range(2):
    for col in range(2):
        labels = 'Garis Interpolasi dengan Derajat ' + str(derajat+1)
        ax[row][col].plot(x, y, 'ro', label='Data')#menampilkan data x,y dengan warna merah lingkaran
        ax[row][col].plot(x_soal, y_jawabx[row][col], 'bs', label='Titik yang Diestimasi')#menampilkan plot xsoal dengan jawabs berwarna biru koatk
        ax[row][col].plot(x_plots[derajat], y_plots[derajat], color=colors[row][col], label=labels)#menapilkan plot interpolanis berdasarkan derajat plinomnnya
        ax[row][col].set_title('Interpolasi Polinom: F(x)= sin(x) + cos(x), Derajat ' + str(derajat + 1))#judul plot
        ax[row][col].set_xlabel("x")#judul label pada sumbu x
        ax[row][col].set_ylabel("f(x) = sin(x) + cos(x)")#judul labell pada sumbu y
        ax[row][col].axis([x_min -0.5, x_max +2 , y_min -5, y_max + 5])# set pada bum x dan xumbu y
        ax[row][col].legend(loc='lower right')#menampilkan legenda pada kanan bawah grafik
        ax[row][col].grid()#menapilkan garis pada grafik
        derajat+=1
fig.tight_layout()#agar grafik mudah di liat
plt.show()#menampilkan grafik