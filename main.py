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
from F08 import *
from F09 import *
from F10 import *
from F11 import *
from F12 import *
from F13 import *
from F14 import *
from F15 import *
from F16 import *

#F13 LOAD
if __name__ == '__main__':
    load()

# cek load_state true atau false, kalau benar baru jalanin loadmaterial
if (globalvars.load_state):
    loadmaterial(globalvars.bahan_bangunan)


while(globalvars.load_state):
    selector = str(input(">>> "))

    #F01 LOGIN
    if selector == "login":
        login()

    #F02 LOGOUT
    elif selector == "logout":
        logout()

    #F03 SUMMON JIN
    elif selector == "summonjin":
        summonjin()

    #F04 HILANGKAN JIN
    elif selector == "hapusjin":
        hilangkanjin()

    #F05 UBAH TIPE JIN
    elif selector == "ubahjin":
        ubahjin()

    #F06 JIN PEMBANGUN
    elif selector == "bangun":
        bangun()

    #F07 JIN PENGUMPUL
    elif selector == "kumpul":
        kumpul()

    #F08 BATCH KUMPUL/BANGUN
    elif selector == "batchkumpul":
        batchkumpul()
    elif selector == "batchbangun":
        batchbangun()
    
    #F09 AMBIL LAPORAN JIN
    elif selector == "laporanjin":
        laporanjin()
    
    #F10 AMBIL LAPORAN CANDI
    elif selector == "laporancandi":
        laporancandi()

    #F11 HANCURKAN CANDI
    elif selector == "hancurkancandi":
        hancurkancandi()
    
    #F12 AYAM BERKOKOK
    elif selector == "ayamberkokok":
        ayamberkokok()
        if globalvars.keluar:
            break
            # Keluar program

    #F14 SAVE
    elif selector == "save":
        save()

    #F15 HELP
    elif selector == "help":
        help()
    
    #F16 EXIT
    elif selector == "exit":
        keluar()
        break
        # Keluar program
    