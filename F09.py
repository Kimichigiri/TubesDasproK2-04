import globalvars
from listoffunction import appends, countJin, sortLex, findMark

def laporanjin():

    if globalvars.current_user != "Bondowoso":      # Cek apakah user adalah Bondowoso
            print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.\n")
            return

    arrayjin = [None for i in range (100)] ; arrayjin[0] = "\0"             # Inisialisasi array jin baru
    candi_dibuat = [None for i in range (100)] ; candi_dibuat[0] = "\0"     # Inisialisasi array penampung jumlah candi yang dibuat oleh jin
    i = 0

    while globalvars.user[i] != "\0":               # Menyalin data jin pembangun dari data asli
        if globalvars.user[i][2] == "jin_pembangun":    
            appends(arrayjin, globalvars.user[i][0])
        i += 1
    i = 0   # i kembali 0

    jumlah_jin = countJin(globalvars.user, "jin_pembangun")     # Menghitung jumlah jin
    for h in range (jumlah_jin):                # Menghitung frekuensi candi yang dibuat oleh jin tertentu secara traversal
        count_candi = 0
        while globalvars.candi[i] != "\0":         # O(N^2)
            if globalvars.candi[i][1] == arrayjin[h]:
                count_candi += 1                                        
            
            i += 1
        appends(candi_dibuat, count_candi)  


    sortLex(arrayjin, candi_dibuat, jumlah_jin)     # Sort secara leksikografis

    
    print()
    print(f"> Total Jin: {findMark(globalvars.user) - 2}")                          # Total jumlah jin
    print(f"> Total Jin Pengumpul: {countJin(globalvars.user, 'jin_pengumpul')}")   # Total jin pengumpul
    print(f"> Total Jin Pembangun: {countJin(globalvars.user, 'jin_pembangun')}")   # Total jin pembangun

    if jumlah_jin <= 0:             # Jika belum memiliki jin
        print(f"> Jin Terajin: -")
        print(f"> Jin Termalas: -")

    else:                           # Jika sudah memiliki jin
        print(f"> Jin Terajin: {arrayjin[0]}")
        print(f"> Jin Termalas: {arrayjin[jumlah_jin - 1]}")
    print(f"> Jumlah Pasir: {globalvars.bahan_bangunan[0][2]} unit")
    print(f"> Jumlah Air: {globalvars.bahan_bangunan[2][2]} unit")
    print(f"> Jumlah Batu: {globalvars.bahan_bangunan[1][2]} unit")
    print()