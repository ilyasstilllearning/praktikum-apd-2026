import os
GARIS = "============================================================================"
nama_admin = "ilyas"
password_admin = "049"
jadwal_penerbangan = dict()
reservasi_tiket = dict()
nomor_reservasi = 1

def hitung_penumpang(kode_penerbangan):
    jumlah = 0
    for data in reservasi_tiket.values():
        if data["kode_penerbangan"] == kode_penerbangan:
            jumlah += 1
    return jumlah


def validasi_kapasitas(teks):
    pesan = "Kapasitas harus berupa bilangan bulat positif"
    if not teks.isdigit():
        raise ValueError(pesan)
    try:
        nilai = int(teks)
    except ValueError:
        raise ValueError(pesan) from None
    if nilai <= 0:
        raise ValueError(pesan)
    return nilai

def buat_kode_reservasi():
    global nomor_reservasi
    kode = f"RSV{nomor_reservasi:04d}"
    nomor_reservasi += 1
    return kode


def login_admin():
    while True:
        tampil_header("LOGIN ADMIN")
        nama = input("Masukan nama admin: ").lower()
        password = input("Masukan password: ")
        if nama == nama_admin and password == password_admin:
            print("Login berhasil!")
            input("Tekan enter untuk melanjutkan")
            return True
        print("Nama admin atau password salah")
        pilihan_login = input("Coba lagi? (y/n): ").lower()
        if pilihan_login != "y":
            return False


def tampil_header(judul):
    os.system("cls" if os.name == "nt" else "clear")
    print(GARIS)
    print(judul)
    print(GARIS)


def sinkronkan_reservasi(kode_reservasi, kode_penerbangan):
    """Prosedur 2: menyalin data jadwal terbaru ke data reservasi."""
    jadwal = jadwal_penerbangan[kode_penerbangan]
    reservasi_tiket[kode_reservasi]["kode_penerbangan"] = kode_penerbangan
    reservasi_tiket[kode_reservasi]["maskapai"] = jadwal["maskapai"]
    reservasi_tiket[kode_reservasi]["asal"] = jadwal["asal"]
    reservasi_tiket[kode_reservasi]["tujuan"] = jadwal["tujuan"]
    reservasi_tiket[kode_reservasi]["tanggal"] = jadwal["tanggal"]
    reservasi_tiket[kode_reservasi]["jam"] = jadwal["jam"]

