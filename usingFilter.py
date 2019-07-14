my_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
obj_filter=filter(lambda a: a % 2 == 0, my_values)
print(list(obj_filter))
