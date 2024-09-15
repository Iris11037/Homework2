my_dict = {"Имя": "Ольга", "Возраст": 24, "Номер телефона": 3749379477}
print(my_dict)
print(my_dict.get("Возраст"))
print(my_dict.get("Фамилия"))
my_dict.update({"Фамилия": "Иванова",
                "Отчество": "Сергеевна"})
a = my_dict.pop("Возраст")
print(a)
print(my_dict)

my_set = {3.9, 5, 5, 3.9, 5, "Hi", "Hi"}
print(my_set)
my_set.add(2)
my_set.add(True)
my_set.remove(3.9)
print(my_set)