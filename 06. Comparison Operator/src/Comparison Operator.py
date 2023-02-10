a = 4
b = 2
print('OPERATOR KOMPARASI')
print('==== < ===')
hasil = a < b
print(a, '<', b, '=', hasil)
hasil = b < a
print(b, '<', a, '=', hasil)
hasil = a < a
print(a, '<', a, '=', hasil)

print('==== > ===')
hasil = a > b
print(a, '>', b, '=', hasil)
hasil = b > a
print(b, '>', a, '=', hasil)
hasil = b > b
print(b, '>', b, '=', hasil)

print('==== <= ===')
hasil = a <= b
print(a, '<=', b, '=', hasil)
hasil = b <= a
print(b, '<=', a, '=', hasil)
hasil = a <= a
print(a, '<=', a, '=', hasil)

print('==== >= ===')
hasil = a >= b
print(a, '>=', b, '=', hasil)
hasil = b >= a
print(b, '>=', a, '=', hasil)
hasil = b >= b
print(b, '>=', b, '=', hasil)

print('==== == ===')
hasil = a == b
print(a, '==', b, '=', hasil)
hasil = a == a
print(a, '==', a, '=', hasil)

print('==== != ===')
hasil = b != a
print(b, '!=', a, '=', hasil)
hasil = b != b
print(b, '!=', b, '=', hasil)

#new in python
#Komparasi Object Identity
#literal(dont have variable) nggak berlaku
#python udah pinter kalau nilainya sama adressnya juga sama, ga kaya c++
print('KOMPARASI OBJECT IDENTITY')
x = 4
y = 4

print('x =', x, 'alamatnya :', hex(id(x)))
print('y =', y, 'alamatnya :', hex(id(y)))


print('==== is ===')
hasil = x is y
print(x, 'is', y, '=', hasil )

print('==== is not ===')
hasil = x is not y
print(x, 'is not', y, '=', hasil )

