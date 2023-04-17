from listoffunction import *

import globalvars

def login():
    if globalvars.login_state:
        print(f'Anda telah login dengan username {globalvars.current_user}, silahkan lakukan "logout" sebelum melakukan login kembali.')
        return

    login_username = str(input("Username: "))
    login_password = str(input("Password: "))
    

    if isMember(globalvars.user, login_username, 0):
        if login_password == globalvars.user[get_index(globalvars.user, login_username, 1)][1]:
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
     
        
