#program Horoskop
# Spesifikasi: Program Horoskop Sendiri dengan Teman
# Versi      : 1.0
# Last Edited: 2020-09-18
# Programmer : Sabda Wahidatulhusna

#kamus
# nama STR
# nim INT
# tanggal lahir INT
# bulan lahir INT

print("Program Horoskop")
print("-"*100)
#algoritma
nama = str(input("Masukan Nama:"))#menginput nama
nim = int(input("Masukan NIM:"))#meninput nim
tanggallahir = int(input("Masukan Tanggal Lahir:"))#menginput tanggal lahir
bulanlahir = int(input("Masukan Bulan Lahir:"))#meninput bulan lahir
namateman = str(input("Masukan Nama Teman:"))
nimteman = int(input("Masukan NIM Teman:"))
tanggallahirteman = int(input("Masukan Tanggal Lahir Teman:"))
bulanlahirteman = int(input("Masukan Bulan Lahir teman:"))


print("==============================================================================================================")

print("Hallo", nama,", NIM kamu adalah", nim)
# if menyeleksi data input yang sesuai dengan syarat if kemudian jika sesuai akan di print
if bulanlahir==3 and 21<=tanggallahir<=31 or bulanlahir==4 and 1<=tanggallahir<=19:
    print("Zodiak Anda Adalah ARIES")
if bulanlahir==4 and 20<=tanggallahir<=31 or bulanlahir==5 and 1<=tanggallahir<=20:
    print("Zodiak Anda Adalah TAURUS")
if bulanlahir==5 and 21<=tanggallahir<=31 or bulanlahir==6 and 1<=tanggallahir<=20:
    print("Zodiak Anda Adalah GEMINI")
if bulanlahir==6 and 21<=tanggallahir<=31 or bulanlahir==7 and 1<=tanggallahir<=22:
    print("Zodiak Anda Adalah CENCER")
if bulanlahir==7 and 23<=tanggallahir<=31 or bulanlahir==8 and 1<=tanggallahir<=22:
    print("Zodiak Anda Adalah LEO")
if bulanlahir==8 and 23<=tanggallahir<=31 or bulanlahir==9 and  1<=tanggallahir<=22:
    print("Zodiak Anda Adalah VIRGO")
if bulanlahir==9 and 23<=tanggallahir<=31 or bulanlahir==10 and 1<=tanggallahir<=22:
    print("Zodiak Anda Adalah LIBRA")
if bulanlahir==10 and 23<=tanggallahir<=31 or bulanlahir==11 and 1<=tanggallahir<=21:
    print("Zodiak Anda Adalah SCORPIO")
if bulanlahir==11 and 22<=tanggallahir<=31 or bulanlahir==12 and 1<=tanggallahir<=21:
    print("Zodiak Anda Adalah SAGITARIUS")
if bulanlahir==12 and 22<=tanggallahir<=31 or bulanlahir==1 and 1<=tanggallahir<=19:
    print("Zodiak Anda Adalah CAPRICORN")
if bulanlahir==1 and 20<=tanggallahir<=31 or bulanlahir==2 and 1<=tanggallahir<=18:
    print("Zodiak Anda Adalah AQUARIUS")
if bulanlahir==2 and 19<=tanggallahir<=31 or bulanlahir==3 and 1<=tanggallahir<=20:
    print("Zodiak Anda Adalah PISCES")


print("===============================================================================================================")
print("Hallo", namateman, ", NIM kamu adalah", nimteman)
if bulanlahirteman==3 and 21<=tanggallahirteman<=31 or bulanlahirteman==4 and 1<=tanggallahirteman<=19:
    print("Zodiak teman Anda Adalah ARIES")
if bulanlahirteman==4 and 20<=tanggallahirteman<= 31 or bulanlahirteman==5 and 1<=tanggallahirteman<=20:
    print("Zodiak teman Anda Adalah TAURUS")
if bulanlahirteman==5 and 21<=tanggallahirteman<=31 or bulanlahirteman==6 and 1<=tanggallahirteman<=20:
    print("Zodiak teman Anda Adalah GEMINI")
if bulanlahirteman==6 and 21<=tanggallahirteman<=31 or bulanlahirteman==7 and 1<=tanggallahirteman<=22:
    print("Zodiak teman Anda Adalah CENCER")
if bulanlahirteman==7 and 23<=tanggallahirteman<=31 or bulanlahirteman==8 and 1<=tanggallahirteman<=22:
    print("Zodiak teman Anda Adalah LEO")
if bulanlahirteman==8 and 23<=tanggallahirteman<=31 or bulanlahirteman==9 and 1<=tanggallahirteman<=22:
    print("Zodiak teman Anda Adalah VIRGO")
if bulanlahirteman==9 and 23<=tanggallahirteman<=31 or bulanlahirteman==10 and 1<=tanggallahirteman<=22:
    print("Zodiak teman Anda Adalah LIBRA")
if bulanlahirteman==10 and 23<=tanggallahirteman<=31 or bulanlahirteman==11 and 1<=tanggallahirteman<=21:
    print("Zodiak teman Anda Adalah SCORPIO")
if bulanlahirteman==11 and 22<=tanggallahirteman<=31 or bulanlahirteman==12 and 1<=tanggallahirteman<=21:
    print("Zodiak teman Anda Adalah SAGITARIUS")
if bulanlahirteman==12 and 22<=tanggallahirteman<=31 or bulanlahirteman==1 and 1<=tanggallahirteman<=19:
    print("Zodiak teman Anda Adalah CAPRICORN")
if bulanlahirteman==1 and 20<=tanggallahirteman<=31 or bulanlahirteman==2 and 1<=tanggallahirteman<=18:
    print("Zodiak teman Anda Adalah AQUARIUS")
if bulanlahirteman==2 and 19<=tanggallahirteman<=31 or bulanlahirteman==3 and 1<=tanggallahirteman<=20:
    print("Zodiak teman Anda Adalah PISCES")
print("=======================================================================================================")