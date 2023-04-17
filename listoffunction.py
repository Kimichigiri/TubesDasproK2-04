


def appends(l, element):
    for i in range (1002):
        if l[i] == "kosoNg":
            l[i] = element
        elif l[i] == "mark":
            l[i] = element
            if i != 1001:
                l[i+1] = "mark"
            break
    return l

def separate(line, arrayoutput=[None for i in range(1002)]):
    arrayoutput[0] = "mark" 
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


def is_empty(list):

    if list == []:
        return True
    else:
        return False


def isMember(list, element, kode_list):

    # Mengecek apakah element merupakan anggota dari list

    # KAMUS LOKAL
    # list          : list                  - 
    # element       : any                   -

    # Cek setiap elemen di list, kembalikan true jika sama dengan element
    i = 0
    while list[i] != "mark" and i < 1002:
        if list[i][kode_list] == element:
            return True
        i += 1
    
    # Output - hanya terjadi apabila tidak ada elemen di list yang sama dengan element
    return False


def get_index(list, element, kode_list):
    i = 0
    while list[i] != "mark":
        if list[i][kode_list] == element:
            return i
        i += 1
    return 0

def sortNone (list):
    for i in range (1002):
        for j in range (1001-i):
            if list[j] == None:
                list[j], list[j+1] = list[j+1], list[j]
    return list

def loadmaterial (matrix):
    for i in range (3):
        matrix[i][2] = int(matrix[i][2])

def findMark (list):
    for i in range (1002):
        if list[i] == "mark" or list[]:
            return i
    