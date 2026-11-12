# ============================================
# Program Sederhana: Pendataan Nilai Mahasiswa
# ============================================
 
import json  # modul bawaan Python untuk mengolah JSON
 
nama_kampus = "STI&K Jakarta"   
batas_lulus = 70                     
aktif = True                         
 
data_json = '{"matkul": "Pemrograman Python", "sks": 3}'
matkul = json.loads(data_json)
 
print("Selamat datang di", nama_kampus)
print("Mata kuliah:", matkul["matkul"], "-", matkul["sks"], "SKS")
 
nama = input("Masukkan nama Anda: ")
jumlah = int(input("Berapa nilai yang ingin diinput? "))
 
daftar_nilai = []
 
for i in range(jumlah):
    nilai = int(input(f"Nilai ke-{i + 1}: "))
    daftar_nilai.append(nilai)
 
total = 0
for n in daftar_nilai:
    total = total + n
rata_rata = total / jumlah
 
if rata_rata >= 85:
    predikat = "A"
elif rata_rata >= 65:
    predikat = "B"
else:
    predikat = "Tidak Lulus"
 
hasil = {
    "nama": nama,
    "rata_rata": rata_rata,
    "predikat": predikat,
    "lulus": rata_rata >= batas_lulus
}
 
if aktif:
    print("\n=== HASIL ===")
    print(json.dumps(hasil, indent=2))
