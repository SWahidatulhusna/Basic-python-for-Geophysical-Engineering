import numpy as np
import math
from statistics import mean
#Define

#lokasi stasiun awal
xs = [443.68274,446.97741,438.15595]#UTM X
ys = [9115.75662,9125.71087,9127.91105]#UTM Y
zs = np.zeros(3)
print(xs)
print(ys)
print(zs)
#cepat rambat gelombang
vs = 6.6

#waktu tempuh gelombang puntukmasing - masing stasiun
tobs = np.array([[31.915],[31.516],[31.889]])

#waktu awal(dari diagram wadati)
to = 28.489

#jumlah stasiun
js = len(xs)

xo = 444.90405
yo = 9124.86139
zo = -20.6656

tcalarray =[]
xsarray =[]
ysarray =[]
zsarray =[]


for i in range(0,js):
    #Menghitung tcal
    tcal= to + math.sqrt((xo - xs[i])**2 + (yo - ys[i])**2 + (zo - zs[i])**2) / vs

    #Komponen x
    x= (xo - xs[i]) / (math.sqrt((xo - xs[i])**2 + (yo - ys[i])**2 + (zo - zs[i])**2) * vs)

    #Komponen y
    y= (yo - ys[i]) / (math.sqrt((xo - xs[i])**2 + (yo - ys[i])**2 + (zo - zs[i])**2) * vs)

    #Komponen z
    z= (zo - zs[i]) / (math.sqrt((xo - xs[i])**2 + (yo - ys[i])**2 + (zo - zs[i])**2) * vs)
    xsarray.append(x)
    ysarray.append(y)
    zsarray.append(z)
    tcalarray.append(tcal)
print(tobs.transpose())
for it in range(0,29):
    # mencari delta t
    dt = np.transpose(tobs) - np.transpose(tcalarray)

    # membentuk matriks Jacobi
    G = [np.transpose(xsarray),np.transpose(ysarray),np.transpose(zsarray)]
    Gtrans= np.transpose(G)

    Ginv= np.linalg.inv(Gtrans*G)
    # menginversi
    dm = Ginv * Gtrans * dt

    # Modifikasi model awal
    xo = xo + dm[0]
    yo = yo + dm[1]
    zo = zo + dm[2]

    # mencari error
    misfit = math.sqrt(mean(dt**2))
