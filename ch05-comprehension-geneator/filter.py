test = [2, 5, 8, 0, 0, 1, 0]
print(list(filter(None, test)))
print(list(filter(lambda x: x, test)))
print(list(filter(lambda x: x > 4, test)))
