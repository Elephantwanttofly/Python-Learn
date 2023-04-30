# data yang dimasukan pasti string
data = input("Masukan data: ")
print("data = ", data, "type =" ,type(data))

# jika kita ingin mengambil int dan float, maka
angka = int(input("masukan angka: "))
angka1 = float(input("masukan angka: "))
print("data = ", angka, "type =", type(angka))
print("data = ", angka1, "type =", type(angka1))

# tipe data boolean
biner = bool(int(input("masukan nilai boolean: ")))
print("data", biner, "type", type(biner))