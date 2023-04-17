import globalvars
import time
from listoffunction import *


def summonjin():
    if globalvars.current_user != "Bondowoso":
        print("Anda tidak memiliki akses!\n")
    elif globalvars.user[102] == "mark":
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")

    else:
        print("Jenis jin yang dapat dipanggil:")
        print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print(" (2) Pembagun - Bertugas membangun candi")
        print()

        while True:
            kode_jin = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
            print()
            if kode_jin == "1" or kode_jin == "2":
                break 
            else:
                print(f'Tidak ada jenis jin bernomor "{kode_jin}"!')
                print()

        if kode_jin == "1":
            print('Memilih jin "Pengumpul".')
            print()
        elif kode_jin == "2":
            print('Memilih jin "Pembangun".')
            print()


        nama_jin = str(input("Masukkan username Jin: "))
        print()


        while isMember(globalvars.user, nama_jin, 0):
            if nama_jin == "Bondowoso" or nama_jin == "Roro":
                print("Nama Bondowoso atau Roro tidak tersedia untuk dijadikan nama sebagai jin.")
            else:
                print(f'Username "{nama_jin}" sudah diambil!')
            print()
            nama_jin = str(input("Masukkan username Jin: "))

        password_jin = str(input("Masukkan password Jin: "))
        print()

        while len(password_jin) < 5 or len(password_jin) > 25:
            print('Password panjangnya harus 5-25 karakter!')
            print()
            password_jin = str(input("Masukkan password Jin: "))

        if kode_jin == "1":
            jin_baru = [nama_jin, password_jin, "jin_pengumpul"]
        elif kode_jin == "2":
            jin_baru = [nama_jin, password_jin, "jin_pembangun"]

        appends(globalvars.user, jin_baru)


        print()
        print("Mengumpulkan sesajen", end="")
        for i in range (3):
            time.sleep(0.3)
            print(".", end="")
        print()
        print("Menyerahkan sesajen", end="")
        for i in range (3):
            time.sleep(0.3)
            print(".", end="")
        print()
        print("Membacakan mantra", end="")
        for i in range (3):
            time.sleep(0.3)
            print(".", end="")
        time.sleep(0.3)
        print() ; print()
        print(f"Jin {nama_jin} berhasil dipanggil!")