def kelola_jadwal():
    while True:
        tampil_header("MANAJEMEN JADWAL PENERBANGAN")
        print("[1]. Tambah jadwal penerbangan")
        print("[2]. Lihat jadwal /penerbangan")
        print("[3]. Ubah jadwal penerbangan")
        print("[4]. Hapus jadwal penerbangan")
        print("[5]. Kembali ke menu utama")
        print(GARIS)
        pilihan = input("Masukan pilihan 1-5: ")

        if pilihan == "1":
            tampil_header("TAMBAH JADWAL PENERBANGAN")
            kode = input("Masukan nomor penerbangan: ").strip().upper()
            if kode == "":
                print("Kode penerbangan tidak boleh kosong")
            elif kode in jadwal_penerbangan:
                print("Kode penerbangan sudah terdaftar")
            else:
                maskapai = input("Masukan nama maskapai: ").strip().upper()
                kota_asal = input("Masukan kota asal: ").strip().upper()
                kota_tujuan = input("Masukan kota tujuan: ").strip().upper()
                tanggal = input("Masukan tanggal penerbangan: ").strip()
                jam = input("Masukan jam keberangkatan: ").strip()
                kapasitas = input("Masukan kapasitas pesawat: ").strip()
                try:
                    if maskapai == "" or kota_asal == "" or kota_tujuan == "" or tanggal == "" or jam == "" or kapasitas == "":
                        raise ValueError("Semua data wajib diisi")
                    if kota_asal == kota_tujuan:
                        raise ValueError("Kota asal dan tujuan tidak boleh sama")
                    kapasitas_valid = validasi_kapasitas(kapasitas)
                except ValueError as pesan_error:
                    print(pesan_error)
                else:
                    jadwal_penerbangan[kode] = {
                        "maskapai": maskapai,
                        "asal": kota_asal,
                        "tujuan": kota_tujuan,
                        "tanggal": tanggal,
                        "jam": jam,
                        "kapasitas": kapasitas_valid
                    }
                    print("Jadwal penerbangan berhasil ditambahkan!")
            input("Tekan enter untuk kembali")

        elif pilihan == "2":
            tampil_header("DAFTAR JADWAL PENERBANGAN")
            if len(jadwal_penerbangan) == 0:
                print("Belum ada jadwal penerbangan")
            else:
                print("-" * 110)
                print(f"{'No.':<5}{'Kode':<12}{'Maskapai':<22}{'Asal':<15}{'Tujuan':<15}{'Tanggal':<15}{'Jam':<10}{'Kapasitas':<10}")
                print("-" * 110)
                nomor = 1
                for kode, data in jadwal_penerbangan.items():
                    print(f"{nomor:<5}{kode:<12}{data['maskapai']:<22}{data['asal']:<15}{data['tujuan']:<15}{data['tanggal']:<15}{data['jam']:<10}{data['kapasitas']:<10}")
                    nomor += 1
            print(GARIS)
            print(f"Total jadwal penerbangan: {len(jadwal_penerbangan)}")
            input("Tekan enter untuk kembali")

        elif pilihan == "3":
            tampil_header("UBAH JADWAL PENERBANGAN")
            ubah = input("Masukan kode penerbangan yang ingin diubah: ").strip().upper()
            try:
                data_lama = jadwal_penerbangan[ubah]
            except KeyError:
                print("Kode penerbangan tidak ditemukan")
            else:
                print("Data penerbangan saat ini:")
                print("Kode penerbangan :", ubah)
                print("Maskapai         :", data_lama["maskapai"])
                print("Kota asal        :", data_lama["asal"])
                print("Kota tujuan      :", data_lama["tujuan"])
                print("Tanggal          :", data_lama["tanggal"])
                print("Jam              :", data_lama["jam"])
                print("Kapasitas        :", data_lama["kapasitas"])
                print(GARIS)
                print("Tekan enter jika data tidak ingin diubah")
                maskapai = input("Masukan maskapai baru: ").strip().upper()
                asal = input("Masukan kota asal baru: ").strip().upper()
                tujuan = input("Masukan kota tujuan baru: ").strip().upper()
                tanggal = input("Masukan tanggal baru: ").strip()
                jam = input("Masukan jam baru: ").strip()
                kapasitas = input("Masukan kapasitas pesawat: ").strip()
                asal_baru = asal if asal != "" else data_lama["asal"]
                tujuan_baru = tujuan if tujuan != "" else data_lama["tujuan"]
                try:
                    if asal_baru == tujuan_baru:
                        raise ValueError("Kota asal dan tujuan tidak boleh sama")
                    if kapasitas != "":
                        kapasitas_baru = validasi_kapasitas(kapasitas)
                    else:
                        kapasitas_baru = data_lama["kapasitas"]
                    if kapasitas_baru < hitung_penumpang(ubah):
                        raise ValueError("Kapasitas tidak boleh lebih kecil dari pada penumpang")
                except ValueError as pesan_error:
                    print(pesan_error)
                else:
                    if maskapai != "":
                        data_lama["maskapai"] = maskapai
                    data_lama["asal"] = asal_baru
                    data_lama["tujuan"] = tujuan_baru
                    if tanggal != "":
                        data_lama["tanggal"] = tanggal
                    if jam != "":
                        data_lama["jam"] = jam
                    data_lama["kapasitas"] = kapasitas_baru
                    for kode_reservasi in reservasi_tiket:
                        if reservasi_tiket[kode_reservasi]["kode_penerbangan"] == ubah:
                            sinkronkan_reservasi(kode_reservasi, ubah)
                    print("Jadwal penerbangan berhasil diubah!")
            input("Tekan enter untuk kembali")

        elif pilihan == "4":
            tampil_header("HAPUS JADWAL PENERBANGAN")
            hapus = input("Masukan kode penerbangan yang ingin dihapus: ").strip().upper()
            if hapus not in jadwal_penerbangan:
                print("Kode penerbangan tidak ditemukan")
            elif hitung_penumpang(hapus) > 0:
                print("Jadwal tidak dapat dihapus karena masih memiliki reservasi")
            else:
                konfirmasi = input("Yakin ingin menghapus? (y/n): ").lower()
                if konfirmasi == "y":
                    try:
                        jadwal_penerbangan.pop(hapus)
                    except KeyError:
                        print("Kode penerbangan tidak ditemukan")
                    else:
                        print("Jadwal penerbangan berhasil dihapus")
                else:
                    print("Penghapusan dibatalkan")
            input("Tekan enter untuk kembali")

        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid")
            input("Tekan enter untuk kembali")
