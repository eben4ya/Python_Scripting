print('\nProgram Konversi Suhu\n')
celcius = float(input('Masukkan suhu celcius : '))
reamur = 4 / 5 * celcius
print('Suhu dalam reamur     :', reamur, 'reamur')

fahrenheit = (9 / 5 * celcius) + 32
print('Suhu dalam fahrenheit :', fahrenheit, 'fahrenheit')

kelvin = celcius + 273
print('Suhu dalam kelvin     :', kelvin, 'kelvin')

# PR kelas terbuka bagian lat Aritmatika
fahrenheit = float(input('masukkan suhu fahrenheit : '))
kelvin = (5 / 9 * (fahrenheit - 32)) + 273 
print('Suhu dalam kelvin :', kelvin, 'kelvin')

kelvin = float(input('masukkan suhu kelvin : '))
fahrenheit = (9 / 5 * (kelvin - 273)) + 32
print('Suhu dalam kelvin :', fahrenheit, 'fahrenheit')