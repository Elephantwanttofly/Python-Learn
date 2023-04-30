
a = 10
b = 3

# operasi penjumlahan +
hasil = a + b
print(a,'+',b,'=',hasil)


# operasi pengurangan -
hasil = a - b
print(a,'-',b,'=',hasil)


# operasi perkalian *
hasil = a * b
print(a,'*',b,'=',hasil)


# operasi pemabagian /
hasil = a / b
print(a,'/',b,'=',hasil)


# operasi eksponen (pangkat) **
hasil = a ** b
print(a,'**',b,'=',hasil)

# operasi modulus
hasil = a % b
print(a,'%',b,'=',hasil)


# operasi floor division // (kebalikan dari modulus)
hasil = a // b
print(a,'//',b,'=',hasil)

# prioritas operasi, operational precedence

'''
    1. ()
    2. Exponen **
    3. Perkalian dan dkk * / ** % //
    4. Penjumlahan dan Pengurangan
'''

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**', y,'*', z,'+', x,'/', y,'-', y,'%', z,'//', x,'=', hasil)


hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)
hasil = (x + y) * z
print('(', x,'+',y,') *',z,'=',hasil)