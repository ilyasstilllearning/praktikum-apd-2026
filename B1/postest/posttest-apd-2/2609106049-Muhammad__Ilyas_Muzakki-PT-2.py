makanan_1 = int (15000)
makanan_2 = int (16000)
makanan_3 = int (19000)
makanan_4 = int (20000)
makanan_5 = int (21000)
makanan_6 = int (22000)
harga_makanan = [makanan_1,makanan_2,makanan_3,makanan_4,makanan_5,makanan_6]
pajak_gojek = int (5000)
total = int (harga_makanan[0] + harga_makanan[1] + harga_makanan[2] + harga_makanan[3] + harga_makanan[4] + harga_makanan[5])
total_pajak = int (total + pajak_gojek)
euro = int (20441)
total_euro = int (total_pajak /euro)
banyak_data = len(harga_makanan)
rata_rata = total_pajak / banyak_data
nim = int (49)
bolean = nim != rata_rata

print ("Total harga yang harus dibayar dalam IDR: ",total_pajak)
print ("Total harga yang harus dibayar dalam EUR: ", total_euro )
print ("Nilai rata-rata: ", rata_rata)
print ("Bolean: ", bolean)