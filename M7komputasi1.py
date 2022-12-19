# Program menampilkan plot
# Spesifikasi: Program menampilkan plot dari fungsi(x,y)
# Versi      : 1.9
# Last Edited: 2020-10-04
# Programmer : Sabda Wahidatulhusna

import numpy as np
import matplotlib.pyplot as plt

#kamus
#x array
#fungsisinus def pernyataan

#Algoritma
def fungsiSinusoidal(A):
    x = np.arange(0,1.5,0.01)#untuk0≤𝑥≤1.5,a.Interval x setiap 0.01
    y = (10*A) -(10*A+0.1)*((np.sin(x))**2) + 0.0021*((np.sin(x))**2)*((np.tan(x))**2)
    return x,y

A = 0.30#dimana A = 0.xx dan xx adalahdua digit akhir dariNIM
x,y = fungsiSinusoidal(A)


judul = r'$\mathcal{Kurva \ dari} $'
rumus = r'$ \mathcal{Y} = 10(A) - (10A+0.1) sin^2 x + 0.0021 sin^2 x tan^2 x $'
plt.plot(x,y,'g')#b.Warna garis hijau
plt.suptitle( judul )#c.Beri judul
plt.title(rumus)
plt.xlabel('sumbu-x')#d.Beri keterangan pada sumbu-x
plt.ylabel('sumbu-y')#e.Beri keterangan pada sumbu y


plt.show()