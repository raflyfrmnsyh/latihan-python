# Tugas vidio youtube kelas terbuka
# Membuat konversi suhu dari kelvin kedalam satuan suhu lainnya

print("\nPROGRAM KONVERSI SUHU kelvin\n")

k = float(input("Masukan nilai suhu kelvin :"))
print("Suhu yang anda input adalah", k, "kelvin")

rumus = k-273

# Konversi kedalam satuan celcius
celcius = rumus
print("Dalam satuan celcius :", celcius, "celcius")

# Konversi kedalam satuan reamur
reamur = (4/5) * (rumus)
print("Dalam satuan reamur :", reamur, "reamur")

# Konversi kedalam satuan fahrenheit
fa = ((rumus) * (9/5)) + 32
print("Dalam satuan fahrenheit : ", fa, "fahrenheit")
