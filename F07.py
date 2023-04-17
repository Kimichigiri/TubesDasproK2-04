import random
import globalvars

def kumpul():
    pasir_kumpul = random.randint(0, 5)
    batu_kumpul = random.randint(0, 5)
    air_kumpul = random.randint(0, 5)

    globalvars.bahan_bangunan[0][2] += pasir_kumpul
    globalvars.bahan_bangunan[1][2] += batu_kumpul
    globalvars.bahan_bangunan[2][2] += air_kumpul



    print(f"Jin menemukan {pasir_kumpul} pasir, {batu_kumpul} batu, dan {air_kumpul} air.")