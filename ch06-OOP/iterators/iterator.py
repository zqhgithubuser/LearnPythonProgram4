class OddEven:
    def __init__(self, data):
        self._data = data
        self.indexes = list(range(0, len(data), 2)) + list(range(1, len(data), 2))

    def __iter__(self):
        return self

    def __next__(self):
        if self.indexes:
            return self._data[self.indexes.pop(0)]
        raise StopIteration


ood_even = OddEven("ThIsIsCoOl!")
print("".join(c for c in ood_even))
odd_even = OddEven("CiAo")
it = iter(odd_even)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))  # StopIteration
