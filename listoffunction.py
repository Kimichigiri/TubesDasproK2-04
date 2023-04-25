

# Fungsi appends
# Menerima list dan element yang ingin dimasukkan kedalam array tersebut lalu mereturn list yang sudah termasuk dengan element baru
# KAMUS LOKAL
# i : Int
# l : Array of any
# element : bisa berupa int / str / float / list (Appends bisa digunakan untuk apapun)
def appends(l, element):
    for i in range (1002):
        if l[i] == "__":
            l[i] = element
            break
        elif l[i] == "\0":
            l[i] = element
            if i != 1001:
                l[i+1] = "\0"
            break
    return l


# Fungsi separate
# Menerima string dan Mengeluarkan array 
# I.S string yang terpisah dengan suatu separator (dalam konteks ini separator adalah ";")
# F.S Array yang terdiri atas string-string yang terpisahkan oleh ";"
# KAMUS LOKAL 
# line, element = Str
# i = Int
# arrayoutput = Array
def separate(line, arrayoutput=[None for i in range(1002)]):
    arrayoutput[0] = "\0" 
    line += ";"
    element = ""
    
    for i in range (len(line)):
        
        if line[i] == "\n" :
            element += ""

        elif line[i] != ";":
            element += line[i]

        else:
            appends(arrayoutput, element)
            element = ""
    return arrayoutput


# Fungsi isMember
def isMember(list, element, kode_list):

    # Mengecek apakah element merupakan anggota dari list

    # KAMUS LOKAL
    # list          : Array of Any                 - 
    # element       : Any                   -

    # Cek setiap elemen di list, kembalikan true jika sama dengan element
    i = 0
    while list[i] != "\0" and i < 1002:
        if list[i][kode_list] == element:
            return True
        i += 1
    
    # False jika tidak ditemukan
    return False


# Fungsi get_index
# Mencari index dari suatu kode element yang di-input oleh pengguna dalam suatu matriks (array of array)
# I.S suatu matriks
# F.S Integer yang merupakan indeks dari matriks yang memenuhi syarat
# KAMUS LOKAL
# list : Matrix of any
# element: Any
# i, kode_list : Integer
def get_index(list, element, kode_list):
    i = 0
    while list[i] != "\0":
        if list[i][kode_list] == element:
            return i
        i += 1
    return -1 # Jika tidak ditemukan indeks yang memenuhi syarat


# Fungsi sortNone
# Fungsi bertujuan untuk memindah seluruh element None yang ada sebelum mark menuju setelah mark
# I.S Sebuah Array
# F.S Sebuah Array dengan element None pindah ke setelah mark
# KAMUS LOKAL
# i, j : Integer
# list : Array of any
def sortNone (list):
    for i in range (1002):
        for j in range (1001-i):
            if list[j] == None:
                list[j], list[j+1] = list[j+1], list[j]
    return list


# Fungsi loadmaterial
# Fungsi merubah seluruh elemen jumlah pada bahan_bangunan.csv sebagai integer
# KAMUS LOKAL
# i : Integer
# matrix : matrix
def loadmaterial (matrix):
    for i in range (3):
        matrix[i][2] = int(matrix[i][2])


# Fungsi findMark
# Fungsi menerima suatu list dan akan mereturn Indeks dimana Mark berada
# KAMUS LOKAL
# i : Integer
# List : Array of any
def findMark (list):
    for i in range (1002):
        if list[i] == "\0" or list[i] == "__":
            return i

# Fungsi countJin
# Fungsi menerima list dan string tipe dari suatu jin dan mereturn suatu integer yang merupakan jumlah dari jin
# KAMUS LOKAL
# count, i  : Integer
# list      : Array of any
def countJin (list, tipe):
    count = 0 ; i = 0
    while list[i] != "\0":
        if list[i][2] == tipe:                      
            count += 1
        i += 1
    return count
    

# Fungsi sortLex
# Fungsi menerima array of string dan array of int (Tabel frekuensi dari array of jin) dan juga panjang dari array
# Konsep nya adalah bubble sort berdasarkan masing-masing dari element array of integer, namun jika ada yang sama dengan, akan disortir berdasarkan element pada array of string.
# Fungsi hanya mereturn array of string yang sudah tersortir
# KAMUS LOKAL
# i, j,, length : Integer
# strlist       : Array of string
# intlist       : Array of Integer
def sortLex (strlist, intlist, length):
    for i in range (length):
        for j in range (length - i - 1):
            if intlist[j] <= intlist[j+1]:
                intlist[j], intlist[j+1] = intlist[j+1], intlist[j]
                strlist[j], strlist[j+1] = strlist[j+1], strlist[j]
                if intlist[j] == intlist[j+1] and strlist[j] > strlist[j+1]:
                    strlist[j], strlist[j+1] = strlist[j+1], strlist[j]
    return strlist


