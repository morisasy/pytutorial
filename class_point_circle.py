
class Point:
    pass
p = Point()
print(p)
p.x = 3.0
p.y = 4.0
p.radius = 5.8

print("X axis is ", p.x)
print("x axis is ", p.x)
print("Radius axis is ", p.radius)
p1 = Point()
p2 = Point()
import copy
p3 = copy.copy(p)
print(p3.x, p3.y, p.radius)



