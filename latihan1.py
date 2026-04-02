x = int(input("masukkan jumlah hari: "))

Tahun = x // 365
Sisa_hari = x % 365
bulan = Sisa_hari // 30
hari = Sisa_hari % 30

print("Hasil Konversi: ")
print("Tahun : ", Tahun)
print("Bulan : ", bulan)
print("Hari : ", hari)