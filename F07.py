import random
import globalvars
from listoffunction import get_index

def kumpul():

    if globalvars.user[get_index(globalvars.user, globalvars.current_user, 0)][2] != "jin_pengumpul":   # Cek apakah user adalah bagian dari jin pengumpul
        print("Anda tidak memiliki akses!\n")
        return

    pasir_kumpul = random.randint(0, 5)     # Randomisasi bahan yang terkumpul
    batu_kumpul = random.randint(0, 5)
    air_kumpul = random.randint(0, 5)

    globalvars.bahan_bangunan[0][2] += pasir_kumpul     # Mengupdate database
    globalvars.bahan_bangunan[1][2] += batu_kumpul
    globalvars.bahan_bangunan[2][2] += air_kumpul



    print(f"Jin menemukan {pasir_kumpul} pasir, {batu_kumpul} batu, dan {air_kumpul} air.")     # Output layar