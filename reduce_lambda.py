from functools import reduce
my_phrase = ['To', 'day', 'is', 'my', 'day', '!']

obj_lambda = lambda a, b: a + " "+ b
obj_reduce = reduce(obj_lambda , my_phrase)
print(obj_reduce)
