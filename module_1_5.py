immutable_var = 1, 2.3, "Hi", True
print(immutable_var)
# immutable_var[0] = 3 (выдаст ошибку)
# Кортеж нельзя изменить так как он относится к неизменяемым типам данных.

mutable_list = [223, 4.2, "hi", True]
mutable_list[0] = 0.4
mutable_list[3] = False
print(mutable_list)