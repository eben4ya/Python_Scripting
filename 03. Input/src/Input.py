""" bentuk 1
data = input("masukan data : ")
print("data :", data) """
""" bentuk 2
print("data :", input("masukan data : ") ) """

print("===DEFAULT(STRING)===")
data_str = input("masukkan data : ")
print("data :", data_str , "tipe :", type(data_str))

print("===INT===") #diisi float gabisa
data_int = int(input("masukkan data : "))
print("data :", data_int , "tipe :", type(data_int))

print("===FLOAT===") # diisi int bisa, hasil (int).0
data_float = float(input("masukkan data : "))
print("data :", data_float , "tipe :", type(data_float))

print("===BOOLEAN===")
data_bool = bool(int(input("masukkan data : ")))
print("data :", data_bool , "tipe :", type(data_bool))

