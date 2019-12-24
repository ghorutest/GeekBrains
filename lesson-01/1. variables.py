a_int = 12
b_int = 49
c_bool = True
d_str = "False"
e_str = "100"
result = "NULL"

print ("Пример 1. int / int = float (второе целое не кртано первому)")
print (f"type {type(a_int)} / type {type(b_int)} = type {type(a_int / b_int)}")
print (f"{a_int} / {b_int}  = {a_int / b_int}\n")

print ("Пример 2. int / bool = float")
print (f"type {type(a_int)} / type {type(c_bool)} = type {type(a_int / c_bool)}")
print (f"{a_int} / {c_bool}  = {a_int / c_bool}\n")

print ("Пример 3. int and str = str (равно 2-й строке)")
print (f"type {type(a_int)} and type {type(d_str)} = type {type(a_int and d_str)}")
print (f"{a_int} and {d_str}  = {a_int and d_str}\n")

print ("Пример 4. int and str = str (равно 2-й строке, даже если в ней только цифры)")
print (f"type {type(a_int)} and type {type(e_str)} = type {type(a_int and e_str)}")
print (f"{a_int} and {e_str}  = {a_int and e_str}\n")

print ("Пример 5. bool and str = str (равно 2-й строке)")
print (f"type {type(c_bool)} and type {type(d_str)} = type {type(c_bool and d_str)}")
print (f"{c_bool} and {d_str}  = {c_bool and d_str}\n")

print ("Пример 6. int and str = str (равно 2-й строке)")
print (f"type {type(a_int)} and type {type(d_str)} = type {type(a_int and d_str)}")
print (f"{a_int} and {d_str}  = {a_int and d_str}\n")

print ("Введите математическое или логическое выражение для проверки вывода, например:\n\
    '12.0 + 10' или 'False and False'")

input_string = input()
exec("result =" + input_string)
print (f"Результат = {result}")
print (f"Тип результата: {type(result)}")
