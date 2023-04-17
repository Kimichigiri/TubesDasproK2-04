import globalvars
from listoffunction import *

def hilangkanjin():
    if globalvars.current_user != "Bondowoso":
        print("Anda tidak memiliki akses!\n")
        return

    hapus_jin = input("Masukkan username jin : ")

    if hapus_jin == "Bondowoso" or hapus_jin == "Roro":
        print("Entitas yang bukan merupakan jin tidak dapat dihapus!\n")
        return

    if isMember(globalvars.user, hapus_jin, 0):
        verifikasi_hapus = input(f"Apakah anda yakin ingin menghapus jin dengan username {hapus_jin} (Y/N)? ")
        print()

        if verifikasi_hapus == "Y":
            i = 0
            while globalvars.candi[i] != "mark" and i < 1002:
                if globalvars.candi[i][1] == hapus_jin:
                    globalvars.candi[i] = "kosoNg"
                i += 1

            globalvars.user[get_index(globalvars.user, hapus_jin, 0)] = None
            sortNone(globalvars.user)

            print("Jin telah berhasil dihapus dari alam gaib.")
            print()

        elif verifikasi_hapus == "N":
            print("Jin tidak jadi dihapus dari alam gaib.")
            print()

        else:
            print("Kode verifikasi hanya dalam bentuk Y atau N!")
            print()

    else:
        print("Tidak ada jin dengan username tersebut.")