import os

def save(user, game_list, ownership, history):
    state = False #state apakah nama folder sudah ada atau belum ada
    parent_dir = './save/' #folder penyimpanan untuk prosedur save
    folder = input("Masukkan nama folder penyimpanan: ")

    valid_input = False
    
    while valid_input == False:
        if folder == "": #handling untuk input nama folder kosong
            print("Input nama folder tidak boleh kosong!")
            folder = input("Masukkan nama folder penyimpanan: ")
            valid_input == False
        elif "/" in folder or "?" in folder or ":" in folder or "<" in folder or ">" in folder or "|" in folder: #handling untuk karakter terlarang
            print("Input nama folder tidak boleh mengandung karakter '/' '?' ':' '<' '>' '|'!")
            folder = input("Masukkan nama folder penyimpanan: ")
            valid_input == False
        else:
            valid_input = True
    
    state = folder_exist(folder, parent_dir)
    
    print()
    print("Saving ...")
    if state: #jika nama foldernya ada
        #overwrite/buat semua file yang ada di sana
        #save user.csv
        save_file(user, "user", parent_dir, folder)

        #save game.csv
        save_file(game_list, "game", parent_dir, folder)

        #save kepemilikan.csv
        save_file(ownership, "kepemilikan", parent_dir, folder)

        #save riwayat.csv
        save_file(history, "riwayat", parent_dir, folder)
        
    else: #jika nama folder tidak ada
        #buat folder nya
        os.mkdir(f'{parent_dir}/{folder}')
        #save user.csv
        save_file(user, "user", parent_dir, folder)

        #save game.csv
        save_file(game_list, "game", parent_dir, folder)

        #save kepemilikan.csv
        save_file(ownership, "kepemilikan", parent_dir, folder)

        #save riwayat.csv
        save_file(history, "riwayat", parent_dir, folder)

    #kalau sudah selesai melakukan save
    print("Data telah disimpan pada folder {}".format(folder))
    return

def save_file(data, jenis, parent_dir, folder):
    #prosedur untuk menyimpan data
    #count columns:
    count_col = 0
    for row in data:
        for col in row:
            count_col += 1
        break
    
    #count rows:
    count_row = 0
    for row in data:
        count_row += 1
    
    #insert data
    with open(f'{parent_dir}/{folder}/{jenis}.csv', 'w') as save_file:
        for i in range(count_row):
            for j in range(count_col):
                if j < (count_col-1):
                    save_file.write(f"{data[i][j]};")
                else:
                    save_file.write(f"{data[i][j]}\n")
    save_file.close()

    return

def folder_exist(folder, parent_dir):
    for (root, files, dirs) in os.walk(f'{parent_dir}'):
        if folder in root: #jika nama folder ada dalam parameter root
            state = True
            break
        else: #jika nama folder tidak ada dalam parameter root
            state = False
    return state