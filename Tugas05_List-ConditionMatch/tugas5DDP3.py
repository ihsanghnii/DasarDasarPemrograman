pilihan = int(input("""Selamat datang, silahkan pilih nomor di bawah ini
=============================
masukan pilihan : 
=============================
1. Menghitung luas persegi
2. Menghitung luas lingkaran
3. Menghitung luas segitiga
=============================
pilihan mu? """))

match pilihan :
    
    case 1:
        print("kamu memilih menghitung luas persegi")
        sisi = int(input("sisi = "))
        LuasPersegi = sisi * sisi
        print("Luas persegi untuk persegi dengan sisi",sisi,"adalah",LuasPersegi)
    case 2:
        print("kamu memilih menghitung luas lingkaran")
        r = int(input("jari-jari = "))
        LuasLingkaran = 3.14*r*r
        print("Luas lingkaran untuk lingkaran dengan jari jari", r, "adalah", LuasLingkaran)
    case 3:
        print("kamu memilih menghitung luas segitiga")
        alas = int(input("alas = "))
        tinggi = int(input("tinggi = "))
        LuasSegitiga= 0.5*alas*tinggi
        print("Luas segitiga untuk segitiga dengan alas", alas,"dan tinggi", tinggi, "adalah", LuasSegitiga)
    case _:
        print("pilihan tidak ada")