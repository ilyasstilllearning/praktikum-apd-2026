harga_angkasa = int (1500000)
nama_ilyas = ("muhammad ilyas muzakki")
nim_ilyas = str(49)

print ("Selamat datang di ANGKASA")
nama = str(input("Masukan nama: ")).lower()
nim = str(input("Masukan nim: "))

if nama == nama_ilyas and nim == nim_ilyas:
    print ("Berikut daftar paket yang bisa anda beli:")
    print ("1.Paket Orbit: Biaya administrasi 1%")
    print ("2.Paket Nebula: Biaya administrasi 3%")
    print ("3.Paket Galaxy: Biaya administrasi 5%")
    print ("4.Paket Supernova: Biaya administrasi 7%")
    pilihan = int(input("Masukan pilihan 1-4: "))
    
    if pilihan == 1:
        print ("Anda memilih paket Orbit")
        total_bayar = int(harga_angkasa + harga_angkasa * 1 / 100)
        print (f"Harga yang harus anda bayar + administrasi adalah: {total_bayar}")
        print ("Dan anda akan mendapatkan fitur: ")
        print ("akses dasar ke lagu-lagu populer")

    elif pilihan == 2:
        print ("Anda memilih paket Nebula")
        total_bayar = int(harga_angkasa + harga_angkasa * 3 / 100)
        print (f"Harga yang harus anda bayar + administrasi adalah: {total_bayar}")
        print ("Dan anda akan mendapatkan fitur: ")
        print ("akses lagu premium dan playlist kustom")

    elif pilihan == 3:
        print ("Anda memilih paket Galaxy")
        total_bayar = int(harga_angkasa + harga_angkasa * 5 / 100)
        print (f"Harga yang harus anda bayar + administrasi adalah: {total_bayar}")
        print ("Dan anda akan mendapatkan fitur: ")
        print ("akses lagu premium, playlist kustom, dan mode offline")
        
    elif pilihan == 4:
        print ("Anda memilih paket Supernova")
        total_bayar = int(harga_angkasa + harga_angkasa * 7 / 100)
        print (f"Harga yang harus anda bayar + administrasi adalah: {total_bayar}")
        print ("Dan anda akan mendapatkan fitur: ")
        print ("akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis")
    else:
        print ("Pilihan hanya tersedia 1-4")
else:
    print ("Nama / Nim salah, silahkan ulangi!")