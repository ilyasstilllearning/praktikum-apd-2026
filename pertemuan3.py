saku = int (input("Masukan saku:"))

while saku > 0:
    pengeluaran = int (input("Masukan pengeluaran: "))
    if pengeluaran <= saku:
        saku -= pengeluaran
        print (f"Saldo setelah pengeluaran: {saku}")
    else:
        print ("Duit kurang ajg")
        break
print (f"Total saldo akhir: {saku}")