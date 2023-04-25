import globalvars
from listoffunction import countJin, appends, findMark, appendCandi, countCandi
import random       

def batchkumpul ():
    if globalvars.current_user != "Bondowoso":      # Cek apakah user adalah Bondowoso
        print("Anda tidak memiliki akses!\n")       
        return

    jumlah_jin = countJin(globalvars.user, "jin_pengumpul")     # Menghitung jumlah jin

    if jumlah_jin <= 0:     # Jika Bondowoso belum memiliki jin
        print("Kumpul gagal. Anda tidak punya Jin pengumpul. Silahkan summon terlebih dahulu.")
        return

    print(f"mengerahkan {jumlah_jin} jin untuk mengumpulkan bahan.")

    pasir_total = 0     # Inisialisasi total bahan yang akan diperlukan
    batu_total = 0
    air_total = 0

    for i in range (jumlah_jin):        # Loop traversal untuk mengetahui jumlah bahan yang akan didapatkan
        pasir_kumpul = random.randint(0, 5)
        batu_kumpul = random.randint(0, 5)
        air_kumpul = random.randint(0, 5)

        globalvars.bahan_bangunan[0][2] += pasir_kumpul
        globalvars.bahan_bangunan[1][2] += batu_kumpul
        globalvars.bahan_bangunan[2][2] += air_kumpul

        pasir_total += pasir_kumpul
        batu_total += batu_kumpul
        air_total += air_kumpul
    
    print(f"Jin menemukan total {pasir_total} pasir, {batu_total} batu, dan {air_total} air.")     # Output layar


def batchbangun():
    if globalvars.current_user != "Bondowoso":      # Cek apakah user adalah Bondowoso
        print("Anda tidak memiliki akses!\n")
        return

    jumlah_jin = countJin(globalvars.user, "jin_pembangun")     # Hitung jumlah jin

    if jumlah_jin <= 0:     # Jika Bondowoso belum memiliki jin
        print("Bangun gagal. Anda tidak punya Jin pembangun. Silahkan summon terlebih dahulu.\n")
        return

    pasir_total = 0     # Inisialisasi  total bahan yang akan diperlukan
    batu_total = 0
    air_total = 0

    arrayjin = [None for i in range (100)] ; arrayjin[0] = "\0"         # Inisialisasi Jin mana saya yang akan membangun
    caloncandi = [None for i in range (100)] ; caloncandi[0] = "\0"     # Inisialisasi data Candi yang akan terbangun

    i = 0           # Inisialisasi i = 0 untuk akses array

    while globalvars.user[i] != "\0":   # Mencatat seluruh jin_pembangun yang ada ke dalam array baru
        if globalvars.user[i][2] == "jin_pembangun":
            appends(arrayjin, globalvars.user[i][0])
        i += 1

    i = 0   # i kembali 0
    
    jumlah_candi = countCandi(globalvars.candi)  # Hitung jumlah candi saat ini

    while arrayjin[i] != "\0":              # Melakukan randomisasi sebanyak jumlah jin pembangun
        pasir_bangun = random.randint(1, 5)
        batu_bangun = random.randint(1, 5)
        air_bangun = random.randint(1, 5)

        pasir_total += pasir_bangun
        batu_total += batu_bangun
        air_total += air_bangun

        appends(caloncandi, [arrayjin[i], pasir_bangun, batu_bangun, air_bangun])   # Menambah ke database candi yang akan dibangun

        i += 1  # Increment
   
    sisa_candi = jumlah_jin


    if jumlah_candi + jumlah_jin > 100:
        sisa_candi = 100 - jumlah_candi     # Memastikan candi tidak akan terbangun lebih dari 100 tetapi bahan tetap digunakan jika ada kelebihan

    print(f"Mengerahkan {jumlah_jin} jin untuk membangun candi dengan total bahan {pasir_total} pasir, {batu_total} batu, dan {air_total} air.")

    if globalvars.bahan_bangunan[0][2] - pasir_total >= 0 and globalvars.bahan_bangunan[1][2] - batu_total >= 0 and globalvars.bahan_bangunan[2][2] - air_total >= 0 :
        print(f"Jin berhasil membangun total {sisa_candi} candi.")      # Jika bahan cukup

        for i in range (sisa_candi):
            appendCandi(globalvars.candi, caloncandi[i][0], caloncandi[i][1], caloncandi[i][2], caloncandi[i][3])
        

        globalvars.bahan_bangunan[0][2] -= pasir_total
        globalvars.bahan_bangunan[1][2] -= batu_total
        globalvars.bahan_bangunan[2][2] -= air_total

    else:       # Jika bahan tidak mencukupi
        kurang_pasir = pasir_total - globalvars.bahan_bangunan[0][2]
        kurang_batu = batu_total - globalvars.bahan_bangunan[1][2]
        kurang_air = air_total - globalvars.bahan_bangunan[2][2]
        if kurang_pasir < 0:
            kurang_pasir = 0
        if kurang_batu < 0:
            kurang_batu = 0
        if kurang_air < 0:
            kurang_air = 0
        print(f"Bangun gagal. Kurang {kurang_pasir} pasir, {kurang_batu} batu, dan {kurang_air} air.")
        print()