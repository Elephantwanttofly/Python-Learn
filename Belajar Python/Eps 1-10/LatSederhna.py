# Lat konversi satuan temperature

# program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATURE\n")

celcius = float(input('Masukan suhu dalam celcius : '))
print("Suhu dalam Celcius Adalah ", celcius, "Celcius")

# reamur
reamur = (4/5) * celcius
print("Suhu dalam Reamur Adalah ", reamur, "Reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam Fahrenheit Adalah ", fahrenheit, "Fahrenheit")

# kelvin
kelvin = 273 + celcius
print("Suhu dalam Kelvin Adalah ", kelvin, "Kelvin")