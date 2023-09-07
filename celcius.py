# Latihan Perkonversian Temperatur

# program konversi celcius pada satuan temperatur lain
print("\nPROGRAM KONVERSI SATUAN TEMPERATUR\n")

celcius = float(input('Masukan satuan celcius : '))
print("Suhu yang anda input adalah :", celcius, "celcius")

# konversi reamur
reamur = (4/5) * celcius
print("Dalam satuan reamur :", reamur, "reamur")

# konversi Fahrenhit
fahrenheit = ((9/5) * celcius) + 32
print("Dalam satuan Fahrenheit :", fahrenheit, "fahrenheit")

# konversi kelvin
kelvin = celcius + 273
print("Dalam satuan Kelvin :", kelvin, "kelvin")
