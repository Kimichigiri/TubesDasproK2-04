import globalvars
from listoffunction import countBahan, countCandi, formatAngka, candiTermahal, candiTermurah

def laporancandi():

    if globalvars.current_user != "Bondowoso":      # Cek apakah user adalah Bondowoso
        print("Anda tidak memiliki akses!\n")
        return
        
    jumlah_candi = countCandi(globalvars.candi)         # Menghitung jumlah candi
    pasir_dipakai = countBahan(globalvars.candi, 2)     # Menghitung jumlah pasir dipakai
    batu_dipakai = countBahan(globalvars.candi, 3)      # Menghitung jumlah batu dipakai
    air_dipakai = countBahan(globalvars.candi, 4)       # Menghitung jumlah air dipakai

    # Output layar
    print()
    print(f"> Total Candi: {jumlah_candi}")
    print(f"> Total Pasir yang digunakan: {pasir_dipakai}")
    print(f"> Total Batu yang digunakan: {batu_dipakai}")
    print(f"> Total Air yang digunakan: {air_dipakai}")

    if jumlah_candi <= 0:       # Jika belum membuat candi sama sekali
        print("> ID Candi Termahal: -")
        print("> ID Candi Termurah: -")

    else:                       # Jika sudah ada candi
        print(f"> ID Candi Termahal : {candiTermahal(globalvars.candi)[0]} (Rp. {formatAngka(candiTermahal(globalvars.candi)[1])})")
        print(f"> ID Candi Termurah : {candiTermurah(globalvars.candi)[0]} (Rp. {formatAngka(candiTermurah(globalvars.candi)[1])})")