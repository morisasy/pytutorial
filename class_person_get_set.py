class Person:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name 
        
    @name.setter
    def name(self):
        self.__name = name
    @property
    def show_details(self):
        return (f" {self.name} you are smart!")

if __name__ == "__main__":

    p1 = Person('Jerin')
    print(p1.name)
    print(p1.show_details)
