import globalvars
from listoffunction import get_index, findMark, appends, countCandi
import random

def bangun():

    if globalvars.user[get_index(globalvars.user, globalvars.current_user, 0)][2] != "jin_pembangun":   # Cek apakah user adalah bagian dari jin pembangun
        print("Anda tidak memiliki akses!\n")
        return

    pasir_bangun = random.randint(1, 5)     # Melakukan random penggunaan barang
    batu_bangun = random.randint(1, 5)
    air_bangun = random.randint(1, 5)
    if globalvars.bahan_bangunan[0][2] - pasir_bangun >= 0 and globalvars.bahan_bangunan[1][2] - batu_bangun >= 0 and globalvars.bahan_bangunan[2][2] - air_bangun >= 0 :

        if globalvars.candi[100] == "\0":           # Cek apakah candi sudah 100 atau belum
            print("Candi berhasil dibangun.")
            print("Sisa candi yang perlu dibangun : 0.")
        
        else:       # Candi belum 100
            id_num = findMark(globalvars.candi)
            candi_terbangun = [id_num, globalvars.current_user, pasir_bangun, batu_bangun, air_bangun]  # Array yang akan di tambah ke database
            appends(globalvars.candi, candi_terbangun)      # Menambah database candi dengan candi baru
            jumlah_candi = countCandi(globalvars.candi)

            print("Candi berhasil dibangun")
            print(f"Sisa candi yang perlu dibangun: {100 - jumlah_candi}.\n")    # Output sisa candi yang perlu dibangun

        globalvars.bahan_bangunan[0][2] -= pasir_bangun     # Penggunaan bahan
        globalvars.bahan_bangunan[1][2] -= batu_bangun
        globalvars.bahan_bangunan[2][2] -= air_bangun

    else:
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")
    