# Tugas vidio youtube kelas terbuka
# Membuat konversi suhu dari fahrenheit kedalam satuan suhu lainnya

print("\nPROGRAM KONVERSI SUHU FAHRENHEIT\n")

fa = float(input("Masukan nilai suhu fahrenheit :"))
print("Suhu yang anda input adalah", fa, "Fahrenheit")

rumus = fa-32

# Konversi kedalam satuan celcius
celcius = (5/9) * (rumus)
print("Dalam satuan celcius :", celcius, "celcius")

# Konversi kedalam satuan reamur
reamur = (4/9) * (rumus)
print("Dalam satuan reamur :", reamur, "reamur")

# Konversi kedalam satuan reamur
kelvin = ((5/9) * (rumus)) + 273.15
print("Dalam satuan kelvin : ", kelvin, "kelvin")