def kelola_reservasi():
    while True:
        tampil_header("MANAJEMEN RESERVASI TIKET")
        print("[1]. Tambah reservasi")
        print("[2]. Lihat reservasi")
        print("[3]. Ubah data reservasi")
        print("[4]. Hapus / batalkan reservasi")
        print("[5]. Cari reservasi")
        print("[6]. Kembali ke menu utama")
        print(GARIS)
        pilihan = input("Masukan pilihan 1-6: ")

        if pilihan == "1":
            tampil_header("TAMBAH RESERVASI")
            if len(jadwal_penerbangan) == 0:
                print("Belum ada jadwal penerbangan")
            else:
                for kode, data in jadwal_penerbangan.items():
                    print(kode, "|", data["maskapai"], "|", data["asal"], "->", data["tujuan"], "|", data["tanggal"], "|", data["jam"])
                nama = input("Masukan nama penumpang: ").strip().upper()
                kode = input("Masukan kode penumpang: ").strip().upper()
                if nama == "":
                    print("Nama penumpang tidak boleh kosong")
                elif kode not in jadwal_penerbangan:
                    print("Kode penerbangan tidak ditemukan")
                else:
                    sudah_memesan = False
                    for data in reservasi_tiket.values():
                        if data["nama"] == nama and data["kode_penerbangan"] == kode:
                            sudah_memesan = True
                    if sudah_memesan:
                        print("Penumpang sudah memiliki reservasi pada penerbangan ini")
                    elif hitung_penumpang(kode) >= jadwal_penerbangan[kode]["kapasitas"]:
                        print("Kapasitas penerbangan sudah penuh")
                    else:
                        kode_reservasi = buat_kode_reservasi()
                        reservasi_tiket[kode_reservasi] = {"nama": nama}
                        sinkronkan_reservasi(kode_reservasi, kode)
                        print("Reservasi berhasil ditambahkan!")
                        print("Kode reservasi:", kode_reservasi)
            input("Tekan enter untuk kembali")

        elif pilihan == "2":
            tampil_header("DAFTAR RESERVASI TIKET")
            if len(reservasi_tiket) == 0:
                print("Belum ada reservasi")
            else:
                print(f"{'Kode Reservasi':<18}{'Nama Penumpang':<25}{'Kode Penerbangan':<20}{'Maskapai':<22}{'Asal':<15}{'Tujuan':<15}")
                print("-" * 115)
                for kode_reservasi, data in reservasi_tiket.items():
                    print(f"{kode_reservasi:<18}{data['nama']:<25}{data['kode_penerbangan']:<20}{data['maskapai']:<22}{data['asal']:<15}{data['tujuan']:<15}")
            print(GARIS)
            print("Total reservasi:", len(reservasi_tiket))
            input("Tekan enter untuk melanjutkan")

        elif pilihan == "3":
            tampil_header("UBAH DATA RESERVASI")
            kode_reservasi = input("Masukan kode reservasi: ").strip().upper()
            try:
                data_reservasi = reservasi_tiket[kode_reservasi]
            except KeyError:
                print("Reservasi tidak ditemukan")
            else:
                print("Nama penumpang:", data_reservasi["nama"])
                print("Kode penerbangan:", data_reservasi["kode_penerbangan"])
                nama_baru = input("Masukan nama baru (enter jika tetap): ").strip().upper()
                kode_baru = input("Masukan kode penerbangan baru (enter jika tetap): ").strip().upper()
                if nama_baru == "":
                    nama_baru = data_reservasi["nama"]
                if kode_baru == "":
                    kode_baru = data_reservasi["kode_penerbangan"]
                if kode_baru not in jadwal_penerbangan:
                    print("Penerbangan tidak ditemukan")
                else:
                    sudah_memesan = False
                    for kode_lain, data in reservasi_tiket.items():
                        if kode_lain != kode_reservasi and data["nama"] == nama_baru and data["kode_penerbangan"] == kode_baru:
                            sudah_memesan = True
                    if sudah_memesan:
                        print("Penumpang sudah memiliki reservasi pada penerbangan ini")
                    elif kode_baru != data_reservasi["kode_penerbangan"] and hitung_penumpang(kode_baru) >= jadwal_penerbangan[kode_baru]["kapasitas"]:
                        print("Penerbangan baru sudah penuh")
                    else:
                        data_reservasi["nama"] = nama_baru
                        sinkronkan_reservasi(kode_reservasi, kode_baru)
                        print("Reservasi berhasil diubah")
            input("Tekan enter untuk melanjutkan")

        elif pilihan == "4":
            tampil_header("HAPUS / BATALKAN RESERVASI")
            kode = input("Masukan kode reservasi: ").strip().upper()
            if kode not in reservasi_tiket:
                print("Reservasi tidak ditemukan")
            else:
                konfirmasi = input("Yakin ingin membatalkan reservasi? (y/n): ").lower()
                if konfirmasi == "y":
                    try:
                        reservasi_tiket.pop(kode)
                    except KeyError:
                        print("Reservasi tidak ditemukan")
                    else:
                        print("Reservasi berhasil dibatalkan")
                else:
                    print("Pembatalan dibatalkan")
            input("Tekan enter untuk kembali")

        elif pilihan == "5":
            tampil_header("CARI RESERVASI")
            kode = input("Masukan kode reservasi: ").strip().upper()
            try:
                data = reservasi_tiket[kode]
            except KeyError:
                print("Reservasi tidak ditemukan")
            else:
                print("Kode reservasi:", kode)
                print("Nama penumpang:", data["nama"])
                print("Kode penerbangan:", data["kode_penerbangan"])
                print("Maskapai:", data["maskapai"])
                print("Kota asal:", data["asal"])
                print("Kota tujuan:", data["tujuan"])
                print("Tanggal:", data["tanggal"])
                print("Jam:", data["jam"])
            input("Tekan enter untuk kembali")

        elif pilihan == "6":
            break
        else:
            print("Pilihan tidak valid")
            input("Tekan enter untuk kembali")


