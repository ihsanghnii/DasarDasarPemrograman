jumlahbaris = int(input("Masukkan Jumlah Baris ="))

for baris in range(1,jumlahbaris + 1):
    for kolom in range(baris):
        print("*", end="")
    print()