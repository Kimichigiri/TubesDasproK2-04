import globalvars
from listoffunction import countCandi

def ayamberkokok():

    if globalvars.current_user != "Roro":       # Mengecek apakah user adalah Roro      
        print("Anda tidak memiliki akses!\n")
        return
    
    jumlah_candi = countCandi(globalvars.candi)     # Menghitung jumlah candi
    print()
    print("Kukuruyuk.. Kukuruyuk..\n")
    print(f"Jumlah Candi: {jumlah_candi}\n")
    
    # Mengecek jumlah candi
    if jumlah_candi < 100:      # Jika candi yang dibangun kurang dari 100

        print("Selamat, Roro Jonggrang memenangkan permainan!\n")
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
        #Keluar program

        
    else:                       # Jika candi berhasil 100

        print("Yah, Bandung Bondowoso memenangkan permainan!")
    

    globalvars.keluar = True
    # Keluar program
    
    