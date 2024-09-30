Nama = str(input("Masukkan Nama: "))
NIM = int(input("Masukkan NIM: "))

Sapaan = f"Selamat datang di program, {Nama}! NIM Anda adalah {NIM}."
print(Sapaan)
print("Selamat Berbelanja^^")

while True:
    Harga = int(input("Masukkan Harga Barang yang Anda Ambil: Rp"))
    Jumlah = int(input("Masukkan Jumlah Barang yang Anda Ambil: "))
    Total = Harga * Jumlah
    print(Total)
    
    if Total > 250000:
        Diskon = 0.25 * Total
        Total_Belanja = float(f"{Total - Diskon}")
        print("Total belanja diatas 250000, Anda mendapatkan diskon sebesar 25%!^^")
        Total_dengan_diskon = f"Total belanja Anda adalah {Total_Belanja}"
        print(Total_dengan_diskon)
    else:
        print("Anda tidak mendapatkan diskon^^")
        Total_tanpa_diskon = f"Total belanja Anda adalah {Total}"
        print(Total_tanpa_diskon)

    Melanjutkan = input("Apakah Anda ingin menghitung barang lagi? (y/n): ")
    if Melanjutkan.lower()!= 'y':
        print("Terimakasih Telah Berbelanja^^")
        break