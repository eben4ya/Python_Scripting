a = 5
b = a
print("nilai a adalah ", a)
print("nilai b adalah ", b)

"""macam - macam 
tipe data"""
#tipe data integer 

data_integer = 10
print("data =", data_integer, "bertipe-", type(data_integer))

#tipe data float
data_float = 11.5
print("data =", data_float, "bertipe-", type(data_float))

#tipe data bool
data_bool = True
print("data =", data_bool, "bertipe-", type(data_bool))

#tipe data string 
data_string = "otong"
print("data =", data_string, "bertipe-", type(data_string))

#tipe data kompleks
data_complex = complex(5,6)
print("data =", complex(5,6), "bertipe-", type(complex(5,6)))

#tipe data bahasa C
from ctypes import c_double
data_c_double = c_double(10.5)
print("data =", data_c_double, "bertipe-", type(data_c_double))
from ctypes import c_char
data_c_char = c_char('y')
print("data =", data_c_char, "bertipe-", type(data_c_char))

#Tipe data sudah terdeklarasi dari inputan
