def help(role): #parameter berupa role dari user yang sedang login
    print("====== HELP MENU ======")
    if role == "admin": #menu yang ditampilkan jika rolenya adalah admin
        print("1. register - menu untuk melakukan registrasi user baru")
        print("2. tambah_game - menu untuk menambah game")
        print("3. ubah_game - Untuk mengubah data game")
        print("4. ubah_stok - Untuk mengubah stok game")
        print("5. list_game_toko - Untuk melihat list game yang dijual pada toko")
        print("6. search_game_at_store - untuk mencari game di toko")
        print("7. topup - untuk melakukan top up saldo pada user")
        print("8. help - untuk melihat perintah yang ada")
        print("10. exit - untuk exit dari program")
        print("11. save - untuk menyimpan data sebagai csv file")
        print("12. kerangajaib - untuk menanyakan sesuatu (seperti magic-8-ball)")
        print("13. tictactoe - bermain tic-tac-toe")
    else: #role user. masukan pasti benar karena diambil dari data user.csv. menu yang ditampilkan jika rolenya adalah user
        print("1. list_game_toko - Untuk melihat list game yang dijual pada toko")
        print("2. buy_game - untuk membeli game")
        print("3. list_game - untuk melihat list game yang dimiliki user")
        print("4. search_my_game - untuk mencari game yang dimiliki user")
        print("5. search_game_at_store - untuk mencari game di toko")
        print("6. riwayat - untuk melihat riwayat pembelian game")
        print("7. help - untuk melihat perintah yang ada")
        print("8. exit - untuk exit dari program")
        print("9. save - untuk menyimpan data sebagai csv file")
        print("10. kerangajaib - untuk menanyakan sesuatu (seperti magic-8-ball)")
        print("11. tictactoe - bermain tic-tac-toe")

    return
#tes
#help("admin")