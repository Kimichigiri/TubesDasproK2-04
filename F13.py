import argparse
import os
import globalvars
from listoffunction import appends, separate, konso

def loading(folder_name):
    # Cek apakah nama folder blank
    if not folder_name:
        print("Tidak ada nama folder yang diberikan!") ; print()
        print("Usage: python main.py <nama_folder>")
        return

    # Membuat path csv dari masing-masing file
    csv_path = "save/" + folder_name + "/user.csv"
    csv_path2 = "save/" + folder_name + "/candi.csv"
    csv_path3 = "save/" + folder_name + "/bahan_bangunan.csv"


    # Mengecek apakah path dari csv yang dimasukkan oleh user ada atau tidak
    if not os.path.exists(csv_path):
        print(f'Folder "{folder_name}" tidak ditemukan.')
        return

    # Melakukan pembacaan dari file csv lalu diubah menjadi array untuk file "user.csv"
    q = 0
    with open(csv_path, 'r') as f:
        for line in f:
            if q != 0:
                splitted_content = separate(line)   # Indeks 0 berisi username, Indeks 1 berisi password, Indeks 2 berisi role
                appends(globalvars.user, [splitted_content[0], splitted_content[1], splitted_content[2]]) 
            q += 1

    # Melakukan pembacaan dari file csv lalu diubah menjadi array untuk file "candi.csv"
    q = 0
    with open(csv_path2, 'r') as f:
        for line in f:
            if q != 0:
                splitted_content = separate(line)
                if q - int(splitted_content[0]) != 1:
                    while q - int(splitted_content[0]) != 1:
                        q += 1
                        konso(globalvars.candi, "__")       # Melakukan pembacaan spesial agar jika ada indeks yang terlewat, langsung dikonversi sebagai suatu kode di dalam array ("__")
                konso(globalvars.candi, [int(splitted_content[0]), splitted_content[1], int(splitted_content[2]), int(splitted_content[3]), int(splitted_content[4])])
                                            # id, pasir, batu, dan air langsung diubah menjadi integer.
                # Indeks 0 adalah id candi
                # Indeks 1 adalah nama pembuat candi
                # Indeks 2 adalah jumlah pasir yang digunakan untuk pembuatan candi tersebut
                # Indeks 3 adalah jumlah batu yang digunakan untuk pembuatan candi tersebut
                # Indeks 4 adalah jumlah air yang digunakan untuk pembuatan candi tersebut

            q += 1


    # Melakukan pembacaan dari file csv lalu diubah menjadi array untuk file "bahan_bangunan.csv"
    q = 0
    with open(csv_path3, 'r') as f:
        for line in f:
            if q != 0:
                splitted_content = separate(line)       # Indeks 0 adalah nama bahan, Indeks 1 adalah deskripsi bahan, Indeks 2 adalah jumlah bahan tersebut
                appends(globalvars.bahan_bangunan, [splitted_content[0], splitted_content[1], splitted_content[2]])
            q += 1
        # globalvars.bahan_bangunan[0][0] = Pasir yang dimiliki
        # globalvars.bahan_bangunan[0][1] = Batu yang dimiliki
        # globalvars.bahan_bangunan[0][2] = Air yang dimiliki


    print('Selamat datang di program "Managerial Candi"')
    print("Silahkan melakukan login")
    globalvars.load_state = True            # Load sudah dilakukan maka diganti menjadi True

def load():
    # Menentukan command
    print("Loading...")
    parser = argparse.ArgumentParser()
    parser.add_argument('folder_name', type=str, nargs='?', help='Name of the folder containing user.csv')
    args = parser.parse_args()

    # Melakukan parse pada command
    args, unknown = parser.parse_known_args()

    # Cek apakah folder yang tidak diberikan
    if args.folder_name is None:            # Jika tidak
        print("Tidak ada folder yang diberikan!") ; print()
        print("Usage: python main.py <nama_folder>")

    else:   # Jika folder aman
        # Call the main function with the specified folder name
        loading(args.folder_name)
   