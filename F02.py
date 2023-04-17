from globalvars import login_state
import globalvars

def logout():
   
    if globalvars.login_state:
        print()
        globalvars.login_state = False
        globalvars.current_user = ""
    else:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