# ----------------------------------------------------------------------------
# Prosedur pendukung: passenger manifest (admin)
# ----------------------------------------------------------------------------
def passenger_manifest():
    tampil_header("PASSENGER MANIFEST")
    if len(jadwal_penerbangan) == 0:
        print("Belum ada jadwal penerbangan")
    else:
        for kode, data in jadwal_penerbangan.items():
            print(kode, "|", data["maskapai"], "|", data["asal"], "->", data["tujuan"], "|", data["tanggal"])
        kode = input("Masukan kode penerbangan: ").strip().upper()
        try:
            jadwal = jadwal_penerbangan[kode]
        except KeyError:
            print("Kode penerbangan tidak ditemukan")
        else:
            print("-" * 70)
            print("PASSENGER MANIFEST:", kode)
            print("Maskapai:", jadwal["maskapai"])
            print("Rute:", jadwal["asal"], "->", jadwal["tujuan"])
            print("Tanggal:", jadwal["tanggal"])
            print("Jam:", jadwal["jam"])
            print("-" * 70)
            print(f"{'No.':<6}{'Kode Reservasi':<20}{'Nama Penumpang':<30}")
            print("-" * 70)
            jumlah_penumpang = 0
            for kode_reservasi, data in reservasi_tiket.items():
                if data["kode_penerbangan"] == kode:
                    jumlah_penumpang += 1
                    print(f"{jumlah_penumpang:<6}{kode_reservasi:<20}{data['nama']:<30}")
            if jumlah_penumpang == 0:
                print("Belum ada penumpang")
            print("-" * 70)
            print("Jumlah penumpang:", jumlah_penumpang)
            print("Kapasitas pesawat:", jadwal["kapasitas"])
            print("Sisa kursi:", jadwal["kapasitas"] - jumlah_penumpang)
    input("Tekan enter untuk kembali")

