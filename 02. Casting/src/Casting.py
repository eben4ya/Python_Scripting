"""Benaya
# Inputan
data_int = 10
data_float = 11.8
data_bool = False
data_str = "otong"

print("Casting ke INT") # int ke str / viceversa gabisa
data_int = 10
print("data : ", data_int)

data_float = int(data_float)
data_bool = int(data_bool)
# data_str = int(data_str) 
print("data : ", data_float)
print("data : ", data_bool)
# print("data : ", data_str)

print("Casting ke float") # float ke str / viceversa gabisa
data_float = 11.8
print("data : ", data_float)

data_int = float(data_int)
data_bool = float(data_bool)
# data_str = float(data_str) 
print("data : ", data_int)
print("data : ", data_bool)
# print("data : ", data_str)

print("Casting ke bool")
data_bool = True
print("data : ", data_bool)

data_int = bool(data_int) #true jika angka != 0, vice versa
data_float = bool(data_float)
data_str = bool(data_str) 
print("data : ", data_int)
print("data : ", data_float)
print("data : ", data_str) #true jika != "", vice versa

print("Casting ke string") # string ke int/float gabisa, vice versa
data_str = "otong"
print("data : ", data_str)

# data_int = str(data_int)
data_bool = str(data_bool)
# data_float = str(data_float) 
# print("data : ", data_int)
print("data : ", data_bool)
# print("data : ", data_float)
"""
# Kelas Terbuka
print("===INT===")
data_int = 10
print("data :", data_int, "\ttipe :", type(data_int))

data_float = float(data_int)
data_bool = bool(data_int)
data_str = str(data_int)
print("data :", data_float, "\ttipe :", type(data_float))
print("data :", data_bool, "\ttipe :", type(data_bool))
print("data :", data_str, "\ttipe :", type(data_str))

print("===FLOAT===")
data_float = 11.8
print("data :", data_float, "\ttipe :", type(data_float))

data_int = int(data_float)
data_bool = bool(data_float)
data_str = str(data_float)
print("data :", data_int, "\ttipe :", type(data_int))
print("data :", data_bool, "\ttipe :", type(data_bool))
print("data :", data_str, "\ttipe :", type(data_str))

print("===BOOLEAN===")
data_bool = True
print("data :", data_bool, "\ttipe :", type(data_bool))

data_float = float(data_bool)
data_int = int(data_bool)
data_str = str(data_bool)
print("data :", data_float, "\ttipe :", type(data_float))
print("data :", data_int, "\ttipe :", type(data_int))
print("data :", data_str, "\ttipe :", type(data_str))

print("===STRING===")
data_str = "otong"
print("data :", data_str, "\ttipe :", type(data_str))

data_float = float(bool(data_str)) #string harus angka biar nggausah dicasting boolean
data_bool = bool(data_str)
data_int = int(bool(data_str)) #string harus angka biar nggausah dicasting boolean
print("data :", data_float, "\ttipe :", type(data_float))
print("data :", data_bool, "\ttipe :", type(data_bool))
print("data :", data_int, "\ttipe :", type(data_int))

