def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

#print_params(43, "Hi", None) Вызов работает
#print_params() Вызов работает
#print_params(b = 25)  Вызов работает
#print_params(c = [1,2,3])  Вызов работает

values_list = [3, "Rip", None]
values_dict = {"a": 23, "b": 'Hi', "c": False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [65.3, "lol"]
print_params(*values_list_2, 42)
