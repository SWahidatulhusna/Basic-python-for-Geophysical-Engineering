import numpy as np
import math
import matplotlib.pyplot as plt

#Define

#lokasi stasiun awal
xs = np.array([443.68274,446.97741,438.15595])#UTM X
ys = np.array([9115.75662,9125.71087,9127.91105])#UTM Y
zs = np.zeros(1, len(xs))

#cepat rambat gelombang
vs = 6.6

#waktu tempuh gelombang puntukmasing - masing stasiun
tobs = [31.915,31.516,31.889]

#waktu awal(dari diagram wadati)
to = 28.489

#jumlah stasiun
js = len(xs)

#PROSES INVERSI

#model awal(didapat dari penghitungan metode 3 lingkaran)
xo = 444.90405
yo = 9124.86139
zo = -20.6656

# 30 kali iterasi
for it in range(1,30):
    # mencari delta t
    dt = tobs.conj().transpose() - tcal.conj().transpose()

    # membentuk matriks Jacobi
    G = [x' y' z'];

         # menginversi
         dm = inv(G'*G)*G' * dt;

    # Modifikasi model awal
    xo = xo + dm(1);
    yo = yo + dm(2);
    zo = zo + dm(3);

    # mencari error
    misfit(it) = sqrt(mean(dt. ^ 2));

    for i in range(1,js):
    #Menghitung tcal
        tcal[i] = to + sqrt((xo - xs[i])^ 2 + (yo - ys[i]) ^ 2 + (zo - zs[i]) ^ 2)) / vs

    #Komponen x
        x[i] = (xo - xs[i]) / (sqrt((xo - xs[i]) ^ 2 + (yo - ys[i]) ^ 2 + (zo - zs[i]) ^ 2) * vs)

    #Komponen y
        y[i]= (yo - ys[i]) / (sqrt((xo - xs[i]) ^ 2 + (yo - ys[i]) ^ 2 + (zo - zs[i]) ^ 2) * vs)

    #Komponen z
        z[i] = (zo - zs[i]) / (sqrt((xo - xs[i]) ^ 2 + (yo - ys[i]) ^ 2 + (zo - zs[i]) ^ 2) * vs)
    break




##menampilkan koordinat hiposenter xo yo zo##

#plot hiposenter figure
plot3(xs, ys, zs, 'ob', xo, yo, zo, '*m')
set(gca, 'ZDir', 'reverse')
grid
on
title('koordinat stasiun dan hiposenter')
xlabel('Sumbu x')
ylabel('Sumbu y')
zlabel('Sumbu z')
hold
on

% plot
error
iterasi
figure
plot(1: length(misfit), misfit);
xlabel('Iterasi');
ylabel('RMS');
title('Grafik RMS');
grid
on