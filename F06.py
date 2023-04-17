import globalvars
from listoffunction import *
import random

def bangun():
    if globalvars
    pasir_bangun = random.randint(1, 5)
    batu_bangun = random.randint(1, 5)
    air_bangun = random.randint(1, 5)
    if globalvars.bahan_bangunan[0][2] - pasir_bangun >= 0 and globalvars.bahan_bangunan[1][2] - batu_bangun >= 0 and globalvars.bahan_bangunan[2][2] - air_bangun >= 0 :

        if globalvars.candi[100] == "mark":
            print("Candi berhasil dibangun.")
            print("Sisa candi yang perlu dibangun : 0.")
        
        else:
            id_num = findMark(globalvars.candi)
            candi_terbangun = [id_num, globalvars.current_user, pasir_bangun, batu_bangun, air_bangun]
            appends(globalvars.candi, candi_terbangun)
            print(globalvars.candi)

        globalvars.bahan_bangunan[0][2] -= pasir_bangun
        globalvars.bahan_bangunan[1][2] -= batu_bangun
        globalvars.bahan_bangunan[2][2] -= air_bangun

        print(f"Sisa candi yang perlu dibangun: {99 - id_num}.")

    else:
        print()
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")
    