import os
import sys
import time 
import argparse
import datetime

from listoffunction import *
from F01 import *
from F02 import *
from F03 import *
from F04 import *
from F05 import *
from F06 import *
from F07 import *
from F13 import *

if __name__ == '__main__':
    load()
loadmaterial(globalvars.bahan_bangunan)


while(globalvars.load_state):
    selector = str(input(">>> "))
    if selector == "exit":
        warning_exit = input("Apakah anda mau melakukan penyimpanan file yuang sudah diubah (y/n?) ")
        if warning_exit == "y":
            save()
        elif warning_exit == "n":
            break
    else:
        if selector == "login":
            login()
        elif selector == "logout":
            logout()
        elif selector == "summonjin":
            summonjin()
        elif selector == "hapusjin":
            hilangkanjin()
        elif selector == "ubahjin":
            ubahjin()
        elif selector == "bangun":
            bangun()
        elif selector == "kumpul":
            kumpul()