class Point:
    x = 10
    y = 7


print(
    Point.__dict__
)  # {'__module__': '__main__', 'x': 10, 'y': 7, '__dict__': <attribute '__dict__' of 'Point' objects>, '__weakref__': <attribute '__weakref__' of 'Point' objects>, '__doc__': None}

p = Point()
print(p.x)
print(p.y)

p.x = 12
print(p.x)
print(Point.x)  # 10

del p.x
print(p.x)  # 10

p.z = 3
print(p.z)
# print(Point.z)  # AttributeError: type object 'Point' has no attribute 'z'
