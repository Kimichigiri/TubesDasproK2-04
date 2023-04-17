import globalvars
from listoffunction import *

def ubahjin():
    ubah_jin = input("Masukkan username jin : ")
    if isMember(globalvars.user, ubah_jin, 0):
        tipe_jin = globalvars.user[get_index(globalvars.user, ubah_jin, 0)][2]
        
        print(tipe_jin)

        if tipe_jin == "jin_pembangun":
            invers_tipe_jin = "Pengumpul"
            teksubah = "Pembangun"
        elif tipe_jin == "jin_pengumpul":
            invers_tipe_jin = "Pembangun"
            teksubah = "Pengumpul"
        
        print(f'Jin ini bertipe "{teksubah}". Yakin ingin mengubah ke tipe "{invers_tipe_jin}" ', end="")
        verif_ubah_jin = input("(Y/N)? ")

        if invers_tipe_jin == "Pengumpul":
            invers_tipe_jin = "jin_pengumpul"
        elif invers_tipe_jin == "Pembangun":
            invers_tipe_jin = "jin_pembangun"

        if verif_ubah_jin == "Y":
            globalvars.user[get_index(globalvars.user, ubah_jin, 0)][2] = invers_tipe_jin
            
            print()
            print("Jin telah berhasil diubah.")
         

        elif verif_ubah_jin == "N":
            print("Jin tidak jadi diubah\n")
        else:
            print('Format hanya dalam "Y" dan "N"!\n')


    else:
        print()
        print("Tidak ada jin dengan username tersebut.")