# Fungsi countCandi
# Fungsi Menerima list candi
# Fungsi mereturn Integer jumlah candi
# Jika element adalah bukan Mark atau bukan Candi yang dihancurkan maka jumlah bertambah 1
# KAMUS LOKAL
# i, count  : Integer
# list      : Array of any
def countCandi (list):
    i = 0
    count = 0
    while list[i] != "\0":
        if list[i] != "__":
            count += 1
        i += 1
    return count


# Fungsi countBahan
# Fungsi menerima matrix bahan bangunan
# Fungsi lalu mereturn jumlah bangunan tergantung berdasarkan kodebahan yang diinput
# Pasir jika 0, Batu jika 1, Air, jika 2
# KAMUS LOKAL
# i, total, kodebahan   : Integer
# list                  : Array of any
def countBahan(list, kodebahan):
    i = 0
    total = 0
    while list[i] != "\0":
        if list[i] != "__":
            total += list[i][kodebahan]
        i += 1
    return total


# Fungsi candiTermahal
# Fungsi menerima matrix candi lalu fungsi mereturn candi yang memiliki harga termahal
# Berdasarkan jumlah pasir, batu, dan air yang dipakai
# KAMUS LOKAL
# i, termahal, idx  : Integer
# list              : Matrix candi
def candiTermahal(list):
    i = 0
    termahal = -9999
    idx = -1
    while list[i] != "\0":
        if list[i] != "__":
            if ((list[i][2] * 10000) + (list[i][3] * 15000) + (list[i][4] * 7500)) > termahal:
                termahal = ((list[i][2] * 10000) + (list[i][3] * 15000) + (list[i][4] * 7500))
                idx = i
        i += 1
    return [idx, termahal]


# Fungsi candiTermurah
# Fungsi menerima matrix candi lalu fungsi mereturn candi yang memiliki harga termurah
# Berdasarkan jumlah pasir, batu, dan air yang dipakai
# KAMUS LOKAL
# i, termurah, idx  : Integer
# list              : Matrix candi
def candiTermurah(list):
    i = 0
    termurah = 999999
    idx = -1
    while list[i] != "\0":
        if list[i] != "__":
            if ((list[i][2] * 10000) + (list[i][3] * 15000) + (list[i][4] * 7500)) < termurah:
                termurah = ((list[i][2] * 10000) + (list[i][3] * 15000) + (list[i][4] * 7500))
                idx = i
        i += 1
    return [idx, termurah]



# Fungsi formatAngka
# Fungsi menerima Integer yang merupakan angka
# Fungsi mereturn String dari angka yang sudah diformat dengan asumsi angka input tidak lebih dari 6 digit (Perhitungan candi tidak akan melebihi 6 digit)
# KAMUS LOKAL
# angka, output     : String
# i                 : Integer
def formatAngka (angka):
    angka = str(angka)
    output = ""
    for i in range (len(angka)):
        if i + 4 == len(angka):
            output += (angka[i] + ".")
        else:
            output += angka[i]

    return output


# Fungsi konso
# Fungsi menerima array of any dan element yang mau dimasukkan ke dalam array tersebut
# Fungsi mereturn array yang sudah terdapat element baru didalamnya
# Element baru akan bertukar tempat dengan Mark lalu Mark bergeser 1 ke kanan
# KAMUS LOKAL
# i         : Integer
# element   : Any
# list      : Array of any
def konso (list, element):
    for i in range (1002):
        if list[i] == "\0" and i < 1001:
            list[i] = element
            list[i+1] = "\0"    
            break


# Fungsi appendCandi
# Fungsi menerima matriks candi, string nama pembuat candi, pasir, batu, dan air yang digunakan
# Fungsi mereturn matriks candi dengan data baru sudah termasuk di dalamnya
# KAMUS LOKAL
# i, pasir, batu, air   : Integer
# pembuat               : String
# l                     : Matrix candi
def appendCandi (l, pembuat, pasir, batu, air):
    for i in range (1002):
        if l[i] == "__":
            l[i] = [i, pembuat, pasir, batu, air]
            break
        elif l[i] == "\0":
            l[i] = [i, pembuat, pasir, batu, air]
            if i != 1001:
                l[i+1] = "\0"
            break
    return l

