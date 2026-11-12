print("PENCARIAN RUANG KELAS")



jumlah_pengecekan = 3

for i in range(jumlah_pengecekan):
    print(f"\n--- Pengecekan ke-{i + 1} ---")
    
    try:
        
        nomor_ruang = int(input("Masukkan nomor ruang kelas (1-30): "))
        
       
        if nomor_ruang >= 1 and nomor_ruang <= 10:
            print(f"Hasil: Ruang nomor {nomor_ruang} adalah ruang kelas FKIP")
        elif nomor_ruang >= 11 and nomor_ruang <= 20:
            print(f"Hasil: Ruang nomor {nomor_ruang} adalah ruang kelas Fakultas Ekonomi.")
        elif nomor_ruang >= 21 and nomor_ruang <= 30:
            print(f"Hasil: Ruang nomor {nomor_ruang} adalah ruang kelas Fakultas Hukum.")
        else:
            print(f"Hasil: Maaf, ruang nomor {nomor_ruang} tidak terdaftar (Gunakan nomor 1 sampai 30).")
            
    except ValueError:
        print("[Error] Masukkan angka yang valid!")