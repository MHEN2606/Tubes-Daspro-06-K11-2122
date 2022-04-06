def searchGameAtStore():
    idGame = input("Masukkan ID Game ")
    namaGame = input("Masukkan Nama game ")
    hargaGame = input("Masukkan Harga Game ")
    kategori = input("Masukkan Kategori Game ")
    tahun = input("Masukkan Tahun Rilis Game ")
    print("")
    #buka database game.csv
    game = []
    temp = ""
    cc = []
    with open('./database/game.csv','r') as games:
        for row in games:
            for char in row:
                if char != ";" and char != "\n":
                        temp += char
                else: #char == ";"
                    cc += [temp]
                    temp = ""
            
            game += [cc]
            cc = []
    games.close()

    #count row dalam game.csv
    count_row = 0
    for row in game:
        count_row += 1
    urut = 1
    true = 0
    if idGame == "" and namaGame == "" and hargaGame =="" and kategori =="" and tahun =="": #keluarkan semua game jika paramater tidak diisi
        for i in range(1,count_row):
            #if idGame == "" and namaGame == "" and hargaGame =="" and kategori == "" and tahun =="":
            # ID | NAMA  | Harga | Kategori | Tahun rilis | stok
            print(f"{urut}. {game[i][0]} | {game[i][1]} | {game[i][2]} | {game[i][3]} | {game[i][4]} | {game[i][5]}")
            urut += 1
            true += 1
    else:
        for i in range(1,count_row):
            if idGame == game[i][0] or namaGame == game[i][1] or hargaGame == game[i][4] or kategori == game[i][2] or tahun == game[i][5]:
                # ID | NAMA  | Harga | Kategori | Tahun rilis | stok
                print(f"{urut}. {game[i][0]} | {game[i][1]} | {game[i][2]} | {game[i][3]} | {game[i][4]} | {game[i][5]}")
                urut += 1
                true += 1
    
    if true <= 0:
        print("Tidak ada data game yang ditemukan")


#TES
#search_game_at_store()