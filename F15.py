import globalvars
from listoffunction import get_index

def help ():

    print("=========== HELP ===========")

    if globalvars.login_state == False: # Pemain yang belum login       
        print("1. login")
        print("   Untuk masuk menggunakan akun")
        print("2. exit")
        print("   Untuk keluar dari program dan kembali ke terminal\n")

    else :                              # Pemain yang sudah login
       
        if globalvars.current_user == "Bondowoso" :     # Pemain yang login sebagai Bondowoso
            print("1. logout")
            print("   Untuk keluar dari akun yang digunakan sekarang")
            print("2. summonjin")
            print("   Untuk memanggil jin")
            print("3. hapusjin")
            print("   Untuk menghapus jin")
            print("4. ubahjin")
            print("   Untuk mengubah tipe jin")
            print("5. batchkumpul")
            print("   Untuk mengerahkan seluruh jin pengumpul untuk mengumpulkan bahan")
            print("6. batchbangun")
            print("   Untuk mengerahkan seluruh jin pembangun untuk membangun candi")
            print("7. laporanjin")
            print("   Untuk mengambil laporan jin untuk mengetahui kinerja dari para jin")
            print("8. laporancandi")
            print("   Untuk mengambil laporan candi untuk mengetahui progress pembangunan candi\n")
        
        elif globalvars.current_user == "Roro" :        # Pemain yang login sebagai Roro
            print("1. logout")
            print("   Untuk keluar dari akun yang digunakan sekarang")
            print("2. hancurkancandi")
            print("   Untuk menghancurkan candi yang tersedia")
            print("3. ayamberkokok")
            print("   Untuk menyelesaikan permainan dengan memalsukan pagi hari\n")

        elif globalvars.user[get_index(globalvars.user, globalvars.current_user, 0)][2] == "jin_pembangun" :        # Yang login sebagai jin pembangun
            print("1. logout")
            print("   Untuk keluar dari akun yang digunakan sekarang")
            print("2. bangun")
            print("   untuk mengumpulkan resource candi\n")

        elif globalvars.user[get_index(globalvars.user, globalvars.current_user, 0)][2] == "jin_pengumpul" :        # Yang login sebagai jin pengumpul
            print("1. logout")
            print("   Untuk keluar dari akun yang digunakan sekarang")
            print("2. kumpul")
            print("   Untuk membangun candi\n")