def menu_admin():
    while True:
        tampil_header("MENU UTAMA ADMIN")
        print("[1]. Manajemen jadwal penerbangan")
        print("[2]. Manajemen reservasi tiket")
        print("[3]. Passenger manifest")
        print("[4]. Keluar dari akun admin")
        print(GARIS)
        pilihan = input("Masukan pilihan 1-4: ")
        if pilihan == "1":
            kelola_jadwal()
        elif pilihan == "2":
            kelola_reservasi()
        elif pilihan == "3":
            passenger_manifest()
        elif pilihan == "4":
            print("Terima kasih telah menggunakan AeroManage!")
            input("Tekan enter untuk melanjutkan")
            break
        else:
            print("Pilihan tidak valid")
            input("Tekan enter untuk melanjutkan")

def menu_user():
    while True:
        tampil_header("                         AEROMANAGE - MENU USER")
        print("[1]. Lihat jadwal penerbangan")
        print("[2]. Cari penerbangan")
        print("[3]. Buat reservasi tiket")
        print("[4]. Lihat reservasi saya")
        print("[5]. Ubah reservasi saya")
        print("[6]. Batalkan reservasi saya")
        print("[7]. Kembali ke menu utama")
        print(GARIS)
        pilihan = input("Masukan pilihan 1-7: ")

        if pilihan == "1":
            tampil_header("DAFTAR JADWAL PENERBANGAN")
            if len(jadwal_penerbangan) == 0:
                print("Belum ada jadwal penerbangan")
            else:
                print(f"{'Kode':<12}{'Maskapai':<22}{'Asal':<15}{'Tujuan':<15}{'Tanggal':<15}{'Jam':<10}{'Kapasitas':<10}")
                print("-" * 100)
                for kode, data in jadwal_penerbangan.items():
                    print(f"{kode:<12}{data['maskapai']:<22}{data['asal']:<15}{data['tujuan']:<15}{data['tanggal']:<15}{data['jam']:<10}{data['kapasitas']:<10}")
            input("Tekan enter untuk melanjutkan")

        elif pilihan == "2":
            tampil_header("CARI PENERBANGAN")
            kode = input("Masukan kode penerbangan: ").strip().upper()
            try:
                jadwal = jadwal_penerbangan[kode]
            except KeyError:
                print("Penerbangan tidak ditemukan")
            else:
                print("Kode penerbangan:", kode)
                print("Maskapai:", jadwal["maskapai"])
                print("Kota asal:", jadwal["asal"])
                print("Kota tujuan:", jadwal["tujuan"])
                print("Tanggal:", jadwal["tanggal"])
                print("Jam:", jadwal["jam"])
                print("Sisa kursi:", jadwal["kapasitas"] - hitung_penumpang(kode))
            input("Tekan enter untuk kembali")
            
        elif pilihan == "3":
            tampil_header("BUAT RESERVASI TIKET")
            if len(jadwal_penerbangan) == 0:
                print("Belum ada jadwal penerbangan")
            else:
                nama = input("Masukan nama lengkap: ").strip().upper()
                if nama == "":
                    print("Nama tidak boleh kosong")
                else:
                    print("\nDaftar penerbangan:")
                    for kode, data in jadwal_penerbangan.items():
                        print(kode, "|", data["maskapai"], "|", data["asal"], "->", data["tujuan"], "|", data["tanggal"], "| Sisa kursi:", data["kapasitas"] - hitung_penumpang(kode))
                    kode = input("Masukan kode penerbangan: ").strip().upper()
                    if kode not in jadwal_penerbangan:
                        print("Penerbangan tidak ditemukan")
                    else:
                        sudah_memesan = False
                        for data in reservasi_tiket.values():
                            if data["nama"] == nama and data["kode_penerbangan"] == kode:
                                sudah_memesan = True
                        if sudah_memesan:
                            print("Anda sudah memiliki reservasi pada penerbangan ini")
                        elif hitung_penumpang(kode) >= jadwal_penerbangan[kode]["kapasitas"]:
                            print("Kapasitas penerbangan sudah penuh")
                        else:
                            kode_reservasi = buat_kode_reservasi()
                            reservasi_tiket[kode_reservasi] = {"nama": nama}
                            sinkronkan_reservasi(kode_reservasi, kode)
                            print("Reservasi berhasil dibuat!")
                            print("Kode reservasi:", kode_reservasi)
            input("Tekan enter untuk kembali")

        elif pilihan == "4":
            tampil_header("RESERVASI SAYA")
            nama = input("Masukan nama lengkap Anda: ").strip().upper()
            ditemukan = False
            for kode_reservasi, data in reservasi_tiket.items():
                if data["nama"] == nama:
                    print("-" * 60)
                    print("Kode reservasi:", kode_reservasi)
                    print("Nama penumpang:", data["nama"])
                    print("Kode penerbangan:", data["kode_penerbangan"])
                    print("Maskapai:", data["maskapai"])
                    print("Rute:", data["asal"], "->", data["tujuan"])
                    print("Tanggal:", data["tanggal"])
                    print("Jam:", data["jam"])
                    ditemukan = True
            if not ditemukan:
                print("Reservasi tidak ditemukan")
            input("Tekan enter untuk kembali")

        elif pilihan == "5":
            tampil_header("UBAH RESERVASI SAYA")
            nama = input("Masukan nama lengkap Anda: ").strip().upper()
            kode_reservasi = input("Masukan kode reservasi: ").strip().upper()
            try:
                data_reservasi = reservasi_tiket[kode_reservasi]
                if data_reservasi["nama"] != nama:
                    raise KeyError(kode_reservasi)
            except KeyError:
                print("Reservasi tidak ditemukan")
            else:
                print("Kode penerbangan saat ini:", data_reservasi["kode_penerbangan"])
                kode_baru = input("Masukan kode penerbangan baru (enter jika tetap): ").strip().upper()
                if kode_baru == "":
                    kode_baru = data_reservasi["kode_penerbangan"]
                if kode_baru not in jadwal_penerbangan:
                    print("Penerbangan tidak ditemukan")
                else:
                    kode_lama = data_reservasi["kode_penerbangan"]
                    if kode_baru != kode_lama and hitung_penumpang(kode_baru) >= jadwal_penerbangan[kode_baru]["kapasitas"]:
                        print("Penerbangan baru sudah penuh")
                    else:
                        sinkronkan_reservasi(kode_reservasi, kode_baru)
                        print("Reservasi berhasil diubah")
            input("Tekan enter untuk kembali")

        elif pilihan == "6":
            tampil_header("BATALKAN RESERVASI")
            nama = input("Masukan nama lengkap Anda: ").strip().upper()
            kode_reservasi = input("Masukan kode reservasi: ").strip().upper()
            try:
                if reservasi_tiket[kode_reservasi]["nama"] != nama:
                    raise KeyError(kode_reservasi)
            except KeyError:
                print("Reservasi tidak ditemukan")
            else:
                konfirmasi = input("Yakin ingin membatalkan reservasi? (y/n): ").lower()
                if konfirmasi == "y":
                    reservasi_tiket.pop(kode_reservasi)
                    print("Reservasi berhasil dibatalkan")
                else:
                    print("Pembatalan dibatalkan")
            input("Tekan enter untuk kembali")

        elif pilihan == "7":
            break
        else:
            print("Pilihan tidak valid")
            input("Tekan enter untuk kembali")

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(GARIS)
        print("                                AEROMANAGE")
        print("                  FLIGHT SCHEDULE & RESERVATION SYSTEM")
        print(GARIS)
        print("Sistem manajemen jadwal penerbangan, reservasi tiket, dan Passenger Manifest")
        print(GARIS)
        print("Silahkan login terlebih dahulu, siapa anda?")
        print("[1]. Admin")
        print("[2]. User")
        print("[3]. Keluar dari program")
        print(GARIS)
        pengguna = input("Masukan pilihan: ")
        if pengguna == "1":
            if login_admin():
                menu_admin()
        elif pengguna == "2":
            menu_user()
        elif pengguna == "3":
            os.system("cls" if os.name == "nt" else "clear")
            print(GARIS)
            print("Terimakasih sudah menggunakan program AeroManage!")
            print(GARIS)
            break
        else:
            print("Pilihan anda tidak valid, silahkan ulangi")
            input("Tekan enter untuk melanjutkan")

main()