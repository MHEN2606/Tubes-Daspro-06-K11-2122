def topup(user):
    found = False
    valid_pos = False
    valid_neg = False
    count = 0
    for row in user:
        count += 1
    count -= 1

    us = input("Masukkan username: ")
    saldo = int(input("Masukkan saldo: "))
    for i in range(1,count+1):
        if user[i][1] == us:
            found = True
            if saldo>0 or saldo+int(user[i][5])>=0:
                saldo_akhir = int(user[i][5])
                saldo_akhir += saldo
                user[i][5] = str(saldo_akhir)
                if saldo>0 :
                    valid_pos = True
                else:
                    valid_neg = True
                break
            else:
                valid_neg = False
                valid_pos = False
    if found==False and valid_pos == False and valid_neg==False:
        print('Username "'+us+ '" tidak ditemukan.')
    elif found and valid_pos:
        print("Top up berhasil. Saldo "+us+ " bertambah menjadi "+str(saldo_akhir))
    elif found and valid_neg:
        print("Top up berhasil. Saldo "+us+" berkurang menjadi " + str(saldo_akhir))
    else:
        print("Masukan tidak valid")
    return
