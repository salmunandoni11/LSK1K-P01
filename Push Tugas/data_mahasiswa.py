
# ==========================================
# PROGRAM DATA MAHASISWA
# Derry Armanda Setyo Utomo
# ==========================================

import json

# 1. VARIABEL
# String
nama_program = "Program Data Mahasiswa"

# Integer
jumlah_mahasiswa = 2

# Boolean
program_aktif = True

# List
data_mahasiswa = []

# 2. OUTPUT
print("================================")
print(nama_program)
print("================================")

# 3. PERCABANGAN
if program_aktif:
    print("Status program: Aktif")

    # 4. LOOPING
    # Mengulang proses sebanyak 2 kali
    for i in range(jumlah_mahasiswa):

        print("\nData mahasiswa ke-", i + 1)

        # 5. INPUT
        nama = input("Masukkan nama: ")
        nim = input("Masukkan NIM: ")
        umur = int(input("Masukkan umur: "))

        # 6. PERCABANGAN BERDASARKAN UMUR
        if umur >= 18:
            dewasa = True
        else:
            dewasa = False

        # 7. MEMBUAT DATA DALAM BENTUK DICTIONARY
        mahasiswa = {
            "nama": nama,
            "nim": nim,
            "umur": umur,
            "dewasa": dewasa
        }

        # Menambahkan data ke dalam list
        data_mahasiswa.append(mahasiswa)

    # 8. MENGUBAH DATA MENJADI FORMAT JSON
    hasil_json = json.dumps(data_mahasiswa, indent=4)

    # 9. OUTPUT DATA JSON
    print("\n===== HASIL DATA JSON =====")
    print(hasil_json)

    # 10. LOOPING UNTUK MENAMPILKAN STATUS
    print("\n===== STATUS MAHASISWA =====")

    for mhs in data_mahasiswa:
        if mhs["dewasa"]:
            print(mhs["nama"], "berstatus dewasa.")
        else:
            print(mhs["nama"], "belum dewasa.")

else:
    print("Program tidak aktif.")
