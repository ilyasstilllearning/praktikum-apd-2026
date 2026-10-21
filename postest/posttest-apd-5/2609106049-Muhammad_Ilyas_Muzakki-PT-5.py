import os
nama_admin = "ilyas"
password_admin = "049"
jadwal_penerbangan = list()
reservasi_tiket = list()
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
                    print ("[3]. Passenger Manifest")
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
                            print ("[2]. Lihat jadwal penerbangan")
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
                                tersedia = True
                                for penerbangan in jadwal_penerbangan:
                                    if penerbangan[0] == kode:
                                        tersedia = False
                                if kode == "":
                                    print ("Kode penerbangan tidak boleh kosong")
                                elif tersedia == False:
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
                                        tambah = [kode, maskapai, kota_asal, kota_tujuan, tanggal, jam, int(kapasitas)]
                                        jadwal_penerbangan.append(tambah)
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
                                    for i in range(len(jadwal_penerbangan)):
                                        print (f"{i + 1:<5}{jadwal_penerbangan[i][0]:<12}{jadwal_penerbangan[i][1]:<22}{jadwal_penerbangan[i][2]:<15}{jadwal_penerbangan[i][3]:<15}{jadwal_penerbangan[i][4]:<15}{jadwal_penerbangan[i][5]:<10}{jadwal_penerbangan[i][6]:<10}")
                                print ("============================================================================")
                                print (f"Total jadwal penerbangan: {len(jadwal_penerbangan)}")
                                input ("Tekan enter untuk kembali")

                            elif pilihan == "3":
                                os.system("cls")
                                print ("============================================================================")
                                print ("UBAH JADWAL PENERBANGAN")
                                print ("============================================================================")
                                ubah = input ("Masukan kode penerbangan yang ingin diubah: ").strip().upper()
                                indeks = -1
                                for i in range(len(jadwal_penerbangan)):
                                    if jadwal_penerbangan[i][0] == ubah:
                                        indeks = i
                                        break
                                if indeks == -1:
                                    print ("Kode penerbangan tidak ditemukan")
                                else:
                                    print ("Data penerbangan saat ini:")
                                    print ("Kode penerbangan :", jadwal_penerbangan[indeks][0])
                                    print ("Maskapai         :", jadwal_penerbangan[indeks][1])
                                    print ("Kota asal        :", jadwal_penerbangan[indeks][2])
                                    print ("Kota tujuan      :", jadwal_penerbangan[indeks][3])
                                    print ("Tanggal          :", jadwal_penerbangan[indeks][4])
                                    print ("Jam              :", jadwal_penerbangan[indeks][5])
                                    print ("Kapasitas        :", jadwal_penerbangan[indeks][6])
                                    print ("============================================================================")
                                    print ("Tekan enter jika data tidak ingin diubah")
                                    maskapai = input ("Masukan maskapai baru: ").strip().upper()
                                    asal = input ("Masukan kota asal baru: ").strip().upper()
                                    tujuan = input ("Masukan kota tujuan baru: ").strip().upper()
                                    tanggal = input ("Masukan tanggal baru: ").strip()
                                    jam = input ("Masukan jam baru: ").strip()
                                    kapasitas = input ("Masukan kapasitas baru: ").strip()
                                    asal_baru = asal if asal != "" else jadwal_penerbangan[indeks][2]
                                    tujuan_baru = tujuan if tujuan != "" else jadwal_penerbangan[indeks][3]
                                    if asal_baru == tujuan_baru:
                                        print ("Kota asal dan tujuan tidak boleh sama")
                                    elif kapasitas != "" and (not kapasitas.isdigit() or int(kapasitas) <= 0):
                                        print ("Kapasitas harus berupa bilangan bulat positif")
                                    else:
                                        jumlah_penumpang = 0
                                        for reservasi in reservasi_tiket:
                                            if reservasi[2] == ubah:
                                                jumlah_penumpang += 1
                                        kapasitas_baru = int(kapasitas) if kapasitas != "" else jadwal_penerbangan[indeks][6]
                                        if kapasitas_baru < jumlah_penumpang:
                                            print ("Kapasitas tidak boleh lebih kecil dari jumlah penumpang")
                                        else:
                                            if maskapai != "":
                                                jadwal_penerbangan[indeks][1] = maskapai
                                            jadwal_penerbangan[indeks][2] = asal_baru
                                            jadwal_penerbangan[indeks][3] = tujuan_baru
                                            if tanggal != "":
                                                jadwal_penerbangan[indeks][4] = tanggal
                                            if jam != "":
                                                jadwal_penerbangan[indeks][5] = jam
                                            jadwal_penerbangan[indeks][6] = kapasitas_baru
                                            for reservasi in reservasi_tiket:
                                                if reservasi[2] == ubah:
                                                    reservasi[3] = jadwal_penerbangan[indeks][1]
                                                    reservasi[4] = jadwal_penerbangan[indeks][2]
                                                    reservasi[5] = jadwal_penerbangan[indeks][3]
                                                    reservasi[6] = jadwal_penerbangan[indeks][4]
                                                    reservasi[7] = jadwal_penerbangan[indeks][5]
                                            print ("Jadwal penerbangan berhasil diubah!")
                                input ("Tekan enter untuk kembali")
                                
                            elif pilihan == "4":
                                os.system("cls")
                                print ("============================================================================")
                                print ("HAPUS JADWAL PENERBANGAN")
                                print ("============================================================================")
                                hapus = input ("Masukan kode penerbangan yang ingin dihapus: ").strip().upper()
                                indeks = -1
                                for i in range(len(jadwal_penerbangan)):
                                    if jadwal_penerbangan[i][0] == hapus:
                                        indeks = i
                                        break
                                if indeks == -1:
                                    print ("Kode penerbangan tidak ditemukan")
                                else:
                                    ada_reservasi = False
                                    for reservasi in reservasi_tiket:
                                        if reservasi[2] == hapus:
                                            ada_reservasi = True
                                    if ada_reservasi:
                                        print ("Jadwal tidak dapat dihapus karena masih memiliki reservasi")
                                    else:
                                        konfirmasi = input ("Yakin ingin menghapus? (y/n): ").lower()
                                        if konfirmasi == "y":
                                            jadwal_penerbangan.pop(indeks)
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
                                    for penerbangan in jadwal_penerbangan:
                                        print (penerbangan[0], "|", penerbangan[1], "|", penerbangan[2], "->", penerbangan[3], "|", penerbangan[4], "|", penerbangan[5])
                                    nama = input ("Masukan nama penumpang: ").strip().upper()
                                    kode = input ("Masukan kode penerbangan: ").strip().upper()
                                    indeks = -1
                                    for i in range(len(jadwal_penerbangan)):
                                        if jadwal_penerbangan[i][0] == kode:
                                            indeks = i
                                            break
                                    if nama == "":
                                        print ("Nama penumpang tidak boleh kosong")
                                    elif indeks == -1:
                                        print ("Kode penerbangan tidak ditemukan")
                                    else:
                                        jumlah_penumpang = 0
                                        sudah_memesan = False
                                        for reservasi in reservasi_tiket:
                                            if reservasi[2] == kode:
                                                jumlah_penumpang += 1
                                            if reservasi[1] == nama and reservasi[2] == kode:
                                                sudah_memesan = True
                                        if sudah_memesan:
                                            print ("Penumpang sudah memiliki reservasi pada penerbangan ini")
                                        elif jumlah_penumpang >= jadwal_penerbangan[indeks][6]:
                                            print ("Kapasitas penerbangan sudah penuh")
                                        else:
                                            kode_reservasi = f"RSV{nomor_reservasi:04d}"
                                            nomor_reservasi += 1
                                            tambah = [kode_reservasi, nama, kode, jadwal_penerbangan[indeks][1], jadwal_penerbangan[indeks][2], jadwal_penerbangan[indeks][3], jadwal_penerbangan[indeks][4], jadwal_penerbangan[indeks][5]]
                                            reservasi_tiket.append(tambah)
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
                                    for reservasi in reservasi_tiket:
                                        print (f"{reservasi[0]:<18}{reservasi[1]:<25}{reservasi[2]:<20}{reservasi[3]:<22}{reservasi[4]:<15}{reservasi[5]:<15}")
                                print ("============================================================================")
                                print ("Total reservasi:", len(reservasi_tiket))
                                input ("Tekan enter untuk kembali")

                            elif pilihan == "3":
                                os.system("cls")
                                print ("============================================================================")
                                print ("UBAH DATA RESERVASI")
                                print ("============================================================================")
                                kode_reservasi = input ("Masukan kode reservasi: ").strip().upper()
                                indeks = -1
                                for i in range(len(reservasi_tiket)):
                                    if reservasi_tiket[i][0] == kode_reservasi:
                                        indeks = i
                                        break
                                if indeks == -1:
                                    print ("Reservasi tidak ditemukan")
                                else:
                                    print ("Nama penumpang:", reservasi_tiket[indeks][1])
                                    print ("Kode penerbangan:", reservasi_tiket[indeks][2])
                                    nama_baru = input ("Masukan nama baru (enter jika tetap): ").strip().upper()
                                    kode_baru = input ("Masukan kode penerbangan baru (enter jika tetap): ").strip().upper()
                                    if nama_baru == "":
                                        nama_baru = reservasi_tiket[indeks][1]
                                    if kode_baru == "":
                                        kode_baru = reservasi_tiket[indeks][2]
                                    indeks_penerbangan = -1
                                    for i in range(len(jadwal_penerbangan)):
                                        if jadwal_penerbangan[i][0] == kode_baru:
                                            indeks_penerbangan = i
                                            break
                                    if indeks_penerbangan == -1:
                                        print ("Penerbangan tidak ditemukan")
                                    else:
                                        jumlah_penumpang = 0
                                        sudah_memesan = False
                                        for i in range(len(reservasi_tiket)):
                                            if reservasi_tiket[i][2] == kode_baru:
                                                jumlah_penumpang += 1
                                            if i != indeks and reservasi_tiket[i][1] == nama_baru and reservasi_tiket[i][2] == kode_baru:
                                                sudah_memesan = True
                                        if sudah_memesan:
                                            print ("Penumpang sudah memiliki reservasi pada penerbangan ini")
                                        elif kode_baru != reservasi_tiket[indeks][2] and jumlah_penumpang >= jadwal_penerbangan[indeks_penerbangan][6]:
                                            print ("Penerbangan baru sudah penuh")
                                        else:
                                            reservasi_tiket[indeks][1] = nama_baru
                                            reservasi_tiket[indeks][2] = kode_baru
                                            reservasi_tiket[indeks][3] = jadwal_penerbangan[indeks_penerbangan][1]
                                            reservasi_tiket[indeks][4] = jadwal_penerbangan[indeks_penerbangan][2]
                                            reservasi_tiket[indeks][5] = jadwal_penerbangan[indeks_penerbangan][3]
                                            reservasi_tiket[indeks][6] = jadwal_penerbangan[indeks_penerbangan][4]
                                            reservasi_tiket[indeks][7] = jadwal_penerbangan[indeks_penerbangan][5]
                                            print ("Reservasi berhasil diubah")
                                input ("Tekan enter untuk kembali")
                                
                            elif pilihan == "4":
                                os.system("cls")
                                print ("============================================================================")
                                print ("HAPUS / BATALKAN RESERVASI")
                                print ("============================================================================")
                                kode = input ("Masukan kode reservasi: ").strip().upper()
                                indeks = -1
                                for i in range(len(reservasi_tiket)):
                                    if reservasi_tiket[i][0] == kode:
                                        indeks = i
                                        break
                                if indeks == -1:
                                    print ("Reservasi tidak ditemukan")
                                else:
                                    konfirmasi = input ("Yakin ingin membatalkan reservasi? (y/n): ").lower()
                                    if konfirmasi == "y":
                                        reservasi_tiket.pop(indeks)
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
                                indeks = -1
                                for i in range(len(reservasi_tiket)):
                                    if reservasi_tiket[i][0] == kode:
                                        indeks = i
                                        break
                                if indeks == -1:
                                    print ("Reservasi tidak ditemukan")
                                else:
                                    print ("Kode reservasi:", reservasi_tiket[indeks][0])
                                    print ("Nama penumpang:", reservasi_tiket[indeks][1])
                                    print ("Kode penerbangan:", reservasi_tiket[indeks][2])
                                    print ("Maskapai:", reservasi_tiket[indeks][3])
                                    print ("Kota asal:", reservasi_tiket[indeks][4])
                                    print ("Kota tujuan:", reservasi_tiket[indeks][5])
                                    print ("Tanggal:", reservasi_tiket[indeks][6])
                                    print ("Jam:", reservasi_tiket[indeks][7])
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
                            for penerbangan in jadwal_penerbangan:
                                print (penerbangan[0], "|", penerbangan[1], "|", penerbangan[2], "->", penerbangan[3], "|", penerbangan[4])
                            kode = input ("Masukan kode penerbangan: ").strip().upper()
                            indeks = -1
                            for i in range(len(jadwal_penerbangan)):
                                if jadwal_penerbangan[i][0] == kode:
                                    indeks = i
                                    break
                            if indeks == -1:
                                print ("Kode penerbangan tidak ditemukan")
                            else:
                                print ("-" * 70)
                                print ("PASSENGER MANIFEST:", kode)
                                print ("Maskapai:", jadwal_penerbangan[indeks][1])
                                print ("Rute:", jadwal_penerbangan[indeks][2], "->", jadwal_penerbangan[indeks][3])
                                print ("Tanggal:", jadwal_penerbangan[indeks][4])
                                print ("Jam:", jadwal_penerbangan[indeks][5])
                                print ("-" * 70)
                                print (f"{'No.':<6}{'Kode Reservasi':<20}{'Nama Penumpang':<30}")
                                print ("-" * 70)
                                jumlah_penumpang = 0
                                for reservasi in reservasi_tiket:
                                    if reservasi[2] == kode:
                                        jumlah_penumpang += 1
                                        print (f"{jumlah_penumpang:<6}{reservasi[0]:<20}{reservasi[1]:<30}")
                                if jumlah_penumpang == 0:
                                    print ("Belum ada penumpang")
                                print ("-" * 70)
                                print ("Jumlah penumpang:", jumlah_penumpang)
                                print ("Kapasitas pesawat:", jadwal_penerbangan[indeks][6])
                                print ("Sisa kursi:", jadwal_penerbangan[indeks][6] - jumlah_penumpang)
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
                    for penerbangan in jadwal_penerbangan:
                        print (f"{penerbangan[0]:<12}{penerbangan[1]:<22}{penerbangan[2]:<15}{penerbangan[3]:<15}{penerbangan[4]:<15}{penerbangan[5]:<10}{penerbangan[6]:<10}")
                input ("Tekan enter untuk kembali")
                
            elif pilihan == "2":
                os.system("cls")
                print ("============================================================================")
                print ("CARI PENERBANGAN")
                print ("============================================================================")
                kode = input ("Masukan kode penerbangan: ").strip().upper()
                indeks = -1
                for i in range(len(jadwal_penerbangan)):
                    if jadwal_penerbangan[i][0] == kode:
                        indeks = i
                        break
                if indeks == -1:
                    print ("Penerbangan tidak ditemukan")
                else:
                    jumlah_penumpang = 0
                    for reservasi in reservasi_tiket:
                        if reservasi[2] == kode:
                            jumlah_penumpang += 1
                    print ("Kode penerbangan:", jadwal_penerbangan[indeks][0])
                    print ("Maskapai:", jadwal_penerbangan[indeks][1])
                    print ("Kota asal:", jadwal_penerbangan[indeks][2])
                    print ("Kota tujuan:", jadwal_penerbangan[indeks][3])
                    print ("Tanggal:", jadwal_penerbangan[indeks][4])
                    print ("Jam:", jadwal_penerbangan[indeks][5])
                    print ("Sisa kursi:", jadwal_penerbangan[indeks][6] - jumlah_penumpang)
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
                        for penerbangan in jadwal_penerbangan:
                            jumlah_penumpang = 0
                            for reservasi in reservasi_tiket:
                                if reservasi[2] == penerbangan[0]:
                                    jumlah_penumpang += 1
                            print (penerbangan[0], "|", penerbangan[1], "|", penerbangan[2], "->", penerbangan[3], "|", penerbangan[4], "| Sisa kursi:", penerbangan[6] - jumlah_penumpang)
                        kode = input ("Masukan kode penerbangan: ").strip().upper()
                        indeks = -1
                        for i in range(len(jadwal_penerbangan)):
                            if jadwal_penerbangan[i][0] == kode:
                                indeks = i
                                break
                        if indeks == -1:
                            print ("Penerbangan tidak ditemukan")
                        else:
                            jumlah_penumpang = 0
                            sudah_memesan = False
                            for reservasi in reservasi_tiket:
                                if reservasi[2] == kode:
                                    jumlah_penumpang += 1
                                if reservasi[1] == nama and reservasi[2] == kode:
                                    sudah_memesan = True
                            if sudah_memesan:
                                print ("Anda sudah memiliki reservasi pada penerbangan ini")
                            elif jumlah_penumpang >= jadwal_penerbangan[indeks][6]:
                                print ("Kapasitas penerbangan sudah penuh")
                            else:
                                kode_reservasi = f"RSV{nomor_reservasi:04d}"
                                nomor_reservasi += 1
                                tambah = [kode_reservasi, nama, kode, jadwal_penerbangan[indeks][1], jadwal_penerbangan[indeks][2], jadwal_penerbangan[indeks][3], jadwal_penerbangan[indeks][4], jadwal_penerbangan[indeks][5]]
                                reservasi_tiket.append(tambah)
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
                for reservasi in reservasi_tiket:
                    if reservasi[1] == nama:
                        print ("-" * 60)
                        print ("Kode reservasi:", reservasi[0])
                        print ("Nama penumpang:", reservasi[1])
                        print ("Kode penerbangan:", reservasi[2])
                        print ("Maskapai:", reservasi[3])
                        print ("Rute:", reservasi[4], "->", reservasi[5])
                        print ("Tanggal:", reservasi[6])
                        print ("Jam:", reservasi[7])
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
                indeks = -1
                for i in range(len(reservasi_tiket)):
                    if reservasi_tiket[i][0] == kode_reservasi and reservasi_tiket[i][1] == nama:
                        indeks = i
                        break
                if indeks == -1:
                    print ("Reservasi tidak ditemukan")
                else:
                    print ("Kode penerbangan saat ini:", reservasi_tiket[indeks][2])
                    kode_baru = input ("Masukan kode penerbangan baru (enter jika tetap): ").strip().upper()
                    if kode_baru == "":
                        kode_baru = reservasi_tiket[indeks][2]
                    indeks_penerbangan = -1
                    for i in range(len(jadwal_penerbangan)):
                        if jadwal_penerbangan[i][0] == kode_baru:
                            indeks_penerbangan = i
                            break
                    if indeks_penerbangan == -1:
                        print ("Penerbangan tidak ditemukan")
                    else:
                        kode_lama = reservasi_tiket[indeks][2]
                        jumlah_penumpang = 0
                        for reservasi in reservasi_tiket:
                            if reservasi[2] == kode_baru:
                                jumlah_penumpang += 1
                        if kode_baru != kode_lama and jumlah_penumpang >= jadwal_penerbangan[indeks_penerbangan][6]:
                            print ("Penerbangan baru sudah penuh")
                        else:
                            reservasi_tiket[indeks][2] = kode_baru
                            reservasi_tiket[indeks][3] = jadwal_penerbangan[indeks_penerbangan][1]
                            reservasi_tiket[indeks][4] = jadwal_penerbangan[indeks_penerbangan][2]
                            reservasi_tiket[indeks][5] = jadwal_penerbangan[indeks_penerbangan][3]
                            reservasi_tiket[indeks][6] = jadwal_penerbangan[indeks_penerbangan][4]
                            reservasi_tiket[indeks][7] = jadwal_penerbangan[indeks_penerbangan][5]
                            print ("Reservasi berhasil diubah")
                input ("Tekan enter untuk kembali")
                
            elif pilihan == "6":
                os.system("cls")
                print ("============================================================================")
                print ("BATALKAN RESERVASI")
                print ("============================================================================")
                nama = input ("Masukan nama lengkap Anda: ").strip().upper()
                kode_reservasi = input ("Masukan kode reservasi: ").strip().upper()
                indeks = -1
                for i in range(len(reservasi_tiket)):
                    if reservasi_tiket[i][0] == kode_reservasi and reservasi_tiket[i][1] == nama:
                        indeks = i
                        break
                if indeks == -1:
                    print ("Reservasi tidak ditemukan")
                else:
                    konfirmasi = input ("Yakin ingin membatalkan reservasi? (y/n): ").lower()
                    if konfirmasi == "y":
                        reservasi_tiket.pop(indeks)
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