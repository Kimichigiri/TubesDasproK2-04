from listoffunction import isMember, get_index
import globalvars

def login():
    if globalvars.login_state:      # Cek kondisi apakah sudah login sebelumnya
        print(f'Anda telah login dengan username {globalvars.current_user}, silahkan lakukan "logout" sebelum melakukan login kembali.')
        return

    login_username = str(input("Username: "))   # Input informasi login
    login_password = str(input("Password: "))
    

    if isMember(globalvars.user, login_username, 0):    # Cek apakah username terdaftar
        if login_password == globalvars.user[get_index(globalvars.user, login_username, 0)][1]:     # Cek apakah password dan username cocok
            print()
            print(f"Selamat datang, {login_username}!")
            print('Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
            globalvars.login_state = True
            globalvars.current_user = login_username
            

        else:
            print()
            print("Password salah!")
        

    else:
        print()
        print("Username tidak terdaftar!")
     
        
