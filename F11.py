import globalvars

def hancurkancandi():

    if globalvars.current_user != "Roro":       # Cek apakah user adalah Roro
        print("Anda tidak memiliki akses!\n")
        return

    id_hancur = int(input("Masukkan ID Candi: "))   # Meminta pengguna untuk memasukkan ID candi yang ingin dihancurkan

    # Mengecek apakah ada candi ddengan ID tersebut
    if globalvars.candi[id_hancur] != "\0" and globalvars.candi[id_hancur] != "__" and globalvars.candi[id_hancur] != None:     # Jika terdapat candi dengan ID tersebut
        verif_hapus_candi = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id_hancur} (Y/N)? ")   
        
        if verif_hapus_candi == "Y" or verif_hapus_candi == "y":

            globalvars.candi[id_hancur] = "__"
            print("Candi telah berhasil dihancurkan.")

        elif verif_hapus_candi == "N" or verif_hapus_candi == "n":
            print("Candi tidak jadi dihapus.\n")

        else:
            print('Hanya menerima dalam bentuk "Y" atau "N"! Silahkan ulangi prosedur hancurkan candi!')


    else:       # Jika tidak terdapat
        print()
        print("Tidak ada candi dengan ID tersebut.")