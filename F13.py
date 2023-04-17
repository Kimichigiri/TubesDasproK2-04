import argparse
import os
import globalvars
from listoffunction import *

def loading(folder_name):
    # Check if folder name is blank
    if not folder_name:
        print("Tidak ada nama folder yang diberikan!") ; print()
        print("Usage: python main.py <nama_folder>")
        return

    # Construct the path to the user.csv file in the specified folder
    csv_path = folder_name + "/user.csv"
    csv_path2 = folder_name + "/candi.csv"
    csv_path3 = folder_name + "/bahan_bangunan.csv"


    # Check if csv file can be found in the folder
    if not os.path.exists(csv_path):
        print(f'Folder "{folder_name}" tidak ditemukan.')
        return

    # Read the contents of the csv file
    q = 0
    with open(csv_path, 'r') as f:
        for line in f:
            if q != 0:
                splitted_content = separate(line)
                appends(globalvars.user, [splitted_content[0], splitted_content[1], splitted_content[2]])
            q += 1
    print(globalvars.user)

    q = 0
    with open(csv_path2, 'r') as f:
        for line in f:
            if q != 0:
                splitted_content = separate(line)
                appends(globalvars.candi, [splitted_content[0], splitted_content[1], splitted_content[2], splitted_content[3], splitted_content[4]])
            q += 1
    print(globalvars.candi)

    q = 0
    with open(csv_path3, 'r') as f:
        for line in f:
            if q != 0:
                splitted_content = separate(line)
                appends(globalvars.bahan_bangunan, [splitted_content[0], splitted_content[1], splitted_content[2]])
            q += 1
    print(globalvars.bahan_bangunan)

    print('Selamat datang di program "Managerial Candi"')
    print("Silahkan melakukan login")
    globalvars.load_state = True
def load():
    # Define the command-line argument
    print("Loading...")
    parser = argparse.ArgumentParser()
    parser.add_argument('folder_name', type=str, nargs='?', help='Name of the folder containing user.csv')
    args = parser.parse_args()

    # Parse the command-line arguments
    args, unknown = parser.parse_known_args()

    # Check if folder name argument is missing
    if args.folder_name is None:
        print("Tidak ada folder yang diberikan!") ; print()
        print("Usage: python main.py <nama_folder>")
    else:
        # Call the main function with the specified folder name
        loading(args.folder_name)
   