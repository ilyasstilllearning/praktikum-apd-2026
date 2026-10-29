import os
nama_admin = "ilyas"
password_admin = "049"
jadwal_penerbangan = dict()
reservasi_tiket = dict()
nomor_reservasi = 1


while True:
    os.system("cls")
    print ("============================================================================")
    print ("                                AEROMANAGE")
    print ("                  FLIGHT SCHEDULE & RESERVATION SYSTEM")
    print ("============================================================================")
    print ("Sistem manajemen jadwal penerbangan, reservasi tiket, dan Passenger Manifest")
    print ("============================================================================")
    print ("Silahkan login terlebih dahulu, siapa anda?")
    print ("[1]. Admin")
    print ("[2]. User")
    print ("[3]. Keluar dari program")
    print ("============================================================================")
    pengguna = input ("Masukan pilihan: ")
    if pengguna == "1":
        while True:
            os.system("cls")
            print ("============================================================================")
            print ("LOGIN ADMIN")
            print ("============================================================================")
            nama = input ("Masukan nama admin: ").lower()
            password = input ("Masukan password: ")
            if nama == nama_admin and password == password_admin:
                print ("Login berhasil!")
                input ("Tekan enter untuk melanjutkan")
                while True:
                    os.system("cls")
                    print ("============================================================================")
                    print ("MENU UTAMA ADMIN")
                    print ("============================================================================")
                    print ("[1]. Manajemen jadwal penerbangan")
                    print ("[2]. Manajemen reservasi tiket")
                    print ("[3]. Passenger manifest")
                    print ("[4]. Keluar dari akun admin")
                    print ("============================================================================")
                    pilihan = input ("Masukan pilihan 1-4: ")
                    if pilihan == "1":
                        while True:
                            os.system("cls")
                            print ("============================================================================")
                            print ("MANAJEMEN JADWAL PENERBANGAN")
                            print ("============================================================================")
                            print ("[1]. Tambah jadwal penerbangan")
                            print ("[2]. Lihat jadwal /penerbangan")
                            print ("[3]. Ubah jadwal penerbangan")
                            print ("[4]. Hapus jadwal penerbangan")
                            print ("[5]. Kembali ke menu utama")
                            print ("============================================================================")
                            pilihan = input ("Masukan pilihan 1-5: ")
                            if pilihan == "1":
                                os.system("cls")
                                print ("============================================================================")
                                print ("TAMBAH JADWAL PENERBANGAN")
                                print ("============================================================================")
                                kode = input ("Masukan nomor penerbangan: ").strip().upper()
                                if kode == "":
                                    print ("Kode penerbangan tidak boleh kosong")
                                elif kode in jadwal_penerbangan:
                                    print ("Kode penerbangan sudah terdaftar")
                                else:
                                    maskapai = input ("Masukan nama maskapai: ").strip().upper()
                                    kota_asal = input ("Masukan kota asal: ").strip().upper()
                                    kota_tujuan = input ("Masukan kota tujuan: ").strip().upper()
                                    tanggal = input ("Masukan tanggal penerbangan: ").strip()
                                    jam = input ("Masukan jam keberangkatan: ").strip()
                                    kapasitas = input ("Masukan kapasitas pesawat: ").strip()
                                    if maskapai == "" or kota_asal == "" or kota_tujuan == "" or tanggal == "" or jam == "" or kapasitas == "":
                                        print ("Semua data wajib diisi")
                                    elif kota_asal == kota_tujuan:
                                        print ("Kota asal dan tujuan tidak boleh sama")
                                    elif not kapasitas.isdigit() or int(kapasitas) <= 0:
                                        print ("Kapasitas harus berupa bilangan bulat positif")
                                    else:
                                        jadwal_penerbangan[kode] = {
                                            "maskapai": maskapai,
                                            "asal": kota_asal,
                                            "tujuan": kota_tujuan,
                                            "tanggal": tanggal,
                                            "jam": jam,
                                            "kapasitas": int(kapasitas)
                                        }
                                        print ("Jadwal penerbangan berhasil ditambahkan!")
                                input ("Tekan enter untuk kembali")
                                
                            elif pilihan == "2":
                                os.system("cls")
                                print ("============================================================================")
                                print ("DAFTAR JADWAL PENERBANGAN")
                                print ("============================================================================")
                                if len(jadwal_penerbangan) == 0:
                                    print ("Belum ada jadwal penerbangan")
                                else:
                                    print ("-" * 110)
                                    print (f"{'No.':<5}{'Kode':<12}{'Maskapai':<22}{'Asal':<15}{'Tujuan':<15}{'Tanggal':<15}{'Jam':<10}{'Kapasitas':<10}")
                                    print ("-" * 110)
                                    nomor = 1
                                    for kode, data in jadwal_penerbangan.items():
                                        print (f"{nomor:<5}{kode:<12}{data['maskapai']:<22}{data['asal']:<15}{data['tujuan']:<15}{data['tanggal']:<15}{data['jam']:<10}{data['kapasitas']:<10}")
                                        nomor += 1
                                print ("============================================================================")
                                print (f"Total jadwal penerbangan: {len(jadwal_penerbangan)}")
                                input ("Tekan enter untuk kembali")

                            elif pilihan == "3":
                                os.system("cls")
                                print ("============================================================================")
                                print ("UBAH JADWAL PENERBANGAN")
                                print ("============================================================================")
                                ubah = input ("Masukan kode penerbangan yang ingin diubah: ").strip().upper()
                                if ubah not in jadwal_penerbangan:
                                    print ("Kode penerbangan tidak ditemukan")                                                                                                                                                                    
                                else:
                                    print ("Data penerbangan saat ini:")
                                    print ("Kode penerbangan :", ubah)
                                    print ("Maskapai         :", jadwal_penerbangan[ubah]["maskapai"])
                                    print ("Kota asal        :", jadwal_penerbangan[ubah]["asal"])
                                    print ("Kota tujuan      :", jadwal_penerbangan[ubah]["tujuan"])
                                    print ("Tanggal          :", jadwal_penerbangan[ubah]["tanggal"])
                                    print ("Jam              :", jadwal_penerbangan[ubah]["jam"])
                                    print ("Kapasitas        :", jadwal_penerbangan[ubah]["kapasitas"])
                                    print ("============================================================================")
                                    print ("Tekan enter jika data tidak ingin diubah")
                                    maskapai = input ("Masukan maskapai baru: ").strip().upper()
                                    asal = input ("Masukan kota asal baru: ").strip().upper()
                                    tujuan = input ("Masukan kota tujuan baru: ").strip().upper()
                                    tanggal = input ("Masukan tanggal baru: ").strip()
                                    jam = input ("Masukan jam baru: ").strip()
                                    kapasitas = input ("Masukan kapasitas pesawat: ").strip()
                                    asal_baru = asal if asal != "" else jadwal_penerbangan[ubah]["asal"]
                                    tujuan_baru = tujuan if tujuan != "" else jadwal_penerbangan[ubah]["tujuan"]
                                    if asal_baru == tujuan_baru:
                                        print ("Kota asal dan tujuan tidak boleh sama")
                                    elif kapasitas != "" and (not kapasitas.isdigit() or int(kapasitas) <= 0):
                                        print ("Kapasitas harus berupa bilangan bulat positif")
                                    else:
                                        jumlah_penumpang = 0
                                        for kode_reservasi in reservasi_tiket:
                                            if reservasi_tiket[kode_reservasi]["kode_penerbangan"] == ubah:
                                                jumlah_penumpang += 1
                                        kapasitas_baru = int(kapasitas) if kapasitas != "" else jadwal_penerbangan[ubah]["kapasitas"]
                                        if kapasitas_baru < jumlah_penumpang:
                                            print ("Kapasitas tidak boleh lebih kecil dari pada penumpang")
                                        else:
                                            if maskapai != "":
                                                jadwal_penerbangan[ubah]["maskapai"] = maskapai
                                            jadwal_penerbangan[ubah]["asal"] = asal_baru
                                            jadwal_penerbangan[ubah]["tujuan"] = tujuan_baru
                                            if tanggal != "":
                                                jadwal_penerbangan[ubah]["tanggal"] = tanggal
                                            if jam != "":
                                                jadwal_penerbangan[ubah]["jam"] = jam
                                            jadwal_penerbangan[ubah]["kapasitas"] = kapasitas_baru
                                            for kode_reservasi in reservasi_tiket:
                                                if reservasi_tiket[kode_reservasi]["kode_penerbangan"] == ubah:
                                                    reservasi_tiket[kode_reservasi]["maskapai"] = jadwal_penerbangan[ubah]["maskapai"]
                                                    reservasi_tiket[kode_reservasi]["asal"] = jadwal_penerbangan[ubah]["asal"]
                                                    reservasi_tiket[kode_reservasi]["tujuan"] = jadwal_penerbangan[ubah]["tujuan"]
                                                    reservasi_tiket[kode_reservasi]["tanggal"] = jadwal_penerbangan[ubah]["tanggal"]
                                                    reservasi_tiket[kode_reservasi]["jam"] = jadwal_penerbangan[ubah]["jam"]
                                            print ("Jadwal penerbangan berhasil diubah!")
                                input ("Tekan enter untuk kembali")
                                
                            elif pilihan == "4":
                                os.system("cls")
                                print ("============================================================================")
                                print ("HAPUS JADWAL PENERBANGAN")
                                print ("============================================================================")
                                hapus = input ("Masukan kode penerbangan yang ingin dihapus: ").strip().upper()
                                if hapus not in jadwal_penerbangan:
                                    print ("Kode penerbangan tidak ditemukan")
                                else:
                                    ada_reservasi = False
                                    for kode_reservasi in reservasi_tiket:
                                        if reservasi_tiket[kode_reservasi]["kode_penerbangan"] == hapus:
                                            ada_reservasi = True
                                    if ada_reservasi:
                                        print ("Jadwal tidak dapat dihapus karena masih memiliki reservasi")
                                    else:
                                        konfirmasi = input ("Yakin ingin menghapus? (y/n): ").lower()
                                        if konfirmasi == "y":
                                            jadwal_penerbangan.pop(hapus)
                                            print ("Jadwal penerbangan berhasil dihapus")
                                        else:
                                            print ("Penghapusan dibatalkan")
                                input ("Tekan enter untuk kembali")
                                
                            elif pilihan == "5":
                                break
                            else:
                                print ("Pilihan tidak valid")
                                input ("Tekan enter untuk kembali")

                    elif pilihan == "2":
                        while True:
                            os.system("cls")
                            print ("============================================================================")
                            print ("MANAJEMEN RESERVASI TIKET")
                            print ("============================================================================")
                            print ("[1]. Tambah reservasi")
                            print ("[2]. Lihat reservasi")
                            print ("[3]. Ubah data reservasi")
                            print ("[4]. Hapus / batalkan reservasi")
                            print ("[5]. Cari reservasi")
                            print ("[6]. Kembali ke menu utama")
                            print ("============================================================================")
                            pilihan = input ("Masukan pilihan 1-6: ")
                            if pilihan == "1":
                                os.system("cls")
                                print ("============================================================================")
                                print ("TAMBAH RESERVASI")
                                print ("============================================================================")
                                if len(jadwal_penerbangan) == 0:
                                    print ("Belum ada jadwal penerbangan")
                                else:
                                    for kode, data in jadwal_penerbangan.items():
                                        print (kode, "|", data["maskapai"], "|", data["asal"], "->", data["tujuan"], "|", data["tanggal"], "|", data["jam"])
                                    nama = input ("Masukan nama penumpang: ").strip().upper()
                                    kode = input ("Masukan kode penumpang: ").strip().upper()
                                    if nama == "":
                                        print ("Nama penumpang tidak boleh kosong")
                                    elif kode not in jadwal_penerbangan:
                                        print ("Kode penerbangan tidak ditemukan")
                                    else:
                                        jumlah_penumpang = 0
                                        sudah_memesan = False
                                        for kode_reservasi in reservasi_tiket:
                                            if reservasi_tiket[kode_reservasi]["kode_penerbangan"] == kode:
                                                jumlah_penumpang += 1
                                            if reservasi_tiket[kode_reservasi]["nama"] == nama and reservasi_tiket[kode_reservasi]["kode_penerbangan"] == kode:
                                                sudah_memesan = True
                                        if sudah_memesan:
                                            print ("Penumpang sudah memiliki reservasi pada penerbangan ini")
                                        elif jumlah_penumpang >= jadwal_penerbangan[kode]["kapasitas"]:
                                            print ("Kapasitas penerbangan sudah penuh")
                                        else:
                                            kode_reservasi = f"RSV{nomor_reservasi:04d}"
                                            nomor_reservasi += 1
                                            reservasi_tiket[kode_reservasi] = {
                                                "nama": nama,
                                                "kode_penerbangan": kode,
                                                "maskapai": jadwal_penerbangan[kode]["maskapai"],
                                                "asal": jadwal_penerbangan[kode]["asal"],
                                                "tujuan": jadwal_penerbangan[kode]["tujuan"],
                                                "tanggal": jadwal_penerbangan[kode]["tanggal"],
                                                "jam": jadwal_penerbangan[kode]["jam"]
                                            }
                                            print ("Reservasi berhasil ditambahkan!")
                                            print ("Kode reservasi:", kode_reservasi)
                                input ("Tekan enter untuk kembali")

                            elif pilihan == "2":
                                os.system("cls")
                                print ("============================================================================")
                                print ("DAFTAR RESERVASI TIKET")
                                print ("============================================================================")
                                if len(reservasi_tiket) == 0:
                                    print ("Belum ada reservasi")
                                else:
                                    print (f"{'Kode Reservasi':<18}{'Nama Penumpang':<25}{'Kode Penerbangan':<20}{'Maskapai':<22}{'Asal':<15}{'Tujuan':<15}")
                                    print ("-" * 115)
                                    for kode_reservasi, data in reservasi_tiket.items():
                                        print (f"{kode_reservasi:<18}{data['nama']:<25}{data['kode_penerbangan']:<20}{data['maskapai']:<22}{data['asal']:<15}{data['tujuan']:<15}")
                                print ("============================================================================")
                                print ("Total reservasi:", len(reservasi_tiket))
                                input ("Tekan enter untuk melanjutkan")

                            elif pilihan == "3":
                                os.system("cls")
                                print ("============================================================================")
                                print ("UBAH DATA RESERVASI")
                                print ("============================================================================")
                                kode_reservasi = input ("Masukan kode reservasi: ").strip().upper()
                                if kode_reservasi not in reservasi_tiket:
                                    print ("Reservasi tidak ditemukan")
                                else:
                                    print ("Nama penumpang:", reservasi_tiket[kode_reservasi]["nama"])
                                    print ("Kode penerbangan:", reservasi_tiket[kode_reservasi]["kode_penerbangan"])
                                    nama_baru = input ("Masukan nama baru (enter jika tetap): ").strip().upper()
                                    kode_baru = input ("Masukan kode penerbangan baru (enter jika tetap): ").strip().upper()
                                    if nama_baru == "":
                                        nama_baru = reservasi_tiket[kode_reservasi]["nama"]
                                    if kode_baru == "":
                                        kode_baru = reservasi_tiket[kode_reservasi]["kode_penerbangan"]
                                    if kode_baru not in jadwal_penerbangan:
                                        print ("Penerbangan tidak ditemukan")
                                    else:
                                        jumlah_penumpang = 0
                                        sudah_memesan = False
                                        for kode_lain in reservasi_tiket:
                                            if reservasi_tiket[kode_lain]["kode_penerbangan"] == kode_baru:
                                                jumlah_penumpang += 1
                                            if kode_lain != kode_reservasi and reservasi_tiket[kode_lain]["nama"] == nama_baru and reservasi_tiket[kode_lain]["kode_penerbangan"] == kode_baru:
                                                sudah_memesan = True
                                        if sudah_memesan:
                                            print ("Penumpang sudah memiliki reservasi pada penerbangan ini")
                                        elif kode_baru != reservasi_tiket[kode_reservasi]["kode_penerbangan"] and jumlah_penumpang >= jadwal_penerbangan[kode_baru]["kapasitas"]:
                                            print ("Penerbangan baru sudah penuh")
                                        else:
                                            reservasi_tiket[kode_reservasi]["nama"] = nama_baru
                                            reservasi_tiket[kode_reservasi]["kode_penerbangan"] = kode_baru
                                            reservasi_tiket[kode_reservasi]["maskapai"] = jadwal_penerbangan[kode_baru]["maskapai"]
                                            reservasi_tiket[kode_reservasi]["asal"] = jadwal_penerbangan[kode_baru]["asal"]
                                            reservasi_tiket[kode_reservasi]["tujuan"] = jadwal_penerbangan[kode_baru]["tujuan"]
                                            reservasi_tiket[kode_reservasi]["tanggal"] = jadwal_penerbangan[kode_baru]["tanggal"]
                                            reservasi_tiket[kode_reservasi]["jam"] = jadwal_penerbangan[kode_baru]["jam"]
                                            print ("Reservasi berhasil diubah")
                                input ("Tekan enter untuk melanjutkan")
                                
                            elif pilihan == "4":
                                os.system("cls")
                                print ("============================================================================")
                                print ("HAPUS / BATALKAN RESERVASI")
                                print ("============================================================================")
                                kode = input ("Masukan kode reservasi: ").strip().upper()
                                if kode not in reservasi_tiket:
                                    print ("Reservasi tidak ditemukan")
                                else:
                                    konfirmasi = input ("Yakin ingin membatalkan reservasi? (y/n): ").lower()
                                    if konfirmasi == "y":
                                        reservasi_tiket.pop(kode)
                                        print ("Reservasi berhasil dibatalkan")
                                    else:
                                        print ("Pembatalan dibatalkan")
                                input ("Tekan enter untuk kembali")
                                
                                
                            elif pilihan == "5":
                                os.system("cls")
                                print ("============================================================================")
                                print ("CARI RESERVASI")
                                print ("============================================================================")
                                kode = input ("Masukan kode reservasi: ").strip().upper()
                                if kode not in reservasi_tiket:
                                    print ("Reservasi tidak ditemukan")
                                else:
                                    print ("Kode reservasi:", kode)
                                    print ("Nama penumpang:", reservasi_tiket[kode]["nama"])
                                    print ("Kode penerbangan:", reservasi_tiket[kode]["kode_penerbangan"])
                                    print ("Maskapai:", reservasi_tiket[kode]["maskapai"])
                                    print ("Kota asal:", reservasi_tiket[kode]["asal"])
                                    print ("Kota tujuan:", reservasi_tiket[kode]["tujuan"])
                                    print ("Tanggal:", reservasi_tiket[kode]["tanggal"])
                                    print ("Jam:", reservasi_tiket[kode]["jam"])
                                input ("Tekan enter untuk kembali")
                            elif pilihan == "6":
                                break
                            else:
                                print ("Pilihan tidak valid")
                                input ("Tekan enter untuk kembali")
                                
                    elif pilihan == "3":
                        os.system("cls")
                        print ("============================================================================")
                        print ("PASSENGER MANIFEST")
                        print ("============================================================================")
                        if len(jadwal_penerbangan) == 0:
                            print ("Belum ada jadwal penerbangan")
                        else:
                            for kode, data in jadwal_penerbangan.items():
                                print (kode, "|", data["maskapai"], "|", data["asal"], "->", data["tujuan"], "|", data["tanggal"])
                            kode = input ("Masukan kode penerbangan: ").strip().upper()
                            if kode not in jadwal_penerbangan:
                                print ("Kode penerbangan tidak ditemukan")
                            else:
                                print ("-" * 70)
                                print ("PASSENGER MANIFEST:", kode)
                                print ("Maskapai:", jadwal_penerbangan[kode]["maskapai"])
                                print ("Rute:", jadwal_penerbangan[kode]["asal"], "->", jadwal_penerbangan[kode]["tujuan"])
                                print ("Tanggal:", jadwal_penerbangan[kode]["tanggal"])
                                print ("Jam:", jadwal_penerbangan[kode]["jam"])
                                print ("-" * 70)
                                print (f"{'No.':<6}{'Kode Reservasi':<20}{'Nama Penumpang':<30}")
                                print ("-" * 70)
                                jumlah_penumpang = 0
                                for kode_reservasi, data in reservasi_tiket.items():
                                    if data["kode_penerbangan"] == kode:
                                        jumlah_penumpang += 1
                                        print (f"{jumlah_penumpang:<6}{kode_reservasi:<20}{data['nama']:<30}")
                                if jumlah_penumpang == 0:
                                    print ("Belum ada penumpang")
                                print ("-" * 70)
                                print ("Jumlah penumpang:", jumlah_penumpang)
                                print ("Kapasitas pesawat:", jadwal_penerbangan[kode]["kapasitas"])
                                print ("Sisa kursi:", jadwal_penerbangan[kode]["kapasitas"] - jumlah_penumpang)
                        input ("Tekan enter untuk kembali")
                        
                    elif pilihan == "4":
                        print ("Terima kasih telah menggunakan AeroManage!")
                        input ("Tekan enter untuk melanjutkan")
                        break
                    else:
                        print ("Pilihan tidak valid")
                        input ("Tekan enter untuk melanjutkan")
                break
            else:
                print ("Nama admin atau password salah")
                pilihan_login = input ("Coba lagi? (y/n): ").lower()
                if pilihan_login != "y":
                    break


    elif pengguna == "2":
        while True:
            os.system("cls")
            print ("============================================================================")
            print ("                         AEROMANAGE - MENU USER")
            print ("============================================================================")
            print ("[1]. Lihat jadwal penerbangan")
            print ("[2]. Cari penerbangan")
            print ("[3]. Buat reservasi tiket")
            print ("[4]. Lihat reservasi saya")
            print ("[5]. Ubah reservasi saya")
            print ("[6]. Batalkan reservasi saya")
            print ("[7]. Kembali ke menu utama")
            print ("============================================================================")
            pilihan = input ("Masukan pilihan 1-7: ")
            if pilihan == "1":
                os.system("cls")
                print ("============================================================================")
                print ("DAFTAR JADWAL PENERBANGAN")
                print ("============================================================================")
                if len(jadwal_penerbangan) == 0:
                    print ("Belum ada jadwal penerbangan")
                else:
                    print (f"{'Kode':<12}{'Maskapai':<22}{'Asal':<15}{'Tujuan':<15}{'Tanggal':<15}{'Jam':<10}{'Kapasitas':<10}")
                    print ("-" * 100)
                    for kode, data in jadwal_penerbangan.items():
                        print (f"{kode:<12}{data['maskapai']:<22}{data['asal']:<15}{data['tujuan']:<15}{data['tanggal']:<15}{data['jam']:<10}{data['kapasitas']:<10}")
                input ("Tekan enter untuk melanjutkan")
                
            elif pilihan == "2":
                os.system("cls")
                print ("============================================================================")
                print ("CARI PENERBANGAN")
                print ("============================================================================")
                kode = input ("Masukan kode penerbangan: ").strip().upper()
                if kode not in jadwal_penerbangan:
                    print ("Penerbangan tidak ditemukan")
                else:
                    jumlah_penumpang = 0
                    for kode_reservasi in reservasi_tiket:
                        if reservasi_tiket[kode_reservasi]["kode_penerbangan"] == kode:
                            jumlah_penumpang += 1
                    print ("Kode penerbangan:", kode)
                    print ("Maskapai:", jadwal_penerbangan[kode]["maskapai"])
                    print ("Kota asal:", jadwal_penerbangan[kode]["asal"])
                    print ("Kota tujuan:", jadwal_penerbangan[kode]["tujuan"])
                    print ("Tanggal:", jadwal_penerbangan[kode]["tanggal"])
                    print ("Jam:", jadwal_penerbangan[kode]["jam"])
                    print ("Sisa kursi:", jadwal_penerbangan[kode]["kapasitas"] - jumlah_penumpang)
                input ("Tekan enter untuk kembali")
                
            elif pilihan == "3":
                os.system("cls")
                print ("============================================================================")
                print ("BUAT RESERVASI TIKET")
                print ("============================================================================")
                if len(jadwal_penerbangan) == 0:
                    print ("Belum ada jadwal penerbangan")
                else:
                    nama = input ("Masukan nama lengkap: ").strip().upper()
                    if nama == "":
                        print ("Nama tidak boleh kosong")
                    else:
                        print ("\nDaftar penerbangan:")
                        for kode, data in jadwal_penerbangan.items():
                            jumlah_penumpang = 0
                            for kode_reservasi in reservasi_tiket:
                                if reservasi_tiket[kode_reservasi]["kode_penerbangan"] == kode:
                                    jumlah_penumpang += 1
                            print (kode, "|", data["maskapai"], "|", data["asal"], "->", data["tujuan"], "|", data["tanggal"], "| Sisa kursi:", data["kapasitas"] - jumlah_penumpang)
                        kode = input ("Masukan kode penerbangan: ").strip().upper()
                        if kode not in jadwal_penerbangan:
                            print ("Penerbangan tidak ditemukan")
                        else:
                            jumlah_penumpang = 0
                            sudah_memesan = False
                            for kode_reservasi in reservasi_tiket:
                                if reservasi_tiket[kode_reservasi]["kode_penerbangan"] == kode:
                                    jumlah_penumpang += 1
                                if reservasi_tiket[kode_reservasi]["nama"] == nama and reservasi_tiket[kode_reservasi]["kode_penerbangan"] == kode:
                                    sudah_memesan = True
                            if sudah_memesan:
                                print ("Anda sudah memiliki reservasi pada penerbangan ini")
                            elif jumlah_penumpang >= jadwal_penerbangan[kode]["kapasitas"]:
                                print ("Kapasitas penerbangan sudah penuh")
                            else:
                                kode_reservasi = f"RSV{nomor_reservasi:04d}"
                                nomor_reservasi += 1
                                reservasi_tiket[kode_reservasi] = {
                                    "nama": nama,
                                    "kode_penerbangan": kode,
                                    "maskapai": jadwal_penerbangan[kode]["maskapai"],
                                    "asal": jadwal_penerbangan[kode]["asal"],
                                    "tujuan": jadwal_penerbangan[kode]["tujuan"],
                                    "tanggal": jadwal_penerbangan[kode]["tanggal"],
                                    "jam": jadwal_penerbangan[kode]["jam"]
                                }
                                print ("Reservasi berhasil dibuat!")
                                print ("Kode reservasi:", kode_reservasi)
                input ("Tekan enter untuk kembali")
                
            elif pilihan == "4":
                os.system("cls")
                print ("============================================================================")
                print ("RESERVASI SAYA")
                print ("============================================================================")
                nama = input ("Masukan nama lengkap Anda: ").strip().upper()
                ditemukan = False
                for kode_reservasi, data in reservasi_tiket.items():
                    if data["nama"] == nama:
                        print ("-" * 60)
                        print ("Kode reservasi:", kode_reservasi)
                        print ("Nama penumpang:", data["nama"])
                        print ("Kode penerbangan:", data["kode_penerbangan"])
                        print ("Maskapai:", data["maskapai"])
                        print ("Rute:", data["asal"], "->", data["tujuan"])
                        print ("Tanggal:", data["tanggal"])
                        print ("Jam:", data["jam"])
                        ditemukan = True
                if ditemukan == False:
                    print ("Reservasi tidak ditemukan")
                input ("Tekan enter untuk kembali")
                
            elif pilihan == "5":
                os.system("cls")
                print ("============================================================================")
                print ("UBAH RESERVASI SAYA")
                print ("============================================================================")
                nama = input ("Masukan nama lengkap Anda: ").strip().upper()
                kode_reservasi = input ("Masukan kode reservasi: ").strip().upper()
                if kode_reservasi not in reservasi_tiket or reservasi_tiket[kode_reservasi]["nama"] != nama:
                    print ("Reservasi tidak ditemukan")
                else:
                    print ("Kode penerbangan saat ini:", reservasi_tiket[kode_reservasi]["kode_penerbangan"])
                    kode_baru = input ("Masukan kode penerbangan baru (enter jika tetap): ").strip().upper()
                    if kode_baru == "":
                        kode_baru = reservasi_tiket[kode_reservasi]["kode_penerbangan"]
                    if kode_baru not in jadwal_penerbangan:
                        print ("Penerbangan tidak ditemukan")
                    else:
                        kode_lama = reservasi_tiket[kode_reservasi]["kode_penerbangan"]
                        jumlah_penumpang = 0
                        for kode_lain in reservasi_tiket:
                            if reservasi_tiket[kode_lain]["kode_penerbangan"] == kode_baru:
                                jumlah_penumpang += 1
                        if kode_baru != kode_lama and jumlah_penumpang >= jadwal_penerbangan[kode_baru]["kapasitas"]:
                            print ("Penerbangan baru sudah penuh")
                        else:
                            reservasi_tiket[kode_reservasi]["kode_penerbangan"] = kode_baru
                            reservasi_tiket[kode_reservasi]["maskapai"] = jadwal_penerbangan[kode_baru]["maskapai"]
                            reservasi_tiket[kode_reservasi]["asal"] = jadwal_penerbangan[kode_baru]["asal"]
                            reservasi_tiket[kode_reservasi]["tujuan"] = jadwal_penerbangan[kode_baru]["tujuan"]
                            reservasi_tiket[kode_reservasi]["tanggal"] = jadwal_penerbangan[kode_baru]["tanggal"]
                            reservasi_tiket[kode_reservasi]["jam"] = jadwal_penerbangan[kode_baru]["jam"]
                            print ("Reservasi berhasil diubah")
                input ("Tekan enter untuk kembali")
                
            elif pilihan == "6":
                os.system("cls")
                print ("============================================================================")
                print ("BATALKAN RESERVASI")
                print ("============================================================================")
                nama = input ("Masukan nama lengkap Anda: ").strip().upper()
                kode_reservasi = input ("Masukan kode reservasi: ").strip().upper()
                if kode_reservasi not in reservasi_tiket or reservasi_tiket[kode_reservasi]["nama"] != nama:
                    print ("Reservasi tidak ditemukan")
                else:
                    konfirmasi = input ("Yakin ingin membatalkan reservasi? (y/n): ").lower()
                    if konfirmasi == "y":
                        reservasi_tiket.pop(kode_reservasi)
                        print ("Reservasi berhasil dibatalkan")
                    else:
                        print ("Pembatalan dibatalkan")
                input ("Tekan enter untuk kembali")
            elif pilihan == "7":
                break
            else:
                print ("Pilihan tidak valid")
                input ("Tekan enter untuk kembali")
                
    elif pengguna == "3":
        os.system("cls")
        print ("============================================================================")
        print ("Terimakasih sudah menggunakan program AeroManage!")
        print ("============================================================================")
        break
    else:
        print ("Pilihan anda tidak valid, silahkan ulangi")
        input ("Tekan enter untuk melanjutkan")