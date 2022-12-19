# Program penentu jarak
# Spesifikasi: Program menentukan jarak hiposenter gempa dengan letak kota
# Versi      : 1.4
# Last Edited: 2020-09-27
# Programmer : Sabda Wahidatulhusna

import numpy as np#mengimport numpy sebagai np
import math#mengimport math


#kamus
#hiposenter array
#bandung array

#Algoritma
hiposenter =np.random.uniform(-55,55,20).reshape(10,2).astype("int32")


Bandung= np.array([32,35])

def penentujarak(hiposenter,Bandung):
    x= hiposenter[0]- Bandung[0]
    j= hiposenter[1]- Bandung[1]
    jarak= math.sqrt(x**2+j**2)
    return round(jarak,3)


for i,j in enumerate(hiposenter):
    print("jarak hiposenterke",i+1,j,"ke bandung adalah", penentujarak(hiposenter[i],Bandung),"KM")