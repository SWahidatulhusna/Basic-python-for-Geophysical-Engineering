# Praktikum komputasi geofisika
# Nama: Sabda Wahdiatulhusna
# NIM: 12319030

a = 1
b = 5

if b < a:
     print ("b lebih kecil dari a")
elif b == a:
    print ("b sama dengan a")
else:
    print(" b lebih besar dari a")

a = 10
b = 15

if a % 5 == 0 and b %5 ==0:
    print ( "keduanya kelipatn 5")
elif  a%5 == 0 or b%5 == 0   :
    print ( "salah satunya kelipatan 5")
else:
    print (" keduanya bukan kelipatan 5")

i = 0


while i<10:
    if i == 4:
      continue
    print(i)
    i+= 1