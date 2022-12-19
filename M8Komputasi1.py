# Program Matriks
# Spesifikasi: Program Matriks dengan Eliminasi Gauss
# Versi      : 1.0
# Last Edited: 2020-10-11
# Programmer : Sabda Wahidatulhusna


#kamus
#a ARRAY
#b ARRAY
#n INT
#b[K] FLOAT
#lam FLOAT

#ALGORITMA
def EliminasiGauss(a,b):
    n=len(b)#jumlah
    #eliminasi
    for k in range (0,n-1): #k=indeks kolom, k=0,1,...
        for i in range (k+1,n): # i= indeks baris, i= 1,2,...
            if a[i,k] != 0.0:
                lam= a[i,k]/a[k,k]
                a[i,k+1:n]= a[i,k+1:n]- lam*a[k,k+1:n]
                b[i]=b[i]- lam*b[k]
    #back subtitusion
    for k in range (n-1,-1,-1):
        b[k]=(b[k]- np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b


import math
import numpy as np

print("Program Eliminasi Gauss untuk menyelesaikan persamaan berikut dan cek solusinya dengan memasukkan hasil ke dalam persamaan.")
print("①. 𝑎+2𝑏=10")
print(" 1.1𝑎+2𝑏=10.4")
x = EliminasiGauss(np.array([[1.0,2.0],[1.1,2.0]]),[10.0,10.4])
print("a =",x[0])
print("b =",x[1])
persamaan1= x[0]+ 2*x[1]#CEK PERSAMAAN
print("Cek Persamaan:")
print("①.𝑎+2𝑏=10")
print("(",x[0],")","+ 2","(",x[1],")","=",persamaan1)
print("="*100)
print("②. 8𝑎+2𝑏−2𝑐=−2")
print("   10𝑎+2𝑏+4𝑐=4")
print("   12𝑎+2𝑏+2𝑐=6")
y = EliminasiGauss(np.array([[8.0,2.0,-2.0],[10.0,2.0,4.0],[12.0,2.0,2.0]]),([-2.0,4.0,6.0]))
print("a =",y[0])
print("b =",y[1])
print("c =",y[2])
persamaan2 = 8 * y[0] + 2 * y[1] - 2 * y[2]#CEK PERSAMAAN
print("Cek Persamaan:")
print("②8𝑎+2𝑏−2𝑐=−2")
print("8","(",y[0],")","+ 2","(",y[1],")","− 2","(",y[2],") =",persamaan2)
print("="*100)
print("③. 2𝑎+𝑏−𝑐+2𝑑=5")
print("    4𝑎+5𝑏−3𝑐+6𝑑=9")
print("   −2𝑎+5𝑏−2𝑐+6𝑑=4")
print("    4𝑎+11𝑏−4𝑐+8𝑑=2")
m = EliminasiGauss(np.array([[2.0,1.0,-1.0,2.0],[4.0,5.0,-3.0,6.0],[-2.0,5.0,-2.0,6.0],[4.0,11.0,-4.0,8.0]]),[5.0,9.0,4.0,2.0])
print("a =",m[0])
print("b =",m[1])
print("c =",m[2])
print("d =",m[3])
persamaan3= 4*m[0]+5*m[1]-3*m[2]+6*m[3]#CEK PERSAMAAN
print("Cek Persamaan:")
print("③. 4𝑎+5𝑏−3𝑐+6𝑑=9")
print("4","(",m[0],")","+ 5","(",m[1],")","− 3","(",m[2],"),+ 6","(",m[3],") =",persamaan3)
print("="*100)
print("④. 2𝑎+𝑏+4𝑐+𝑑−𝑒=7")
print("   −𝑎+3𝑏−2𝑐−𝑑+2𝑒=1")
print("   5𝑎+𝑏+3𝑐−4𝑑+𝑒=33")
print("   3𝑎−2𝑏−2𝑐−2𝑑+3𝑒=24")
print("  −4𝑎−𝑏−5𝑐+3𝑑−4𝑒=−49")
z= EliminasiGauss(np.array([[2.0,1.0,4.0,1.0,-1.0],[-1.0,3.0,-2.0,-1.0,2.0],
                            [5.0,1.0,3.0,-4.0,1.0],[3.0,-2.0,-2.0,-2.0,3.0],
                            [-4.0,-1.0,-5.0,3.0,-4.0]]),[7.0,1.0,33.0,24.0,-49.0])
print("a =",z[0])
print("b =",z[1])
print("c =",z[2])
print("d =",z[3])
print("e =",z[4])
persamaan4= math.floor(5*z[0]+z[1]+3*z[2]-4*z[3]+z[4])#CEK PERSAMAAN
print("Cek Persamaan:")
print("④. 5𝑎+𝑏+3𝑐−4𝑑+𝑒=33 ")
print("5","(",z[0],")","+","(",z[1],")","+ 3","(",z[2],")","- 4","(",z[3],")","+","(",z[4],") =",persamaan4)
print("="*100)
print("⑤. 𝑎+𝑏−2𝑐+𝑑+3𝑒−𝑓=4")
print("   2𝑎−𝑏+𝑐+2𝑑+𝑒−3𝑓=20")
print("    𝑎+3𝑏−3𝑐−𝑑+2𝑒+𝑓=−15")
print("   5𝑎+2𝑏−𝑐−𝑑+2𝑒+𝑓=−3")
print("  −3𝑎−𝑏+2𝑐+3𝑑+𝑒+3𝑓=16")
print("   4𝑎+3𝑏+𝑐−6𝑑−3𝑒−2𝑓=−27")
v = EliminasiGauss(np.array([[1.0,1.0,-2.0,1.0,3.0,-1.0],
                             [2.0,-1.0,1.0,2.0,1.0,-3.0],
                             [1.0,3.0,-3.0,-1.0,2.0,1.0],
                             [5.0,2.0,-1.0,-1.0,2.0,1.0],
                             [-3.0,-1.0,2.0,3.0,1.0,3.0],
                             [4.0,3.0,1.0,-6.0,-3.0,-2.0]]),[4.0,20.0,-15.0,-3.0,16.0,-27.0])
print("a =",v[0])
print("b =",v[1])
print("c =",v[2])
print("d =",v[3])
print("e =",v[4])
print("f =",v[5])
persamaan5 =round(4*v[0]+3*v[1]+v[2]-6*v[3]-3*v[4]-2*v[5],1)#CEK PERSAMAAN
print("Cek Persamaan:")
print("⑤. 4𝑎+3𝑏+𝑐−6𝑑−3𝑒−2𝑓=−27")
print("4","(",v[0],")","+ 3","(",v[1],")","+","(",v[2],")","- 6","(",v[3],")","- 3","(",v[4],"- 2","(",v[5],") =",persamaan5)
print("="*100)