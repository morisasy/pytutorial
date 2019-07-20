class Fruits:

    def __init__(self, name):
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

obj1 = Fruits('Banana')
print(f' The fruit name is {obj1.get_name()}')
