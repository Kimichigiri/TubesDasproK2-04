import globalvars
import time
from listoffunction import isMember, appends


def summonjin():
    if globalvars.current_user != "Bondowoso":      # Cek apakah user adalah Bondowoso
        print("Anda tidak memiliki akses!\n")

    elif globalvars.user[102] == "\0":              # Cek jumlah jin
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")

    else:
        print("Jenis jin yang dapat dipanggil:")
        print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print(" (2) Pembangun - Bertugas membangun candi")
        print()

        while True:
            kode_jin = input("Masukkan nomor jenis jin yang ingin dipanggil: ")         # Pemilihan nomor jenis jin
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


        nama_jin = str(input("Masukkan username Jin: "))    # Input username jin
        print()


        while isMember(globalvars.user, nama_jin, 0):           # Cek apakah username sudah terdaftar
            if nama_jin == "Bondowoso" or nama_jin == "Roro":
                print("Nama Bondowoso atau Roro tidak tersedia untuk dijadikan nama sebagai jin.")
            else:
                print(f'Username "{nama_jin}" sudah diambil!')
            print()
            nama_jin = str(input("Masukkan username Jin: "))

        password_jin = str(input("Masukkan password Jin: "))       # Input password jin
        print()

        while len(password_jin) < 5 or len(password_jin) > 25:      # Validasi passwod (karakter panjangnya 5-25)
            print('Password panjangnya harus 5-25 karakter!')
            print()
            password_jin = str(input("Masukkan password Jin: "))

        if kode_jin == "1":
            jin_baru = [nama_jin, password_jin, "jin_pengumpul"]
        elif kode_jin == "2":
            jin_baru = [nama_jin, password_jin, "jin_pembangun"]

        appends(globalvars.user, jin_baru)      # Menambah data jin baru ke database


        # Loading Screen
        
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