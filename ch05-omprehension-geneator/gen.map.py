def adder(*n):
    return sum(n)


list1 = list(
    map(adder, range(100), range(1, 101))
)
print(list1)

list2 = list(
    (adder(*n) for n in zip(range(100), range(1, 101)))
)
print(list2)
