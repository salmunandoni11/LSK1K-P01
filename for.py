print("angka ganjil genap")


jumlah = int(input("Masukkan jumlah angka yang ingin dianalisis: "))

total_genap = 0
total_ganjil = 0

for i in range(jumlah):

    angka = int(input(f"Masukkan angka ke-{i + 1}: "))

if angka > 0:
    status = "Positif"
elif angka < 0:
    status = "Negatif"
else:
    status = "Nol"
    
if angka % 2 == 0:
    jenis = "Genap"
    total_genap += 1
else:
    jenis = "Ganjil"
    total_ganjil += 1


print(f"-> Angka {angka} adalah {status} dan {jenis}\n")

print("--- Ringkasan ---")
print(f"Total Genap: {total_genap}")
print(f"Total Ganjil: {total_ganjil}")