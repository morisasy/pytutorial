
class UsingMap:
    def sq(self, var1):
        self.var1 = var1
        return var1**2
obj = UsingMap()
obj_map = map(obj.sq, range(10))
print(list(obj_map))
