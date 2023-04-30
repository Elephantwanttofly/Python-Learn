print("\nPROGRAM KONVERSI F KE K\n")
# FAHRENHEIT KE KELVIN
fahrenheit = float(input('Masukan Suhu dalam Fahrenheit : '))
celcius = ((5/9) * fahrenheit) - 32
kelvin = celcius + 273
print("suhu dalam kelvin adalah = ", kelvin,"K")

print("==========================")

print("\nPROGRAM KONVERSI K KE F\n")
# KELVIN KE FAHRENHEIT
kelvin = float(input('Masukan suhu dalam Kelvin : '))
celcius = kelvin - 273
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah = ", fahrenheit, "F")