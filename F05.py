import globalvars
from listoffunction import isMember, get_index

def ubahjin():

    if globalvars.current_user != "Bondowoso":     # Cek apakah user adalah Bondowoso
        print("Anda tidak memiliki akses!\n")
        return

    ubah_jin = input("Masukkan username jin : ")   # Input username jin yang role nya ingin diubah
    if isMember(globalvars.user, ubah_jin, 0):
        tipe_jin = globalvars.user[get_index(globalvars.user, ubah_jin, 0)][2]      # Cek tipe sekarang

        if tipe_jin == "jin_pembangun":
            invers_tipe_jin = "Pengumpul"
            teksubah = "Pembangun"
        elif tipe_jin == "jin_pengumpul":
            invers_tipe_jin = "Pembangun"
            teksubah = "Pengumpul"
        
        verif_ubah_jin = input(f'Jin ini bertipe "{teksubah}". Yakin ingin mengubah ke tipe "{invers_tipe_jin}" (Y/N)? ')       

        if invers_tipe_jin == "Pengumpul":
            invers_tipe_jin = "jin_pengumpul"
        elif invers_tipe_jin == "Pembangun":
            invers_tipe_jin = "jin_pembangun"

         # Verifikasi pengubahan tipe
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
