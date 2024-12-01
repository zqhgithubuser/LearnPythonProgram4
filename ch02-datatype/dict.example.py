d = dict(zip("hello", range(5)))
print(d.keys())  # dict_keys(['h', 'e', 'l', 'o'])
print(d.values())  # dict_values([0, 1, 3, 4])
print(d.items())  # dict_items([('h', 0), ('e', 1), ('l', 3), ('o', 4)])

d = {}
d.setdefault("a", 1)  # {'a': 1}
print(d)

d = {"a": "A", "b": "B"}
e = {"b": 8, "c": "C"}
print(d | e)  # {'a': 'A', 'b': 8, 'c': 'C'}
print(e | d)  # {'b': 'B', 'c': 'C', 'a': 'A'}
print({**d, **e})  # {'a': 'A', 'b': 8, 'c': 'C'}
print({**e, **d})  # {'b': 'B', 'c': 'C', 'a': 'A'}
d |= e  # 就地
print(d)  # {'a': 'A', 'b': 8, 'c': 'C'}
