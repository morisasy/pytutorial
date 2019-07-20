class Cal:
    def add(self, x, y):
        self.x = x
        self.y = y
        return x + y
    def sub(self, x, y):
        self.x = x
        self.y = y
        return x + y
    def mul(self, x, y):
        self.x = x
        self.y = y
        return x*y
obj = Cal()
print(obj.add(5, 6))
print(Cal.mul(obj, 4, 7))
