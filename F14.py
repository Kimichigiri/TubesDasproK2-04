import globalvars
import os


def save():

    print()
    nama_folder = input("Masukkan nama folder: ")   # Input nama folder
    print()
    
    csvpath = "save/" + nama_folder                 # Inisialisasi path
    csvpath1 = csvpath + "/user.csv"
    csvpath2 = csvpath + "/bahan_bangunan.csv"
    csvpath3 = csvpath + "/candi.csv"

    save_exist = True               # Inisialisasi boolean apakah folder save ada
    folder_exist = True             # Inisialisasi boolean apakah folder input ada didalam save

    if not os.path.exists("save"):      # Cek apakah folder save ada
        os.mkdir("save")    # Jika tidak akan dibuatkan
        save_exist = False

    if not os.path.exists(csvpath):     # Cek apakah folder yang dimasukkan user ada
        folder_exist = False
        os.makedirs(csvpath)        # Jika tidak akan dibuatkan


    # Proses writing "user.csv"
    with open(csvpath1, 'w') as f:
        i = 0
        f.write("username;password;role\n")
        while globalvars.user[i] != "\0":
            f.write(globalvars.user[i][0]+";"+globalvars.user[i][1]+";"+globalvars.user[i][2]+"\n")
            i += 1
    
    # Proses writing "bahan_bangunan.csv"
    with open(csvpath2, 'w') as f:
        f.write("nama;deskripsi;jumlah\n")
        for i in range (3):                                                                 # Merubah integer ke string untuk ditulis ke dalam csv
            f.write(globalvars.bahan_bangunan[i][0]+";"+globalvars.bahan_bangunan[i][1]+";"+str(globalvars.bahan_bangunan[i][2])+"\n")

    # Proses writing "candi.csv"
    with open(csvpath3, 'w') as f:
        i = 0
        f.write("id;pembuat;pasir;batu;air\n")
        while globalvars.candi[i] != "\0":
            if globalvars.candi[i] != "__":     # Candi yang dihancurkan tidak ikut ditulis ke csv
                f.write(str(globalvars.candi[i][0])+";"+globalvars.candi[i][1]+";"+str(globalvars.candi[i][2])+";"+str(globalvars.candi[i][3])+";"+str(globalvars.candi[i][4])+"\n")
            i += 1
                                                                # Jangan lupa yang berupa integer diubah dulu ke string


    # Output layar
    print("Saving...\n")
    print()
    if not save_exist:
        print("Membuat folder save...")
    if not folder_exist:
        print(f"Membuat folder save/{nama_folder}...")
    print()
    print(f"Berhasil menyimpan data di folder {csvpath}!")
    

    
        
