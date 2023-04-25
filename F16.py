from F14 import *           # Inisialisasi prosedur save

def keluar() :

    opsi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")    # Inisialisasi input

    while True:         # Validasi input

        if opsi == "N" or opsi == "n" :     # Jika tidak mau save, langsung exit
            print()
            print("Sampai berjumpa lagi.")
            break
            
        elif opsi == "Y" or opsi == "y" :   # Jika mau save, jalankan prosedur save
            save()
            break
        
        opsi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")