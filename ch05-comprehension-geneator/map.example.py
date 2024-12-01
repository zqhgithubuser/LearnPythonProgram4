print(list(map(lambda *a: a, range(3))))
print(list(map(lambda *a: a, range(3), "abc")))
print(list(map(lambda *a: a, range(3), "abc", range(4, 7))))
# map stops at the shortest iterator
print(list(map(lambda *a: a, (), "abc")))
print(list(map(lambda *a: a, (1, 2), "abc")))
print(list(map(lambda *a: a, (1, 2, 3, 4), "abc")))
