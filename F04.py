import globalvars
from listoffunction import isMember, get_index, sortNone

def hilangkanjin():
    if globalvars.current_user != "Bondowoso":      # Cek apakah user adalah Bondowoso
        print("Anda tidak memiliki akses!\n")
        return

    hapus_jin = input("Masukkan username jin : ")   # Input username jin yang ingin dihapus

    if hapus_jin == "Bondowoso" or hapus_jin == "Roro":                 # Perlindungan pada Roro dan Bondowoso dari terhapus
        print("Entitas yang bukan merupakan jin tidak dapat dihapus!\n")
        return

    if isMember(globalvars.user, hapus_jin, 0):     # Cek apakah yang mau dihapus ada di dalam database
        verifikasi_hapus = input(f"Apakah anda yakin ingin menghapus jin dengan username {hapus_jin} (Y/N)? ")      # Verifikasi hapus
        print()

        if verifikasi_hapus == "Y":
            i = 0
            while globalvars.candi[i] != "\0" and i < 1002:
                if globalvars.candi[i][1] == hapus_jin:
                    globalvars.candi[i] = "__"                  # Menghapus setiap candi yang dibuat oleh jin yang terhapus
                i += 1

            globalvars.user[get_index(globalvars.user, hapus_jin, 0)] = None            # Menghapus jin
            sortNone(globalvars.user)       # Melakukan penyesuaian pada database dengan melakukan sort ulang

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