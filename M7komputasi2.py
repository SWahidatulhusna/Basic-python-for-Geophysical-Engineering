# Program menampilkan plot
# Spesifikasi: Program menampilkan plot dari dekomposisi fungsi sinus atau cosinus
# Versi      : 1.8
# Last Edited: 2020-10-04
# Programmer : Sabda Wahidatulhusna

import numpy as np
import matplotlib.pyplot as plt
#kamus
#fungsi (x,n) & fungsi (v,m) def
#x & v array range
#max_N &max_M int
#sumY & sumZ int
#N & M int
#n & m int

#Algoritma
def fungsi(x,n):
    return np.sin(n*x)/n

x = np.arange(-10,10,0.0002)#a.Nilai x antara -10 dan 10
max_N = 90  #c.Suku terbesar sampai suku ke xx+60.
            # d.Dimana xx adalah NIM. Misal nim 40
sumY = 0
N = 1
while N <= max_N:
     n = 2*N-1
     sumY += fungsi(x,n)
     N += 1
y = 0.5 +2*sumY/np.pi

aPlot = plt.plot(x,y)
plt.setp(aPlot ,color = 'r')#b.Warna Garis Merah

def fungsi(v,m):
    return np.sin(m*v)/m

v = np.arange(-10,10,0.0002)
max_M = 100#e.sampai suku ke 100 yaitu sin 199x /199
sumZ = 0
M = 1
while M <= max_M:
     m = 2*M-1
     sumZ += fungsi(v,m)
     M += 1
z = 0.5 +2*sumZ/np.pi

b = plt.plot(v,z)


plt.setp(b, color ='r')
#f.Beri judul dan label
plt.title('Fungsi Kotak')
plt.xlabel('time(s)')
plt.ylabel('amplitude')
plt.show()