username_benar = "ilyas"
password_benar = "049"
pulau_1 = "kalimantan"
pulau_2 = "sumatera"
lahan_1 = "gambut"
lahan_2 = "mineral"
total_kalimantan_gambut = 0
total_kalimantan_mineral = 0
total_sumatera_gambut = 0
total_sumatera_mineral = 0

print("================================================================================")
print("       PROGRAM REKAPITULASI SEBARAN TITIK API KEBAKARAN HUTAN DAN LAHAN")
print("================================================================================")
print("FORM LOGIN")
print()

while True:
    username = input("Masukkan username anda: ").lower()
    password = input("Masukkan password anda: ")

    if username == "" or password == "":
        print("Username dan password tidak boleh kosong!")
        print()
    elif username == username_benar and password == password_benar:
        print("Login berhasil!")
        print()
        break
    elif username != username_benar and password == password_benar:
        print("Username anda salah, silakan cek kembali.")
        print()
    elif username == username_benar and password != password_benar:
        print("Password anda salah, silakan cek kembali.")
        print()
    else:
        print("Username dan password anda salah!")
        print()

while True:
    print("--------------------------------------------------------------------------------")
    print("INPUT DATA TITIK API")
    print("--------------------------------------------------------------------------------")
    pilih_pulau = input("Masukkan nama pulau (Kalimantan/Sumatera): ").lower()
    if pilih_pulau == "":
        print("Nama pulau tidak boleh kosong!")
        continue
    if pilih_pulau == pulau_1:
        jenis = input("Masukkan jenis lahan (Gambut/Mineral): ").lower()
        if jenis == "":
            print("Jenis lahan tidak boleh kosong!")
            continue
        if jenis == lahan_1:
            print(f"Anda memilih {pilih_pulau}-{jenis}")
            titik_api = input("Masukkan jumlah titik api: ")
            if titik_api == "":
                print("Jumlah titik api tidak boleh kosong!")
                continue
            titik_api = int(titik_api)
            luas_terbakar = titik_api * 5
            total_kalimantan_gambut += luas_terbakar
            print(f"Luas lahan terbakar: {luas_terbakar} hektare")

        elif jenis == lahan_2:
            print(f"Anda memilih {pilih_pulau}-{jenis}")
            titik_api = input("Masukkan jumlah titik api: ")
            if titik_api == "":
                print("Jumlah titik api tidak boleh kosong!")
                continue
            titik_api = int(titik_api)
            luas_terbakar = titik_api * 5
            total_kalimantan_mineral += luas_terbakar
            print(f"Luas lahan terbakar: {luas_terbakar} hektare")
        else:
            print("Jenis lahan tidak tersedia.")
            continue
            
    elif pilih_pulau == pulau_2:
        jenis = input("Masukkan jenis lahan (Gambut/Mineral): ").lower()
        if jenis == "":
            print("Jenis lahan tidak boleh kosong!")
            continue
        if jenis == lahan_1:
            print(f"Anda memilih {pilih_pulau}-{jenis}")
            titik_api = input("Masukkan jumlah titik api: ")
            if titik_api == "":
                print("Jumlah titik api tidak boleh kosong!")
                continue
            titik_api = int(titik_api)
            luas_terbakar = titik_api * 5
            total_sumatera_gambut += luas_terbakar
            print(f"Luas lahan terbakar: {luas_terbakar} hektare")
        elif jenis == lahan_2:
            print(f"Anda memilih {pilih_pulau}-{jenis}")
            titik_api = input("Masukkan jumlah titik api: ")
            if titik_api == "":
                print("Jumlah titik api tidak boleh kosong!")
                continue
            titik_api = int(titik_api)
            luas_terbakar = titik_api * 5
            total_sumatera_mineral += luas_terbakar
            print(f"Luas lahan terbakar: {luas_terbakar} hektare")
        else:
            print("Jenis lahan tidak tersedia.")
            continue
    else:
        print("Pilihan pulau tidak tersedia.")
        continue

    ulangi = input("Apakah anda masih mau input data titik api lagi? (Y/N): ").lower()

    while ulangi != "y" and ulangi != "n":
        print("Input hanya boleh Y atau N.")
        ulangi = input("Apakah anda masih mau input data titik api lagi? (Y/N): ").lower()

    if ulangi == "n":
        break


print()
print("================================================================================")
print("                         RINGKASAN DATA KEBAKARAN")
print("================================================================================")
print(f"Kalimantan - Gambut  : {total_kalimantan_gambut} hektare")
print(f"Kalimantan - Mineral : {total_kalimantan_mineral} hektare")
print(f"Sumatera   - Gambut  : {total_sumatera_gambut} hektare")
print(f"Sumatera   - Mineral : {total_sumatera_mineral} hektare")
print("================================================================================")