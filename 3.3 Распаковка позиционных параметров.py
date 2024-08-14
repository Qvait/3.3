def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
values_list = [24.4, "Dibka", True]
values_dict = {"a" : 25.3 , "b" : "Biba" , "c" : True}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [22.1, "Giga"]
print_params(*values_list_2, 42)