my_phrase = "To day is may day"
my_words = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
obj_lambda = lambda x: x in my_phrase
obj_filter = filter(obj_lambda , my_words)
print(list(obj_filter))
